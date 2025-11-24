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
    <div className="space-y-4 p-4">
      {context?.context_message && (
        <div className="bg-blue-50 border-l-4 border-blue-500 p-4 rounded-r-lg mb-4 shadow-sm">
          <p className="text-sm font-medium text-blue-800">{context.context_message}</p>
        </div>
      )}
      <h3 className="text-xl font-bold tracking-tight">{title}</h3>
      <div className="grid grid-cols-1 gap-4">
        {items.map((plan) => (
          <Card
            key={plan.id}
            className="cursor-pointer hover:shadow-xl hover:-translate-y-0.5 transition-all duration-300 border-0 shadow-md rounded-xl overflow-hidden group relative"
            onClick={() => onPlanClick?.(plan)}
          >
            {/* Left accent border */}
            <div className="absolute left-0 top-0 bottom-0 w-1.5 bg-gradient-to-b from-teal-400 to-cyan-600" />
            
            <CardContent className="p-5 pl-7">
              <div className="flex items-start justify-between mb-4">
                <div>
                  <h4 className="font-bold text-xl text-gray-900">{plan.name}</h4>
                  <Badge variant="secondary" className="mt-1 uppercase text-[10px] tracking-wider font-semibold">
                    {plan.type}
                  </Badge>
                </div>
                <div className="text-right">
                  <p className="text-3xl font-bold text-primary">£{plan.price_monthly}</p>
                  <p className="text-xs text-muted-foreground font-medium uppercase tracking-wide">Per Month</p>
                </div>
              </div>

              <div className="grid grid-cols-3 gap-4 mb-4 py-4 border-y border-gray-100">
                <div className={`text-center ${isPriority('data') ? 'scale-110 transition-transform' : ''}`}>
                  <p className="text-xs text-muted-foreground uppercase tracking-wider mb-1">Data</p>
                  <p className={`font-bold text-lg ${isPriority('data') ? 'text-primary' : 'text-gray-700'}`}>{plan.data}</p>
                </div>
                <div className={`text-center ${isPriority('minutes') ? 'scale-110 transition-transform' : ''}`}>
                  <p className="text-xs text-muted-foreground uppercase tracking-wider mb-1">Minutes</p>
                  <p className={`font-bold text-lg ${isPriority('minutes') ? 'text-primary' : 'text-gray-700'}`}>{plan.minutes}</p>
                </div>
                <div className={`text-center ${isPriority('texts') ? 'scale-110 transition-transform' : ''}`}>
                  <p className="text-xs text-muted-foreground uppercase tracking-wider mb-1">Texts</p>
                  <p className={`font-bold text-lg ${isPriority('texts') ? 'text-primary' : 'text-gray-700'}`}>{plan.texts}</p>
                </div>
              </div>

              {plan.highlights && plan.highlights.length > 0 && (
                <div className="flex flex-wrap gap-2">
                  {plan.highlights.map((h, idx) => {
                    const isRoaming = h.toLowerCase().includes('roam');
                    const isHighlighted = isRoaming && isPriority('international_roaming');
                    return (
                      <Badge
                        key={idx}
                        variant={isHighlighted ? 'default' : 'outline'}
                        className={`text-xs py-1 px-2 ${isHighlighted ? 'bg-primary text-white border-transparent shadow-md' : 'bg-gray-50 text-gray-600 border-gray-200'}`}
                      >
                        {isHighlighted && <Check size={12} weight="bold" className="mr-1" />}
                        {h}
                      </Badge>
                    );
                  })}
                  {plan["5g"] && (
                    <Badge
                      className={`text-xs py-1 px-2 ${isPriority('5g') ? 'bg-blue-600 text-white shadow-md' : 'bg-blue-50 text-blue-700 border-blue-100'}`}
                    >
                      {isPriority('5g') && <Check size={12} weight="bold" className="mr-1" />}
                      5G Ready
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
