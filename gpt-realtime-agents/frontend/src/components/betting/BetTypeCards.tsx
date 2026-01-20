import { Card, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';

interface BetType {
  id: string;
  name: string;
  type?: string;  // category like "main", "player", "advanced", "combo"
  description?: string;
  risk_level?: string;
  popularity?: string;
  potential_return?: number;
  highlights?: string[];
}

interface BetTypeCardsProps {
  title: string;
  items: BetType[];
  onBetTypeClick?: (betType: BetType) => void;
}

// Get emoji for bet type category
function getCategoryEmoji(type?: string): string {
  switch (type?.toLowerCase()) {
    case 'main': return '⚽';
    case 'player': return '👤';
    case 'advanced': return '🎯';
    case 'combo': return '🔗';
    default: return '📊';
  }
}

// Get risk badge color
function getRiskColor(risk?: string): string {
  switch (risk?.toLowerCase()) {
    case 'low': return 'bg-green-600/20 text-green-400 border-green-600/30';
    case 'medium': return 'bg-yellow-600/20 text-yellow-400 border-yellow-600/30';
    case 'high': return 'bg-red-600/20 text-red-400 border-red-600/30';
    default: return 'bg-slate-600/20 text-slate-400 border-slate-600/30';
  }
}

// Get popularity indicator
function getPopularityStars(popularity?: string): string {
  switch (popularity?.toLowerCase()) {
    case 'very_high': return '🔥🔥🔥';
    case 'high': return '🔥🔥';
    case 'medium': return '🔥';
    case 'low': return '';
    default: return '';
  }
}

export function BetTypeCards({ title, items, onBetTypeClick }: BetTypeCardsProps) {
  return (
    <div className="space-y-4">
      <h3 className="text-lg font-bold text-white">{title}</h3>
      <div className="grid grid-cols-1 gap-3">
        {items.map((betType) => (
          <Card
            key={betType.id}
            className="cursor-pointer hover:shadow-lg hover:border-emerald-500/50 transition-all bg-slate-800 border-slate-700"
            onClick={() => onBetTypeClick?.(betType)}
          >
            <CardContent className="p-4">
              <div className="flex items-start justify-between mb-2">
                <div className="flex items-center gap-2">
                  <span className="text-2xl">{getCategoryEmoji(betType.type)}</span>
                  <div>
                    <h4 className="font-bold text-lg text-white">{betType.name}</h4>
                    {betType.type && (
                      <p className="text-xs text-slate-400 uppercase">{betType.type}</p>
                    )}
                  </div>
                </div>
                {betType.potential_return && (
                  <div className="text-right">
                    <p className="text-xl font-bold text-emerald-400">£{betType.potential_return.toFixed(2)}</p>
                    <p className="text-xs text-slate-400">potential</p>
                  </div>
                )}
              </div>

              {betType.description && (
                <p className="text-sm text-slate-300 mb-3">{betType.description}</p>
              )}

              <div className="flex flex-wrap gap-2 pt-2 border-t border-slate-700">
                {betType.risk_level && (
                  <Badge variant="outline" className={`text-xs ${getRiskColor(betType.risk_level)}`}>
                    Risk: {betType.risk_level}
                  </Badge>
                )}
                {betType.popularity && (
                  <Badge variant="outline" className="text-xs bg-slate-700/50 text-slate-300 border-slate-600">
                    Popularity: {betType.popularity} {getPopularityStars(betType.popularity)}
                  </Badge>
                )}
                {betType.highlights?.map((h, idx) => (
                  <Badge key={idx} variant="secondary" className="text-xs bg-slate-700 text-slate-200">
                    {h}
                  </Badge>
                ))}
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}
