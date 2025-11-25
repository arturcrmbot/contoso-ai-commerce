import { Card, CardHeader, CardContent } from '@/components/ui/card';
import { Sparkles, ForkKnife, Bicycle, Briefcase, Check } from '@phosphor-icons/react';

interface Facilities {
  wellness?: string[];
  dining?: string[];
  activities?: string[];
  business?: string[];
}

interface FacilityMatrixProps {
  facilities: Facilities;
}

export function FacilityMatrix({ facilities }: FacilityMatrixProps) {
  const categories = [
    { key: 'wellness', label: 'Wellness', icon: Sparkles, items: facilities.wellness || [] },
    { key: 'dining', label: 'Dining', icon: ForkKnife, items: facilities.dining || [] },
    { key: 'activities', label: 'Activities', icon: Bicycle, items: facilities.activities || [] },
    { key: 'business', label: 'Business', icon: Briefcase, items: facilities.business || [] },
  ].filter(cat => cat.items.length > 0);

  return (
    <Card>
      <CardHeader className="pb-3">
        <h4 className="font-semibold text-sm flex items-center gap-2">
          <Sparkles size={16} weight="fill" />
          Facilities & Amenities
        </h4>
      </CardHeader>
      <CardContent className="space-y-4">
        {categories.map((category) => {
          const Icon = category.icon;
          return (
            <div key={category.key}>
              <div className="flex items-center gap-2 mb-2">
                <Icon size={14} weight="fill" className="text-teal-600" />
                <span className="text-xs font-semibold text-gray-700 dark:text-gray-300">
                  {category.label}
                </span>
              </div>
              <div className="space-y-1 pl-6">
                {category.items.map((item, idx) => (
                  <div key={idx} className="flex items-center gap-2 text-xs text-gray-600 dark:text-gray-400">
                    <Check size={12} weight="bold" className="text-teal-500 flex-shrink-0" />
                    <span>{item}</span>
                  </div>
                ))}
              </div>
            </div>
          );
        })}
      </CardContent>
    </Card>
  );
}
