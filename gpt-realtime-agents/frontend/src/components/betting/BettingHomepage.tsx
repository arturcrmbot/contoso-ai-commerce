import { SuggestionCard } from '@/lib/types';
import { DEFAULT_SUGGESTION_CARDS } from '@/lib/constants';
import { Trophy, Lightning, TrendUp, Stack, Gift, Heart, Question, Globe, SoccerBall, Fire, Star } from '@phosphor-icons/react';

interface BettingHomepageProps {
  onSuggestionClick: (prompt: string) => void;
  disabled?: boolean;
}

// Mock featured matches for the homepage
const FEATURED_MATCHES = [
  {
    id: 'featured-1',
    home: 'Arsenal',
    away: 'Chelsea',
    league: 'Premier League',
    time: 'Today 15:00',
    odds: { home: 2.10, draw: 3.40, away: 3.20 },
    isFeatured: true,
    promo: 'BOOSTED ODDS'
  },
  {
    id: 'featured-2',
    home: 'Man City',
    away: 'Liverpool',
    league: 'Premier League',
    time: 'Tomorrow 17:30',
    odds: { home: 1.85, draw: 3.60, away: 3.80 },
    isLive: false
  },
  {
    id: 'featured-3',
    home: 'Real Madrid',
    away: 'Barcelona',
    league: 'La Liga',
    time: 'Sat 20:00',
    odds: { home: 2.40, draw: 3.30, away: 2.90 },
    isFeatured: true,
    promo: 'ACCA BOOST'
  }
];

const QUICK_LINKS = [
  { icon: Trophy, label: 'Premier League', prompt: 'Show me Premier League matches' },
  { icon: Globe, label: 'Champions League', prompt: 'Show me Champions League matches' },
  { icon: Lightning, label: 'Live Now', prompt: 'Show me live matches' },
  { icon: Stack, label: 'Accumulators', prompt: 'Help me build an accumulator' },
  { icon: Fire, label: 'Popular', prompt: 'Show me the most popular bets today' },
  { icon: Star, label: 'Best Odds', prompt: 'What are the best value bets today?' }
];

// Team badge colors
const getTeamColor = (team: string): string => {
  const colors: Record<string, string> = {
    'Arsenal': 'bg-red-600',
    'Chelsea': 'bg-blue-700',
    'Man City': 'bg-sky-500',
    'Liverpool': 'bg-red-700',
    'Real Madrid': 'bg-white border border-slate-300',
    'Barcelona': 'bg-blue-800',
  };
  return colors[team] || 'bg-slate-600';
};

const getTeamInitials = (team: string): string => {
  const initials: Record<string, string> = {
    'Arsenal': 'ARS',
    'Chelsea': 'CHE',
    'Man City': 'MCI',
    'Liverpool': 'LIV',
    'Real Madrid': 'RMA',
    'Barcelona': 'BAR',
  };
  return initials[team] || team.substring(0, 3).toUpperCase();
};

