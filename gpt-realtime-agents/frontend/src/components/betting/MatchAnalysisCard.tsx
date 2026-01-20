import React from 'react';

interface TeamData {
  name: string;
  form: string;
  home_form?: string;
  away_form?: string;
  league_position: number | string;
  home_win_rate?: string;
  away_win_rate?: string;
  avg_goals_home?: number;
  avg_goals_away?: number;
  clean_sheet_rate?: string;
  injuries: string[];
  key_insight: string;
}

interface MatchAnalysis {
  expected_total_goals: number;
  btts_likelihood: string;
  over_2_5_history: string;
  home_advantage_strong: boolean;
  away_team_poor_travellers: boolean;
}

interface MatchOdds {
  home_win: number;
  draw: number;
  away_win: number;
  btts_yes?: number;
  over_2_5?: number;
}

interface MatchData {
  match: string;
  event_id: string;
  kick_off: string;
  league: string;
  venue: string;
  home_team: TeamData;
  away_team: TeamData;
  odds: MatchOdds;
  analysis: MatchAnalysis;
  head_to_head: string;
}

interface MatchAnalysisCardProps {
  data: {
    matches?: MatchData[];
    quick_picks?: {
      strongest_home_teams: string[];
      high_scoring_likely: string[];
      btts_candidates: string[];
    };
    title?: string;
  };
  onAction?: (action: string, data: any) => void;
  emphasis?: 'low' | 'medium' | 'high';
}

const FormDisplay: React.FC<{ form: string }> = ({ form }) => (
  <div className="flex gap-0.5">
    {form.split('').map((result, i) => (
      <span
        key={i}
        className={`w-5 h-5 flex items-center justify-center rounded text-xs font-bold ${
          result === 'W' ? 'bg-green-500 text-white' :
          result === 'D' ? 'bg-yellow-500 text-black' :
          result === 'L' ? 'bg-red-500 text-white' : 'bg-gray-600 text-gray-300'
        }`}
      >
        {result}
      </span>
    ))}
  </div>
);

