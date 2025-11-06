import { Card, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { CheckCircle, TrendUp, Sparkle } from '@phosphor-icons/react';

interface TradeInValueProps {
  data: {
    device_model: string;
    condition: 'excellent' | 'good' | 'fair' | 'poor';
    trade_in_value: number;
    original_price?: number;
    factors?: {
      screen_condition: string;
      battery_health: string;
      physical_damage: string;
    };
    bonus_offer?: string;
    next_steps?: string[];
  };
  emphasis?: 'low' | 'medium' | 'high' | 'critical';
}

export function TradeInValue({ data, emphasis = 'medium' }: TradeInValueProps) {
  const getConditionConfig = () => {
    switch (data.condition) {
      case 'excellent':
        return {
          color: 'text-green-600',
          bgColor: 'bg-green-100',
          badge: 'default',
          icon: <CheckCircle size={32} weight="fill" className="text-green-600" />
        };
      case 'good':
        return {
          color: 'text-blue-600',
          bgColor: 'bg-blue-100',
          badge: 'secondary',
          icon: <TrendUp size={32} weight="fill" className="text-blue-600" />
        };
      case 'fair':
        return {
          color: 'text-yellow-600',
          bgColor: 'bg-yellow-100',
          badge: 'secondary',
          icon: <TrendUp size={32} weight="regular" className="text-yellow-600" />
        };
      case 'poor':
        return {
          color: 'text-gray-600',
          bgColor: 'bg-gray-100',
          badge: 'secondary',
          icon: <TrendUp size={32} weight="light" className="text-gray-600" />
        };
    }
  };

  const config = getConditionConfig();
  const emphasisClasses = {
    low: '',
    medium: 'border-2',
    high: 'border-2 shadow-lg',
    critical: 'border-4 shadow-2xl'
  };

  const percentOfOriginal = data.original_price
    ? Math.round((data.trade_in_value / data.original_price) * 100)
    : null;

  return (
    <Card className={`${emphasisClasses[emphasis]} transition-all`}>
      <CardContent className="p-6">
        {/* Device Model */}
        <div className="text-center mb-4">
          <h3 className="text-xl font-bold mb-1">{data.device_model}</h3>
          <Badge variant={config.badge as any} className="capitalize">
            {data.condition} Condition
          </Badge>
        </div>

        {/* Trade-In Value - Prominent Display */}
        <div className={`${config.bgColor} rounded-lg p-6 mb-4 text-center`}>
          <div className="flex items-center justify-center gap-2 mb-2">
            {config.icon}
            <p className="text-sm text-muted-foreground font-medium">Trade-In Value</p>
          </div>
          <p className={`text-5xl font-bold ${config.color}`}>
            £{data.trade_in_value}
          </p>
          {percentOfOriginal && (
            <p className="text-xs text-muted-foreground mt-2">
              {percentOfOriginal}% of original value
            </p>
          )}
        </div>

        {/* Bonus Offer */}
        {data.bonus_offer && (
          <div className="bg-gradient-to-r from-purple-100 to-pink-100 rounded-lg p-4 mb-4 flex items-start gap-3">
            <Sparkle size={24} weight="fill" className="text-purple-600 flex-shrink-0" />
            <div>
              <p className="font-semibold text-sm mb-1">Bonus Offer!</p>
              <p className="text-sm text-muted-foreground">{data.bonus_offer}</p>
            </div>
          </div>
        )}

        {/* Condition Factors */}
        {data.factors && (
          <div className="mb-4">
            <h4 className="text-sm font-semibold mb-2">Condition Assessment:</h4>
            <div className="space-y-2 text-sm">
              <div className="flex justify-between">
                <span className="text-muted-foreground">Screen:</span>
                <span className="font-medium">{data.factors.screen_condition}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-muted-foreground">Battery:</span>
                <span className="font-medium">{data.factors.battery_health}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-muted-foreground">Physical:</span>
                <span className="font-medium">{data.factors.physical_damage}</span>
              </div>
            </div>
          </div>
        )}

        {/* Next Steps */}
        {data.next_steps && data.next_steps.length > 0 && (
          <div className="border-t pt-4">
            <h4 className="text-sm font-semibold mb-2">Next Steps:</h4>
            <ul className="space-y-1">
              {data.next_steps.map((step, idx) => (
                <li key={idx} className="text-sm text-muted-foreground flex items-start gap-2">
                  <span className={config.color}>✓</span>
                  {step}
                </li>
              ))}
            </ul>
          </div>
        )}
      </CardContent>
    </Card>
  );
}
