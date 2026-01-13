import { ProductShowcase } from './ProductShowcase';
import { ProductCard } from './ProductCard';
import { PromoBanner } from './PromoBanner';
import { PlanCards } from './PlanCards';
import { BettingHomepage } from '../betting/BettingHomepage';
import { Button } from '@/components/ui/button';
import { ArrowLeft } from '@phosphor-icons/react';
import { FlexibleRenderer } from '../visual-primitives/FlexibleRenderer';
import { VisualConfig, isFlexibleVisual, LegacyVisual } from '../visual-primitives/types';

interface DynamicVisualCanvasProps {
  visualConfig: VisualConfig | null;
  onProductClick?: (item: any) => void;
  onBackToSuggestions: () => void;
  onSuggestionClick: (prompt: string) => void;
  disabled?: boolean;
}

export function DynamicVisualCanvas({
  visualConfig,
  onProductClick,
  onBackToSuggestions,
  onSuggestionClick,
  disabled
}: DynamicVisualCanvasProps) {
  // No visual data - show betting homepage
  if (!visualConfig) {
    return (
      <BettingHomepage
        onSuggestionClick={onSuggestionClick}
        disabled={disabled}
      />
    );
  }

  // Handle action callbacks from flexible renderer
  const handleAction = (action: string, params?: any) => {
    console.log('[DynamicVisualCanvas] Action:', action, params);

    switch (action) {
      case 'product_click':
      case 'add_to_cart':
      case 'add_accessory':
      case 'add_to_slip':
      case 'view_match':
        if (onProductClick) {
          onProductClick({ action, ...params });
        }
        break;

      case 'plan_select':
        if (onProductClick) {
          onProductClick({ action: 'plan_select', type: 'plan', ...params });
        }
        break;

      default:
        console.log('[DynamicVisualCanvas] Unhandled action:', action);
    }
  };

  // New flexible visual system
  if (isFlexibleVisual(visualConfig)) {
    return (
      <div className="h-full flex flex-col bg-gradient-to-b from-slate-900 via-slate-900 to-slate-800 -m-4 p-4">
        <Button
          variant="ghost"
          size="sm"
          onClick={onBackToSuggestions}
          className="mb-3 -ml-2 self-start flex-shrink-0 text-slate-400 hover:text-white hover:bg-slate-800"
        >
          <ArrowLeft size={16} className="mr-1" />
          Back to home
        </Button>

        <div className="flex-1 min-h-0 overflow-y-auto">
          <FlexibleRenderer visual={visualConfig} onAction={handleAction} />
        </div>
      </div>
    );
  }

  // Legacy visual types (backwards compatibility)
  const legacyVisual = visualConfig as LegacyVisual;

  return (
    <div className="h-full flex flex-col bg-gradient-to-b from-slate-900 via-slate-900 to-slate-800 -m-4 p-4">
      <Button
        variant="ghost"
        size="sm"
        onClick={onBackToSuggestions}
        className="mb-3 -ml-2 self-start text-slate-400 hover:text-white hover:bg-slate-800"
      >
        <ArrowLeft size={16} className="mr-1" />
        Back to home
      </Button>

      <div className="flex-1 overflow-y-auto">
        {legacyVisual.type === 'product_grid' && legacyVisual.items && (
          <ProductShowcase
            products={legacyVisual.items}
            highlightedId={null}
            onProductClick={onProductClick || (() => {})}
          />
        )}

        {legacyVisual.type === 'promo_banner' && legacyVisual.items && (
          <PromoBanner
            title={legacyVisual.title || ''}
            items={legacyVisual.items}
          />
        )}

        {legacyVisual.type === 'plan_cards' && legacyVisual.items && (
          <PlanCards
            title={legacyVisual.title || ''}
            items={legacyVisual.items}
            onPlanClick={onProductClick}
          />
        )}

        {legacyVisual.type === 'comparison_table' && legacyVisual.devices && (
          <div className="space-y-3">
            <h3 className="text-lg font-bold text-white">{legacyVisual.title}</h3>
            <div className="grid grid-cols-2 gap-4">
              {legacyVisual.devices.map((device: any) => (
                <ProductCard
                  key={device.id}
                  device={device}
                  onClick={() => onProductClick?.(device)}
                />
              ))}
            </div>
          </div>
        )}

        {legacyVisual.type === 'cart_preview' && legacyVisual.items && (
          <div className="space-y-3">
            <h3 className="text-lg font-bold text-white">{legacyVisual.title}</h3>
            <div className="space-y-2">
              {legacyVisual.items.map((item: any, idx: number) => (
                <div key={idx} className="bg-slate-800 border border-slate-700 rounded p-3">
                  <p className="font-semibold text-sm text-white">{item.name}</p>
                  <p className="text-xs text-slate-400">
                    £{item.price_monthly || item.price}/mo
                  </p>
                </div>
              ))}
              {legacyVisual.summary && (
                <div className="border-t border-slate-700 pt-3 mt-3">
                  <p className="font-bold text-white">Total: £{legacyVisual.summary.monthly}/mo</p>
                  <p className="text-xs text-slate-400">
                    24-month total: £{legacyVisual.summary.total_24m}
                  </p>
                </div>
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
