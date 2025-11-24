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
  // No visual data - show suggestions (HOMEPAGE)
  if (!visualConfig) {
    return (
      <div className="flex flex-col min-h-full">
        {/* Hero Section */}
        <div className="relative w-full h-[400px] flex items-center justify-center overflow-hidden mb-8">
          <div 
            className="absolute inset-0 bg-cover bg-center z-0"
            style={{ 
              backgroundImage: 'url(https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?w=1600&h=900&fit=crop)',
            }}
          />
          <div className="absolute inset-0 bg-black/40 z-10" />
          <div className="relative z-20 text-center text-white px-4 max-w-3xl mx-auto">
            <h1 className="text-5xl md:text-6xl font-bold mb-6 drop-shadow-lg tracking-tight">
              Your Dream Trip Awaits
            </h1>
            <p className="text-xl md:text-2xl mb-8 text-white/90 drop-shadow-md font-light">
              Discover amazing deals, hidden gems, and personalized itineraries with your AI travel companion.
            </p>
            <Button 
              size="lg" 
              className="bg-teal-500 hover:bg-teal-600 text-white border-none text-lg px-8 py-6 rounded-full shadow-xl transition-transform hover:scale-105"
              onClick={() => onSuggestionClick("Help me plan a trip")}
              disabled={disabled}
            >
              Start Planning
            </Button>
          </div>
        </div>

        {/* Suggestions Section */}
        <div className="flex-1 px-6 pb-12 max-w-7xl mx-auto w-full">
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-2xl font-bold text-gray-800 dark:text-white">Popular Destinations & Themes</h2>
          </div>
          <SuggestionCards
            onSuggestionClick={onSuggestionClick}
            disabled={disabled}
          />
        </div>
      </div>
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

      case 'deal_click':
        if (onProductClick) {
          // Pass deal click to trigger AI detail view
          onProductClick({ action: 'deal_click', ...params });
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
      <div className="h-full flex flex-col p-6">
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
    <div className="h-full flex flex-col p-6">
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
