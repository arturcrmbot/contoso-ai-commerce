import { Card } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Star, MapPin } from '@phosphor-icons/react';
import { RatingBars } from './RatingBars';
import { RoomGrid } from './RoomGrid';
import { FacilityMatrix } from './FacilityMatrix';
import { PriceComparison } from './PriceComparison';

interface ComparisonData {
  hotels: Array<{
    id: string;
    name: string;
    city: string;
    stars: number;
    rating: number;
    ratings?: {
      overall?: number;
      breakfast?: number;
      cleanliness?: number;
      location?: number;
      service?: number;
      value?: number;
      facilities?: number;
    };
    price_per_night: number;
    image?: string;
    rooms?: Array<{
      id?: string;
      name: string;
      image?: string;
      size_sqm: number;
      beds: string;
      max_guests: number;
      price_per_night?: number;
      features?: string[];
    }>;
    facilities?: {
      wellness?: string[];
      dining?: string[];
      activities?: string[];
      business?: string[];
    };
    price_calculation?: {
      nights: number;
      guests: number;
      price_per_night: number;
      base_price: number;
      total: number;
    };
  }>;
  aspects: string[];
  has_price_calculation?: boolean;
}

interface ComparisonViewProps {
  data: ComparisonData;
}

export function ComparisonView({ data }: ComparisonViewProps) {
  const { hotels, aspects } = data;

  console.log('[ComparisonView] Data received:', { hotels, aspects });

  if (!hotels || hotels.length < 2) {
    return (
      <div className="p-6 text-center text-muted-foreground">
        <p>Need at least 2 hotels to compare</p>
      </div>
    );
  }

  const [hotel1, hotel2] = hotels;
  console.log('[ComparisonView] Hotel 1:', hotel1);
  console.log('[ComparisonView] Hotel 2:', hotel2);

  const showRatings = aspects.includes('ratings') || aspects.includes('overview');
  const showRooms = aspects.includes('rooms');
  const showFacilities = aspects.includes('facilities');
  const showPricing = aspects.includes('pricing') || data.has_price_calculation;

  return (
    <div className="h-full overflow-y-auto bg-gray-50 dark:bg-gray-950">
      <div className="max-w-7xl mx-auto p-6">
        <h2 className="text-2xl font-bold mb-6 text-gray-900 dark:text-white">
          Hotel Comparison
        </h2>

        {/* Side-by-side comparison grid */}
        <div className="grid grid-cols-2 gap-6">
          {/* Hotel 1 */}
          <div className="space-y-4">
            <HotelHeader hotel={hotel1} />
            {showRatings && hotel1.ratings && <RatingBars ratings={hotel1.ratings} />}
            {showRooms && hotel1.rooms && <RoomGrid rooms={hotel1.rooms} />}
            {showFacilities && hotel1.facilities && <FacilityMatrix facilities={hotel1.facilities} />}
            {showPricing && hotel1.price_calculation && <PriceComparison calculation={hotel1.price_calculation} />}
          </div>

          {/* Hotel 2 */}
          <div className="space-y-4">
            <HotelHeader hotel={hotel2} />
            {showRatings && hotel2.ratings && <RatingBars ratings={hotel2.ratings} />}
            {showRooms && hotel2.rooms && <RoomGrid rooms={hotel2.rooms} />}
            {showFacilities && hotel2.facilities && <FacilityMatrix facilities={hotel2.facilities} />}
            {showPricing && hotel2.price_calculation && <PriceComparison calculation={hotel2.price_calculation} />}
          </div>
        </div>
      </div>
    </div>
  );
}

interface HotelHeaderProps {
  hotel: {
    name: string;
    city: string;
    stars: number;
    rating: number;
    price_per_night: number;
    image?: string;
  };
}

function HotelHeader({ hotel }: HotelHeaderProps) {
  console.log('[HotelHeader] Rendering hotel:', hotel);

  return (
    <Card className="overflow-hidden">
      {hotel.image && (
        <div
          className="h-48 bg-cover bg-center"
          style={{ backgroundImage: `url(${hotel.image})` }}
        />
      )}
      <div className="p-4 space-y-2">
        <div className="flex items-start justify-between">
          <div className="flex-1">
            <h3 className="text-xl font-bold text-gray-900 dark:text-white">
              {hotel.name || '[No name]'}
            </h3>
            <div className="flex items-center gap-1 text-sm text-gray-600 dark:text-gray-400 mt-1">
              <MapPin size={14} weight="fill" />
              <span>{hotel.city || '[No city]'}</span>
            </div>
          </div>
          <div className="flex flex-col items-end gap-1 flex-shrink-0">
            <div className="flex items-center gap-1 bg-teal-500/10 px-2 py-1 rounded">
              <Star size={16} weight="fill" className="text-teal-600" />
              <span className="text-sm font-bold text-teal-700 dark:text-teal-400">
                {hotel.rating?.toFixed(1) || '0.0'}
              </span>
            </div>
            {hotel.stars && hotel.stars > 0 && (
              <div className="text-yellow-500">
                {Array.from({ length: hotel.stars }).map((_, i) => (
                  <Star key={i} size={14} weight="fill" className="inline" />
                ))}
              </div>
            )}
          </div>
        </div>
        <div className="pt-2 border-t border-gray-200 dark:border-gray-700">
          <div className="flex items-baseline justify-between">
            <span className="text-2xl font-bold text-gray-900 dark:text-white">
              £{hotel.price_per_night || '0'}
            </span>
            <span className="text-sm text-gray-600 dark:text-gray-400">per night</span>
          </div>
        </div>
      </div>
    </Card>
  );
}
