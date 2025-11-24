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
      className="relative group flex items-center justify-center w-12 h-12 rounded-full bg-white/90 backdrop-blur-sm shadow-lg hover:shadow-xl hover:bg-white transition-all duration-300 border border-white/20"
      aria-label="My trips"
    >
      <Suitcase 
        size={24} 
        weight={count > 0 ? 'fill' : 'regular'} 
        className="text-teal-600 group-hover:scale-110 transition-transform duration-300" 
      />
      {count > 0 && (
        <span className="absolute -top-1 -right-1 flex h-5 w-5 items-center justify-center rounded-full bg-gradient-to-r from-pink-500 to-rose-500 text-[10px] font-bold text-white shadow-sm ring-2 ring-white animate-in zoom-in duration-300">
          {count}
        </span>
      )}
    </button>
  );
}
