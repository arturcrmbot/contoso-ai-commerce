import { Card, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { DeviceMobile, Star } from '@phosphor-icons/react';
import { VisualContext } from './types';

interface Device {
  id: string;
  name: string;
  brand: string;
  price_upfront?: number;
  price_monthly?: number;
  image_url?: string;
  rating?: number;
  attributes?: any;
}

interface ComparisonTableProps {
  data: {
    devices: Device[];
    matrix: Record<string, any[]>;
  };
  context?: VisualContext;
  title?: string;
}

export function ComparisonTable({ data, context, title }: ComparisonTableProps) {
  const { devices, matrix } = data;
  const isPriority = (attr: string) => context?.user_priorities?.includes(attr);

  // Format attribute name for display
  const formatAttributeName = (attr: string) => {
    return attr.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
  };

  // Determine winner for a priority attribute (e.g., "excellent" > "very_good")
  const isWinner = (attr: string, value: any, allValues: any[]) => {
    if (!isPriority(attr)) return false;

    // For quality attributes
    const qualityOrder = { 'excellent': 3, 'very_good': 2, 'good': 1 };
    if (typeof value === 'string' && qualityOrder[value as keyof typeof qualityOrder]) {
      const maxQuality = Math.max(...allValues.map(v => qualityOrder[v as keyof typeof qualityOrder] || 0));
      return qualityOrder[value as keyof typeof qualityOrder] === maxQuality;
    }

    // For numeric attributes (higher is better for battery, lower is better for price)
    if (typeof value === 'number') {
      if (attr.includes('price')) {
        return value === Math.min(...allValues.filter(v => typeof v === 'number'));
      }
      return value === Math.max(...allValues.filter(v => typeof v === 'number'));
    }

    return false;
  };

  return (
    <div className="space-y-4">
      {title && <h3 className="text-lg font-bold">{title}</h3>}

      {/* Context Banner */}
      {context?.context_message && (
        <div className="bg-primary/10 border-l-4 border-primary p-3 rounded">
          <p className="text-sm font-medium">{context.context_message}</p>
        </div>
      )}

      <div className="overflow-x-auto">
        <div className="grid gap-4" style={{ gridTemplateColumns: `200px repeat(${devices.length}, 1fr)` }}>
          {/* Device Headers */}
          <div></div>
          {devices.map((device) => (
            <Card key={device.id} className="overflow-hidden">
              <CardContent className="p-3">
                <div className="aspect-square bg-gradient-to-br from-muted to-muted/50 rounded-lg mb-2 flex items-center justify-center overflow-hidden">
                  {device.image_url ? (
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
                  ) : (
                    <DeviceMobile size={32} className="text-muted-foreground" weight="thin" />
                  )}
                </div>
                <div className="text-center">
                  <p className="text-xs text-muted-foreground">{device.brand}</p>
                  <h4 className="font-semibold text-sm">{device.name}</h4>
                  {device.rating && (
                    <div className="flex items-center justify-center gap-1 mt-1">
                      <Star size={12} weight="fill" className="text-yellow-500" />
                      <span className="text-xs">{device.rating}</span>
                    </div>
                  )}
                </div>
              </CardContent>
            </Card>
          ))}

          {/* Comparison Rows */}
          {Object.entries(matrix).map(([attr, values]) => {
            const isAttrPriority = isPriority(attr);
            return (
              <>
                <div
                  key={`label-${attr}`}
                  className={`flex items-center p-3 rounded ${
                    isAttrPriority ? 'bg-primary/10 border-l-4 border-primary font-semibold' : 'bg-muted/30'
                  }`}
                >
                  <div>
                    <p className="text-sm">
                      {isAttrPriority && '✓ '}
                      {formatAttributeName(attr)}
                    </p>
                    {isAttrPriority && context?.priority_quotes?.[attr] && (
                      <p className="text-xs text-muted-foreground mt-1">
                        You mentioned: "{context.priority_quotes[attr]}"
                      </p>
                    )}
                  </div>
                </div>
                {values.map((value, idx) => (
                  <div
                    key={`value-${attr}-${idx}`}
                    className={`flex items-center justify-center p-3 rounded ${
                      isAttrPriority ? 'bg-primary/5' : 'bg-muted/10'
                    }`}
                  >
                    {isWinner(attr, value, values) ? (
                      <Badge variant="default" className="text-sm">
                        ⭐ {value}
                      </Badge>
                    ) : (
                      <span className="text-sm">{value}</span>
                    )}
                  </div>
                ))}
              </>
            );
          })}
        </div>
      </div>
    </div>
  );
}
