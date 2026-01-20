import { MatchCard, Match } from './MatchCard';
import { Trophy, Lightning } from '@phosphor-icons/react';

interface MatchGridProps {
  matches: Match[];
  title?: string;
  subtitle?: string;
  onAddToBetSlip?: (eventId: string, selection: { market: string; selection: string; odds: number; team: string }) => void;
  onViewDetails?: (eventId: string) => void;
  layout?: 'grid' | 'list' | 'featured';
}

export function MatchGrid({
  matches,
  title,
  subtitle,
  onAddToBetSlip,
  onViewDetails,
  layout = 'list'
}: MatchGridProps) {
  if (!matches || matches.length === 0) {
    return (
      <div className="text-center py-12">
        <Trophy size={48} className="mx-auto text-slate-600 mb-4" />
        <p className="text-slate-400">No matches found</p>
        <p className="text-sm text-slate-500 mt-1">Try a different search or check back later</p>
      </div>
    );
  }

  // Group matches by league
  const matchesByLeague = matches.reduce((acc, match) => {
    const league = match.league || 'Other';
    if (!acc[league]) acc[league] = [];
    acc[league].push(match);
    return acc;
  }, {} as Record<string, Match[]>);

  // Featured layout - first match as hero, rest as list
  if (layout === 'featured' && matches.length > 0) {
    const [featured, ...rest] = matches;
    return (
      <div className="space-y-4">
        {title && (
          <div className="flex items-center gap-2 mb-2">
            <Lightning size={20} className="text-yellow-400" weight="fill" />
            <h2 className="text-lg font-bold text-white">{title}</h2>
            {subtitle && <span className="text-sm text-slate-400">({subtitle})</span>}
          </div>
        )}

        {/* Featured match - full card */}
        <MatchCard
          match={featured}
          onAddToBetSlip={onAddToBetSlip}
          onViewDetails={onViewDetails}
          compact={false}
        />

        {/* Rest as compact list */}
        {rest.length > 0 && (
          <div className="bg-slate-800/50 rounded-lg overflow-hidden border border-slate-700/50">
            {rest.map((match) => (
              <MatchCard
                key={match.id}
                match={match}
                onAddToBetSlip={onAddToBetSlip}
                onViewDetails={onViewDetails}
                compact={true}
              />
            ))}
          </div>
        )}
      </div>
    );
  }

  // Grid layout - all as cards
  if (layout === 'grid') {
    return (
      <div className="space-y-4">
        {title && (
          <div className="flex items-center gap-2 mb-2">
            <Trophy size={20} className="text-emerald-400" />
            <h2 className="text-lg font-bold text-white">{title}</h2>
            {subtitle && <span className="text-sm text-slate-400">({subtitle})</span>}
          </div>
        )}

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {matches.map((match) => (
            <MatchCard
              key={match.id}
              match={match}
              onAddToBetSlip={onAddToBetSlip}
              onViewDetails={onViewDetails}
              compact={false}
            />
          ))}
        </div>
      </div>
    );
  }

  // Default list layout - grouped by league
  return (
    <div className="space-y-6">
      {title && (
        <div className="flex items-center gap-2">
          <Trophy size={20} className="text-emerald-400" />
          <h2 className="text-lg font-bold text-white">{title}</h2>
          {subtitle && <span className="text-sm text-slate-400">- {subtitle}</span>}
        </div>
      )}

      {Object.entries(matchesByLeague).map(([league, leagueMatches]) => (
        <div key={league}>
          {/* League header */}
          <div className="flex items-center gap-2 mb-2 px-1">
            <div className="w-1 h-4 bg-emerald-500 rounded-full" />
            <span className="text-sm font-semibold text-white">{league}</span>
            <span className="text-xs text-slate-500">({leagueMatches.length} matches)</span>
          </div>

          {/* Matches list */}
          <div className="bg-slate-800/50 rounded-lg overflow-hidden border border-slate-700/50">
            {leagueMatches.map((match) => (
              <MatchCard
                key={match.id}
                match={match}
                onAddToBetSlip={onAddToBetSlip}
                onViewDetails={onViewDetails}
                compact={true}
              />
            ))}
          </div>
        </div>
      ))}

      {/* Results count */}
      <div className="text-center text-xs text-slate-500 pt-2">
        Showing {matches.length} match{matches.length !== 1 ? 'es' : ''}
      </div>
    </div>
  );
}
