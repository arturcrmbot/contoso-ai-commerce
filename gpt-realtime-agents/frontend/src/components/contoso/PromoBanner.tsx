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
    <div className="space-y-4">
      <h3 className="text-xl font-bold tracking-tight">{title}</h3>
      {items.map((promo, idx) => (
        <Card key={idx} className="border-0 bg-gradient-to-r from-violet-500 to-fuchsia-600 text-white shadow-lg overflow-hidden relative">
          {/* Decorative circles */}
          <div className="absolute -top-10 -right-10 w-32 h-32 bg-white/10 rounded-full blur-2xl" />
          <div className="absolute -bottom-10 -left-10 w-32 h-32 bg-black/10 rounded-full blur-2xl" />
          
          <CardContent className="p-5 relative z-10">
            <div className="flex items-start justify-between mb-3">
              <div className="flex items-center gap-2">
                <div className="bg-white/20 p-1.5 rounded-lg backdrop-blur-sm">
                  <Tag size={20} className="text-white" weight="fill" />
                </div>
                <h4 className="font-bold text-lg">{promo.title}</h4>
              </div>
              {promo.auto_apply && (
                <Badge className="bg-white/20 hover:bg-white/30 text-white border-0 backdrop-blur-sm">Auto-applied</Badge>
              )}
            </div>
            <p className="text-sm text-white/90 mb-4 font-medium leading-relaxed">{promo.description}</p>
            {promo.code && !promo.auto_apply && (
              <div className="flex items-center gap-2 bg-black/20 p-1.5 rounded-lg backdrop-blur-sm">
                <code className="flex-1 px-3 py-1.5 font-mono text-sm font-bold tracking-wider text-white">
                  {promo.code}
                </code>
                <Button
                  size="sm"
                  variant="ghost"
                  onClick={() => copyCode(promo.code!)}
                  className="gap-1 text-white hover:bg-white/20 hover:text-white h-8"
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
