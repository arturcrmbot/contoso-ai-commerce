import { Card, CardHeader, CardContent } from '@/components/ui/card';
import { Star } from '@phosphor-icons/react';

interface Ratings {
  overall?: number;
  breakfast?: number;
  cleanliness?: number;
  location?: number;
  service?: number;
  value?: number;
  facilities?: number;
}

interface RatingBarsProps {
  ratings: Ratings;
}

export function RatingBars({ ratings }: RatingBarsProps) {
  const ratingCategories = [
    { key: 'breakfast', label: 'Breakfast', value: ratings.breakfast },
    { key: 'cleanliness', label: 'Cleanliness', value: ratings.cleanliness },
    { key: 'location', label: 'Location', value: ratings.location },
    { key: 'service', label: 'Service', value: ratings.service },
    { key: 'value', label: 'Value', value: ratings.value },
    { key: 'facilities', label: 'Facilities', value: ratings.facilities },
  ].filter(cat => cat.value !== undefined);

  return (
    <Card>
      <CardHeader className="pb-3">
        <h4 className="font-semibold text-sm flex items-center gap-2">
          <Star size={16} weight="fill" className="text-teal-600" />
          Ratings Breakdown
        </h4>
      </CardHeader>
      <CardContent className="space-y-3">
        {ratingCategories.map((category) => (
          <div key={category.key}>
            <div className="flex items-center justify-between mb-1">
              <span className="text-xs font-medium text-gray-700 dark:text-gray-300">
                {category.label}
              </span>
              <span className="text-xs font-bold text-gray-900 dark:text-white">
                {category.value?.toFixed(1)}
              </span>
            </div>
            <div className="h-2 bg-gray-200 dark:bg-gray-800 rounded-full overflow-hidden">
              <div
                className="h-full bg-gradient-to-r from-teal-500 to-cyan-500 rounded-full transition-all"
                style={{ width: `${((category.value || 0) / 5) * 100}%` }}
              />
            </div>
          </div>
        ))}
      </CardContent>
    </Card>
  );
}
