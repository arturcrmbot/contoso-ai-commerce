import { Badge } from '@/components/ui/badge';
import { Clock, Lightning } from '@phosphor-icons/react';

export interface Match {
  id: string;
  home_team: string;
  away_team: string;
  league: string;
  kick_off: string;
  venue?: string;
  status: 'upcoming' | 'live' | 'finished';
  odds: {
    home: number;
    draw: number;
    away: number;
  };
  live_score?: { home: number; away: number; minute: number };
}

interface MatchCardProps {
  match: Match;
  onAddToBetSlip?: (eventId: string, selection: { market: string; selection: string; odds: number; team: string }) => void;
  onViewDetails?: (eventId: string) => void;
  compact?: boolean;
}

// Team badge colors based on team name (consistent hashing)
const getTeamColors = (teamName: string): { bg: string; text: string } => {
  const colors = [
    { bg: 'bg-red-600', text: 'text-white' },
    { bg: 'bg-blue-600', text: 'text-white' },
    { bg: 'bg-green-600', text: 'text-white' },
    { bg: 'bg-yellow-500', text: 'text-black' },
    { bg: 'bg-purple-600', text: 'text-white' },
    { bg: 'bg-orange-500', text: 'text-white' },
    { bg: 'bg-sky-500', text: 'text-white' },
    { bg: 'bg-rose-600', text: 'text-white' },
    { bg: 'bg-indigo-600', text: 'text-white' },
    { bg: 'bg-emerald-600', text: 'text-white' },
  ];
  const hash = teamName.split('').reduce((acc, char) => acc + char.charCodeAt(0), 0);
  return colors[hash % colors.length];
};

// Get team initials
const getTeamInitials = (teamName: string): string => {
  const words = teamName.split(' ');
  if (words.length === 1) return teamName.substring(0, 3).toUpperCase();
  return words.map(w => w[0]).join('').substring(0, 3).toUpperCase();
};

