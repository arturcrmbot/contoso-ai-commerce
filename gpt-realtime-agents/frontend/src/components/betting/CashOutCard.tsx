import { Card, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { CheckCircle, TrendUp, Warning } from '@phosphor-icons/react';

interface CashOutCardProps {
  data: {
    bet_id?: string;
    device_model?: string;  // Legacy compatibility - will show bet info
    condition?: string;  // Legacy - will show status
    trade_in_value: number;  // Cash out value
    original_price?: number;  // Original stake
    factors?: Record<string, string>;  // Bet details
    bonus_offer?: string;
    next_steps?: string[];
  };
  emphasis?: 'low' | 'medium' | 'high' | 'critical';
  onAction?: (action: string, params?: any) => void;
}

export function CashOutCard({ data, emphasis = 'high', onAction }: CashOutCardProps) {
  const cashOutValue = data.trade_in_value;
  const originalStake = data.original_price || 0;
  const profit = cashOutValue - originalStake;
  const isProfitable = profit > 0;

  const emphasisClasses = {
    low: 'border border-slate-700',
    medium: 'border-2 border-slate-600',
    high: 'border-2 border-emerald-600/50 shadow-lg',
    critical: 'border-4 border-emerald-500 shadow-2xl'
  };

  return (
    <Card className={`${emphasisClasses[emphasis]} bg-slate-800 transition-all`}>
      <CardContent className="p-6">
        {/* Header */}
        <div className="text-center mb-4">
          <div className="inline-flex items-center justify-center w-16 h-16 rounded-full bg-emerald-900/30 mb-3">
            <TrendUp size={32} className="text-emerald-400" weight="bold" />
          </div>
          <h3 className="text-xl font-bold text-white">Cash Out Available</h3>
          {data.device_model && (
            <p className="text-sm text-slate-400">{data.device_model}</p>
          )}
          {data.condition && (
            <Badge className="mt-2 bg-emerald-600/20 text-emerald-400 border-emerald-600/30">
              {data.condition}
            </Badge>
          )}
        </div>

        {/* Cash Out Value - Prominent */}
        <div className="bg-gradient-to-r from-emerald-900/40 to-emerald-800/20 rounded-xl p-6 mb-4 text-center border border-emerald-700/30">
          <p className="text-sm text-emerald-300 mb-2">Cash Out Now For</p>
          <p className="text-5xl font-bold text-emerald-400">
            £{cashOutValue.toFixed(2)}
          </p>
          {originalStake > 0 && (
            <p className={`text-sm mt-2 ${isProfitable ? 'text-emerald-400' : 'text-red-400'}`}>
              {isProfitable ? '📈' : '📉'} {isProfitable ? '+' : ''}£{profit.toFixed(2)} {isProfitable ? 'profit' : 'loss'}
            </p>
          )}
        </div>

        {/* Bet Details */}
        {data.factors && Object.keys(data.factors).length > 0 && (
          <div className="mb-4 space-y-2">
            <h4 className="text-sm font-semibold text-slate-300">Bet Details</h4>
            {Object.entries(data.factors).map(([key, value]) => (
              <div key={key} className="flex justify-between text-sm">
                <span className="text-slate-400">{key}</span>
                <span className="text-white font-medium">{value}</span>
              </div>
            ))}
          </div>
        )}

        {/* Bonus Offer */}
        {data.bonus_offer && (
          <div className="bg-yellow-900/20 border border-yellow-600/30 rounded-lg p-3 mb-4 flex items-start gap-2">
            <Warning size={20} className="text-yellow-400 flex-shrink-0 mt-0.5" />
            <p className="text-sm text-yellow-200">{data.bonus_offer}</p>
          </div>
        )}

        {/* Next Steps */}
        {data.next_steps && data.next_steps.length > 0 && (
          <div className="border-t border-slate-700 pt-4 mb-4">
            <h4 className="text-sm font-semibold text-slate-300 mb-2">What happens next:</h4>
            <ul className="space-y-1">
              {data.next_steps.map((step, idx) => (
                <li key={idx} className="text-sm text-slate-400 flex items-start gap-2">
                  <CheckCircle size={16} className="text-emerald-400 flex-shrink-0 mt-0.5" />
                  {step}
                </li>
              ))}
            </ul>
          </div>
        )}

        {/* Cash Out Button */}
        <Button
          className="w-full h-12 text-lg font-bold bg-emerald-600 hover:bg-emerald-700"
          onClick={() => onAction?.('cash_out', { bet_id: data.bet_id, value: cashOutValue })}
        >
          Cash Out £{cashOutValue.toFixed(2)}
        </Button>
      </CardContent>
    </Card>
  );
}
