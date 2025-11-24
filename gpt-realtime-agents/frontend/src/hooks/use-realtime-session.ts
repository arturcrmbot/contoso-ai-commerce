import { useState, useRef, useCallback } from 'react';
import { ChatMessage } from '@/lib/types';
import { CLIENT_CONFIG as CONFIG, SYSTEM_PROMPT } from '@/lib/constants';

interface SessionState {
  status: 'idle' | 'connecting' | 'connected' | 'ended';
  isMuted: boolean;
  voiceResponseEnabled: boolean;
  isProcessing: boolean;
}

interface UseRealtimeSessionProps {
  onMessage: (message: ChatMessage) => void;
  onStateChange: (state: any) => void;
  onProductsDiscovered?: (products: any[]) => void;
  onCartUpdated?: (cartData: any) => void;
  onVisualUpdate?: (visualConfig: any) => void;
  onRecommendationsReceived?: (recommendations: any[], customerName?: string) => void;
  onError?: (error: Error, context?: string) => void;
  accountNumber?: string | null;
}



let cachedTools: any[] | null = null;
let toolChoice = "auto";

// Convert simple visual hints to flexible layout structure
function convertToFlexibleVisual(visual: any): any {
  // Already flexible (from customise_webpage or new format)
  if (visual.layout && visual.sections) {
    return visual;
  }

  // Legacy simple visual types - auto-convert
  const type = visual.type;
  const legacyTypes = ['product_grid', 'plan_cards', 'promo_banner', 'comparison_table', 'cart_preview'];

  if (legacyTypes.includes(type)) {
    // Return as-is for legacy renderer (Vodafone phone types only)
    return visual;
  }

  // New simple hints - convert to flexible
  const typeToComponent: Record<string, string> = {
    'product_grid': 'product_grid',
    'product_hero': 'product_hero',
    'plan_cards': 'plan_selector',
    'accessory_grid': 'accessory_grid',
    'price_breakdown': 'price_breakdown',
    'credit_check_status': 'credit_check_status',
    'info_callout': 'info_callout',
    'deal_grid': 'deal_grid',
    'deal_hero': 'deal_hero',
    'deal_detail_page': 'deal_detail_page',
    'deal_comparison': 'deal_comparison',
    'cart_drawer': 'cart_drawer',
    'cart_confirmation': 'cart_confirmation',
    'empty_state': 'empty_state'
  };

  const componentType = typeToComponent[type] || 'info_callout';

  return {
    layout: 'flow',
    sections: [{
      type: componentType,
      data: visual.items ? {items: visual.items} : (visual.data || visual),
      title: visual.title,
      emphasis: visual.emphasis || 'medium'
    }],
    header: visual.title ? {title: visual.title, subtitle: visual.subtitle} : undefined,
    animation: 'fade'
  };
}

