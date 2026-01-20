import { FlexibleVisual, VisualSection, CTAConfig } from './types';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import * as PhosphorIcons from '@phosphor-icons/react';

// Import generic primitives (betting-compatible)
import { CheckoutStepper } from './CheckoutStepper';

// Import promo (generic)
import { PromoBanner } from '../contoso/PromoBanner';

// Import ALL betting components
import { MatchCard } from '../betting/MatchCard';
import { MatchGrid } from '../betting/MatchGrid';
import { BetConfirmation } from '../betting/BetConfirmation';
import { BetTypeCards } from '../betting/BetTypeCards';
import { MatchHero } from '../betting/MatchHero';
import { CashOutCard } from '../betting/CashOutCard';
import { BetCombosGrid } from '../betting/BetCombosGrid';
import { BettingReturns } from '../betting/BettingReturns';
import { PlayerAnalysisCard } from '../betting/PlayerAnalysisCard';
import { MatchAnalysisCard } from '../betting/MatchAnalysisCard';

interface FlexibleRendererProps {
  visual: FlexibleVisual;
  onAction?: (action: string, params?: any) => void;
}

export function FlexibleRenderer({ visual, onAction }: FlexibleRendererProps) {

  // Render a single section based on its type
  const renderSection = (section: VisualSection) => {
    // Safety check - allow sections without data for certain types that can handle it
    if (!section || !section.type) {
      console.warn('[FlexibleRenderer] Invalid section (missing type):', section);
      return null;
    }

    // For most section types, data is required
    const typesAllowingEmptyData = ['section_divider'];
    if (!section.data && !typesAllowingEmptyData.includes(section.type)) {
      console.warn('[FlexibleRenderer] Section missing data:', section.type, section);
      return null;
    }

    const sectionClasses = getSectionClasses(section);

    try {
      switch (section.type) {
        // ===========================================
        // BETTING COMPONENTS (Primary for Contoso Bet)
        // ===========================================

        // Match Hero - detailed match view with odds
        case 'match_hero':
        case 'product_hero':  // Legacy mapping - product_hero now shows match
          return <MatchHero data={section.data} onAction={onAction} emphasis={section.emphasis} />;

        // Player Analysis - intelligent player market analysis
        case 'player_analysis':
          return <PlayerAnalysisCard data={section.data} onAction={onAction} emphasis={section.emphasis} />;

        // Match Analysis - intelligent match betting analysis
        case 'match_analysis':
          return <MatchAnalysisCard data={section.data} onAction={onAction} emphasis={section.emphasis} />;

        // Cash Out Card - shows cash out value for active bets
        case 'cash_out':
        case 'trade_in_value':  // Legacy mapping - trade_in now shows cash out
          return <CashOutCard data={section.data} onAction={onAction} emphasis={section.emphasis} />;

        // Bet Combos Grid - accumulator/parlay suggestions
        case 'bet_combos':
        case 'accessory_grid':  // Legacy mapping - accessory_grid now shows bet combos
          const comboItems = section.data?.items || [];
          if (!Array.isArray(comboItems) || comboItems.length === 0) {
            return null;
          }
          return (
            <BetCombosGrid
              title={section.title}
              items={comboItems}
              onAction={onAction}
            />
          );

      // ===========================================
      // PROGRESS COMPONENTS (Generic - OK for betting)
      // ===========================================
      case 'checkout_stepper':
      case 'bet_progress':
        return <CheckoutStepper data={section.data} emphasis={section.emphasis} />;

      // Info components - betting returns breakdown
      case 'price_breakdown':
      case 'betting_returns':
        return <BettingReturns data={section.data} style={section.style} />;

      // Bet type cards (for showing available markets, bet recommendations, etc.)
      case 'bet_type_cards':
      case 'plan_selector':  // Legacy mapping - plan_selector now shows bet types
        const betTypeItems = Array.isArray(section.data) ? section.data : (section.data?.items || []);
        if (!Array.isArray(betTypeItems) || betTypeItems.length === 0) {
          return null;
        }
        return (
          <BetTypeCards
            title={section.title || 'Available Bet Types'}
            items={betTypeItems}
            onBetTypeClick={(betType) => onAction?.('bet_type_select', { bet_type_id: betType.id })}
          />
        );

      // Promotional
      case 'promo_banner':
        const promoItems = section.data?.items || [];
        if (!Array.isArray(promoItems) || promoItems.length === 0) {
          return null;
        }
        return (
          <PromoBanner
            title={section.title || ''}
            items={promoItems}
          />
        );

      // Utility components
      case 'section_divider':
        return (
          <div className="py-4">
            {section.title && (
              <h3 className="text-lg font-bold text-center mb-2">{section.title}</h3>
            )}
            <div className="border-t" />
          </div>
        );

      case 'info_callout':
        return (
          <div className={`rounded-lg p-4 ${
            section.style === 'emphasized' ? 'bg-primary/10 border-2 border-primary' :
            'bg-muted/50'
          }`}>
            {section.title && (
              <h4 className="font-semibold mb-1">{section.title}</h4>
            )}
            {section.data.message && (
              <p className="text-sm text-muted-foreground">{section.data.message}</p>
            )}
          </div>
        );

      // Betting components
      case 'match_card':
        return (
          <MatchCard
            match={section.data}
            onAddToBetSlip={(eventId, selection) => onAction?.('add_to_slip', { eventId, ...selection })}
            onViewDetails={(eventId) => onAction?.('view_match', { eventId })}
          />
        );

      case 'match_grid':
        const matches = section.data?.matches || section.data?.items || section.data || [];
        return (
          <MatchGrid
            matches={Array.isArray(matches) ? matches : []}
            title={section.title}
            subtitle={section.subtitle}
            onAddToBetSlip={(eventId, selection) => onAction?.('add_to_slip', { eventId, ...selection })}
            onViewDetails={(eventId) => onAction?.('view_match', { eventId })}
          />
        );

      case 'bet_confirmation':
        return <BetConfirmation {...section.data} />;

      case 'bet_slip_preview':
        const selections = section.data?.selections || [];
        const combinedOdds = section.data?.combined_odds || 0;
        const stake = section.data?.stake || 10;
        const potentialReturn = section.data?.potential_return || 0;
        const potentialProfit = potentialReturn - stake;

        // Format market name for display
        const formatMarket = (market: string) => {
          return market.replace(/_/g, ' ').replace(/\b\w/g, (l: string) => l.toUpperCase());
        };

        // Format selection for display
        const formatSelection = (selection: string) => {
          if (selection === 'home') return 'Home Win';
          if (selection === 'away') return 'Away Win';
          if (selection === 'draw') return 'Draw';
          return selection.replace(/\b\w/g, (l: string) => l.toUpperCase());
        };

        return (
          <div className="rounded-xl border border-slate-700 bg-gradient-to-b from-slate-800 to-slate-900 overflow-hidden">
            {/* Header */}
            <div className="bg-slate-800 border-b border-slate-700 px-4 py-3 flex items-center justify-between">
              <div className="flex items-center gap-2">
                <span className="text-xl">🎫</span>
                <h4 className="font-bold text-lg text-white">Bet Slip</h4>
                {selections.length > 0 && (
                  <span className="bg-emerald-600 text-white text-xs font-bold px-2 py-0.5 rounded-full">
                    {selections.length}
                  </span>
                )}
              </div>
              {selections.length > 1 && (
                <span className="text-xs bg-yellow-500/20 text-yellow-400 px-2 py-1 rounded flex items-center gap-1">
                  ⚡ {selections.length}-Fold Acca
                </span>
              )}
            </div>

            {selections.length > 0 ? (
              <>
                {/* Selections */}
                <div className="p-3 space-y-2 max-h-80 overflow-y-auto">
                  {selections.map((sel: any, idx: number) => (
                    <div key={sel.id || idx} className="bg-slate-800/80 rounded-lg p-3 border border-slate-700/50">
                      <p className="font-semibold text-white text-sm">{sel.event_name}</p>
                      <p className="text-xs text-slate-400 mt-1">{formatMarket(sel.market)}</p>
                      <div className="flex items-center justify-between mt-2 pt-2 border-t border-slate-700/50">
                        <span className="text-sm font-medium text-emerald-400">{formatSelection(sel.selection)}</span>
                        <span className="font-bold text-yellow-400 text-lg">{sel.odds?.toFixed(2)}</span>
                      </div>
                    </div>
                  ))}
                </div>

                {/* Summary */}
                <div className="border-t border-slate-700 bg-slate-900/50 p-4 space-y-3">
                  <div className="flex justify-between items-center">
                    <span className="text-slate-400 text-sm">Combined Odds</span>
                    <span className="font-bold text-xl text-yellow-400">{combinedOdds.toFixed(2)}</span>
                  </div>
                  <div className="flex justify-between items-center">
                    <span className="text-slate-400 text-sm">Stake</span>
                    <span className="text-white font-medium">£{stake.toFixed(2)}</span>
                  </div>
                  <div className="bg-emerald-900/30 border border-emerald-700/50 rounded-lg p-3 mt-2">
                    <div className="flex justify-between items-center">
                      <span className="text-emerald-300 text-sm">Potential Return</span>
                      <span className="font-bold text-2xl text-emerald-400">£{potentialReturn.toFixed(2)}</span>
                    </div>
                    <div className="flex justify-between items-center mt-1">
                      <span className="text-emerald-300/70 text-xs">Profit</span>
                      <span className="text-emerald-400 text-sm">+£{potentialProfit.toFixed(2)}</span>
                    </div>
                  </div>
                </div>
              </>
            ) : (
              <div className="p-8 text-center">
                <span className="text-4xl opacity-50">🎫</span>
                <p className="text-slate-400 mt-2">No selections yet</p>
              </div>
            )}
          </div>
        );

        default:
          console.warn(`Unknown section type: ${section.type}`);
          return null;
      }
    } catch (error) {
      console.error('[FlexibleRenderer] Error rendering section:', section.type, error);
      return (
        <div className="text-sm text-destructive p-4 border border-destructive rounded">
          Error rendering {section.type}
        </div>
      );
    }
  };

  const getSectionClasses = (section: VisualSection) => {
    const classes: string[] = [];

    if (section.emphasis === 'critical') classes.push('animate-pulse');
    if (section.className) classes.push(section.className);

    return classes.join(' ');
  };

  // Render CTA button(s)
  const renderCTA = (cta: CTAConfig) => {
    const IconComponent = cta.icon ? (PhosphorIcons as any)[cta.icon] : null;

    const variantMap = {
      primary: 'default',
      secondary: 'secondary',
      subtle: 'ghost'
    };

    return (
      <Button
        key={cta.text}
        size="lg"
        variant={variantMap[cta.prominence]}
        className={cta.prominence === 'primary' ? 'w-full' : ''}
        onClick={() => onAction?.(cta.action, cta.params)}
      >
        {IconComponent && <IconComponent size={20} className="mr-2" />}
        {cta.text}
      </Button>
    );
  };

  // Get layout container classes
  const getLayoutClasses = () => {
    switch (visual.layout) {
      case 'single_focus':
        return 'flex flex-col items-center max-w-4xl mx-auto';
      case 'two_column':
        return 'grid md:grid-cols-2 gap-6';
      case 'grid':
        return 'grid grid-cols-1 md:grid-cols-2 gap-4';
      case 'flow':
        return 'space-y-4';
      case 'multi_section':
        return 'space-y-6';
      case 'wizard':
        return 'max-w-2xl mx-auto space-y-6';
      default:
        return 'space-y-4';
    }
  };

  // Animation classes
  const getAnimationClasses = () => {
    switch (visual.animation) {
      case 'fade':
        return 'animate-in fade-in duration-300';
      case 'slide':
        return 'animate-in slide-in-from-bottom duration-300';
      case 'scale':
        return 'animate-in zoom-in duration-200';
      default:
        return '';
    }
  };

  // Theme classes
  const getThemeClasses = () => {
    switch (visual.theme) {
      case 'success':
        return 'bg-green-50/50';
      case 'warning':
        return 'bg-yellow-50/50';
      case 'info':
        return 'bg-blue-50/50';
      default:
        return '';
    }
  };

  return (
    <div className={`h-full flex flex-col ${getThemeClasses()} ${getAnimationClasses()}`}>
      {/* Header */}
      {visual.header && (
        <div className="mb-6 flex-shrink-0">
          <div className="flex items-start justify-between">
            <div>
              <h2 className="text-2xl font-bold">{visual.header.title}</h2>
              {visual.header.subtitle && (
                <p className="text-sm text-muted-foreground mt-1">
                  {visual.header.subtitle}
                </p>
              )}
            </div>
            {visual.header.badge && (
              <Badge variant="default">{visual.header.badge}</Badge>
            )}
          </div>
        </div>
      )}

      {/* Main Content */}
      <div className={`flex-1 overflow-y-auto ${getLayoutClasses()}`}>
        {visual.sections.map((section, index) => (
          <div key={section.id || index} className={getSectionClasses(section)}>
            {renderSection(section)}
          </div>
        ))}
      </div>

      {/* Footer with CTAs */}
      {(visual.cta || visual.footer) && (
        <div className="flex-shrink-0 border-t pt-4 mt-6">
          {visual.footer?.text && (
            <p className="text-sm text-muted-foreground mb-3">{visual.footer.text}</p>
          )}

          <div className="flex gap-3">
            {/* Single CTA */}
            {visual.cta && !Array.isArray(visual.cta) && renderCTA(visual.cta)}

            {/* Multiple CTAs */}
            {visual.cta && Array.isArray(visual.cta) && visual.cta.map(renderCTA)}

            {/* Footer actions */}
            {visual.footer?.actions?.map(renderCTA)}
          </div>
        </div>
      )}
    </div>
  );
}
