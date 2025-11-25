import { Card, CardHeader, CardContent } from '@/components/ui/card';
import { CurrencyPound, Moon, Users } from '@phosphor-icons/react';

interface PriceCalculation {
  nights: number;
  guests: number;
  price_per_night: number;
  base_price: number;
  total: number;
}

interface PriceComparisonProps {
  calculation: PriceCalculation;
}

export function PriceComparison({ calculation }: PriceComparisonProps) {
  return (
    <Card className="bg-teal-50 dark:bg-teal-950/20 border-teal-200 dark:border-teal-800">
      <CardHeader className="pb-3">
        <h4 className="font-semibold text-sm flex items-center gap-2 text-teal-700 dark:text-teal-400">
          <CurrencyPound size={16} weight="fill" />
          Total Cost
        </h4>
      </CardHeader>
      <CardContent className="space-y-3">
        <div className="flex items-center justify-between text-sm">
          <div className="flex items-center gap-2 text-gray-700 dark:text-gray-300">
            <Moon size={14} />
            <span>{calculation.nights} {calculation.nights === 1 ? 'night' : 'nights'}</span>
          </div>
          <span className="font-medium text-gray-900 dark:text-white">
            £{calculation.price_per_night}
          </span>
        </div>
        <div className="flex items-center justify-between text-sm">
          <div className="flex items-center gap-2 text-gray-700 dark:text-gray-300">
            <Users size={14} />
            <span>{calculation.guests} {calculation.guests === 1 ? 'guest' : 'guests'}</span>
          </div>
        </div>
        <div className="pt-3 border-t border-teal-200 dark:border-teal-800">
          <div className="flex items-center justify-between">
            <span className="text-sm font-semibold text-gray-700 dark:text-gray-300">
              Total
            </span>
            <span className="text-2xl font-bold text-teal-600 dark:text-teal-400">
              £{calculation.total}
            </span>
          </div>
          <p className="text-xs text-gray-500 dark:text-gray-400 mt-1">
            £{calculation.price_per_night} × {calculation.nights} {calculation.nights === 1 ? 'night' : 'nights'}
          </p>
        </div>
      </CardContent>
    </Card>
  );
}
