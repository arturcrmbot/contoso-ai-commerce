import { CheckCircle, Receipt, Copy } from '@phosphor-icons/react';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { toast } from 'sonner';

interface BetConfirmationProps {
  betId: string;
  confirmationNumber: string;
  selections: Array<{
    event_name: string;
    market: string;
    selection: string;
    odds: number;
  }>;
  stake: number;
  combinedOdds: number;
  potentialReturn: number;
}

export function BetConfirmation({
  betId,
  confirmationNumber,
  selections,
  stake,
  combinedOdds,
  potentialReturn
}: BetConfirmationProps) {
  const copyConfirmation = () => {
    navigator.clipboard.writeText(confirmationNumber);
    toast.success('Confirmation number copied!');
  };

  const formatSelection = (selection: string) => {
    if (selection === 'home') return 'Home Win';
    if (selection === 'away') return 'Away Win';
    if (selection === 'draw') return 'Draw';
    return selection.replace(/\b\w/g, l => l.toUpperCase());
  };

  return (
    <div className="h-full flex flex-col items-center justify-center p-6">
      <div className="max-w-md w-full space-y-6">
        {/* Success Icon */}
        <div className="flex flex-col items-center text-center">
          <div className="w-16 h-16 rounded-full bg-green-100 flex items-center justify-center mb-4">
            <CheckCircle size={40} weight="fill" className="text-green-600" />
          </div>
          <h2 className="text-2xl font-bold text-green-600">Bet Placed!</h2>
          <p className="text-muted-foreground mt-1">Your bet has been confirmed</p>
        </div>

        {/* Confirmation Number */}
        <div className="bg-muted/50 rounded-lg p-4 flex items-center justify-between">
          <div>
            <p className="text-xs text-muted-foreground">Confirmation Number</p>
            <p className="font-mono font-bold text-lg">{confirmationNumber}</p>
          </div>
          <Button variant="ghost" size="sm" onClick={copyConfirmation}>
            <Copy size={16} />
          </Button>
        </div>

        {/* Selections */}
        <div className="border rounded-lg p-4 space-y-3">
          <div className="flex items-center gap-2 mb-2">
            <Receipt size={18} />
            <span className="font-semibold">
              {selections.length === 1 ? 'Single' : `${selections.length}-Fold Accumulator`}
            </span>
          </div>

          {selections.map((sel, idx) => (
            <div key={idx} className="border-b last:border-0 pb-2 last:pb-0">
              <p className="font-medium text-sm">{sel.event_name}</p>
              <div className="flex items-center justify-between mt-1">
                <span className="text-sm text-primary">{formatSelection(sel.selection)}</span>
                <Badge variant="secondary">{sel.odds.toFixed(2)}</Badge>
              </div>
            </div>
          ))}
        </div>

        {/* Summary */}
        <div className="bg-green-50 dark:bg-green-950/20 rounded-lg p-4 space-y-2">
          <div className="flex justify-between text-sm">
            <span className="text-muted-foreground">Stake</span>
            <span className="font-medium">£{stake.toFixed(2)}</span>
          </div>
          <div className="flex justify-between text-sm">
            <span className="text-muted-foreground">Combined Odds</span>
            <span className="font-medium">{combinedOdds.toFixed(2)}</span>
          </div>
          <div className="border-t pt-2 mt-2">
            <div className="flex justify-between">
              <span className="font-medium">Potential Return</span>
              <span className="font-bold text-lg text-green-600">£{potentialReturn.toFixed(2)}</span>
            </div>
          </div>
        </div>

        {/* Bet ID */}
        <p className="text-xs text-center text-muted-foreground">
          Bet ID: {betId}
        </p>
      </div>
    </div>
  );
}
