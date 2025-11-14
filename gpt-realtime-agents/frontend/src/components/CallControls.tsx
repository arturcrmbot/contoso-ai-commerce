import { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Input } from '@/components/ui/input';
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from '@/components/ui/tooltip';
import { SessionState } from '@/lib/types';
import { Phone, PhoneX, Microphone, MicrophoneSlash, PhoneCall, SpeakerHigh, SpeakerSlash } from '@phosphor-icons/react';
import { VoiceActivityIndicator } from '@/components/VoiceActivityIndicator';
import { WaveformVisualizer } from '@/components/WaveformVisualizer';
import { SimpleVoiceIndicator } from '@/components/SimpleVoiceIndicator';
import { useVoiceActivity } from '@/hooks/use-voice-activity';
import { useIsMobile } from '@/hooks/use-mobile';
import { CLIENT_CONFIG } from '@/lib/constants';
import { toast } from 'sonner';

interface CallControlsProps {
  sessionState: SessionState;
  onStartCall: () => void;
  onEndCall: () => void;
  onToggleMute: () => void;
  onToggleVoiceResponse: () => void;
  getCurrentMediaStream: () => MediaStream | null;
  cartIcon?: React.ReactNode;
}

export function CallControls({ sessionState, onStartCall, onEndCall, onToggleMute, onToggleVoiceResponse, getCurrentMediaStream, cartIcon }: CallControlsProps) {
  const isMobile = useIsMobile();
  const mediaStream = getCurrentMediaStream();
  const [phoneNumber, setPhoneNumber] = useState('');
  const [isCallingMobile, setIsCallingMobile] = useState(false);
  
  const voiceActivity = useVoiceActivity(
    sessionState.status === 'connected' && !sessionState.isMuted ? mediaStream : null,
    {
      threshold: 25,
      smoothing: 0.7,
      minSpeakingTime: 150,
      minSilenceTime: 400
    }
  );

  const getStatusText = () => {
    switch (sessionState.status) {
      case 'idle': return 'Idle';
      case 'connecting': return 'Connecting';
      case 'connected': return 'Live';
      case 'ended': return 'Ended';
      default: return 'Unknown';
    }
  };

  const getStatusVariant = () => {
    switch (sessionState.status) {
      case 'idle': return 'secondary' as const;
      case 'connecting': return 'default' as const;
      case 'connected': return 'default' as const;
      case 'ended': return 'destructive' as const;
      default: return 'secondary' as const;
    }
  };

  const isConnected = sessionState.status === 'connected';
  const isConnecting = sessionState.status === 'connecting';

  const handleCallMobile = async () => {
    if (!phoneNumber.trim()) {
      toast.error('Please enter a phone number');
      return;
    }

    setIsCallingMobile(true);
    try {
      const response = await fetch(`${CLIENT_CONFIG.backendBaseUrl}/call`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          number: phoneNumber,
        }),
      });

      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`Call failed: ${errorText}`);
      }

      const result = await response.json();
      toast.success(`Call initiated to ${phoneNumber}`);
      console.log('Call response:', result);
    } catch (error: any) {
      toast.error(`Failed to call: ${error.message}`);
      console.error('Call error:', error);
    } finally {
      setIsCallingMobile(false);
    }
  };
  
  return (
    <TooltipProvider>
      <div className="sticky top-0 z-50 bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60 border-b">
        <div className="flex items-center justify-between p-4">
          <div className="flex items-center gap-4">
            {/* Travel Agent Branding */}
            <div className="flex items-center gap-3 mr-2">
              <div className="flex items-center gap-2">
                <svg className="w-8 h-8 text-teal-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                <div>
                  <h1 className="text-xl font-bold bg-gradient-to-r from-teal-600 to-cyan-600 bg-clip-text text-transparent">Travel Agent AI</h1>
                </div>
              </div>
            </div>

            <Button
              onClick={isConnected ? onEndCall : onStartCall}
              disabled={isConnecting}
              variant={isConnected ? "destructive" : "default"}
              size="lg"
              className={`gap-2 px-6 py-3 text-base font-semibold ${
                isConnected
                  ? ''
                  : 'bg-gradient-to-r from-teal-500 to-cyan-600 hover:from-teal-600 hover:to-cyan-700 text-white'
              } ${!isConnected && !isConnecting ? 'start-call-pulse' : ''}`}
            >
              {isConnected ? (
                <>
                  <PhoneX size={22} />
                  End Session
                </>
              ) : (
                <>
                  <Phone size={22} />
                  {isConnecting ? 'Connecting...' : 'Start Session'}
                </>
              )}
            </Button>

            
            {isConnected && (
              <div className="flex items-center gap-1">
                <Tooltip>
                  <TooltipTrigger asChild>
                    <Button
                      onClick={onToggleMute}
                      variant="outline"
                      size="lg"
                      className="gap-2"
                    >
                      {sessionState.isMuted ? (
                        <MicrophoneSlash size={20} />
                      ) : (
                        <Microphone size={20} />
                      )}
                    </Button>
                  </TooltipTrigger>
                  <TooltipContent>
                    {sessionState.isMuted ? "Unmute microphone" : "Mute microphone"}
                  </TooltipContent>
                </Tooltip>

                <Tooltip>
                  <TooltipTrigger asChild>
                    <Button
                      onClick={onToggleVoiceResponse}
                      variant={sessionState.voiceResponseEnabled ? "default" : "outline"}
                      size="lg"
                      className="gap-2"
                    >
                      {sessionState.voiceResponseEnabled ? (
                        <SpeakerHigh size={20} />
                      ) : (
                        <SpeakerSlash size={20} />
                      )}
                    </Button>
                  </TooltipTrigger>
                  <TooltipContent>
                    {sessionState.voiceResponseEnabled ? "Voice responses ON" : "Voice responses OFF (text only)"}
                  </TooltipContent>
                </Tooltip>
                {/* Voice activity indicator with tooltip */}
                <Tooltip>
                  <TooltipTrigger asChild>
                    <div className="flex items-center">
                      {/* Use simpler indicator on mobile for better performance */}
                      {isMobile ? (
                        <SimpleVoiceIndicator
                          isSpeaking={voiceActivity.isSpeaking}
                          isActive={voiceActivity.isActive && !sessionState.isMuted}
                          className="ml-1"
                        />
                      ) : (
                        <VoiceActivityIndicator
                          isSpeaking={voiceActivity.isSpeaking}
                          audioLevel={voiceActivity.audioLevel}
                          isActive={voiceActivity.isActive && !sessionState.isMuted}
                          size="sm"
                          className="ml-1"
                        />
                      )}
                    </div>
                  </TooltipTrigger>
                  <TooltipContent>
                    <p>
                      {sessionState.isMuted 
                        ? "Microphone muted" 
                        : voiceActivity.isSpeaking 
                          ? "Voice detected" 
                          : voiceActivity.isActive 
                            ? "Listening for voice" 
                            : "Voice detection inactive"
                      }
                    </p>
                  </TooltipContent>
                </Tooltip>
              </div>
            )}
            
            {/* Voice Activity Waveform - Only on desktop */}
            {isConnected && !sessionState.isMuted && !isMobile && (
              <Tooltip>
                <TooltipTrigger asChild>
                  <div className="flex items-center gap-2 px-3 py-2 bg-muted/30 rounded-lg">
                    <WaveformVisualizer
                      mediaStream={mediaStream}
                      isActive={voiceActivity.isActive}
                      width={80}
                      height={24}
                      barCount={8}
                    />
                    {voiceActivity.isSpeaking && (
                      <span className="text-xs text-primary font-medium">Speaking</span>
                    )}
                  </div>
                </TooltipTrigger>
                <TooltipContent>
                  <p>Live audio waveform - shows your voice activity</p>
                </TooltipContent>
              </Tooltip>
            )}
          </div>

          <div className="flex items-center gap-3">
            {cartIcon}
            <Badge variant={getStatusVariant()}>
              {getStatusText()}
              {sessionState.isMuted && ' (Muted)'}
            </Badge>
          </div>
        </div>
      </div>
    </TooltipProvider>
  );
}