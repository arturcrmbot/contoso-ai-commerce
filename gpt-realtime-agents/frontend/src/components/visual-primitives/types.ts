/**
 * Flexible Visual Component System
 * AI composes layouts dynamically based on conversation context
 */

export type ComponentType =
  // Product components
  | 'product_card'
  | 'product_hero'
  | 'product_carousel'
  | 'product_comparison'
  | 'product_grid'
  // Info components
  | 'price_breakdown'
  | 'specs_table'
  | 'reviews_widget'
  | 'stock_indicator'
  | 'feature_list'
  // Action components
  | 'cta_button'
  | 'quick_add_button'
  | 'compare_toggle'
  // Progress components
  | 'checkout_stepper'
  | 'credit_check_status'
  | 'delivery_timeline'
  | 'progress_indicator'
  // Accessory components
  | 'accessory_card'
  | 'accessory_carousel'
  | 'accessory_grid'
  // Plan components
  | 'plan_card'
  | 'plan_comparison'
  | 'plan_selector'
  // Promotional
  | 'promo_banner'
  | 'deal_highlight'
  // Layout components
  | 'section_divider'
  | 'info_callout'
  | 'empty_state'
  // Betting components
  | 'match_card'
  | 'match_grid'
  | 'bet_slip_preview'
  | 'bet_confirmation'
  | 'odds_display';

export type LayoutType =
  | 'single_focus'      // One main element (hero product)
  | 'two_column'        // Side-by-side (comparison)
  | 'multi_section'     // Stacked sections
  | 'grid'              // Grid of items
  | 'flow'              // Natural flow layout
  | 'wizard';           // Step-by-step process

export type Emphasis = 'low' | 'medium' | 'high' | 'critical';
export type Size = 'sm' | 'md' | 'lg' | 'xl';
export type Position = 'above' | 'below' | 'left' | 'right' | 'inline';

export interface VisualSection {
  id?: string;
  type: ComponentType;
  data: any;
  emphasis?: Emphasis;
  size?: Size;
  position?: Position;
  title?: string;
  subtitle?: string;
  style?: 'default' | 'minimal' | 'emphasized' | 'muted';
  className?: string;
  onClick?: {
    action: string;
    params?: any;
  };
}

export interface CTAConfig {
  text: string;
  action: string;
  params?: any;
  prominence: 'primary' | 'secondary' | 'subtle';
  position?: Position;
  icon?: string;
}

export interface FlexibleVisual {
  layout: LayoutType;
  sections: VisualSection[];
  cta?: CTAConfig | CTAConfig[];
  header?: {
    title: string;
    subtitle?: string;
    badge?: string;
  };
  footer?: {
    text?: string;
    actions?: CTAConfig[];
  };
  theme?: 'default' | 'success' | 'warning' | 'info';
  animation?: 'fade' | 'slide' | 'scale' | 'none';
}

// Backwards compatibility - map old visual types to new flexible system
export interface LegacyVisual {
  type: 'product_grid' | 'comparison_table' | 'plan_cards' | 'promo_banner' | 'cart_preview';
  title?: string;
  items?: any[];
  devices?: any[];
  matrix?: any;
  summary?: any;
}

export type VisualConfig = FlexibleVisual | LegacyVisual;

// Type guard
export function isFlexibleVisual(visual: VisualConfig): visual is FlexibleVisual {
  return 'layout' in visual && 'sections' in visual;
}
