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

  // Chat visibility state
  const [chatExpanded, setChatExpanded] = useState(false);

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

  // Clear cart on browser refresh/mount
  useEffect(() => {
    setCartItems([]);
  }, []);

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

  const handleEndCall = () => {
    // Clear the cart when ending the call
    setCartItems([]);
    setCartOpen(false);
    endSession();
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
      <CallControls
        sessionState={sessionState}
        onStartCall={handleStartCall}
        onEndCall={handleEndCall}
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

      {/* Full-width deal area */}
      <div className="flex-1 overflow-hidden min-h-0">
        <div className="h-full p-6 overflow-y-auto">
          <DynamicVisualCanvas
            visualConfig={currentVisual}
            onProductClick={handleProductClick}
            onBackToSuggestions={() => setCurrentVisual(null)}
            onSuggestionClick={handleSuggestionClick}
            disabled={!isConnected}
          />
        </div>
      </div>

      {/* Floating Chat Button */}
      {!chatExpanded && (
        <button
          onClick={() => setChatExpanded(true)}
          className="fixed bottom-6 right-6 z-40 w-16 h-16 bg-gradient-to-r from-teal-500 to-cyan-600 hover:from-teal-600 hover:to-cyan-700 text-white rounded-full shadow-2xl flex items-center justify-center transition-all hover:scale-110"
        >
          <svg className="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
          </svg>
          {(messages || []).length > 0 && (
            <span className="absolute -top-1 -right-1 w-6 h-6 bg-red-500 rounded-full text-xs flex items-center justify-center font-bold">
              {(messages || []).length}
            </span>
          )}
        </button>
      )}

      {/* Floating Chat Window */}
      {chatExpanded && (
        <div className="fixed bottom-6 right-6 z-40 w-96 h-[600px] bg-white dark:bg-gray-900 rounded-2xl shadow-2xl flex flex-col overflow-hidden border border-gray-200 dark:border-gray-800">
          {/* Chat Header */}
          <div className="bg-gradient-to-r from-teal-500 to-cyan-600 p-4 flex items-center justify-between text-white flex-shrink-0">
            <div className="flex items-center gap-2">
              <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
              </svg>
              <h3 className="font-semibold">Travel Assistant</h3>
            </div>
            <div className="flex items-center gap-2">
              <Button
                variant="ghost"
                size="sm"
                onClick={handleClearChat}
                disabled={(messages || []).length === 0}
                className="h-8 px-2 text-xs text-white hover:bg-white/20"
              >
                <Trash size={14} className="mr-1" />
                Clear
              </Button>
              <button
                onClick={() => setChatExpanded(false)}
                className="hover:bg-white/20 rounded-full p-1.5"
              >
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>
          </div>

          {/* Chat Messages */}
          <div
            ref={chatScrollRef}
            className="flex-1 overflow-y-auto p-4 space-y-4 bg-gray-50 dark:bg-gray-950"
          >
            {(messages || []).length === 0 ? (
              <div className="flex items-center justify-center h-full text-muted-foreground">
                <div className="text-center">
                  <h3 className="text-lg font-semibold mb-2">Your Travel Assistant</h3>
                  <p className="text-sm">Start a session to discover amazing deals</p>
                </div>
              </div>
            ) : (
              (messages || []).map((message) => (
                <MessageBubble key={message.id} message={message} />
              ))
            )}
          </div>

          {/* Chat Composer */}
          <div className="flex-shrink-0 bg-white dark:bg-gray-900 border-t dark:border-gray-800">
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
      )}

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
