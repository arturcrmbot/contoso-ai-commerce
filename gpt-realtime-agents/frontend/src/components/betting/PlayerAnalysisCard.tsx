import React from 'react';

interface PlayerStats {
  goals_this_season: number;
  games_played: number;
  goals_per_game: number;
  recent_form: string[];
  home_rate: number;
  away_rate: number;
  penalties: boolean;
  hot_streak: boolean;
}

interface PlayerOdds {
  anytime_scorer: number;
  first_scorer: number;
}

interface PlayerData {
  player: string;
  team: string;
  opponent: string;
  match: string;
  kick_off: string;
  is_home: boolean;
  stats: PlayerStats;
  odds: PlayerOdds;
}

interface PlayerAnalysisCardProps {
  data: {
    players?: PlayerData[];
    analysis_summary?: {
      hot_players_count: number;
      penalty_takers_count: number;
      best_home_scorers: string[];
    };
    title?: string;
  };
  onAction?: (action: string, data: any) => void;
  emphasis?: 'low' | 'medium' | 'high';
}

export const PlayerAnalysisCard: React.FC<PlayerAnalysisCardProps> = ({
  data,
  onAction,
  emphasis = 'medium'
}) => {
  const players = data.players || [];
  const summary = data.analysis_summary;

  // Sort by hot streak and goals per game
  const sortedPlayers = [...players].sort((a, b) => {
    if (a.stats.hot_streak && !b.stats.hot_streak) return -1;
    if (!a.stats.hot_streak && b.stats.hot_streak) return 1;
    return b.stats.goals_per_game - a.stats.goals_per_game;
  }).slice(0, 6); // Show top 6

  const handleAddToBetSlip = (player: PlayerData, betType: 'anytime' | 'first') => {
    if (onAction) {
      onAction('add_to_bet_slip', {
        type: betType === 'anytime' ? 'Anytime Scorer' : 'First Scorer',
        selection: player.player,
        odds: betType === 'anytime' ? player.odds.anytime_scorer : player.odds.first_scorer,
        match: player.match
      });
    }
  };

  return (
    <div className={`rounded-xl overflow-hidden ${
      emphasis === 'high' ? 'ring-2 ring-green-500' : ''
    }`} style={{ backgroundColor: '#1a1a2e' }}>
      {/* Header */}
      <div className="px-4 py-3 border-b border-gray-700" style={{ backgroundColor: '#16213e' }}>
        <h3 className="text-lg font-bold text-white flex items-center gap-2">
          <span className="text-xl">*</span>
          {data.title || 'Player Market Analysis'}
        </h3>
        {summary && (
          <div className="flex gap-4 mt-2 text-sm">
            <span className="text-green-400">{summary.hot_players_count} on hot streak</span>
            <span className="text-yellow-400">{summary.penalty_takers_count} penalty takers</span>
          </div>
        )}
      </div>

      {/* Players Grid */}
      <div className="p-4 grid gap-3">
        {sortedPlayers.map((player, idx) => (
          <div
            key={idx}
            className="rounded-lg p-3 border border-gray-700 hover:border-green-500 transition-colors"
            style={{ backgroundColor: '#0f0f23' }}
          >
            <div className="flex justify-between items-start mb-2">
              <div>
                <div className="flex items-center gap-2">
                  <span className="font-bold text-white">{player.player}</span>
                  {player.stats.hot_streak && (
                    <span className="px-2 py-0.5 bg-orange-500/20 text-orange-400 text-xs rounded-full">
                      HOT
                    </span>
                  )}
                  {player.stats.penalties && (
                    <span className="px-2 py-0.5 bg-blue-500/20 text-blue-400 text-xs rounded-full">
                      PEN
                    </span>
                  )}
                </div>
                <div className="text-sm text-gray-400">
                  {player.team} {player.is_home ? '(H)' : '(A)'} vs {player.opponent}
                </div>
              </div>
              <div className="text-right">
                <div className="text-xs text-gray-500">Goals/Game</div>
                <div className={`font-bold ${
                  player.stats.goals_per_game >= 0.8 ? 'text-green-400' :
                  player.stats.goals_per_game >= 0.5 ? 'text-yellow-400' : 'text-gray-300'
                }`}>
                  {player.stats.goals_per_game.toFixed(2)}
                </div>
              </div>
            </div>

            {/* Stats Row */}
            <div className="flex gap-4 text-xs text-gray-400 mb-3">
              <span>{player.stats.goals_this_season} goals in {player.stats.games_played} games</span>
              <span>|</span>
              <span>Home: {(player.stats.home_rate * 100).toFixed(0)}%</span>
              <span>Away: {(player.stats.away_rate * 100).toFixed(0)}%</span>
            </div>

            {/* Recent Form */}
            <div className="flex items-center gap-2 mb-3">
              <span className="text-xs text-gray-500">Last 5:</span>
              <div className="flex gap-1">
                {player.stats.recent_form.map((result, i) => (
                  <span
                    key={i}
                    className={`px-1.5 py-0.5 rounded text-xs ${
                      result.includes('GOAL') ? 'bg-green-500/20 text-green-400' : 'bg-gray-700 text-gray-500'
                    }`}
                  >
                    {result === '-' ? '-' : result.replace('GOAL', 'G').replace(' x2', 'x2')}
                  </span>
                ))}
              </div>
            </div>

            {/* Odds Buttons */}
            <div className="flex gap-2">
              <button
                onClick={() => handleAddToBetSlip(player, 'anytime')}
                className="flex-1 py-2 px-3 rounded-lg bg-green-600 hover:bg-green-500 transition-colors text-white text-sm font-medium"
              >
                Anytime @ {player.odds.anytime_scorer.toFixed(2)}
              </button>
              <button
                onClick={() => handleAddToBetSlip(player, 'first')}
                className="flex-1 py-2 px-3 rounded-lg bg-blue-600 hover:bg-blue-500 transition-colors text-white text-sm font-medium"
              >
                First @ {player.odds.first_scorer.toFixed(2)}
              </button>
            </div>
          </div>
        ))}
      </div>

      {/* Footer hint */}
      <div className="px-4 py-2 border-t border-gray-700 text-center">
        <span className="text-xs text-gray-500">
          Showing top {sortedPlayers.length} of {players.length} players - sorted by form & scoring rate
        </span>
      </div>
    </div>
  );
};

export default PlayerAnalysisCard;
