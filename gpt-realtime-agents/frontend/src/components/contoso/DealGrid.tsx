import { DealCard } from './DealCard';

interface Deal {
  id: string;
  type: string;
  title: string;
  destination: {
    city: string;
    country: string;
    region: string;
  };
  dates?: {
    available_from?: string;
    available_to?: string;
    min_nights?: number;
    max_nights?: number;
  };
  pricing: {
    original_price: number;
    deal_price: number;
    discount_percent: number;
    currency: string;
    per: string;
    includes?: string[];
  };
  images?: string[];
  rating?: number;
  review_count?: number;
  features?: {
    accommodation?: string;
    amenities?: string[];
    room_type?: string;
    suitable_for?: string[];
    accessibility?: string[];
  };
  urgency?: {
    ending_soon?: boolean;
    spots_left?: number;
    last_booked?: string;
  };
}

interface DealGridProps {
  deals: Deal[];
  highlightedId?: string | null;
  highlightSavings?: boolean;
  highlightUrgency?: boolean;
  onDealClick?: (deal: Deal) => void;
  title?: string;
  subtitle?: string;
}

export function DealGrid({
  deals,
  highlightedId,
  highlightSavings = false,
  highlightUrgency = false,
  onDealClick,
  title = "Travel Deals",
  subtitle
}: DealGridProps) {
  const defaultSubtitle = `${deals.length} ${deals.length === 1 ? 'deal' : 'deals'} found`;

  return (
    <div className="h-full flex flex-col">
      {/* Header */}
      <div className="mb-4 flex-shrink-0">
        <h2 className="text-xl font-bold text-foreground">{title}</h2>
        <p className="text-sm text-muted-foreground">
          {subtitle || defaultSubtitle}
        </p>
      </div>

      {/* Deal Grid */}
      <div className="flex-1 overflow-y-auto min-h-0">
        <div className="grid grid-cols-2 gap-4 pb-4">
          {deals.map((deal) => (
            <DealCard
              key={deal.id}
              deal={deal}
              isHighlighted={deal.id === highlightedId}
              highlightSavings={highlightSavings}
              highlightUrgency={highlightUrgency}
              onClick={() => onDealClick?.(deal)}
            />
          ))}
        </div>

        {deals.length === 0 && (
          <div className="flex items-center justify-center h-full text-muted-foreground">
            <p className="text-sm">No deals to display yet</p>
          </div>
        )}
      </div>
    </div>
  );
}
