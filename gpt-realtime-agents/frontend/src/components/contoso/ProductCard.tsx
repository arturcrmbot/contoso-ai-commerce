import { Card, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { DeviceMobile, Star } from '@phosphor-icons/react';

interface Device {
  id: string;
  name: string;
  brand: string;
  price_upfront: number;
  price_monthly: number;
  image_url?: string;
  attributes?: {
    battery_life?: string;
    camera_quality?: string;
    storage_options?: number[];
    screen_size?: number;
    "5g"?: boolean;
  };
  rating?: number;
  reviews_count?: number;
}

interface ProductCardProps {
  device: Device;
  isHighlighted?: boolean;
  onClick: () => void;
}

export function ProductCard({ device, isHighlighted = false, onClick }: ProductCardProps) {
  const getBadgeVariant = (quality: string) => {
    switch (quality) {
      case 'excellent': return 'default';
      case 'very_good': return 'secondary';
      default: return 'outline';
    }
  };

  return (
    <Card
      className={`cursor-pointer transition-all hover:shadow-lg border-2 ${
        isHighlighted
          ? 'border-primary shadow-lg animate-pulse'
          : 'border-border hover:border-primary/50'
      }`}
      onClick={onClick}
    >
      <CardContent className="p-4">
        {/* Device Image */}
        <div className="aspect-square bg-gradient-to-br from-muted to-muted/50 rounded-lg mb-3 flex items-center justify-center overflow-hidden relative">
          {device.image_url ? (
            <>
              <img
                src={device.image_url}
                alt={device.name}
                className="w-full h-full object-contain p-2"
                onError={(e) => {
                  e.currentTarget.style.display = 'none';
                  const fallback = e.currentTarget.parentElement?.querySelector('.fallback-icon');
                  fallback?.classList.remove('hidden');
                }}
              />
              <DeviceMobile size={48} className="text-muted-foreground absolute hidden fallback-icon" weight="thin" />
            </>
          ) : (
            <DeviceMobile size={48} className="text-muted-foreground" weight="thin" />
          )}
        </div>

        {/* Device Info */}
        <div className="space-y-2">
          <div>
            <p className="text-xs text-muted-foreground">{device.brand}</p>
            <h3 className="font-semibold text-sm leading-tight">{device.name}</h3>
          </div>

          {/* Rating */}
          {device.rating && (
            <div className="flex items-center gap-1 text-xs">
              <Star size={12} weight="fill" className="text-yellow-500" />
              <span className="font-medium">{device.rating}</span>
              <span className="text-muted-foreground">
                ({device.reviews_count?.toLocaleString()})
              </span>
            </div>
          )}

          {/* Key Attributes */}
          {device.attributes && (
            <div className="flex flex-wrap gap-1">
              {device.attributes.battery_life && (
                <Badge variant={getBadgeVariant(device.attributes.battery_life)} className="text-xs">
                  Battery: {device.attributes.battery_life}
                </Badge>
              )}
              {device.attributes.camera_quality && (
                <Badge variant={getBadgeVariant(device.attributes.camera_quality)} className="text-xs">
                  Camera: {device.attributes.camera_quality}
                </Badge>
              )}
              {device.attributes["5g"] && (
                <Badge variant="default" className="text-xs">5G</Badge>
              )}
            </div>
          )}

          {/* Pricing */}
          <div className="pt-2 border-t">
            <div className="flex items-baseline justify-between">
              <div>
                <p className="text-xs text-muted-foreground">From</p>
                <p className="text-lg font-bold">£{device.price_monthly}<span className="text-xs font-normal">/mo</span></p>
              </div>
              {device.price_upfront > 0 && (
                <div className="text-right">
                  <p className="text-xs text-muted-foreground">Upfront</p>
                  <p className="text-sm font-semibold">£{device.price_upfront}</p>
                </div>
              )}
            </div>
          </div>

          {/* CTA */}
          <button
            className="w-full mt-2 px-3 py-2 bg-primary text-primary-foreground rounded-md text-xs font-medium hover:bg-primary/90 transition-colors"
            onClick={(e) => { e.stopPropagation(); onClick(); }}
          >
            Learn more
          </button>
        </div>
      </CardContent>
    </Card>
  );
}
