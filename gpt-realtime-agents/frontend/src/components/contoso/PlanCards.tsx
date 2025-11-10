import { Card, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Check } from '@phosphor-icons/react';
import { VisualContext } from '@/components/visual-primitives/types';

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
  context?: VisualContext;
}

export function PlanCards({ title, items, onPlanClick, context }: PlanCardsProps) {
  const isPriority = (attr: string) => context?.user_priorities?.includes(attr);

  return (
    <div className="space-y-3">
      {context?.context_message && (
        <div className="bg-primary/10 border-l-4 border-primary p-3 rounded mb-3">
          <p className="text-sm font-medium">{context.context_message}</p>
        </div>
      )}
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
                <div className={`flex items-center gap-2 ${isPriority('data') ? 'font-bold' : ''}`}>
                  <Check size={16} weight="bold" className={isPriority('data') ? 'text-primary' : 'text-primary'} />
                  <span>
                    {isPriority('data') && '✓ '}
                    <strong>{plan.data}</strong> data
                  </span>
                </div>
                <div className={`flex items-center gap-2 ${isPriority('minutes') ? 'font-bold' : ''}`}>
                  <Check size={16} weight="bold" className="text-primary" />
                  <span>
                    {isPriority('minutes') && '✓ '}
                    <strong>{plan.minutes}</strong> minutes
                  </span>
                </div>
                <div className={`flex items-center gap-2 ${isPriority('texts') ? 'font-bold' : ''}`}>
                  <Check size={16} weight="bold" className="text-primary" />
                  <span>
                    {isPriority('texts') && '✓ '}
                    <strong>{plan.texts}</strong> texts
                  </span>
                </div>
              </div>

              {plan.highlights && plan.highlights.length > 0 && (
                <div className="flex flex-wrap gap-1 pt-2 border-t">
                  {plan.highlights.map((h, idx) => {
                    const isRoaming = h.toLowerCase().includes('roam');
                    const isHighlighted = isRoaming && isPriority('international_roaming');
                    return (
                      <Badge
                        key={idx}
                        variant={isHighlighted ? 'default' : 'secondary'}
                        className={`text-xs ${isHighlighted ? 'ring-2 ring-primary shadow-lg' : ''}`}
                      >
                        {isHighlighted && '✓ '}
                        {h}
                      </Badge>
                    );
                  })}
                  {plan["5g"] && (
                    <Badge
                      variant={isPriority('5g') ? 'default' : 'default'}
                      className={`text-xs ${isPriority('5g') ? 'ring-2 ring-primary shadow-lg' : ''}`}
                    >
                      {isPriority('5g') && '✓ '}
                      5G
                    </Badge>
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