export function BettingHomepage({ onSuggestionClick, disabled }: BettingHomepageProps) {
  const iconMap: Record<string, any> = {
    'Trophy': Trophy,
    'Lightning': Lightning,
    'TrendingUp': TrendUp,
    'Stack': Stack,
    'Gift': Gift,
    'Heart': Heart,
    'Question': Question,
    'Globe': Globe,
  };

  return (
    <div className="h-full flex flex-col bg-gradient-to-b from-slate-900 via-slate-900 to-slate-800 -m-4 p-4 overflow-y-auto">
      {/* Hero Banner */}
      <div className="relative rounded-xl overflow-hidden mb-6 bg-gradient-to-r from-emerald-600 to-emerald-800">
        <div className="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAiIGhlaWdodD0iNDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGRlZnM+PHBhdHRlcm4gaWQ9ImdyaWQiIHdpZHRoPSI0MCIgaGVpZ2h0PSI0MCIgcGF0dGVyblVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTSAwIDEwIEwgNDAgMTAgTSAxMCAwIEwgMTAgNDAgTSAwIDIwIEwgNDAgMjAgTSAyMCAwIEwgMjAgNDAgTSAwIDMwIEwgNDAgMzAgTSAzMCAwIEwgMzAgNDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0icmdiYSgyNTUsMjU1LDI1NSwwLjA1KSIgc3Ryb2tlLXdpZHRoPSIxIi8+PC9wYXR0ZXJuPjwvZGVmcz48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSJ1cmwoI2dyaWQpIi8+PC9zdmc+')] opacity-30" />
        <div className="relative p-6">
          <div className="flex items-center gap-3 mb-2">
            <SoccerBall size={32} weight="fill" className="text-white" />
            <h1 className="text-2xl font-bold text-white">Contoso Bet</h1>
          </div>
          <p className="text-emerald-100 text-sm mb-4">Your AI-powered football betting assistant</p>
          <div className="flex gap-2">
            <span className="bg-yellow-400 text-black text-xs font-bold px-3 py-1 rounded-full">NEW USER BONUS</span>
            <span className="bg-white/20 text-white text-xs font-medium px-3 py-1 rounded-full">Bet £10 Get £30</span>
          </div>
        </div>
      </div>

      {/* Quick Links */}
      <div className="flex gap-2 mb-6 overflow-x-auto pb-2 flex-shrink-0">
        {QUICK_LINKS.map((link, idx) => (
          <button
            key={idx}
            onClick={() => !disabled && onSuggestionClick(link.prompt)}
            disabled={disabled}
            className={`flex items-center gap-2 px-4 py-2 rounded-full bg-slate-800 border border-slate-700 hover:border-emerald-500 hover:bg-slate-700 transition-all whitespace-nowrap ${disabled ? 'opacity-50 cursor-not-allowed' : ''}`}
          >
            <link.icon size={16} className="text-emerald-400" />
            <span className="text-sm text-white font-medium">{link.label}</span>
          </button>
        ))}
      </div>

      {/* Featured Matches */}
      <div className="mb-6">
        <div className="flex items-center justify-between mb-3">
          <h2 className="text-lg font-bold text-white flex items-center gap-2">
            <Fire size={20} className="text-orange-400" />
            Featured Matches
          </h2>
          <button
            onClick={() => !disabled && onSuggestionClick('Show me all upcoming matches')}
            className="text-xs text-emerald-400 hover:text-emerald-300"
          >
            View all
          </button>
        </div>

        <div className="space-y-2">
          {FEATURED_MATCHES.map((match) => (
            <div
              key={match.id}
              className={`bg-slate-800/80 rounded-lg p-3 border border-slate-700/50 hover:border-emerald-500/50 transition-all cursor-pointer ${disabled ? 'opacity-50' : ''}`}
              onClick={() => !disabled && onSuggestionClick(`Tell me about ${match.home} vs ${match.away}`)}
            >
              <div className="flex items-center justify-between mb-2">
                <div className="flex items-center gap-2">
                  <span className="text-xs text-slate-400">{match.league}</span>
                  {match.promo && (
                    <span className="bg-yellow-400/20 text-yellow-400 text-[10px] font-bold px-2 py-0.5 rounded">{match.promo}</span>
                  )}
                </div>
                <span className="text-xs text-slate-400">{match.time}</span>
              </div>

              <div className="flex items-center gap-3">
                {/* Teams */}
                <div className="flex-1">
                  <div className="flex items-center gap-2 mb-1">
                    <div className={`w-6 h-6 rounded ${getTeamColor(match.home)} flex items-center justify-center`}>
                      <span className={`text-[8px] font-bold ${match.home === 'Real Madrid' ? 'text-slate-800' : 'text-white'}`}>{getTeamInitials(match.home)}</span>
                    </div>
                    <span className="text-sm text-white font-medium">{match.home}</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <div className={`w-6 h-6 rounded ${getTeamColor(match.away)} flex items-center justify-center`}>
                      <span className={`text-[8px] font-bold ${match.away === 'Real Madrid' ? 'text-slate-800' : 'text-white'}`}>{getTeamInitials(match.away)}</span>
                    </div>
                    <span className="text-sm text-white font-medium">{match.away}</span>
                  </div>
                </div>

                {/* Odds */}
                <div className="flex gap-1">
                  <div className="w-12 h-12 bg-slate-700 hover:bg-emerald-600 rounded flex flex-col items-center justify-center transition-colors">
                    <span className="text-[9px] text-slate-400">1</span>
                    <span className="text-sm font-bold text-yellow-400">{match.odds.home.toFixed(2)}</span>
                  </div>
                  <div className="w-12 h-12 bg-slate-700 hover:bg-emerald-600 rounded flex flex-col items-center justify-center transition-colors">
                    <span className="text-[9px] text-slate-400">X</span>
                    <span className="text-sm font-bold text-yellow-400">{match.odds.draw.toFixed(2)}</span>
                  </div>
                  <div className="w-12 h-12 bg-slate-700 hover:bg-emerald-600 rounded flex flex-col items-center justify-center transition-colors">
                    <span className="text-[9px] text-slate-400">2</span>
                    <span className="text-sm font-bold text-yellow-400">{match.odds.away.toFixed(2)}</span>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Popular Actions Grid */}
      <div className="mb-6">
        <h2 className="text-lg font-bold text-white mb-3">What would you like to do?</h2>
        <div className="grid grid-cols-2 gap-2">
          {DEFAULT_SUGGESTION_CARDS.slice(0, 4).map((card) => {
            const IconComponent = iconMap[card.icon] || Trophy;
            return (
              <button
                key={card.id}
                onClick={() => !disabled && onSuggestionClick(card.prompt)}
                disabled={disabled}
                className={`bg-slate-800/60 hover:bg-slate-700/60 border border-slate-700/50 hover:border-emerald-500/50 rounded-lg p-4 text-left transition-all ${disabled ? 'opacity-50 cursor-not-allowed' : ''}`}
              >
                <IconComponent size={24} className="text-emerald-400 mb-2" />
                <h3 className="text-sm font-semibold text-white mb-1">{card.title}</h3>
                <p className="text-xs text-slate-400">{card.subtitle}</p>
              </button>
            );
          })}
        </div>
      </div>

      {/* More Options */}
      <div className="grid grid-cols-4 gap-2 mb-6">
        {DEFAULT_SUGGESTION_CARDS.slice(4).map((card) => {
          const IconComponent = iconMap[card.icon] || Trophy;
          return (
            <button
              key={card.id}
              onClick={() => !disabled && onSuggestionClick(card.prompt)}
              disabled={disabled}
              className={`bg-slate-800/40 hover:bg-slate-700/40 border border-slate-700/30 hover:border-slate-600 rounded-lg p-3 text-center transition-all ${disabled ? 'opacity-50 cursor-not-allowed' : ''}`}
            >
              <IconComponent size={20} className="text-slate-400 mx-auto mb-1" />
              <span className="text-[10px] text-slate-400 block">{card.title}</span>
            </button>
          );
        })}
      </div>

      {/* Responsible Gambling Footer */}
      <div className="mt-auto pt-4 border-t border-slate-700/50">
        <p className="text-[10px] text-slate-500 text-center">
          18+ Only. Gamble responsibly. BeGambleAware.org
        </p>
      </div>
    </div>
  );
}
