import { Card, CardHeader, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Bed, Users, Ruler } from '@phosphor-icons/react';

interface Room {
  id?: string;
  name: string;
  image?: string;
  size_sqm: number;
  beds: string;
  max_guests: number;
  price_per_night?: number;
  features?: string[];
}

interface RoomGridProps {
  rooms: Room[];
}

export function RoomGrid({ rooms }: RoomGridProps) {
  return (
    <Card>
      <CardHeader className="pb-3">
        <h4 className="font-semibold text-sm flex items-center gap-2">
          <Bed size={16} weight="fill" />
          Rooms Available
        </h4>
      </CardHeader>
      <CardContent className="space-y-3">
        {rooms.slice(0, 4).map((room, idx) => (
          <div
            key={room.id || idx}
            className="flex gap-3 p-3 bg-gray-50 dark:bg-gray-900 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"
          >
            {room.image && (
              <div
                className="w-24 h-20 flex-shrink-0 bg-cover bg-center rounded-md"
                style={{ backgroundImage: `url(${room.image})` }}
              />
            )}
            <div className="flex-1 min-w-0">
              <h5 className="font-semibold text-sm text-gray-900 dark:text-white truncate">
                {room.name}
              </h5>
              <div className="flex items-center gap-3 mt-1 text-xs text-muted-foreground">
                <div className="flex items-center gap-1">
                  <Ruler size={12} />
                  <span>{room.size_sqm}m²</span>
                </div>
                <div className="flex items-center gap-1">
                  <Bed size={12} />
                  <span>{room.beds}</span>
                </div>
                <div className="flex items-center gap-1">
                  <Users size={12} />
                  <span>{room.max_guests}</span>
                </div>
              </div>
              {room.price_per_night && (
                <div className="mt-2">
                  <span className="text-sm font-bold text-teal-600 dark:text-teal-400">
                    £{room.price_per_night}/night
                  </span>
                </div>
              )}
            </div>
          </div>
        ))}
        {rooms.length > 4 && (
          <p className="text-xs text-center text-muted-foreground pt-2">
            +{rooms.length - 4} more room types
          </p>
        )}
      </CardContent>
    </Card>
  );
}