export const MatchAnalysisCard: React.FC<MatchAnalysisCardProps> = ({
  data,
  onAction,
  emphasis = 'medium'
}) => {
  const matches = data.matches || [];
  const quickPicks = data.quick_picks;

  const handleAddToBetSlip = (match: MatchData, betType: string, selection: string, odds: number) => {
    if (onAction) {
      onAction('add_to_bet_slip', {
        type: betType,
        selection: selection,
        odds: odds,
        match: match.match,
        event_id: match.event_id
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
          <span className="text-xl">#</span>
          {data.title || 'Match Analysis'}
        </h3>
        {quickPicks && (
          <div className="flex flex-wrap gap-2 mt-2 text-xs">
            {quickPicks.strongest_home_teams.length > 0 && (
              <span className="px-2 py-1 bg-green-500/20 text-green-400 rounded">
                Strong Home: {quickPicks.strongest_home_teams.join(', ')}
              </span>
            )}
            {quickPicks.high_scoring_likely.length > 0 && (
              <span className="px-2 py-1 bg-blue-500/20 text-blue-400 rounded">
                Goals Expected: {quickPicks.high_scoring_likely.length} matches
              </span>
            )}
          </div>
        )}
      </div>

      {/* Matches */}
      <div className="p-4 space-y-4">
        {matches.slice(0, 4).map((match, idx) => (
          <div
            key={idx}
            className="rounded-lg border border-gray-700 overflow-hidden"
            style={{ backgroundColor: '#0f0f23' }}
          >
            {/* Match Header */}
            <div className="px-4 py-2 border-b border-gray-700 flex justify-between items-center"
                 style={{ backgroundColor: '#1a1a2e' }}>
              <div>
                <span className="text-white font-bold">{match.match}</span>
                <span className="text-gray-500 text-sm ml-2">{match.kick_off}</span>
              </div>
              <span className="text-xs text-gray-400">{match.league}</span>
            </div>

            {/* Teams Comparison */}
            <div className="p-4 grid grid-cols-2 gap-4">
              {/* Home Team */}
              <div className="space-y-2">
                <div className="flex items-center justify-between">
                  <span className="font-medium text-white">{match.home_team.name}</span>
                  <span className="text-xs text-gray-400">#{match.home_team.league_position}</span>
                </div>
                <div className="flex items-center gap-2">
                  <span className="text-xs text-gray-500">Form:</span>
                  <FormDisplay form={match.home_team.home_form || match.home_team.form} />
                </div>
                <div className="text-xs text-gray-400">
                  Home Win Rate: <span className="text-green-400">{match.home_team.home_win_rate}</span>
                </div>
                <div className="text-xs text-blue-400 italic">
                  {match.home_team.key_insight}
                </div>
                {match.home_team.injuries.length > 0 && (
                  <div className="text-xs text-red-400">
                    Out: {match.home_team.injuries.slice(0, 2).join(', ')}
                  </div>
                )}
              </div>

              {/* Away Team */}
              <div className="space-y-2">
                <div className="flex items-center justify-between">
                  <span className="font-medium text-white">{match.away_team.name}</span>
                  <span className="text-xs text-gray-400">#{match.away_team.league_position}</span>
                </div>
                <div className="flex items-center gap-2">
                  <span className="text-xs text-gray-500">Form:</span>
                  <FormDisplay form={match.away_team.away_form || match.away_team.form} />
                </div>
                <div className="text-xs text-gray-400">
                  Away Win Rate: <span className="text-yellow-400">{match.away_team.away_win_rate}</span>
                </div>
                <div className="text-xs text-blue-400 italic">
                  {match.away_team.key_insight}
                </div>
                {match.away_team.injuries.length > 0 && (
                  <div className="text-xs text-red-400">
                    Out: {match.away_team.injuries.slice(0, 2).join(', ')}
                  </div>
                )}
              </div>
            </div>

            {/* Analysis Stats */}
            <div className="px-4 py-2 border-t border-gray-700 flex gap-4 text-xs"
                 style={{ backgroundColor: '#1a1a2e' }}>
              <div className="flex items-center gap-1">
                <span className="text-gray-500">Expected Goals:</span>
                <span className={`font-bold ${
                  match.analysis.expected_total_goals > 2.5 ? 'text-green-400' : 'text-gray-300'
                }`}>
                  {match.analysis.expected_total_goals}
                </span>
              </div>
              <div className="flex items-center gap-1">
                <span className="text-gray-500">BTTS:</span>
                <span className={`font-bold ${
                  parseInt(match.analysis.btts_likelihood) > 65 ? 'text-green-400' : 'text-gray-300'
                }`}>
                  {match.analysis.btts_likelihood}
                </span>
              </div>
              <div className="flex items-center gap-1">
                <span className="text-gray-500">Over 2.5:</span>
                <span className="text-gray-300">{match.analysis.over_2_5_history}</span>
              </div>
            </div>

            {/* Betting Options */}
            <div className="p-3 border-t border-gray-700 grid grid-cols-5 gap-2">
              <button
                onClick={() => handleAddToBetSlip(match, 'Match Result', match.home_team.name, match.odds.home_win)}
                className="py-2 px-2 rounded bg-gray-700 hover:bg-green-600 transition-colors text-center"
              >
                <div className="text-xs text-gray-400">Home</div>
                <div className="font-bold text-white">{match.odds.home_win.toFixed(2)}</div>
              </button>
              <button
                onClick={() => handleAddToBetSlip(match, 'Match Result', 'Draw', match.odds.draw)}
                className="py-2 px-2 rounded bg-gray-700 hover:bg-yellow-600 transition-colors text-center"
              >
                <div className="text-xs text-gray-400">Draw</div>
                <div className="font-bold text-white">{match.odds.draw.toFixed(2)}</div>
              </button>
              <button
                onClick={() => handleAddToBetSlip(match, 'Match Result', match.away_team.name, match.odds.away_win)}
                className="py-2 px-2 rounded bg-gray-700 hover:bg-blue-600 transition-colors text-center"
              >
                <div className="text-xs text-gray-400">Away</div>
                <div className="font-bold text-white">{match.odds.away_win.toFixed(2)}</div>
              </button>
              {match.odds.btts_yes && (
                <button
                  onClick={() => handleAddToBetSlip(match, 'BTTS', 'Yes', match.odds.btts_yes!)}
                  className="py-2 px-2 rounded bg-gray-700 hover:bg-purple-600 transition-colors text-center"
                >
                  <div className="text-xs text-gray-400">BTTS</div>
                  <div className="font-bold text-white">{match.odds.btts_yes.toFixed(2)}</div>
                </button>
              )}
              {match.odds.over_2_5 && (
                <button
                  onClick={() => handleAddToBetSlip(match, 'Over/Under', 'Over 2.5', match.odds.over_2_5!)}
                  className="py-2 px-2 rounded bg-gray-700 hover:bg-orange-600 transition-colors text-center"
                >
                  <div className="text-xs text-gray-400">O2.5</div>
                  <div className="font-bold text-white">{match.odds.over_2_5.toFixed(2)}</div>
                </button>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default MatchAnalysisCard;
