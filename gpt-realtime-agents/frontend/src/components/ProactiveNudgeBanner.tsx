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
    border: 'border-orange-400',
    bg: 'bg-gradient-to-r from-orange-100 to-red-100',
    text: 'text-orange-900',
    badge: 'bg-orange-200 text-orange-900 border-orange-400',
    icon: 'text-orange-600'
  },
  medium: {
    border: 'border-blue-400',
    bg: 'bg-gradient-to-r from-blue-100 to-indigo-100',
    text: 'text-blue-900',
    badge: 'bg-blue-200 text-blue-900 border-blue-400',
    icon: 'text-blue-600'
  },
  low: {
    border: 'border-gray-400',
    bg: 'bg-gradient-to-r from-gray-100 to-slate-100',
    text: 'text-gray-900',
    badge: 'bg-gray-200 text-gray-900 border-gray-400',
    icon: 'text-gray-600'
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
    <Card className={`${styles.border} ${styles.bg} border-2 shadow-lg mb-6 overflow-hidden`}>
      <div className="p-6 flex items-start gap-4">
        {/* Icon */}
        <div className={`flex-shrink-0 ${styles.icon}`}>
          <IconComponent size={32} weight="duotone" />
        </div>

        {/* Content */}
        <div className="flex-1 min-w-0">
          {/* Type Badge */}
          <div className="flex items-center gap-2 mb-2">
            <span className={`text-xs font-medium px-3 py-1 rounded-full border ${styles.badge}`}>
              {label}
            </span>
            {priority === 'high' && (
              <span className="text-xs font-semibold text-orange-700 animate-pulse">
                ⚡ High Priority
              </span>
            )}
          </div>

          {/* Title */}
          {topRecommendation.title && (
            <h4 className={`font-semibold text-base mb-2 ${styles.text}`}>
              {topRecommendation.title}
            </h4>
          )}

          {/* Talking Point */}
          <p className="text-sm text-gray-900 mb-3 leading-relaxed">
            {topRecommendation.talking_point}
          </p>

          {/* Savings Badge */}
          {topRecommendation.estimated_savings && (
            <div className="inline-flex items-center gap-1 text-xs font-medium text-green-700 bg-green-100 px-3 py-1.5 rounded mb-3">
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
          className="flex-shrink-0 p-2 rounded hover:bg-white/50 transition-colors text-gray-400 hover:text-gray-600"
          aria-label="Dismiss"
        >
          <X size={20} weight="bold" />
        </button>
      </div>
    </Card>
  );
}
