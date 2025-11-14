import { Suitcase } from '@phosphor-icons/react';
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
      aria-label="My trips"
    >
      <Suitcase size={24} weight={count > 0 ? 'fill' : 'regular'} className="text-teal-600" />
      {count > 0 && (
        <Badge
          className="absolute -top-1 -right-1 h-5 w-5 flex items-center justify-center p-0 text-xs bg-gradient-to-r from-teal-500 to-cyan-600 text-white border-0"
        >
          {count}
        </Badge>
      )}
    </button>
  );
}
