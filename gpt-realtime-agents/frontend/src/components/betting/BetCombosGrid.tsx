import { Card, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { Plus, Lightning } from '@phosphor-icons/react';

interface BetCombo {
  id: string;
  name: string;
  type?: string;
  price?: number;  // combined odds
  description?: string;
  in_stock?: boolean;  // always true for bets
}

interface BetCombosGridProps {
  title?: string;
  items: BetCombo[];
  onAction?: (action: string, params?: any) => void;
}

export function BetCombosGrid({ title, items, onAction }: BetCombosGridProps) {
  return (
    <div className="space-y-3">
      {title && (
        <h3 className="text-lg font-bold text-white flex items-center gap-2">
          <Lightning size={20} className="text-yellow-400" />
          {title}
        </h3>
      )}
      <div className="grid grid-cols-1 gap-3">
        {items.map((combo) => (
          <Card
            key={combo.id}
            className="bg-slate-800 border-slate-700 hover:border-emerald-500/50 transition-all cursor-pointer"
            onClick={() => onAction?.('add_combo', { combo_id: combo.id })}
          >
            <CardContent className="p-4">
              <div className="flex items-start justify-between gap-3">
                <div className="flex-1">
                  <div className="flex items-center gap-2 mb-1">
                    {combo.type && (
                      <Badge variant="outline" className="text-xs bg-yellow-500/10 text-yellow-400 border-yellow-500/30">
                        {combo.type}
                      </Badge>
                    )}
                  </div>
                  <h4 className="font-semibold text-white text-sm">{combo.name}</h4>
                  {combo.description && (
                    <p className="text-xs text-slate-400 mt-1">{combo.description}</p>
                  )}
                </div>

                <div className="flex flex-col items-end gap-2">
                  {combo.price && (
                    <div className="text-right">
                      <p className="text-xs text-slate-400">Combined Odds</p>
                      <p className="text-xl font-bold text-emerald-400">{combo.price.toFixed(2)}</p>
                    </div>
                  )}
                  <Button
                    size="sm"
                    className="bg-emerald-600 hover:bg-emerald-700"
                    onClick={(e) => {
                      e.stopPropagation();
                      onAction?.('add_combo', { combo_id: combo.id });
                    }}
                  >
                    <Plus size={14} weight="bold" className="mr-1" />
                    Add
                  </Button>
                </div>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}
