import { Card, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Tag, Copy } from '@phosphor-icons/react';
import { Button } from '@/components/ui/button';
import { toast } from 'sonner';

interface Promo {
  title: string;
  description: string;
  code?: string;
  auto_apply?: boolean;
}

interface PromoBannerProps {
  title: string;
  items: Promo[];
  onPromoClick?: (code: string) => void;
}

export function PromoBanner({ title, items, onPromoClick }: PromoBannerProps) {
  const copyCode = (code: string) => {
    navigator.clipboard.writeText(code);
    toast.success(`Copied code: ${code}`);
  };

  return (
    <div className="space-y-3">
      <h3 className="text-lg font-bold">{title}</h3>
      {items.map((promo, idx) => (
        <Card key={idx} className="border-2 border-primary/20 bg-gradient-to-br from-primary/5 to-primary/10">
          <CardContent className="p-4">
            <div className="flex items-start justify-between mb-2">
              <div className="flex items-center gap-2">
                <Tag size={20} className="text-primary" weight="fill" />
                <h4 className="font-semibold">{promo.title}</h4>
              </div>
              {promo.auto_apply && (
                <Badge variant="secondary" className="text-xs">Auto-applied</Badge>
              )}
            </div>
            <p className="text-sm text-muted-foreground mb-3">{promo.description}</p>
            {promo.code && !promo.auto_apply && (
              <div className="flex items-center gap-2">
                <code className="flex-1 px-3 py-2 bg-background rounded border font-mono text-sm">
                  {promo.code}
                </code>
                <Button
                  size="sm"
                  variant="outline"
                  onClick={() => copyCode(promo.code!)}
                  className="gap-1"
                >
                  <Copy size={14} />
                  Copy
                </Button>
              </div>
            )}
          </CardContent>
        </Card>
      ))}
    </div>
  );
}
