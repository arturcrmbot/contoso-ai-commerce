import { Ticket } from '@phosphor-icons/react';

interface BetSlipIconProps {
  count: number;
  potentialReturn?: number;
  onClick: () => void;
}

export function BetSlipIcon({ count, potentialReturn, onClick }: BetSlipIconProps) {
  return (
    <button
      onClick={onClick}
      className="relative flex items-center gap-2 px-3 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-700 transition-colors text-white"
    >
      <div className="relative">
        <Ticket size={20} weight="fill" />
        {count > 0 && (
          <span className="absolute -top-1 -right-1 h-4 w-4 bg-yellow-400 text-black text-[10px] font-bold rounded-full flex items-center justify-center">
            {count}
          </span>
        )}
      </div>

      <div className="flex flex-col items-start">
        <span className="text-xs font-medium leading-none">Bet Slip</span>
        {potentialReturn !== undefined && potentialReturn > 0 ? (
          <span className="text-xs text-yellow-300 font-bold leading-none mt-0.5">
            £{potentialReturn.toFixed(2)}
          </span>
        ) : (
          <span className="text-[10px] text-emerald-200 leading-none mt-0.5">
            {count === 0 ? 'Empty' : `${count} bet${count !== 1 ? 's' : ''}`}
          </span>
        )}
      </div>
    </button>
  );
}
