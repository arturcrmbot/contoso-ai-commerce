import { Card, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { DeviceMobile, Star, ShoppingCart } from '@phosphor-icons/react';

interface ProductHeroProps {
  data: {
    id: string;
    name: string;
    brand: string;
    price_upfront?: number;
    price_monthly?: number;
    image_url?: string;
    rating?: number;
    reviews_count?: number;
    attributes?: any;
    description?: string;
    stock_status?: string;
  };
  onAction?: (action: string, params?: any) => void;
  emphasis?: 'low' | 'medium' | 'high' | 'critical';
}

export function ProductHero({ data, onAction, emphasis = 'high' }: ProductHeroProps) {
  const emphasisClasses = {
    low: 'border',
    medium: 'border-2',
    high: 'border-2 shadow-lg',
    critical: 'border-4 border-primary shadow-2xl animate-pulse'
  };

  return (
    <Card className={`${emphasisClasses[emphasis]} transition-all`}>
      <CardContent className="p-6">
        <div className="grid md:grid-cols-2 gap-6">
          {/* Product Image */}
          <div className="aspect-square bg-gradient-to-br from-muted to-muted/30 rounded-xl flex items-center justify-center overflow-hidden relative">
            {data.image_url ? (
              <>
                <img
                  src={data.image_url}
                  alt={data.name}
                  className="w-full h-full object-contain p-4"
                  onError={(e) => {
                    e.currentTarget.style.display = 'none';
                    const fallback = e.currentTarget.parentElement?.querySelector('.fallback-icon');
                    fallback?.classList.remove('hidden');
                  }}
                />
                <DeviceMobile size={96} className="text-muted-foreground absolute hidden fallback-icon" weight="thin" />
              </>
            ) : (
              <DeviceMobile size={96} className="text-muted-foreground" weight="thin" />
            )}
            {data.stock_status && (
              <Badge className="absolute top-4 right-4" variant={data.stock_status === 'In stock' ? 'default' : 'secondary'}>
                {data.stock_status}
              </Badge>
            )}
          </div>

          {/* Product Details */}
          <div className="flex flex-col">
            <div className="flex-1">
              <div className="mb-2">
                <p className="text-sm text-muted-foreground uppercase tracking-wide">{data.brand}</p>
                <h2 className="text-3xl font-bold mb-2">{data.name}</h2>
              </div>

              {/* Rating */}
              {data.rating && (
                <div className="flex items-center gap-2 mb-4">
                  <div className="flex">
                    {[...Array(5)].map((_, i) => (
                      <Star
                        key={i}
                        size={16}
                        weight={i < Math.floor(data.rating!) ? 'fill' : 'regular'}
                        className="text-yellow-500"
                      />
                    ))}
                  </div>
                  <span className="text-sm font-medium">{data.rating}</span>
                  <span className="text-sm text-muted-foreground">
                    ({data.reviews_count?.toLocaleString()} reviews)
                  </span>
                </div>
              )}

              {/* Description */}
              {data.description && (
                <p className="text-sm text-muted-foreground mb-4">{data.description}</p>
              )}

              {/* Key Attributes */}
              {data.attributes && (
                <div className="flex flex-wrap gap-2 mb-4">
                  {data.attributes.battery_life && (
                    <Badge variant="outline">🔋 {data.attributes.battery_life} battery</Badge>
                  )}
                  {data.attributes.camera_quality && (
                    <Badge variant="outline">📸 {data.attributes.camera_quality} camera</Badge>
                  )}
                  {data.attributes.screen_size && (
                    <Badge variant="outline">📱 {data.attributes.screen_size}" screen</Badge>
                  )}
                  {data.attributes["5g"] && (
                    <Badge variant="default">5G</Badge>
                  )}
                </div>
              )}
            </div>

            {/* Pricing & CTA */}
            <div className="border-t pt-4 mt-4">
              <div className="flex items-end justify-between mb-4">
                <div>
                  <p className="text-sm text-muted-foreground mb-1">Monthly cost</p>
                  <p className="text-4xl font-bold">
                    £{data.price_monthly}
                    <span className="text-lg font-normal text-muted-foreground">/mo</span>
                  </p>
                </div>
                {data.price_upfront && data.price_upfront > 0 && (
                  <div className="text-right">
                    <p className="text-sm text-muted-foreground mb-1">Upfront cost</p>
                    <p className="text-2xl font-semibold">£{data.price_upfront}</p>
                  </div>
                )}
              </div>

              <Button
                size="lg"
                className="w-full"
                onClick={() => onAction?.('add_to_cart', { device_id: data.id })}
              >
                <ShoppingCart size={20} className="mr-2" />
                Add to Cart
              </Button>
            </div>
          </div>
        </div>
      </CardContent>
    </Card>
  );
}
