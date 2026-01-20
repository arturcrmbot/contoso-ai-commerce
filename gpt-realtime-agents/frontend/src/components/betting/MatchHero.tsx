import { Card, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';

interface MatchHeroProps {
  data: {
    id?: string;
    name: string;  // e.g. "Arsenal vs Chelsea"
    description?: string;
    image_url?: string;
    home_odds?: number;
    attributes?: Record<string, string>;  // League, Venue, Kick-off, Status
  };
  onAction?: (action: string, params?: any) => void;
  emphasis?: 'low' | 'medium' | 'high' | 'critical';
}

export function MatchHero({ data, onAction, emphasis = 'high' }: MatchHeroProps) {
  const emphasisClasses = {
    low: 'border border-slate-700',
    medium: 'border-2 border-slate-600',
    high: 'border-2 border-slate-600 shadow-lg',
    critical: 'border-4 border-emerald-500 shadow-2xl'
  };

  // Extract teams from name
  const teams = data.name?.split(' vs ') || ['Home', 'Away'];
  const homeTeam = teams[0] || 'Home';
  const awayTeam = teams[1] || 'Away';

  return (
    <Card className={`${emphasisClasses[emphasis]} bg-slate-800 transition-all overflow-hidden`}>
      <CardContent className="p-0">
        {/* Hero Image */}
        <div className="relative h-48 bg-gradient-to-br from-slate-700 to-slate-900 flex items-center justify-center overflow-hidden">
          {data.image_url ? (
            <>
              <img
                src={data.image_url}
                alt={data.name}
                className="w-full h-full object-cover opacity-60"
                onError={(e) => {
                  e.currentTarget.style.display = 'none';
                }}
              />
              <div className="absolute inset-0 bg-gradient-to-t from-slate-900/90 to-transparent" />
            </>
          ) : (
            <div className="text-6xl">⚽</div>
          )}

          {/* Match Title Overlay */}
          <div className="absolute bottom-4 left-4 right-4 text-white">
            <h2 className="text-2xl font-bold drop-shadow-lg">{data.name}</h2>
          </div>
        </div>

        {/* Match Details */}
        <div className="p-6 space-y-4">
          {/* Description */}
          {data.description && (
            <p className="text-slate-300">{data.description}</p>
          )}

          {/* Attributes/Info */}
          {data.attributes && Object.keys(data.attributes).length > 0 && (
            <div className="flex flex-wrap gap-2">
              {Object.entries(data.attributes).map(([key, value]) => (
                <Badge key={key} variant="outline" className="bg-slate-700/50 text-slate-200 border-slate-600">
                  {key}: {value}
                </Badge>
              ))}
            </div>
          )}

          {/* Quick Odds */}
          {data.home_odds && (
            <div className="bg-slate-900/50 rounded-lg p-4 border border-slate-700">
              <p className="text-sm text-slate-400 mb-3">Match Result Odds</p>
              <div className="grid grid-cols-3 gap-3">
                <Button
                  variant="outline"
                  className="flex flex-col h-auto py-3 bg-slate-800 border-slate-600 hover:border-emerald-500 hover:bg-emerald-900/20"
                  onClick={() => onAction?.('add_to_slip', { selection: 'home', team: homeTeam })}
                >
                  <span className="text-xs text-slate-400">{homeTeam}</span>
                  <span className="text-lg font-bold text-emerald-400">{data.home_odds?.toFixed(2)}</span>
                </Button>
                <Button
                  variant="outline"
                  className="flex flex-col h-auto py-3 bg-slate-800 border-slate-600 hover:border-emerald-500 hover:bg-emerald-900/20"
                  onClick={() => onAction?.('add_to_slip', { selection: 'draw' })}
                >
                  <span className="text-xs text-slate-400">Draw</span>
                  <span className="text-lg font-bold text-yellow-400">3.40</span>
                </Button>
                <Button
                  variant="outline"
                  className="flex flex-col h-auto py-3 bg-slate-800 border-slate-600 hover:border-emerald-500 hover:bg-emerald-900/20"
                  onClick={() => onAction?.('add_to_slip', { selection: 'away', team: awayTeam })}
                >
                  <span className="text-xs text-slate-400">{awayTeam}</span>
                  <span className="text-lg font-bold text-emerald-400">3.60</span>
                </Button>
              </div>
            </div>
          )}
        </div>
      </CardContent>
    </Card>
  );
}
