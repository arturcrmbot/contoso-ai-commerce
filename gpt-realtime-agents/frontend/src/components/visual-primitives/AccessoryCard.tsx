import { Card, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { Plus } from '@phosphor-icons/react';

interface AccessoryCardProps {
  data: {
    id: string;
    name: string;
    type: string;
    price: number;
    image_url?: string;
    description?: string;
    compatibility?: string;
    in_stock?: boolean;
  };
  onAction?: (action: string, params?: any) => void;
  size?: 'sm' | 'md' | 'lg';
}

export function AccessoryCard({ data, onAction, size = 'md' }: AccessoryCardProps) {
  const sizeClasses = {
    sm: 'text-xs',
    md: 'text-sm',
    lg: 'text-base'
  };

  const getTypeEmoji = (type: string | undefined) => {
    if (!type) return '📦';
    const map: Record<string, string> = {
      'case': '🛡️',
      'screen_protector': '📱',
      'charger': '🔌',
      'earbuds': '🎧',
      'cable': '🔗',
      'adapter': '🔌'
    };
    return map[type] || '📦';
  };

  return (
    <Card className="h-full hover:shadow-md transition-all hover:border-primary/50 cursor-pointer">
      <CardContent className="p-3">
        {/* Accessory Image/Icon */}
        <div className="aspect-square bg-muted/30 rounded-lg mb-2 flex items-center justify-center overflow-hidden">
          {data.image_url ? (
            <img
              src={data.image_url}
              alt={data.name}
              className="w-full h-full object-cover"
              onError={(e) => {
                e.currentTarget.style.display = 'none';
                const fallback = e.currentTarget.parentElement?.querySelector('.fallback-emoji');
                if (fallback) fallback.classList.remove('hidden');
              }}
            />
          ) : null}
          <span className={`text-4xl ${data.image_url ? 'hidden' : ''} fallback-emoji`}>
            {getTypeEmoji(data.type)}
          </span>
        </div>

        {/* Accessory Info */}
        <div className="space-y-1">
          <div className="flex items-start justify-between gap-1">
            {data.type && (
              <Badge variant="secondary" className="text-xs">
                {data.type.replace('_', ' ')}
              </Badge>
            )}
            {!data.in_stock && (
              <Badge variant="outline" className="text-xs">Out of stock</Badge>
            )}
          </div>

          <h4 className={`font-semibold leading-tight ${sizeClasses[size]}`}>
            {data.name}
          </h4>

          {data.description && (
            <p className="text-xs text-muted-foreground line-clamp-2">
              {data.description}
            </p>
          )}

          {/* Pricing */}
          <div className="flex items-center justify-between pt-2">
            <p className="font-bold text-lg">£{data.price.toFixed(2)}</p>
            <Button
              size="sm"
              variant={data.in_stock ? "default" : "secondary"}
              disabled={!data.in_stock}
              onClick={(e) => {
                e.stopPropagation();
                onAction?.('add_accessory', { accessory_id: data.id });
              }}
            >
              <Plus size={14} weight="bold" />
            </Button>
          </div>
        </div>
      </CardContent>
    </Card>
  );
}