export function MatchCard({ match, onAddToBetSlip, onViewDetails, compact = false }: MatchCardProps) {
  const formatKickOff = (kickOff: string) => {
    const date = new Date(kickOff);
    const now = new Date();
    const isToday = date.toDateString() === now.toDateString();
    const isTomorrow = date.toDateString() === new Date(now.getTime() + 86400000).toDateString();

    const timeStr = date.toLocaleTimeString('en-GB', { hour: '2-digit', minute: '2-digit' });

    if (isToday) return `Today ${timeStr}`;
    if (isTomorrow) return `Tomorrow ${timeStr}`;
    return date.toLocaleDateString('en-GB', { day: 'numeric', month: 'short' }) + ` ${timeStr}`;
  };

  const handleOddsClick = (e: React.MouseEvent, selection: 'home' | 'draw' | 'away', odds: number) => {
    e.stopPropagation();
    if (!onAddToBetSlip) return;

    const team = selection === 'home' ? match.home_team :
                 selection === 'away' ? match.away_team : 'Draw';

    onAddToBetSlip(match.id, {
      market: 'match_result',
      selection,
      odds,
      team
    });
  };

  const homeColors = getTeamColors(match.home_team);
  const awayColors = getTeamColors(match.away_team);

  // Compact row style (like bet365 list view)
  if (compact) {
    return (
      <div
        className="bg-slate-800/50 hover:bg-slate-700/50 border-b border-slate-700/50 px-3 py-2 cursor-pointer transition-colors"
        onClick={() => onViewDetails?.(match.id)}
      >
        <div className="flex items-center gap-3">
          {/* Time / Live indicator */}
          <div className="w-16 flex-shrink-0">
            {match.status === 'live' ? (
              <div className="flex items-center gap-1">
                <span className="w-2 h-2 bg-red-500 rounded-full animate-pulse" />
                <span className="text-xs text-red-400 font-medium">{match.live_score?.minute}'</span>
              </div>
            ) : (
              <span className="text-xs text-slate-400">{formatKickOff(match.kick_off)}</span>
            )}
          </div>

          {/* Teams */}
          <div className="flex-1 min-w-0">
            <div className="flex items-center gap-2">
              <div className={`w-5 h-5 rounded-sm ${homeColors.bg} flex items-center justify-center`}>
                <span className={`text-[8px] font-bold ${homeColors.text}`}>{getTeamInitials(match.home_team)}</span>
              </div>
              <span className="text-sm text-white truncate">{match.home_team}</span>
              {match.live_score && <span className="text-sm font-bold text-white ml-auto">{match.live_score.home}</span>}
            </div>
            <div className="flex items-center gap-2 mt-1">
              <div className={`w-5 h-5 rounded-sm ${awayColors.bg} flex items-center justify-center`}>
                <span className={`text-[8px] font-bold ${awayColors.text}`}>{getTeamInitials(match.away_team)}</span>
              </div>
              <span className="text-sm text-white truncate">{match.away_team}</span>
              {match.live_score && <span className="text-sm font-bold text-white ml-auto">{match.live_score.away}</span>}
            </div>
          </div>

          {/* Odds */}
          <div className="flex gap-1">
            <button
              onClick={(e) => handleOddsClick(e, 'home', match.odds.home)}
              className="w-14 h-10 bg-slate-700 hover:bg-emerald-600 rounded text-center transition-colors"
            >
              <span className="text-xs text-slate-400 block">1</span>
              <span className="text-sm font-bold text-yellow-400">{match.odds.home.toFixed(2)}</span>
            </button>
            <button
              onClick={(e) => handleOddsClick(e, 'draw', match.odds.draw)}
              className="w-14 h-10 bg-slate-700 hover:bg-emerald-600 rounded text-center transition-colors"
            >
              <span className="text-xs text-slate-400 block">X</span>
              <span className="text-sm font-bold text-yellow-400">{match.odds.draw.toFixed(2)}</span>
            </button>
            <button
              onClick={(e) => handleOddsClick(e, 'away', match.odds.away)}
              className="w-14 h-10 bg-slate-700 hover:bg-emerald-600 rounded text-center transition-colors"
            >
              <span className="text-xs text-slate-400 block">2</span>
              <span className="text-sm font-bold text-yellow-400">{match.odds.away.toFixed(2)}</span>
            </button>
          </div>
        </div>
      </div>
    );
  }

  // Card style (featured match)
  return (
    <div
      className="bg-gradient-to-br from-slate-800 to-slate-900 rounded-xl overflow-hidden border border-slate-700/50 hover:border-emerald-500/50 transition-all cursor-pointer group"
      onClick={() => onViewDetails?.(match.id)}
    >
      {/* Header with league and live badge */}
      <div className="bg-slate-900/80 px-4 py-2 flex items-center justify-between border-b border-slate-700/50">
        <div className="flex items-center gap-2">
          <span className="text-xs font-medium text-slate-400">{match.league}</span>
        </div>
        {match.status === 'live' ? (
          <Badge className="bg-red-500 text-white animate-pulse text-xs">
            <Lightning size={10} weight="fill" className="mr-1" />
            LIVE {match.live_score?.minute}'
          </Badge>
        ) : (
          <div className="flex items-center gap-1 text-slate-400">
            <Clock size={12} />
            <span className="text-xs">{formatKickOff(match.kick_off)}</span>
          </div>
        )}
      </div>

      {/* Match content */}
      <div className="p-4">
        {/* Teams with badges */}
        <div className="flex items-center justify-between mb-4">
          {/* Home team */}
          <div className="flex-1 text-center">
            <div className={`w-12 h-12 rounded-lg ${homeColors.bg} flex items-center justify-center mx-auto mb-2 shadow-lg`}>
              <span className={`text-lg font-bold ${homeColors.text}`}>{getTeamInitials(match.home_team)}</span>
            </div>
            <p className="font-semibold text-white text-sm truncate">{match.home_team}</p>
          </div>

          {/* VS / Score */}
          <div className="px-4">
            {match.status === 'live' && match.live_score ? (
              <div className="text-center">
                <div className="text-2xl font-bold text-white">
                  {match.live_score.home} - {match.live_score.away}
                </div>
              </div>
            ) : (
              <div className="text-slate-500 font-bold text-lg">VS</div>
            )}
          </div>

          {/* Away team */}
          <div className="flex-1 text-center">
            <div className={`w-12 h-12 rounded-lg ${awayColors.bg} flex items-center justify-center mx-auto mb-2 shadow-lg`}>
              <span className={`text-lg font-bold ${awayColors.text}`}>{getTeamInitials(match.away_team)}</span>
            </div>
            <p className="font-semibold text-white text-sm truncate">{match.away_team}</p>
          </div>
        </div>

        {/* Odds buttons */}
        <div className="grid grid-cols-3 gap-2">
          <button
            onClick={(e) => handleOddsClick(e, 'home', match.odds.home)}
            className="bg-slate-700/50 hover:bg-emerald-600 border border-slate-600 hover:border-emerald-500 rounded-lg py-3 transition-all group/btn"
          >
            <span className="text-[10px] text-slate-400 group-hover/btn:text-white block">HOME</span>
            <span className="text-lg font-bold text-yellow-400 group-hover/btn:text-white">{match.odds.home.toFixed(2)}</span>
          </button>
          <button
            onClick={(e) => handleOddsClick(e, 'draw', match.odds.draw)}
            className="bg-slate-700/50 hover:bg-emerald-600 border border-slate-600 hover:border-emerald-500 rounded-lg py-3 transition-all group/btn"
          >
            <span className="text-[10px] text-slate-400 group-hover/btn:text-white block">DRAW</span>
            <span className="text-lg font-bold text-yellow-400 group-hover/btn:text-white">{match.odds.draw.toFixed(2)}</span>
          </button>
          <button
            onClick={(e) => handleOddsClick(e, 'away', match.odds.away)}
            className="bg-slate-700/50 hover:bg-emerald-600 border border-slate-600 hover:border-emerald-500 rounded-lg py-3 transition-all group/btn"
          >
            <span className="text-[10px] text-slate-400 group-hover/btn:text-white block">AWAY</span>
            <span className="text-lg font-bold text-yellow-400 group-hover/btn:text-white">{match.odds.away.toFixed(2)}</span>
          </button>
        </div>
      </div>

      {/* More markets hint */}
      <div className="bg-slate-900/50 px-4 py-2 text-center border-t border-slate-700/50">
        <span className="text-xs text-emerald-400 group-hover:text-emerald-300">+50 more markets</span>
      </div>
    </div>
  );
}
