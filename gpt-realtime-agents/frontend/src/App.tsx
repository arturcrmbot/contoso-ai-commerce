import { useState, useCallback, useEffect, useRef } from 'react';
import { toast, Toaster } from 'sonner';
import { CallControls } from '@/components/CallControls';
import { DynamicVisualCanvas } from '@/components/contoso/DynamicVisualCanvas';
import { BetSlipIcon } from '@/components/betting/BetSlipIcon';
import { BetSlipPanel, BetSelection } from '@/components/betting/BetSlipPanel';
import { MessageBubble } from '@/components/MessageBubble';
import { ChatComposer } from '@/components/ChatComposer';
import { useRealtimeSession } from '@/hooks/use-realtime-session';
import { ChatMessage, EscalationState } from '@/lib/types';
import { Button } from '@/components/ui/button';
import { Trash } from '@phosphor-icons/react';

function App() {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [escalationState, setEscalationState] = useState<EscalationState>({ status: 'available' });
  const chatScrollRef = useRef<HTMLDivElement>(null);

  // Dynamic visual state
  const [currentVisual, setCurrentVisual] = useState<any | null>(null);

  // Bet slip state (replaces cart)
  const [betSelections, setBetSelections] = useState<BetSelection[]>([]);
  const [betSlipOpen, setBetSlipOpen] = useState(false);

  // Prefilled text state
  const [prefilledText, setPrefilledText] = useState<string>('');

  const handleMessage = useCallback((message: ChatMessage) => {
    setMessages(prev => [...(prev || []), message]);
  }, [setMessages]);

  const handleStateChange = useCallback((state: any) => {
    if (state.status === 'connected') {
      toast.success('Call connected successfully');
    } else if (state.status === 'ended') {
      toast.info('Call ended');
    }
  }, []);

  const handleVisualUpdate = useCallback((visualConfig: any) => {
    console.log('[APP] Visual update received:', visualConfig);
    setCurrentVisual(visualConfig);
  }, []);

  const handleBetSlipUpdated = useCallback((slipData: any) => {
    console.log('[APP] Bet slip updated:', slipData);
    if (slipData.selections) {
      setBetSelections(slipData.selections);
    }
  }, []);

  const { sessionState, startSession, endSession, toggleMute, toggleVoiceResponse, sendTextMessage, isConnected, getCurrentMediaStream } = useRealtimeSession({
    onMessage: handleMessage,
    onStateChange: handleStateChange,
    onVisualUpdate: handleVisualUpdate,
    onBetSlipUpdated: handleBetSlipUpdated
  });

  // Auto-scroll to bottom when new messages arrive
  useEffect(() => {
    if (chatScrollRef.current) {
      chatScrollRef.current.scrollTop = chatScrollRef.current.scrollHeight;
    }
  }, [messages]);

  const handleStartCall = async () => {
    try {
      await startSession();
    } catch (error: any) {
      toast.error(`Failed to start call: ${error.message}`);
    }
  };

  const handleSendMessage = (text: string) => {
    try {
      sendTextMessage(text);
    } catch (error: any) {
      toast.error(`Failed to send message: ${error.message}`);
    }
  };

  const handleSuggestionClick = (prompt: string) => {
    if (isConnected) {
      handleSendMessage(prompt);
    } else {
      toast.info('Please start a call first');
    }
  };

  // Handle actions from visual components (match cards, etc.)
  const handleVisualAction = (params: any) => {
    if (!params) return;

    let message = '';

    // Handle betting actions from MatchCard/MatchGrid
    if (params.action === 'add_to_slip') {
      const { eventId, market, selection, odds, team } = params;
      message = `Add ${team || selection} to win at odds ${odds} to my bet slip for match ${eventId}`;
    }
    // Handle view match details
    else if (params.action === 'view_match') {
      message = `Show me details for match ${params.eventId}`;
    }
    // Legacy: handle product clicks (for backwards compatibility)
    else if (params.action === 'add_to_cart' || params.action === 'add_accessory') {
      const itemName = params.name || params.device_id || params.item_id || 'this item';
      message = `I want to purchase ${itemName}`;
    }
    else if (params.id && params.name) {
      message = `Tell me more about the ${params.name}`;
    }
    else {
      const name = params.name || params.title || 'this item';
      message = `Tell me more about ${name}`;
    }

    if (isConnected && message) {
      handleSendMessage(message);
    } else if (!isConnected) {
      toast.info('Please start a call first');
    }
  };

  const handlePrefilledTextUsed = () => {
    setPrefilledText('');
  };

  const handleRemoveSelection = (selectionId: string) => {
    // Send message to AI to remove selection from bet slip
    handleSendMessage(`Remove selection ${selectionId} from my bet slip`);
  };

  const handlePlaceBet = (stake: number) => {
    setBetSlipOpen(false);
    handleSendMessage(`Place my bet with a stake of £${stake}`);
  };

  const handleClearSlip = () => {
    handleSendMessage('Clear my bet slip');
  };

  const handleEscalate = () => {
    setEscalationState({ status: 'queued', queuePosition: 1 });
    toast.info('Connecting you to a human agent...');

    // Simulate queue processing
    setTimeout(() => {
      setEscalationState({ status: 'connected' });
      toast.success('Connected to human agent');

      // Add human agent message
      const humanMessage: ChatMessage = {
        id: crypto.randomUUID(),
        role: 'human_agent',
        content: 'Hi! I\'m a human agent taking over this conversation. I can see your chat history. How can I help you further?',
        timestamp: Date.now()
      };
      setMessages(prev => [...(prev || []), humanMessage]);
    }, 3000);
  };

  const handleClearChat = () => {
    setMessages([]);
    setCurrentVisual(null);
    toast.info('Chat cleared');
  };

  // Calculate potential return for bet slip icon
  const combinedOdds = betSelections.reduce((acc, sel) => acc * sel.odds, 1);
  const defaultStake = 10;
  const potentialReturn = betSelections.length > 0 ? defaultStake * combinedOdds : 0;

  return (
    <div className="h-screen bg-slate-900 flex flex-col overflow-hidden">
      <CallControls
        sessionState={sessionState}
        onStartCall={handleStartCall}
        onEndCall={endSession}
        onToggleMute={toggleMute}
        onToggleVoiceResponse={toggleVoiceResponse}
        getCurrentMediaStream={getCurrentMediaStream}
        cartIcon={
          <BetSlipIcon
            count={betSelections.length}
            potentialReturn={potentialReturn}
            onClick={() => setBetSlipOpen(true)}
          />
        }
      />

      <div className="flex-1 flex overflow-hidden min-h-0">
        {/* Left Panel - Dynamic Visual Canvas (70%) */}
        <div className="w-[70%] border-r border-slate-700 bg-slate-900 min-w-0 overflow-hidden">
          <div className="h-full p-4 flex flex-col min-h-0">
            <DynamicVisualCanvas
              visualConfig={currentVisual}
              onProductClick={handleVisualAction}
              onBackToSuggestions={() => setCurrentVisual(null)}
              onSuggestionClick={handleSuggestionClick}
              disabled={!isConnected}
            />
          </div>
        </div>

        {/* Right Panel - Chat (30%) */}
        <div className="w-[30%] flex flex-col min-w-0 overflow-hidden">
          <div className="flex-1 bg-slate-800 border-l border-slate-700 overflow-hidden flex flex-col min-h-0">
            {/* Chat Header with Clear Button */}
            <div className="border-b border-slate-700 p-3 flex items-center justify-between bg-slate-800 flex-shrink-0">
              <h3 className="font-semibold text-sm text-white">Chat</h3>
              <Button
                variant="ghost"
                size="sm"
                onClick={handleClearChat}
                disabled={(messages || []).length === 0}
                className="h-8 px-2 text-xs text-slate-400 hover:text-white hover:bg-slate-700"
              >
                <Trash size={14} className="mr-1" />
                Clear
              </Button>
            </div>

            {/* Chat Messages */}
            <div
              ref={chatScrollRef}
              className="flex-1 overflow-y-auto p-4 space-y-4 chat-scroll min-h-0 bg-slate-800"
            >
              {(messages || []).length === 0 ? (
                <div className="flex items-center justify-center h-full text-slate-400">
                  <div className="text-center">
                    <h3 className="text-lg font-semibold mb-2 text-white">Welcome to Contoso Bet</h3>
                    <p className="text-sm text-slate-400">Start betting on football matches</p>
                  </div>
                </div>
              ) : (
                (messages || []).map((message) => (
                  <MessageBubble key={message.id} message={message} />
                ))
              )}
            </div>

            {/* Chat Composer */}
            <div className="flex-shrink-0">
              <ChatComposer
                onSendMessage={handleSendMessage}
                onEscalate={handleEscalate}
                escalationState={escalationState}
                disabled={!isConnected}
                getCurrentMediaStream={getCurrentMediaStream}
                isConnected={isConnected}
                isMuted={sessionState.isMuted}
                prefilledText={prefilledText}
                onPrefilledTextUsed={handlePrefilledTextUsed}
              />
            </div>
          </div>
        </div>
      </div>

      {/* Bet Slip Panel */}
      <BetSlipPanel
        isOpen={betSlipOpen}
        onClose={() => setBetSlipOpen(false)}
        selections={betSelections}
        onRemoveSelection={handleRemoveSelection}
        onPlaceBet={handlePlaceBet}
        onClearSlip={handleClearSlip}
      />

      <Toaster position="top-right" />
    </div>
  );
}

export default App;
