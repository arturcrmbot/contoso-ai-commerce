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
    <div className="h-full flex flex-col px-6 pb-6">
      {/* Header */}
      <div className="mb-6 flex-shrink-0">
        <h2 className="text-2xl font-bold text-foreground tracking-tight">{title}</h2>
        <p className="text-base text-muted-foreground">
          {subtitle || defaultSubtitle}
        </p>
      </div>

      {/* Deal Grid */}
      <div className="flex-1 overflow-y-auto min-h-0 pr-2 -mr-2">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 pb-8">
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
          <div className="flex flex-col items-center justify-center h-64 text-muted-foreground bg-gray-50 rounded-xl border-2 border-dashed">
            <p className="text-lg font-medium">No deals found</p>
            <p className="text-sm">Try adjusting your search criteria</p>
          </div>
        )}
      </div>
    </div>
  );
}
