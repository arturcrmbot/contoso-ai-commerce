import { useState } from 'react';
import { X, Trash, Receipt, Lightning } from '@phosphor-icons/react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
} from '@/components/ui/sheet';

export interface BetSelection {
  id: string;
  event_id: string;
  event_name: string;
  market: string;
  selection: string;
  odds: number;
}

interface BetSlipPanelProps {
  isOpen: boolean;
  onClose: () => void;
  selections: BetSelection[];
  onRemoveSelection: (id: string) => void;
  onPlaceBet: (stake: number) => void;
  onClearSlip: () => void;
}

export function BetSlipPanel({
  isOpen,
  onClose,
  selections,
  onRemoveSelection,
  onPlaceBet,
  onClearSlip
}: BetSlipPanelProps) {
  const [stake, setStake] = useState<number>(10);

  // Calculate combined odds (multiply all odds together for accumulator)
  const combinedOdds = selections.reduce((acc, sel) => acc * sel.odds, 1);

  // Calculate potential return
  const potentialReturn = stake * combinedOdds;
  const potentialProfit = potentialReturn - stake;

  // Format market name for display
  const formatMarket = (market: string) => {
    return market.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
  };

  // Format selection for display
  const formatSelection = (selection: string) => {
    if (selection === 'home') return 'Home Win';
    if (selection === 'away') return 'Away Win';
    if (selection === 'draw') return 'Draw';
    return selection.replace(/\b\w/g, l => l.toUpperCase());
  };

  return (
    <Sheet open={isOpen} onOpenChange={onClose}>
      <SheetContent className="w-[400px] sm:w-[450px] flex flex-col bg-slate-900 border-slate-700 text-white">
        <SheetHeader className="flex-shrink-0 border-b border-slate-700 pb-4">
          <div className="flex items-center justify-between">
            <SheetTitle className="flex items-center gap-2 text-white">
              <Receipt size={20} className="text-emerald-400" />
              Bet Slip
              {selections.length > 0 && (
                <span className="bg-emerald-600 text-white text-xs font-bold px-2 py-0.5 rounded-full">
                  {selections.length}
                </span>
              )}
            </SheetTitle>
            {selections.length > 0 && (
              <Button variant="ghost" size="sm" onClick={onClearSlip} className="text-slate-400 hover:text-white hover:bg-slate-800">
                <Trash size={16} className="mr-1" />
                Clear All
              </Button>
            )}
          </div>
        </SheetHeader>

        <div className="flex-1 overflow-y-auto py-4">
          {selections.length === 0 ? (
            <div className="flex flex-col items-center justify-center h-full text-slate-400">
              <Receipt size={48} className="mb-4 opacity-50" />
              <p className="text-lg font-medium text-white">Your bet slip is empty</p>
              <p className="text-sm">Click on odds to add selections</p>
            </div>
          ) : (
            <div className="space-y-2">
              {selections.map((selection) => (
                <div
                  key={selection.id}
                  className="bg-slate-800 border border-slate-700 rounded-lg p-3"
                >
                  <div className="flex items-start justify-between">
                    <div className="flex-1">
                      <p className="font-medium text-sm text-white">{selection.event_name}</p>
                      <p className="text-xs text-slate-400 mt-1">
                        {formatMarket(selection.market)}
                      </p>
                      <div className="flex items-center justify-between mt-2">
                        <span className="text-sm font-semibold text-emerald-400">
                          {formatSelection(selection.selection)}
                        </span>
                        <span className="font-bold text-yellow-400">{selection.odds.toFixed(2)}</span>
                      </div>
                    </div>
                    <Button
                      variant="ghost"
                      size="sm"
                      className="h-6 w-6 p-0 ml-2 text-slate-500 hover:text-red-400 hover:bg-slate-700"
                      onClick={() => onRemoveSelection(selection.id)}
                    >
                      <X size={14} />
                    </Button>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>

        {selections.length > 0 && (
          <div className="flex-shrink-0 border-t border-slate-700 pt-4 space-y-4">
            {/* Bet Type Indicator */}
            <div className="flex items-center justify-between text-sm">
              <span className="text-slate-400">Bet Type</span>
              <span className="font-medium text-white flex items-center gap-1">
                {selections.length === 1 ? 'Single' : (
                  <>
                    <Lightning size={14} className="text-yellow-400" />
                    {selections.length}-Fold Accumulator
                  </>
                )}
              </span>
            </div>

            {/* Combined Odds */}
            <div className="flex items-center justify-between">
              <span className="text-slate-400 text-sm">Combined Odds</span>
              <span className="font-bold text-xl text-yellow-400">{combinedOdds.toFixed(2)}</span>
            </div>

            {/* Stake Input */}
            <div className="space-y-2">
              <label className="text-sm text-slate-400">Stake</label>
              <div className="flex items-center gap-2">
                <span className="text-lg font-medium text-white">£</span>
                <Input
                  type="number"
                  min={1}
                  step={1}
                  value={stake}
                  onChange={(e) => setStake(Math.max(1, Number(e.target.value)))}
                  className="text-lg font-medium bg-slate-800 border-slate-600 text-white"
                />
              </div>
              {/* Quick stake buttons */}
              <div className="flex gap-2">
                {[5, 10, 20, 50].map((amount) => (
                  <Button
                    key={amount}
                    variant={stake === amount ? 'default' : 'outline'}
                    size="sm"
                    className={`flex-1 ${stake === amount ? 'bg-emerald-600 hover:bg-emerald-700' : 'bg-slate-800 border-slate-600 text-white hover:bg-slate-700'}`}
                    onClick={() => setStake(amount)}
                  >
                    £{amount}
                  </Button>
                ))}
              </div>
            </div>

            {/* Returns */}
            <div className="bg-slate-800 border border-slate-700 rounded-lg p-4 space-y-2">
              <div className="flex items-center justify-between">
                <span className="text-slate-400 text-sm">Potential Return</span>
                <span className="font-bold text-2xl text-emerald-400">
                  £{potentialReturn.toFixed(2)}
                </span>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-slate-400 text-sm">Potential Profit</span>
                <span className="font-semibold text-emerald-400">
                  £{potentialProfit.toFixed(2)}
                </span>
              </div>
            </div>

            {/* Place Bet Button */}
            <Button
              className="w-full h-12 text-lg font-bold bg-emerald-600 hover:bg-emerald-700"
              onClick={() => onPlaceBet(stake)}
            >
              Place Bet - £{stake.toFixed(2)}
            </Button>

            <p className="text-[10px] text-center text-slate-500">
              18+ | Gamble Responsibly | BeGambleAware.org
            </p>
          </div>
        )}
      </SheetContent>
    </Sheet>
  );
}
