import { useState } from 'react';
import { X, Sparkle, TrendUp, Phone, CreditCard, Crown } from '@phosphor-icons/react';
import { Card } from '@/components/ui/card';
import { Button } from '@/components/ui/button';

interface ProactiveRecommendation {
  type: string;
  priority: 'high' | 'medium' | 'low';
  title: string;
  talking_point: string;
  estimated_savings?: number;
  action_items?: string[];
}

interface ProactiveNudgeBannerProps {
  recommendations: ProactiveRecommendation[];
  onDismiss?: () => void;
  onInteract?: (recommendation: ProactiveRecommendation) => void;
}

const PRIORITY_STYLES = {
  high: {
    border: 'border-orange-500',
    bg: 'bg-gradient-to-r from-orange-50 to-red-50',
    text: 'text-orange-700',
    badge: 'bg-orange-100 text-orange-700 border-orange-300',
    icon: 'text-orange-500'
  },
  medium: {
    border: 'border-blue-500',
    bg: 'bg-gradient-to-r from-blue-50 to-indigo-50',
    text: 'text-blue-700',
    badge: 'bg-blue-100 text-blue-700 border-blue-300',
    icon: 'text-blue-500'
  },
  low: {
    border: 'border-gray-400',
    bg: 'bg-gradient-to-r from-gray-50 to-slate-50',
    text: 'text-gray-700',
    badge: 'bg-gray-100 text-gray-700 border-gray-300',
    icon: 'text-gray-500'
  }
};

const TYPE_ICONS: Record<string, any> = {
  plan_upgrade: TrendUp,
  roaming_pass: Phone,
  device_upgrade: Sparkle,
  payment_plan: CreditCard,
  loyalty_reward: Crown
};

const TYPE_LABELS: Record<string, string> = {
  plan_upgrade: 'Data Savings Opportunity',
  roaming_pass: 'Travel Savings',
  device_upgrade: 'Upgrade Offer',
  payment_plan: 'Payment Options',
  loyalty_reward: 'VIP Benefit'
};

export function ProactiveNudgeBanner({
  recommendations,
  onDismiss,
  onInteract
}: ProactiveNudgeBannerProps) {
  const [dismissed, setDismissed] = useState(false);

  if (!recommendations || recommendations.length === 0 || dismissed) {
    return null;
  }

  // Show only the top priority recommendation
  const topRecommendation = recommendations[0];
  const priority = topRecommendation.priority || 'medium';
  const styles = PRIORITY_STYLES[priority];
  const IconComponent = TYPE_ICONS[topRecommendation.type] || Sparkle;
  const label = TYPE_LABELS[topRecommendation.type] || 'Recommendation';

  const handleDismiss = () => {
    setDismissed(true);
    onDismiss?.();
  };

  const handleInteract = () => {
    onInteract?.(topRecommendation);
  };

  return (
    <Card className={`${styles.border} ${styles.bg} border-2 shadow-md mb-4 overflow-hidden`}>
      <div className="p-4 flex items-start gap-3">
        {/* Icon */}
        <div className={`flex-shrink-0 ${styles.icon}`}>
          <IconComponent size={24} weight="duotone" />
        </div>

        {/* Content */}
        <div className="flex-1 min-w-0">
          {/* Type Badge */}
          <div className="flex items-center gap-2 mb-1">
            <span className={`text-xs font-medium px-2 py-0.5 rounded-full border ${styles.badge}`}>
              {label}
            </span>
            {priority === 'high' && (
              <span className="text-xs font-semibold text-orange-600 animate-pulse">
                ⚡ High Priority
              </span>
            )}
          </div>

          {/* Title */}
          {topRecommendation.title && (
            <h4 className={`font-semibold text-sm mb-1 ${styles.text}`}>
              {topRecommendation.title}
            </h4>
          )}

          {/* Talking Point */}
          <p className="text-sm text-gray-700 mb-2">
            {topRecommendation.talking_point}
          </p>

          {/* Savings Badge */}
          {topRecommendation.estimated_savings && (
            <div className="inline-flex items-center gap-1 text-xs font-medium text-green-700 bg-green-100 px-2 py-1 rounded">
              💰 Save up to £{topRecommendation.estimated_savings}/month
            </div>
          )}

          {/* CTA */}
          {onInteract && (
            <Button
              variant="outline"
              size="sm"
              onClick={handleInteract}
              className={`mt-2 ${styles.text} border-current hover:bg-white/50`}
            >
              Ask me about this
            </Button>
          )}
        </div>

        {/* Dismiss Button */}
        <button
          onClick={handleDismiss}
          className="flex-shrink-0 p-1 rounded hover:bg-white/50 transition-colors text-gray-400 hover:text-gray-600"
          aria-label="Dismiss"
        >
          <X size={18} weight="bold" />
        </button>
      </div>
    </Card>
  );
}
