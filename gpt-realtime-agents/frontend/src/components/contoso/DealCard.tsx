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
      className={`cursor-pointer transition-all hover:shadow-lg border-2 ${
        isHighlighted
          ? 'border-primary shadow-lg animate-pulse'
          : 'border-border hover:border-primary/50'
      }`}
      onClick={onClick}
    >
      <CardContent className="p-0">
        {/* Deal Image */}
        <div className="aspect-video bg-gradient-to-br from-muted to-muted/50 rounded-t-lg overflow-hidden relative">
          {deal.images && deal.images.length > 0 ? (
            <>
              <img
                src={deal.images[0]}
                alt={deal.title}
                className="w-full h-full object-cover"
                onError={(e) => {
                  e.currentTarget.style.display = 'none';
                  const fallback = e.currentTarget.parentElement?.querySelector('.fallback-icon');
                  fallback?.classList.remove('hidden');
                }}
              />
              <MapPin size={32} className="text-muted-foreground absolute hidden fallback-icon top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2" weight="thin" />
            </>
          ) : (
            <MapPin size={32} className="text-muted-foreground absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2" weight="thin" />
          )}

          {/* Urgency Badge */}
          {highlightUrgency && deal.urgency?.ending_soon && (
            <Badge variant="destructive" className="absolute top-2 right-2 text-xs">
              <Clock size={12} className="mr-1" />
              Ending Soon
            </Badge>
          )}

          {/* Discount Badge */}
          {(highlightSavings || deal.pricing.discount_percent >= 30) && (
            <Badge variant="default" className="absolute top-2 left-2 text-xs font-bold">
              <TrendingDown size={12} className="mr-1" />
              {deal.pricing.discount_percent}% OFF
            </Badge>
          )}
        </div>

        {/* Deal Info */}
        <div className="p-4 space-y-2">
          <div>
            <div className="flex items-start justify-between gap-2">
              <div className="flex-1">
                <p className="text-xs text-muted-foreground flex items-center gap-1">
                  <MapPin size={12} weight="bold" />
                  {deal.destination.city}, {deal.destination.country}
                </p>
                <h3 className="font-semibold text-sm leading-tight mt-1">{deal.title}</h3>
              </div>
            </div>
          </div>

          {/* Rating & Stars */}
          <div className="flex items-center gap-2">
            {deal.rating && (
              <div className="flex items-center gap-1 text-xs">
                <Star size={12} weight="fill" className="text-yellow-500" />
                <span className="font-medium">{deal.rating}</span>
                <span className="text-muted-foreground">
                  ({deal.review_count?.toLocaleString()})
                </span>
              </div>
            )}
            {stars && (
              <Badge variant="outline" className="text-xs">
                {stars}★ Hotel
              </Badge>
            )}
          </div>

          {/* Suitable For Tags */}
          {deal.features?.suitable_for && deal.features.suitable_for.length > 0 && (
            <div className="flex flex-wrap gap-1">
              {deal.features.suitable_for.slice(0, 3).map((tag) => (
                <Badge key={tag} variant="secondary" className="text-xs capitalize">
                  {tag.replace('_', ' ')}
                </Badge>
              ))}
            </div>
          )}

          {/* Pricing */}
          <div className="pt-2 border-t">
            <div className="flex items-baseline justify-between">
              <div>
                <p className="text-xs text-muted-foreground">From</p>
                <div className="flex items-baseline gap-2">
                  <p className="text-lg font-bold text-primary">
                    {formatCurrency(deal.pricing.deal_price, deal.pricing.currency)}
                    <span className="text-xs font-normal text-muted-foreground">/{deal.pricing.per}</span>
                  </p>
                  {deal.pricing.discount_percent > 0 && (
                    <p className="text-xs text-muted-foreground line-through">
                      {formatCurrency(deal.pricing.original_price, deal.pricing.currency)}
                    </p>
                  )}
                </div>
              </div>
              <div className="text-right">
                <p className="text-xs text-green-600 font-semibold">
                  Save {deal.pricing.discount_percent}%
                </p>
              </div>
            </div>
          </div>

          {/* Urgency Indicator */}
          {deal.urgency && deal.urgency.spots_left && deal.urgency.spots_left <= 10 && (
            <p className="text-xs text-orange-600 font-medium">
              Only {deal.urgency.spots_left} spots left!
            </p>
          )}

          {/* CTA */}
          <button
            className="w-full mt-2 px-3 py-2 bg-gradient-to-r from-teal-500 to-cyan-600 hover:from-teal-600 hover:to-cyan-700 text-white rounded-md text-xs font-medium transition-all shadow-sm hover:shadow-md"
            onClick={(e) => { e.stopPropagation(); onClick?.(); }}
          >
            View Deal
          </button>
        </div>
      </CardContent>
    </Card>
  );
}
