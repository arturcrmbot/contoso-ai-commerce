import { ProductShowcase } from './ProductShowcase';
import { ProductCard } from './ProductCard';
import { PromoBanner } from './PromoBanner';
import { PlanCards } from './PlanCards';
import { SuggestionCards } from '../SuggestionCards';
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
  // No visual data - show suggestions
  if (!visualConfig) {
    return (
      <>
        <div className="mb-4">
          <h2 className="text-xl font-bold text-foreground mb-1">Vodafone Three Agentic Sales Assistant</h2>
          <p className="text-sm text-muted-foreground">Find your perfect phone and plan</p>
        </div>
        <SuggestionCards
          onSuggestionClick={onSuggestionClick}
          disabled={disabled}
        />
      </>
    );
  }

  // Handle action callbacks from flexible renderer
  const handleAction = (action: string, params?: any) => {
    console.log('[DynamicVisualCanvas] Action:', action, params);

    switch (action) {
      case 'product_click':
      case 'add_to_cart':
      case 'add_accessory':
        if (onProductClick) {
          // Pass the action type along with params
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
      <div className="h-full flex flex-col">
        <Button
          variant="ghost"
          size="sm"
          onClick={onBackToSuggestions}
          className="mb-3 -ml-2 self-start flex-shrink-0"
        >
          <ArrowLeft size={16} className="mr-1" />
          Back to suggestions
        </Button>

        <div className="flex-1 min-h-0">
          <FlexibleRenderer visual={visualConfig} onAction={handleAction} />
        </div>
      </div>
    );
  }

  // Legacy visual types (backwards compatibility)
  const legacyVisual = visualConfig as LegacyVisual;

  return (
    <div className="h-full flex flex-col">
      <Button
        variant="ghost"
        size="sm"
        onClick={onBackToSuggestions}
        className="mb-3 -ml-2 self-start"
      >
        <ArrowLeft size={16} className="mr-1" />
        Back to suggestions
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
            <h3 className="text-lg font-bold">{legacyVisual.title}</h3>
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
            <h3 className="text-lg font-bold">{legacyVisual.title}</h3>
            <div className="space-y-2">
              {legacyVisual.items.map((item: any, idx: number) => (
                <div key={idx} className="border rounded p-3">
                  <p className="font-semibold text-sm">{item.name}</p>
                  <p className="text-xs text-muted-foreground">
                    £{item.price_monthly || item.price}/mo
                  </p>
                </div>
              ))}
              {legacyVisual.summary && (
                <div className="border-t pt-3 mt-3">
                  <p className="font-bold">Total: £{legacyVisual.summary.monthly}/mo</p>
                  <p className="text-xs text-muted-foreground">
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
