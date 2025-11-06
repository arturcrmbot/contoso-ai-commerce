import { Card, CardContent } from '@/components/ui/card';

interface PriceBreakdownProps {
  data: {
    items: Array<{
      label: string;
      amount: number;
      type?: 'upfront' | 'monthly' | 'total';
      description?: string;
    }>;
    total_upfront?: number;
    total_monthly?: number;
    total_24m?: number;
    discount?: number;
    promo_applied?: string;
  };
  style?: 'default' | 'minimal' | 'emphasized';
}

export function PriceBreakdown({ data, style = 'default' }: PriceBreakdownProps) {
  const isMinimal = style === 'minimal';
  const isEmphasized = style === 'emphasized';

  return (
    <Card className={isEmphasized ? 'border-2 border-primary shadow-lg' : ''}>
      <CardContent className={isMinimal ? 'p-4' : 'p-6'}>
        <h3 className={`font-bold mb-4 ${isMinimal ? 'text-base' : 'text-lg'}`}>
          Price Breakdown
        </h3>

        <div className="space-y-3">
          {/* Line Items */}
          {data.items.map((item, idx) => (
            <div key={idx} className="flex justify-between items-start">
              <div className="flex-1">
                <p className={`${isMinimal ? 'text-sm' : 'text-base'} font-medium`}>
                  {item.label}
                </p>
                {item.description && (
                  <p className="text-xs text-muted-foreground">{item.description}</p>
                )}
              </div>
              <p className={`${isMinimal ? 'text-sm' : 'text-base'} font-semibold`}>
                £{item.amount.toFixed(2)}
                {item.type === 'monthly' && <span className="text-xs text-muted-foreground">/mo</span>}
              </p>
            </div>
          ))}

          {/* Discount */}
          {data.discount && data.discount > 0 && (
            <>
              <div className="border-t pt-3" />
              <div className="flex justify-between items-center">
                <div>
                  <p className="text-sm font-medium text-green-600">Discount</p>
                  {data.promo_applied && (
                    <p className="text-xs text-muted-foreground">{data.promo_applied}</p>
                  )}
                </div>
                <p className="text-sm font-semibold text-green-600">
                  -£{data.discount.toFixed(2)}
                </p>
              </div>
            </>
          )}

          {/* Totals */}
          <div className="border-t pt-3 space-y-2">
            {data.total_upfront !== undefined && (
              <div className="flex justify-between">
                <p className="text-sm text-muted-foreground">Total Upfront</p>
                <p className="text-sm font-semibold">£{data.total_upfront.toFixed(2)}</p>
              </div>
            )}
            {data.total_monthly !== undefined && (
              <div className="flex justify-between">
                <p className="text-sm text-muted-foreground">Monthly Cost</p>
                <p className="text-sm font-semibold">
                  £{data.total_monthly.toFixed(2)}/mo
                </p>
              </div>
            )}
            {data.total_24m !== undefined && (
              <div className="flex justify-between items-baseline pt-2 border-t">
                <p className="text-base font-bold">24-Month Total</p>
                <p className="text-2xl font-bold text-primary">
                  £{data.total_24m.toLocaleString()}
                </p>
              </div>
            )}
          </div>

          {/* Payment Info */}
          <div className="bg-muted/50 rounded-lg p-3 text-xs text-muted-foreground">
            <p>💳 First payment due today. Subsequent payments monthly.</p>
          </div>
        </div>
      </CardContent>
    </Card>
  );
}
