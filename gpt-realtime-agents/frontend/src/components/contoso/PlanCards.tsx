import { Card, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Check } from '@phosphor-icons/react';

interface Plan {
  id: string;
  name: string;
  type: string;
  data: string;
  minutes: string;
  texts: string;
  price_monthly: number;
  highlights?: string[];
  "5g"?: boolean;
}

interface PlanCardsProps {
  title: string;
  items: Plan[];
  onPlanClick?: (plan: Plan) => void;
}

export function PlanCards({ title, items, onPlanClick }: PlanCardsProps) {
  return (
    <div className="space-y-3">
      <h3 className="text-lg font-bold">{title}</h3>
      <div className="grid grid-cols-1 gap-3">
        {items.map((plan) => (
          <Card
            key={plan.id}
            className="cursor-pointer hover:shadow-lg hover:border-primary/50 transition-all"
            onClick={() => onPlanClick?.(plan)}
          >
            <CardContent className="p-4">
              <div className="flex items-start justify-between mb-3">
                <div>
                  <h4 className="font-bold text-lg">{plan.name}</h4>
                  <p className="text-xs text-muted-foreground uppercase">{plan.type}</p>
                </div>
                <div className="text-right">
                  <p className="text-2xl font-bold">£{plan.price_monthly}</p>
                  <p className="text-xs text-muted-foreground">/month</p>
                </div>
              </div>

              <div className="space-y-1 mb-3 text-sm">
                <div className="flex items-center gap-2">
                  <Check size={16} weight="bold" className="text-primary" />
                  <span><strong>{plan.data}</strong> data</span>
                </div>
                <div className="flex items-center gap-2">
                  <Check size={16} weight="bold" className="text-primary" />
                  <span><strong>{plan.minutes}</strong> minutes</span>
                </div>
                <div className="flex items-center gap-2">
                  <Check size={16} weight="bold" className="text-primary" />
                  <span><strong>{plan.texts}</strong> texts</span>
                </div>
              </div>

              {plan.highlights && plan.highlights.length > 0 && (
                <div className="flex flex-wrap gap-1 pt-2 border-t">
                  {plan.highlights.map((h, idx) => (
                    <Badge key={idx} variant="secondary" className="text-xs">
                      {h}
                    </Badge>
                  ))}
                  {plan["5g"] && (
                    <Badge variant="default" className="text-xs">5G</Badge>
                  )}
                </div>
              )}
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}
