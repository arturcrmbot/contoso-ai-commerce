import { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Badge } from '@/components/ui/badge';
import { EscalationState } from '@/lib/types';
import { Microphone, PaperPlaneTilt, User, Clock } from '@phosphor-icons/react';
import { VoiceActivityIndicator } from '@/components/VoiceActivityIndicator';
import { SimpleVoiceIndicator } from '@/components/SimpleVoiceIndicator';
import { useVoiceActivity } from '@/hooks/use-voice-activity';
import { useIsMobile } from '@/hooks/use-mobile';

interface ChatComposerProps {
  onSendMessage: (message: string) => void;
  onEscalate: () => void;
  escalationState: EscalationState;
  disabled?: boolean;
  getCurrentMediaStream: () => MediaStream | null;
  isConnected: boolean;
  isMuted: boolean;
  prefilledText?: string;
  onPrefilledTextUsed?: () => void;
}

export function ChatComposer({
  onSendMessage,
  onEscalate,
  escalationState,
  disabled = false,
  getCurrentMediaStream,
  isConnected,
  isMuted,
  prefilledText,
  onPrefilledTextUsed
}: ChatComposerProps) {
  const [message, setMessage] = useState('');

  // Update message when prefilled text changes
  if (prefilledText && prefilledText !== message) {
    setMessage(prefilledText);
    onPrefilledTextUsed?.();
  }
  const isMobile = useIsMobile();

  const mediaStream = getCurrentMediaStream();
  const voiceActivity = useVoiceActivity(
    isConnected && !isMuted ? mediaStream : null,
    {
      threshold: 25,
      smoothing: 0.7,
      minSpeakingTime: 100,
      minSilenceTime: 300
    }
  );

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (message.trim() && !disabled) {
      onSendMessage(message.trim());
      setMessage('');
    }
  };

  const getEscalationButton = () => {
    switch (escalationState.status) {
      case 'available':
        return (
          <Button
            variant="outline"
            size="sm"
            onClick={onEscalate}
            disabled={disabled}
            className="gap-2"
          >
            <User size={16} />
            Request Human
          </Button>
        );
      case 'queued':
        return (
          <Badge variant="secondary" className="gap-2 py-2 px-3">
            <Clock size={16} />
            Queued
            {escalationState.queuePosition && ` (#${escalationState.queuePosition})`}
          </Badge>
        );
      case 'connected':
        return (
          <Badge variant="default" className="gap-2 py-2 px-3">
            <User size={16} />
            Connected to Human
          </Badge>
        );
    }
  };

  return (
    <div className="border-t bg-white/80 backdrop-blur-md supports-[backdrop-filter]:bg-white/60 shadow-[0_-4px_20px_-4px_rgba(0,0,0,0.1)] z-10">
      <div className="p-4 space-y-4 max-w-4xl mx-auto">
        <form onSubmit={handleSubmit} className="flex gap-3 items-end">
          <div className="flex-1 relative group">
            <div className="absolute inset-0 bg-gradient-to-r from-teal-500/20 to-cyan-500/20 rounded-2xl blur opacity-0 group-hover:opacity-100 transition-opacity duration-500" />
            <Input
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              placeholder="Ask about flights, hotels, or travel tips..."
              disabled={disabled}
              className="pr-12 h-14 rounded-2xl border-gray-200 shadow-sm focus-visible:ring-teal-500 text-lg bg-white relative z-10"
            />
            <Button
              type="button"
              variant="ghost"
              size="sm"
              className="absolute right-2 top-1/2 -translate-y-1/2 h-10 w-10 p-0 rounded-xl hover:bg-teal-50 text-teal-600 z-20"
              disabled={disabled}
            >
              <Microphone size={20} weight={voiceActivity.isSpeaking ? "fill" : "regular"} />
              {isMobile ? (
                <SimpleVoiceIndicator
                  isSpeaking={voiceActivity.isSpeaking}
                  isActive={voiceActivity.isActive}
                />
              ) : (
                <VoiceActivityIndicator
                  isSpeaking={voiceActivity.isSpeaking}
                  audioLevel={voiceActivity.audioLevel}
                  isActive={voiceActivity.isActive}
                  size="sm"
                />
              )}
            </Button>
          </div>
          
          <Button 
            type="submit" 
            disabled={disabled || !message.trim()}
            className="h-14 px-6 rounded-2xl bg-gradient-to-r from-teal-600 to-cyan-600 hover:from-teal-700 hover:to-cyan-700 shadow-lg hover:shadow-teal-500/25 transition-all duration-300"
          >
            <PaperPlaneTilt size={20} weight="fill" />
            <span className="ml-2 font-semibold">Send</span>
          </Button>
        </form>

        <div className="flex justify-between items-center px-1">
          <div className="flex items-center gap-3">
            <div className="text-xs font-medium text-gray-500 flex items-center gap-1.5">
              <span className="w-1.5 h-1.5 rounded-full bg-teal-500" />
              Press Enter to send
            </div>
            {voiceActivity.isSpeaking && (
              <Badge variant="outline" className="text-xs py-0.5 px-2 gap-1.5 border-teal-200 bg-teal-50 text-teal-700">
                <div className="w-1.5 h-1.5 bg-teal-500 rounded-full animate-pulse" />
                Listening...
              </Badge>
            )}
          </div>
          
          {getEscalationButton()}
        </div>
      </div>
    </div>
  );
}