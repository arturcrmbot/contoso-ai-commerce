import { Card, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { Zap, Clock, TrendUp } from '@phosphor-icons/react';

interface BundleOfferProps {
  data: {
    title: string;
    subtitle?: string;
    device: {
      name: string;
      image_url?: string;
      price_monthly: number;
    };
    plan: {
      name: string;
      data: string;
      price_monthly: number;
    };
    accessories?: Array<{
      name: string;
      original_price?: number;
      bundle_price: number;
    }>;
    bundle_price_monthly: number;
    original_price_monthly: number;
    savings: number;
    urgency_message?: string;
    expires_in?: string;
  };
  onAction?: (action: string, params?: any) => void;
  emphasis?: 'low' | 'medium' | 'high' | 'critical';
}

export function BundleOffer({ data, onAction, emphasis = 'critical' }: BundleOfferProps) {
  const savingsPercent = Math.round((data.savings / data.original_price_monthly) * 100);

  return (
    <Card className="border-4 border-primary shadow-2xl overflow-hidden animate-pulse-slow bg-gradient-to-br from-primary/5 to-primary/10">
      {/* Urgency Banner */}
      <div className="bg-gradient-to-r from-red-600 to-orange-600 text-white px-4 py-2 flex items-center justify-between">
        <div className="flex items-center gap-2">
          <Zap size={20} weight="fill" />
          <span className="font-bold text-sm">
            {data.urgency_message || "⚡ TODAY ONLY - EXCLUSIVE BUNDLE DEAL"}
          </span>
        </div>
        {data.expires_in && (
          <div className="flex items-center gap-1 bg-white/20 px-2 py-1 rounded">
            <Clock size={16} />
            <span className="text-xs font-bold">{data.expires_in}</span>
          </div>
        )}
      </div>

      <CardContent className="p-6">
        {/* Title */}
        <div className="text-center mb-4">
          <h2 className="text-2xl font-bold mb-1">{data.title}</h2>
          {data.subtitle && (
            <p className="text-sm text-muted-foreground">{data.subtitle}</p>
          )}
        </div>

        {/* Savings Badge */}
        <div className="flex justify-center mb-4">
          <Badge className="text-lg px-4 py-2 bg-gradient-to-r from-green-600 to-emerald-600 text-white">
            <TrendUp size={20} className="mr-2" weight="bold" />
            SAVE £{data.savings}/month ({savingsPercent}% OFF)
          </Badge>
        </div>

        {/* Bundle Contents */}
        <div className="grid md:grid-cols-3 gap-4 mb-6">
          {/* Device */}
          <div className="bg-muted/50 rounded-lg p-4 text-center">
            <div className="aspect-square bg-gradient-to-br from-muted to-muted/30 rounded-lg mb-2 flex items-center justify-center">
              {data.device.image_url ? (
                <img
                  src={data.device.image_url}
                  alt={data.device.name}
                  className="w-full h-full object-contain p-2"
                />
              ) : (
                <span className="text-4xl">📱</span>
              )}
            </div>
            <h4 className="font-semibold text-sm">{data.device.name}</h4>
            <p className="text-xs text-muted-foreground">£{data.device.price_monthly}/mo</p>
          </div>

          {/* Plan */}
          <div className="bg-muted/50 rounded-lg p-4 text-center flex flex-col justify-center">
            <div className="text-4xl mb-2">📶</div>
            <h4 className="font-semibold text-sm">{data.plan.name}</h4>
            <p className="text-xs font-bold text-primary">{data.plan.data} data</p>
            <p className="text-xs text-muted-foreground">£{data.plan.price_monthly}/mo</p>
          </div>

          {/* Accessories */}
          <div className="bg-muted/50 rounded-lg p-4 text-center flex flex-col justify-center">
            <div className="text-4xl mb-2">🎁</div>
            <h4 className="font-semibold text-sm">FREE Accessories</h4>
            {data.accessories && data.accessories.length > 0 ? (
              <div className="text-xs space-y-1 mt-2">
                {data.accessories.map((acc, idx) => (
                  <div key={idx}>
                    <p className="font-medium">{acc.name}</p>
                    {acc.original_price && (
                      <p className="text-muted-foreground line-through">
                        £{acc.original_price}
                      </p>
                    )}
                  </div>
                ))}
              </div>
            ) : (
              <p className="text-xs text-muted-foreground">Case + Screen Protector</p>
            )}
          </div>
        </div>

        {/* Pricing */}
        <div className="bg-primary/10 border-2 border-primary rounded-lg p-4 mb-4">
          <div className="flex items-center justify-between mb-2">
            <span className="text-sm text-muted-foreground">Normal Price:</span>
            <span className="text-lg font-semibold line-through text-muted-foreground">
              £{data.original_price_monthly}/mo
            </span>
          </div>
          <div className="flex items-center justify-between">
            <span className="text-lg font-bold">TODAY'S BUNDLE PRICE:</span>
            <span className="text-3xl font-bold text-primary">
              £{data.bundle_price_monthly}/mo
            </span>
          </div>
        </div>

        {/* CTA */}
        <Button
          size="lg"
          className="w-full text-lg font-bold bg-gradient-to-r from-primary to-primary/80 hover:from-primary/90 hover:to-primary/70 animate-pulse-slow"
          onClick={() => onAction?.('claim_bundle', data)}
        >
          🔥 CLAIM THIS DEAL NOW
        </Button>

        {/* Fine Print */}
        <p className="text-xs text-center text-muted-foreground mt-3">
          Limited time offer • While stocks last • Terms apply
        </p>
      </CardContent>
    </Card>
  );
}
