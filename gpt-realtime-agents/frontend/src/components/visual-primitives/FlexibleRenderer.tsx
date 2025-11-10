import { FlexibleVisual, VisualSection, CTAConfig } from './types';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import * as PhosphorIcons from '@phosphor-icons/react';

// Import all primitives
import { ProductHero } from './ProductHero';
import { AccessoryCard } from './AccessoryCard';
import { CheckoutStepper } from './CheckoutStepper';
import { CreditCheckStatus } from './CreditCheckStatus';
import { PriceBreakdown } from './PriceBreakdown';
import { TradeInValue } from './TradeInValue';
import { ComparisonTable } from './ComparisonTable';

// Import existing components (backwards compatibility)
import { ProductCard } from '../contoso/ProductCard';
import { PlanCards } from '../contoso/PlanCards';
import { PromoBanner } from '../contoso/PromoBanner';

interface FlexibleRendererProps {
  visual: FlexibleVisual;
  onAction?: (action: string, params?: any) => void;
}

export function FlexibleRenderer({ visual, onAction }: FlexibleRendererProps) {

  // Render a single section based on its type
  const renderSection = (section: VisualSection) => {
    // Safety check
    if (!section || !section.type || !section.data) {
      console.warn('[FlexibleRenderer] Invalid section:', section);
      return null;
    }

    const sectionClasses = getSectionClasses(section);

    try {
      switch (section.type) {
        // Product components
        case 'product_hero':
          return <ProductHero data={section.data} onAction={onAction} emphasis={section.emphasis} context={section.context || visual.context} />;

        case 'product_card':
          return (
            <ProductCard
              device={section.data}
              onClick={() => section.onClick && onAction?.(section.onClick.action, section.onClick.params)}
            />
          );

      case 'product_grid':
        const gridItems = section.data?.items || section.data || [];
        if (!Array.isArray(gridItems) || gridItems.length === 0) {
          return <div className="text-sm text-muted-foreground">No items to display</div>;
        }
        return (
          <div className="grid grid-cols-2 gap-4">
            {gridItems.map((item: any) => (
              <ProductCard
                key={item.id || Math.random()}
                device={item}
                onClick={() => onAction?.('product_click', { device_id: item.id })}
                context={section.context || visual.context}
              />
            ))}
          </div>
        );

      case 'comparison_table':
      case 'product_comparison':
        return <ComparisonTable data={section.data} context={section.context || visual.context} title={section.title} />;

      // Accessory components
      case 'accessory_card':
        return <AccessoryCard data={section.data} onAction={onAction} size={section.size} />;

      case 'accessory_grid':
        const accessoryGridItems = section.data?.items || [];
        if (!Array.isArray(accessoryGridItems) || accessoryGridItems.length === 0) {
          return null;
        }
        return (
          <div>
            {section.title && (
              <h3 className="text-lg font-bold mb-3">{section.title}</h3>
            )}
            <div className="grid grid-cols-2 md:grid-cols-3 gap-3">
              {accessoryGridItems.map((item: any) => (
                <AccessoryCard
                  key={item.id || Math.random()}
                  data={item}
                  onAction={onAction}
                  size={section.size}
                />
              ))}
            </div>
          </div>
        );

      case 'accessory_carousel':
        const carouselItems = section.data?.items || [];
        if (!Array.isArray(carouselItems) || carouselItems.length === 0) {
          return null;
        }
        return (
          <div>
            {section.title && (
              <h3 className="text-lg font-bold mb-3">{section.title}</h3>
            )}
            <div className="flex gap-3 overflow-x-auto pb-2">
              {carouselItems.map((item: any) => (
                <div key={item.id || Math.random()} className="flex-shrink-0 w-48">
                  <AccessoryCard data={item} onAction={onAction} size="sm" />
                </div>
              ))}
            </div>
          </div>
        );

      // Progress components
      case 'checkout_stepper':
        return <CheckoutStepper data={section.data} emphasis={section.emphasis} />;

      case 'credit_check_status':
        return <CreditCheckStatus data={section.data} emphasis={section.emphasis} />;

      case 'trade_in_value':
        return <TradeInValue data={section.data} emphasis={section.emphasis} />;

      // Info components
      case 'price_breakdown':
        return <PriceBreakdown data={section.data} style={section.style} />;

      // Plan components
      case 'plan_card':
      case 'plan_selector':
        const planItems = Array.isArray(section.data) ? section.data : (section.data?.items || []);
        if (!Array.isArray(planItems) || planItems.length === 0) {
          return null;
        }
        return (
          <PlanCards
            title={section.title || 'Available Plans'}
            items={planItems}
            onPlanClick={(plan) => onAction?.('plan_select', { plan_id: plan.id })}
            context={section.context || visual.context}
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

      {/* Context Banner */}
      {visual.context?.context_message && (
        <div className="bg-primary/10 border-l-4 border-primary p-3 rounded mb-4 flex-shrink-0">
          <p className="text-sm font-medium">{visual.context.context_message}</p>
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
