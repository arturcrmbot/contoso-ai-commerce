import { useState, useCallback, useEffect, useRef } from 'react';
import { toast, Toaster } from 'sonner';
import { CallControls } from '@/components/CallControls';
import { DynamicVisualCanvas } from '@/components/contoso/DynamicVisualCanvas';
import { CartIcon } from '@/components/contoso/CartIcon';
import { CartSummary } from '@/components/contoso/CartSummary';
import { MessageBubble } from '@/components/MessageBubble';
import { ChatComposer } from '@/components/ChatComposer';
import { ProfileSelector } from '@/components/ProfileSelector';
import { ProactiveNudgeBanner } from '@/components/ProactiveNudgeBanner';
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

  // Cart state
  const [cartItems, setCartItems] = useState<any[]>([]);
  const [cartOpen, setCartOpen] = useState(false);

  // Prefilled text state
  const [prefilledText, setPrefilledText] = useState<string>('');

  // Customer profile state
  const [selectedProfile, setSelectedProfile] = useState<string | null>(null);
  const [recommendations, setRecommendations] = useState<any[]>([]);
  const [customerName, setCustomerName] = useState<string | null>(null);

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

  const handleCartUpdated = useCallback((cartData: any) => {
    if (cartData.items) {
      setCartItems(cartData.items);
    }
  }, []);

  const handleRecommendationsReceived = useCallback((recs: any[], name?: string) => {
    setRecommendations(recs);
    if (name) {
      setCustomerName(name);
    }
  }, []);

  const { sessionState, startSession, endSession, toggleMute, toggleVoiceResponse, sendTextMessage, isConnected, getCurrentMediaStream } = useRealtimeSession({
    onMessage: handleMessage,
    onStateChange: handleStateChange,
    onVisualUpdate: handleVisualUpdate,
    onCartUpdated: handleCartUpdated,
    onRecommendationsReceived: handleRecommendationsReceived,
    accountNumber: selectedProfile
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

  const handleProductClick = (params: any) => {
    // Handle different click types
    if (!params) return;

    let message = '';

    // If it's an explicit add_to_cart action from a button
    if (params.action === 'add_to_cart' || params.action === 'add_accessory') {
      const itemName = params.name || params.device_id || params.item_id || 'this item';
      message = `I want to purchase ${itemName}`;
    }
    // If it's a product object from clicking a card (just browsing)
    else if (params.id && params.name) {
      message = `Tell me more about the ${params.name}`;
    }
    // Fallback - assume it's browsing, not purchasing
    else {
      const name = params.name || params.title || 'this item';
      message = `Tell me more about ${name}`;
    }

    // Auto-send the message instead of just prefilling
    if (isConnected && message) {
      handleSendMessage(message);
    } else if (!isConnected) {
      toast.info('Please start a call first');
    }
  };

  const handlePrefilledTextUsed = () => {
    setPrefilledText('');
  };

  const handleRemoveCartItem = (itemId: string) => {
    // Send message to AI to remove item
    handleSendMessage(`Please remove item ${itemId} from my cart`);
  };

  const handleCheckout = () => {
    setCartOpen(false);
    handleSendMessage('I would like to proceed with checkout');
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

  const handleRecommendationInteract = (recommendation: any) => {
    // User clicked "Ask me about this" on a recommendation
    const message = `Tell me more about ${recommendation.title || 'this recommendation'}`;
    handleSendMessage(message);
  };

  const handleRecommendationDismiss = () => {
    setRecommendations([]);
  };

  const totalMonthly = cartItems.reduce((sum, item) => sum + (item.price_monthly || 0), 0);

  return (
    <div className="h-screen bg-background flex flex-col overflow-hidden">
      <ProfileSelector
        selectedProfile={selectedProfile}
        onProfileChange={setSelectedProfile}
        disabled={sessionState.status !== 'idle'}
      />
      <CallControls
        sessionState={sessionState}
        onStartCall={handleStartCall}
        onEndCall={endSession}
        onToggleMute={toggleMute}
        onToggleVoiceResponse={toggleVoiceResponse}
        getCurrentMediaStream={getCurrentMediaStream}
        cartIcon={
          <CartIcon
            count={cartItems.length}
            totalMonthly={totalMonthly}
            onClick={() => setCartOpen(true)}
          />
        }
      />

      <div className="flex-1 flex overflow-hidden min-h-0">
        {/* Left Panel - Dynamic Visual Canvas (70%) */}
        <div className="w-[70%] border-r bg-muted/30 min-w-0 overflow-hidden">
          <div className="h-full p-4 flex flex-col min-h-0">
            {/* Proactive Nudge Banner */}
            {isConnected && recommendations.length > 0 && (
              <ProactiveNudgeBanner
                recommendations={recommendations}
                onDismiss={handleRecommendationDismiss}
                onInteract={handleRecommendationInteract}
              />
            )}

            <DynamicVisualCanvas
              visualConfig={currentVisual}
              onProductClick={handleProductClick}
              onBackToSuggestions={() => setCurrentVisual(null)}
              onSuggestionClick={handleSuggestionClick}
              disabled={!isConnected}
            />
          </div>
        </div>

        {/* Right Panel - Chat (30%) */}
        <div className="w-[30%] flex flex-col min-w-0 overflow-hidden">
          <div className="flex-1 bg-card border-l overflow-hidden flex flex-col min-h-0">
            {/* Chat Header with Clear Button */}
            <div className="border-b p-3 flex items-center justify-between bg-card flex-shrink-0">
              <h3 className="font-semibold text-sm">Chat</h3>
              <Button
                variant="ghost"
                size="sm"
                onClick={handleClearChat}
                disabled={(messages || []).length === 0}
                className="h-8 px-2 text-xs"
              >
                <Trash size={14} className="mr-1" />
                Clear
              </Button>
            </div>

            {/* Chat Messages */}
            <div
              ref={chatScrollRef}
              className="flex-1 overflow-y-auto p-4 space-y-4 chat-scroll min-h-0"
            >
              {(messages || []).length === 0 ? (
                <div className="flex items-center justify-center h-full text-muted-foreground">
                  <div className="text-center">
                    <h3 className="text-lg font-semibold mb-2">Welcome to Vodafone Three</h3>
                    <p className="text-sm">Start Session to get started</p>
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

      {/* Cart Summary Modal */}
      <CartSummary
        isOpen={cartOpen}
        onClose={() => setCartOpen(false)}
        items={cartItems}
        onRemoveItem={handleRemoveCartItem}
        onCheckout={handleCheckout}
      />

      <Toaster position="top-right" />
    </div>
  );
}

export default App;
