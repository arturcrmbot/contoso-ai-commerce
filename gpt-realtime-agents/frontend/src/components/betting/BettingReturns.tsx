import { Card, CardContent } from '@/components/ui/card';

interface BettingReturnsProps {
  data: {
    items: Array<{
      label: string;
      amount: number;
      type?: 'stake' | 'odds' | 'return' | 'upfront';
      description?: string;
    }>;
    total_upfront?: number;  // Stake
    total_monthly?: number;  // Not used in betting, ignored
    total_24m?: number;      // Potential return
    discount?: number;       // Odds boost
    promo_applied?: string;
  };
  style?: 'default' | 'minimal' | 'emphasized';
}

export function BettingReturns({ data, style = 'default' }: BettingReturnsProps) {
  const isMinimal = style === 'minimal';
  const isEmphasized = style === 'emphasized';

  return (
    <Card className={`bg-slate-800 border-slate-700 ${isEmphasized ? 'border-2 border-emerald-600/50 shadow-lg' : ''}`}>
      <CardContent className={isMinimal ? 'p-4' : 'p-6'}>
        <h3 className={`font-bold mb-4 text-white ${isMinimal ? 'text-base' : 'text-lg'}`}>
          Bet Returns
        </h3>

        <div className="space-y-3">
          {/* Line Items */}
          {data.items.map((item, idx) => (
            <div key={idx} className="flex justify-between items-start">
              <div className="flex-1">
                <p className={`${isMinimal ? 'text-sm' : 'text-base'} font-medium text-slate-200`}>
                  {item.label}
                </p>
                {item.description && (
                  <p className="text-xs text-slate-400">{item.description}</p>
                )}
              </div>
              <p className={`${isMinimal ? 'text-sm' : 'text-base'} font-semibold ${
                item.type === 'odds' ? 'text-yellow-400' :
                item.type === 'return' ? 'text-emerald-400' : 'text-white'
              }`}>
                {item.type === 'odds' ? '' : '£'}{item.amount.toFixed(2)}
              </p>
            </div>
          ))}

          {/* Odds Boost */}
          {data.discount && data.discount > 0 && (
            <>
              <div className="border-t border-slate-700 pt-3" />
              <div className="flex justify-between items-center">
                <div>
                  <p className="text-sm font-medium text-emerald-400">Odds Boost</p>
                  {data.promo_applied && (
                    <p className="text-xs text-slate-400">{data.promo_applied}</p>
                  )}
                </div>
                <p className="text-sm font-semibold text-emerald-400">
                  +{data.discount}%
                </p>
              </div>
            </>
          )}

          {/* Totals */}
          <div className="border-t border-slate-700 pt-3 space-y-2">
            {data.total_upfront !== undefined && data.total_upfront > 0 && (
              <div className="flex justify-between">
                <p className="text-sm text-slate-400">Total Stake</p>
                <p className="text-sm font-semibold text-white">£{data.total_upfront.toFixed(2)}</p>
              </div>
            )}
            {data.total_24m !== undefined && data.total_24m > 0 && (
              <div className="flex justify-between items-baseline pt-2 border-t border-slate-700">
                <p className="text-base font-bold text-slate-200">Potential Return</p>
                <p className="text-2xl font-bold text-emerald-400">
                  £{data.total_24m.toLocaleString()}
                </p>
              </div>
            )}
          </div>

          {/* Betting Info */}
          <div className="bg-slate-900/50 rounded-lg p-3 text-xs text-slate-400 border border-slate-700/50">
            <p>⚽ Returns calculated based on current odds. Odds may change.</p>
          </div>
        </div>
      </CardContent>
    </Card>
  );
}
