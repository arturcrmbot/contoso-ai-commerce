import { ShoppingCart } from '@phosphor-icons/react';
import { Badge } from '@/components/ui/badge';

interface CartIconProps {
  count: number;
  totalMonthly?: number;
  onClick: () => void;
}

export function CartIcon({ count, totalMonthly, onClick }: CartIconProps) {
  return (
    <button
      onClick={onClick}
      className="relative p-2 hover:bg-accent rounded-md transition-colors"
      aria-label="Shopping cart"
    >
      <ShoppingCart size={24} weight={count > 0 ? 'fill' : 'regular'} />
      {count > 0 && (
        <>
          <Badge
            variant="destructive"
            className="absolute -top-1 -right-1 h-5 w-5 flex items-center justify-center p-0 text-xs"
          >
            {count}
          </Badge>
          {totalMonthly !== undefined && totalMonthly > 0 && (
            <span className="absolute -bottom-6 left-1/2 -translate-x-1/2 text-xs font-semibold whitespace-nowrap">
              £{totalMonthly}/mo
            </span>
          )}
        </>
      )}
    </button>
  );
}
