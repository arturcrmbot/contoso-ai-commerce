import { Card, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { DeviceMobile, Star } from '@phosphor-icons/react';
import { VisualContext } from '@/components/visual-primitives/types';

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
  context?: VisualContext;
}

export function ProductCard({ device, isHighlighted = false, onClick, context }: ProductCardProps) {
  const isPriority = (attr: string) => context?.user_priorities?.includes(attr);

  const getBadgeVariant = (quality: string, attr: string) => {
    if (isPriority(attr)) return 'default';
    switch (quality) {
      case 'excellent': return 'default';
      case 'very_good': return 'secondary';
      default: return 'outline';
    }
  };

  const formatAttributeName = (attr: string) => {
    return attr.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
  };

  return (
    <Card
      className={`cursor-pointer transition-all duration-300 border-0 shadow-sm hover:shadow-xl hover:-translate-y-1 rounded-xl overflow-hidden bg-card ${
        isHighlighted
          ? 'ring-2 ring-primary shadow-lg'
          : ''
      }`}
      onClick={onClick}
    >
      <CardContent className="p-5">
        {/* Device Image */}
        <div className="aspect-square bg-gray-50 rounded-xl mb-4 flex items-center justify-center overflow-hidden relative group">
          {device.image_url ? (
            <>
              <img
                src={device.image_url}
                alt={device.name}
                className="w-3/4 h-3/4 object-contain transition-transform duration-500 group-hover:scale-110"
                onError={(e) => {
                  e.currentTarget.style.display = 'none';
                  const fallback = e.currentTarget.parentElement?.querySelector('.fallback-icon');
                  fallback?.classList.remove('hidden');
                }}
              />
              <DeviceMobile size={48} className="text-muted-foreground absolute hidden fallback-icon" weight="thin" />
            </>
          ) : (
            <DeviceMobile size={48} className="text-muted-foreground/30" weight="thin" />
          )}
        </div>

        {/* Device Info */}
        <div className="space-y-3">
          <div>
            <p className="text-xs font-medium text-muted-foreground uppercase tracking-wider">{device.brand}</p>
            <h3 className="font-bold text-lg leading-tight text-foreground">{device.name}</h3>
          </div>

          {/* Rating */}
          {device.rating && (
            <div className="flex items-center gap-1.5 text-sm">
              <div className="flex text-yellow-400">
                <Star size={14} weight="fill" />
              </div>
              <span className="font-semibold">{device.rating}</span>
              <span className="text-muted-foreground text-xs">
                ({device.reviews_count?.toLocaleString()})
              </span>
            </div>
          )}

          {/* Key Attributes */}
          {device.attributes && (
            <div className="flex flex-wrap gap-1.5">
              {device.attributes.battery_life && (
                <Badge
                  variant={getBadgeVariant(device.attributes.battery_life, 'battery_life')}
                  className={`text-[10px] px-2 py-0.5 ${isPriority('battery_life') ? 'ring-2 ring-primary shadow-md' : ''}`}
                >
                  {isPriority('battery_life') && '✓ '}
                  {device.attributes.battery_life}
                </Badge>
              )}
              {device.attributes.camera_quality && (
                <Badge
                  variant={getBadgeVariant(device.attributes.camera_quality, 'camera_quality')}
                  className={`text-[10px] px-2 py-0.5 ${isPriority('camera_quality') ? 'ring-2 ring-primary shadow-md' : ''}`}
                >
                  {isPriority('camera_quality') && '✓ '}
                  {device.attributes.camera_quality} Cam
                </Badge>
              )}
              {device.attributes["5g"] && (
                <Badge variant="secondary" className="text-[10px] px-2 py-0.5 bg-blue-50 text-blue-700 hover:bg-blue-100">5G</Badge>
              )}
            </div>
          )}

          {/* Pricing */}
          <div className="pt-3 border-t flex items-end justify-between">
            <div>
              <p className="text-xs text-muted-foreground mb-0.5">Monthly</p>
              <p className="text-xl font-bold text-primary">£{device.price_monthly}<span className="text-xs font-normal text-muted-foreground">/mo</span></p>
            </div>
            {device.price_upfront > 0 && (
              <div className="text-right">
                <p className="text-xs text-muted-foreground mb-0.5">Upfront</p>
                <p className="text-sm font-semibold">£{device.price_upfront}</p>
              </div>
            )}
          </div>

          {/* CTA */}
          <button
            className="w-full mt-2 px-4 py-2.5 bg-primary text-primary-foreground rounded-lg text-sm font-semibold hover:bg-primary/90 transition-all shadow-sm hover:shadow-md"
            onClick={(e) => { e.stopPropagation(); onClick(); }}
          >
            View Details
          </button>
        </div>
      </CardContent>
    </Card>
  );
}
