import { Card, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { MapPin, Star, TrendingDown, Clock } from '@phosphor-icons/react';
import { VisualContext } from '@/components/visual-primitives/types';

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

interface DealCardProps {
  deal: Deal;
  isHighlighted?: boolean;
  highlightSavings?: boolean;
  highlightUrgency?: boolean;
  onClick?: () => void;
  context?: VisualContext;
}

export function DealCard({
  deal,
  isHighlighted = false,
  highlightSavings = false,
  highlightUrgency = false,
  onClick,
  context
}: DealCardProps) {

  const formatCurrency = (amount: number, currency: string = 'GBP') => {
    return `£${amount}`;
  };

  const getStarRating = () => {
    if (!deal.features?.accommodation) return null;
    const match = deal.features.accommodation.match(/(\d+)-star/);
    return match ? parseInt(match[1]) : null;
  };

  const stars = getStarRating();

  return (
    <Card
      className={`cursor-pointer transition-all duration-300 group border-0 shadow-sm hover:shadow-xl hover:-translate-y-1 rounded-xl overflow-hidden bg-card ${
        isHighlighted
          ? 'ring-2 ring-primary shadow-lg'
          : ''
      }`}
      onClick={onClick}
    >
      <CardContent className="p-0">
        {/* Deal Image */}
        <div className="aspect-[4/3] bg-gray-100 relative overflow-hidden">
          {deal.images && deal.images.length > 0 ? (
            <>
              <img
                src={deal.images[0]}
                alt={deal.title}
                className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110"
                onError={(e) => {
                  e.currentTarget.style.display = 'none';
                  const fallback = e.currentTarget.parentElement?.querySelector('.fallback-icon');
                  fallback?.classList.remove('hidden');
                }}
              />
              <MapPin size={32} className="text-muted-foreground absolute hidden fallback-icon top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2" weight="thin" />
            </>
          ) : (
            <div className="w-full h-full flex items-center justify-center bg-gray-100">
              <MapPin size={32} className="text-muted-foreground/50" weight="thin" />
            </div>
          )}

          {/* Gradient Overlay */}
          <div className="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent opacity-60" />

          {/* Urgency Badge */}
          {highlightUrgency && deal.urgency?.ending_soon && (
            <Badge variant="destructive" className="absolute top-3 right-3 shadow-lg animate-pulse">
              <Clock size={12} className="mr-1" />
              Ending Soon
            </Badge>
          )}

          {/* Discount Badge */}
          {(highlightSavings || deal.pricing.discount_percent >= 30) && (
            <Badge className="absolute top-3 left-3 bg-green-600 hover:bg-green-700 shadow-lg font-bold border-0">
              <TrendingDown size={12} className="mr-1" />
              -{deal.pricing.discount_percent}%
            </Badge>
          )}

          {/* Location Overlay */}
          <div className="absolute bottom-3 left-3 text-white flex items-center gap-1 text-sm font-medium drop-shadow-md">
            <MapPin size={14} weight="fill" />
            {deal.destination.city}, {deal.destination.country}
          </div>
        </div>

        {/* Deal Info */}
        <div className="p-4 space-y-3">
          <div>
            <h3 className="font-bold text-base leading-tight line-clamp-2 group-hover:text-primary transition-colors">
              {deal.title}
            </h3>
          </div>

          {/* Rating & Stars */}
          <div className="flex items-center gap-2 text-sm">
            {deal.rating && (
              <div className="flex items-center gap-1 bg-yellow-50 px-1.5 py-0.5 rounded text-yellow-700 font-medium">
                <Star size={12} weight="fill" className="text-yellow-500" />
                <span>{deal.rating}</span>
              </div>
            )}
            {stars && (
              <span className="text-muted-foreground text-xs border px-1.5 py-0.5 rounded">
                {stars}★ Hotel
              </span>
            )}
            {deal.review_count && (
              <span className="text-muted-foreground text-xs">
                ({deal.review_count} reviews)
              </span>
            )}
          </div>

          {/* Suitable For Tags */}
          {deal.features?.suitable_for && deal.features.suitable_for.length > 0 && (
            <div className="flex flex-wrap gap-1.5">
              {deal.features.suitable_for.slice(0, 3).map((tag) => (
                <span key={tag} className="text-[10px] uppercase tracking-wider font-semibold text-muted-foreground bg-secondary/50 px-2 py-1 rounded-full">
                  {tag.replace('_', ' ')}
                </span>
              ))}
            </div>
          )}

          {/* Pricing */}
          <div className="pt-3 border-t flex items-end justify-between">
            <div>
              <p className="text-xs text-muted-foreground mb-0.5">Total price from</p>
              <div className="flex items-baseline gap-2">
                <p className="text-xl font-bold text-primary">
                  {formatCurrency(deal.pricing.deal_price, deal.pricing.currency)}
                </p>
                {deal.pricing.discount_percent > 0 && (
                  <p className="text-xs text-muted-foreground line-through decoration-red-500/50">
                    {formatCurrency(deal.pricing.original_price, deal.pricing.currency)}
                  </p>
                )}
              </div>
            </div>
            
            <Button 
              size="sm" 
              className="rounded-full px-4 bg-primary/10 text-primary hover:bg-primary hover:text-white transition-colors font-semibold shadow-none hover:shadow-md"
            >
              View
            </Button>
          </div>

          {/* Urgency Indicator */}
          {deal.urgency && deal.urgency.spots_left && deal.urgency.spots_left <= 10 && (
            <p className="text-xs text-orange-600 font-medium flex items-center gap-1 bg-orange-50 p-1.5 rounded justify-center">
              <Clock size={12} weight="bold" />
              Only {deal.urgency.spots_left} spots left!
            </p>
          )}
        </div>
      </CardContent>
    </Card>
  );
}