export function useRealtimeSession({ onMessage, onStateChange, onProductsDiscovered, onCartUpdated, onVisualUpdate, onRecommendationsReceived, onError, accountNumber }: UseRealtimeSessionProps) {
  const [sessionState, setSessionState] = useState<SessionState>({
    status: 'idle',
    isMuted: false,
    voiceResponseEnabled: false, // Start with voice responses OFF
    isProcessing: false,
  });

  const sessionRef = useRef<{
    dataChannel: RTCDataChannel | null;
    peerConnection: RTCPeerConnection | null;
    clientMedia: MediaStream | null;
  }>({
    dataChannel: null,
    peerConnection: null,
    clientMedia: null,
  });

  const customerDataRef = useRef<{
    name: string | null;
    recommendations: any[];
  }>({
    name: null,
    recommendations: [],
  });

  const logMessage = useCallback((message: string) => {
    console.log('[VoiceCare]', message);
  }, []);

  const ensureToolsLoaded = useCallback(async () => {
    if (cachedTools !== null) {
      return;
    }

    const response = await fetch(`${CONFIG.backendBaseUrl}/tools`);
    if (!response.ok) {
      throw new Error(`Unable to retrieve tool definitions (${response.status})`);
    }

    const data = await response.json();
    cachedTools = data.tools ?? [];
    toolChoice = data.tool_choice ?? "auto";

    logMessage(`Loaded ${cachedTools?.length || 0} tool definition(s)`);

    // Log the actual tools for debugging
    logMessage(`Tools loaded: ${cachedTools?.map(t => t.name).join(', ') || 'none'}`);
  }, [logMessage]);

  const requestSession = useCallback(async (accountNumber?: string | null) => {
    const requestBody: any = {
      deployment: CONFIG.deployment,
      voice: CONFIG.voice,
    };

    if (accountNumber) {
      requestBody.account_number = accountNumber;
    }

    const response = await fetch(`${CONFIG.backendBaseUrl}/session`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(requestBody),
    });

    if (!response.ok) {
      const details = await response.text();
      throw new Error(`Session request failed: ${details}`);
    }

    const payload = await response.json();
    return {
      sessionId: payload.session_id,
      ephemeralKey: payload.ephemeral_key,
      webrtcUrl: payload.webrtc_url,
      customerName: payload.customer_name,
      proactiveRecommendations: payload.proactive_recommendations || [],
    };
  }, []);

  const sendSessionUpdate = useCallback((dataChannel: RTCDataChannel, tools: any[], toolChoiceValue: string, voiceEnabled: boolean = false) => {
    let instructions = SYSTEM_PROMPT;

    // Inject customer context if available
    const { name, recommendations } = customerDataRef.current;
    if (name && recommendations.length > 0) {
      const topRec = recommendations[0];
      const customerContext = `\n\n## CURRENT CUSTOMER CONTEXT\n\nYou are speaking with ${name}.\n\nTOP PRIORITY RECOMMENDATION:\n- Type: ${topRec.type}\n- Priority: ${topRec.priority}\n- Title: ${topRec.title}\n- Talking Point: ${topRec.talking_point}\n${topRec.estimated_savings ? `- Potential Savings: £${topRec.estimated_savings}/month` : ''}\n\nIMPORTANT: Mention this recommendation naturally in your FIRST response, following the proactive nudging guidelines above.`;
      instructions += customerContext;
    }

    const sessionPayload = {
      type: "session.update",
      session: {
        instructions,
        modalities: voiceEnabled ? ["text", "audio"] : ["text"], // Control audio output
        input_audio_transcription: {
          model: "whisper-1"
        }
      },
    };

    if (Array.isArray(tools) && tools.length > 0) {
      (sessionPayload.session as any).tools = tools;
      (sessionPayload.session as any).tool_choice = toolChoiceValue ?? "auto";
    }

    dataChannel.send(JSON.stringify(sessionPayload));
    logMessage(`Sent session.update with ${tools.length} tools, voice=${voiceEnabled}, customer=${name || 'anonymous'}`);
  }, [logMessage]);

  const fulfillFunctionCall = useCallback(async (functionCallItem: any, dataChannel: RTCDataChannel) => {
    const callId = functionCallItem.call_id;
    const functionName = functionCallItem.name;
    const argumentsPayload = functionCallItem.arguments ?? {};

    logMessage(`Model requested function: ${functionName}`);

    // Add tool call message to UI
    onMessage({
      id: crypto.randomUUID(),
      role: 'tool_call',
      content: `Calling ${functionName}`,
      timestamp: Date.now(),
      toolName: functionName,
      toolArgs: argumentsPayload
    });

    try {
      const response = await fetch(`${CONFIG.backendBaseUrl}/function-call`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: functionName,
          call_id: callId,
          arguments: argumentsPayload,
        }),
      });

      if (!response.ok) {
        const detail = await response.text();
        throw new Error(`Backend error (${response.status}): ${detail}`);
      }

      const result = await response.json();

      // Add tool result message to UI
      onMessage({
        id: crypto.randomUUID(),
        role: 'tool_result',
        content: JSON.stringify(result.output, null, 2),
        timestamp: Date.now(),
        toolName: functionName
      });

      // Extract visual metadata from tool result
      if (onVisualUpdate && result.output._visual) {
        console.log('[VISUAL UPDATE]', functionName, result.output._visual);

        // Convert simple visual hints to flexible layout
        const visual = convertToFlexibleVisual(result.output._visual);
        onVisualUpdate(visual);
      }

      // Extract products from device-related tool results
      if (onProductsDiscovered) {
        const deviceTools = [
          'search_devices_by_attributes',
          'get_device_details',
          'compare_devices',
          'get_similar_devices'
        ];

        if (deviceTools.includes(functionName)) {
          const output = result.output;
          let products: any[] = [];

          if (functionName === 'search_devices_by_attributes' && output.devices) {
            products = output.devices;
          } else if (functionName === 'get_device_details' && output.id) {
            products = [output];
          } else if (functionName === 'compare_devices' && output.devices) {
            products = output.devices;
          } else if (functionName === 'get_similar_devices') {
            products = [
              ...(output.cheaper_options || []),
              ...(output.similar_price || []),
              ...(output.premium_options || [])
            ];
          }

          if (products.length > 0) {
            console.log('[PRODUCTS DISCOVERED]', products.length, products);
            onProductsDiscovered(products);
          }
        }

        // Also show accessories as products
        if (functionName === 'get_compatible_accessories' && output.accessories) {
          const accessories = output.accessories.map((acc: any) => ({
            ...acc,
            price_monthly: 0, // Accessories are one-time
            brand: 'Accessory',
            attributes: {}
          }));
          console.log('[ACCESSORIES DISCOVERED]', accessories.length, accessories);
          onProductsDiscovered(accessories);
        }
      }

      // Extract cart updates
      if (onCartUpdated) {
        if (functionName === 'add_to_cart' && result.output.cart_count) {
          // When item added, fetch full cart summary
          try {
            const cartResponse = await fetch(`${CONFIG.backendBaseUrl}/function-call`, {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({
                name: "get_cart_summary",
                call_id: "cart_refresh",
                arguments: { session_id: "default" }
              }),
            });
            if (cartResponse.ok) {
              const cartResult = await cartResponse.json();
              onCartUpdated(cartResult.output);
            }
          } catch (e) {
            console.error("Failed to fetch cart", e);
          }
        } else if (functionName === 'get_cart_summary') {
          onCartUpdated(result.output);
        }
      }

      sendFunctionCallOutput(dataChannel, callId, result.output);
      logMessage(`Provided output for ${functionName}`);
    } catch (error: any) {
      console.error(`Function ${functionName} failed`, error);
      const errorPayload = { error: error.message };
      sendFunctionCallOutput(dataChannel, callId, errorPayload);
      logMessage(`Function ${functionName} failed: ${error.message}`);

      // Notify app of error
      if (onError) {
        onError(error, `Failed to execute ${functionName}`);
      }
    }
  }, [logMessage, onMessage, onError]);

  const sendFunctionCallOutput = useCallback((dataChannel: RTCDataChannel, callId: string, output: any) => {
    const conversationEvent = {
      type: "conversation.item.create",
      item: {
        type: "function_call_output",
        call_id: callId,
        output: JSON.stringify(output),
      },
    };

    dataChannel.send(JSON.stringify(conversationEvent));
    dataChannel.send(JSON.stringify({ type: "response.create" }));
    logMessage(`Sent function_call_output for call ${callId}`);
  }, [logMessage]);

  const handleResponseDone = useCallback(async (event: any, dataChannel: RTCDataChannel) => {
    const response = event.response;
    if (!response || !Array.isArray(response.output)) {
      return;
    }

    for (const item of response.output) {
      if (item.type === "function_call") {
        await fulfillFunctionCall(item, dataChannel);
      }
    }
  }, [fulfillFunctionCall]);

  const initSession = useCallback(async ({ sessionId, ephemeralKey, webrtcUrl, tools, toolChoice }: any) => {
    logMessage(`Negotiating WebRTC connection for session ${sessionId}`);

    const peerConnection = new RTCPeerConnection();
    const audioElement = document.createElement('audio');
    audioElement.autoplay = true;
    document.body.appendChild(audioElement);

    peerConnection.ontrack = (event) => {
      audioElement.srcObject = event.streams[0];
    };

    const clientMedia = await navigator.mediaDevices.getUserMedia({ audio: true });
    const audioTrack = clientMedia.getAudioTracks()[0];
    peerConnection.addTrack(audioTrack);

    const dataChannel = peerConnection.createDataChannel('realtime-channel');

    sessionRef.current = {
      dataChannel,
      peerConnection,
      clientMedia,
    };

    dataChannel.addEventListener('open', () => {
      logMessage('Data channel is open');
      sendSessionUpdate(dataChannel, tools, toolChoice, sessionState.voiceResponseEnabled);
      setSessionState(prev => ({ ...prev, status: 'connected' }));
      onStateChange({ status: 'connected' });
    });

    dataChannel.addEventListener('message', async (event) => {
      const realtimeEvent = JSON.parse(event.data);
      console.log('[REALTIME EVENT]', realtimeEvent.type, realtimeEvent);

      if (realtimeEvent.type === "session.error") {
        logMessage(`Error: ${realtimeEvent.error.message}`);
        // Clear processing state on error
        setSessionState(prev => ({ ...prev, isProcessing: false }));
        // Notify app of error
        if (onError) {
          onError(new Error(realtimeEvent.error.message), 'Session error');
        }
      } else if (realtimeEvent.type === "session.end") {
        logMessage("Session ended.");
      } else if (realtimeEvent.type === "response.output_text.delta") {
        // Handle streaming text (ignore for now, wait for done)
      } else if (realtimeEvent.type === "response.output_text.done" || realtimeEvent.type === "response.text.done") {
        // Add assistant message from text response
        const textContent = realtimeEvent.text || realtimeEvent.output;
        if (textContent) {
          onMessage({
            id: crypto.randomUUID(),
            role: 'assistant',
            content: textContent,
            timestamp: Date.now()
          });
        }
        // Clear processing state when text response is done
        setSessionState(prev => ({ ...prev, isProcessing: false }));
      } else if (realtimeEvent.type === "response.output_audio_transcript.delta") {
        logMessage(`Transcript delta: ${realtimeEvent.delta}`);
      } else if (realtimeEvent.type === "response.audio_transcript.done") {
        // Handle completed AI audio transcript
        if (realtimeEvent.transcript) {
          onMessage({
            id: crypto.randomUUID(),
            role: 'assistant',
            content: realtimeEvent.transcript,
            timestamp: Date.now()
          });
        }
        // Clear processing state when audio transcript is done
        setSessionState(prev => ({ ...prev, isProcessing: false }));
      } else if (realtimeEvent.type === "conversation.item.input_audio_transcription.completed") {
        // Handle user audio transcription
        if (realtimeEvent.transcript) {
          onMessage({
            id: crypto.randomUUID(),
            role: 'user',
            content: realtimeEvent.transcript,
            timestamp: Date.now()
          });
        }
      } else if (realtimeEvent.type === "response.done") {
        await handleResponseDone(realtimeEvent, dataChannel);
        // Clear processing state when response is completely done
        setSessionState(prev => ({ ...prev, isProcessing: false }));
      }
    });

    dataChannel.addEventListener('close', () => {
      logMessage('Data channel is closed');
      setSessionState(prev => ({ ...prev, status: 'ended' }));
      onStateChange({ status: 'ended' });
    });

    const offer = await peerConnection.createOffer();
    await peerConnection.setLocalDescription(offer);

    const sdpResponse = await fetch(`${webrtcUrl}?model=${encodeURIComponent(CONFIG.deployment)}`, {
      method: "POST",
      body: offer.sdp,
      headers: {
        Authorization: `Bearer ${ephemeralKey}`,
        "Content-Type": "application/sdp",
      },
    });

    if (!sdpResponse.ok) {
      throw new Error(`WebRTC negotiation failed (${sdpResponse.status})`);
    }

    const answer: RTCSessionDescriptionInit = { type: "answer" as RTCSdpType, sdp: await sdpResponse.text() };
    await peerConnection.setRemoteDescription(answer);
  }, [logMessage, sendSessionUpdate, handleResponseDone, onMessage, onStateChange]);

  const startSession = useCallback(async () => {
    try {
      setSessionState(prev => ({ ...prev, status: 'connecting' }));
      await ensureToolsLoaded();
      const session = await requestSession(accountNumber);

      logMessage("Ephemeral Key Received: ***");
      logMessage(`WebRTC Session Id = ${session.sessionId}`);

      // Store customer data for session instructions
      if (session.proactiveRecommendations && session.proactiveRecommendations.length > 0) {
        customerDataRef.current = {
          name: session.customerName || null,
          recommendations: session.proactiveRecommendations,
        };
        onRecommendationsReceived?.(session.proactiveRecommendations, session.customerName);
        logMessage(`Received ${session.proactiveRecommendations.length} proactive recommendation(s) for ${session.customerName || 'customer'}`);
      }

      await initSession({
        sessionId: session.sessionId,
        ephemeralKey: session.ephemeralKey,
        webrtcUrl: session.webrtcUrl,
        tools: cachedTools,
        toolChoice,
      });
    } catch (error: any) {
      console.error("Failed to start session", error);
      logMessage(`Error starting session: ${error.message}`);
      setSessionState(prev => ({ ...prev, status: 'idle' }));
      throw error;
    }
  }, [ensureToolsLoaded, requestSession, initSession, logMessage, onRecommendationsReceived, accountNumber]);

  const endSession = useCallback(() => {
    const { dataChannel, peerConnection, clientMedia } = sessionRef.current;
    
    if (dataChannel && dataChannel.readyState === "open") {
      dataChannel.close();
    }
    if (peerConnection) {
      peerConnection.getSenders().forEach(sender => sender.track?.stop());
      peerConnection.close();
    }
    if (clientMedia) {
      clientMedia.getTracks().forEach(track => track.stop());
    }

    // Remove audio element
    const audioElements = document.querySelectorAll('audio[autoplay]');
    audioElements.forEach(el => el.remove());

    sessionRef.current = {
      dataChannel: null,
      peerConnection: null,
      clientMedia: null,
    };

    customerDataRef.current = {
      name: null,
      recommendations: [],
    };

    setSessionState({ status: 'idle', isMuted: false, voiceResponseEnabled: false, isProcessing: false });
    logMessage("Session closed.");
  }, [logMessage]);

  const toggleMute = useCallback(() => {
    const { clientMedia } = sessionRef.current;
    if (clientMedia) {
      const audioTrack = clientMedia.getAudioTracks()[0];
      if (audioTrack) {
        audioTrack.enabled = !audioTrack.enabled;
        setSessionState(prev => ({ ...prev, isMuted: !audioTrack.enabled }));
      }
    }
  }, []);

  const toggleVoiceResponse = useCallback(() => {
    const { dataChannel } = sessionRef.current;
    if (dataChannel && dataChannel.readyState === 'open') {
      const newVoiceState = !sessionState.voiceResponseEnabled;
      setSessionState(prev => ({ ...prev, voiceResponseEnabled: newVoiceState }));

      // Send session update with new modality
      if (cachedTools) {
        sendSessionUpdate(dataChannel, cachedTools, toolChoice, newVoiceState);
      }

      logMessage(newVoiceState ? "Voice responses enabled" : "Voice responses disabled (text only)");
    }
  }, [sessionState.voiceResponseEnabled, logMessage, sendSessionUpdate]);

  const sendTextMessage = useCallback((text: string) => {
    const { dataChannel } = sessionRef.current;
    if (!dataChannel || dataChannel.readyState !== "open") {
      throw new Error("Data channel is not ready. Start the session first.");
    }

    if (!text.trim()) {
      throw new Error("Please enter a message before sending.");
    }

    // Set processing state
    setSessionState(prev => ({ ...prev, isProcessing: true }));

    const conversationEvent = {
      type: "conversation.item.create",
      item: {
        type: "message",
        role: "user",
        content: [
          {
            type: "input_text",
            text,
          },
        ],
      },
    };

    dataChannel.send(JSON.stringify(conversationEvent));
    dataChannel.send(JSON.stringify({ type: "response.create" }));

    // Add user message to UI
    onMessage({
      id: crypto.randomUUID(),
      role: 'user',
      content: text,
      timestamp: Date.now()
    });

    logMessage(`Sent user text: ${text}`);
  }, [logMessage, onMessage]);

  const isConnected = sessionState.status === 'connected';

  // Get current media stream for voice activity detection
  const getCurrentMediaStream = useCallback((): MediaStream | null => {
    return sessionRef.current.clientMedia;
  }, []);

  return {
    sessionState,
    startSession,
    endSession,
    toggleMute,
    toggleVoiceResponse,
    sendTextMessage,
    isConnected,
    getCurrentMediaStream,
  };
}