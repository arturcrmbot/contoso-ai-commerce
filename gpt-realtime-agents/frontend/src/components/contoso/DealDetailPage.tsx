import { Card, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { MapPin, Star, Phone, Mail, Globe, Users, Bed, Maximize2, Check } from '@phosphor-icons/react';
import { useState } from 'react';

interface DealDetailPageProps {
  deal: any;
  onAddToCart?: () => void;
}

export function DealDetailPage({ deal, onAddToCart }: DealDetailPageProps) {
  const [selectedImage, setSelectedImage] = useState(0);

  const formatCurrency = (amount: number, currency: string = 'GBP') => {
    return `£${amount}`;
  };

  const renderStars = (rating: number) => {
    return Array.from({ length: 5 }).map((_, i) => (
      <Star
        key={i}
        size={16}
        weight={i < Math.floor(rating) ? 'fill' : 'regular'}
        className={i < Math.floor(rating) ? 'text-yellow-500' : 'text-gray-300'}
      />
    ));
  };

  return (
    <div className="max-w-6xl mx-auto space-y-6">
      {/* Image Gallery */}
      <Card>
        <CardContent className="p-0">
          <div className="aspect-[21/9] bg-gray-100 overflow-hidden rounded-t-lg">
            <img
              src={deal.images?.[selectedImage] || deal.images?.[0]}
              alt={deal.title}
              className="w-full h-full object-cover"
            />
          </div>
          <div className="p-4 grid grid-cols-6 gap-2">
            {deal.images?.slice(0, 6).map((img: string, idx: number) => (
              <button
                key={idx}
                onClick={() => setSelectedImage(idx)}
                className={`aspect-video rounded overflow-hidden border-2 ${
                  selectedImage === idx ? 'border-primary' : 'border-transparent'
                }`}
              >
                <img src={img} alt={`View ${idx + 1}`} className="w-full h-full object-cover" />
              </button>
            ))}
          </div>
        </CardContent>
      </Card>

      {/* Header */}
      <div className="flex items-start justify-between">
        <div>
          <div className="flex items-center gap-2 mb-2">
            <h1 className="text-3xl font-bold">{deal.title}</h1>
            {deal.features?.accommodation && (
              <Badge variant="outline">{deal.features.accommodation}</Badge>
            )}
          </div>
          <div className="flex items-center gap-4 text-muted-foreground">
            <div className="flex items-center gap-1">
              <MapPin size={16} weight="bold" />
              <span className="text-sm">
                {deal.address?.street}, {deal.destination?.city}
              </span>
            </div>
            {deal.rating && (
              <div className="flex items-center gap-1">
                <div className="flex">{renderStars(deal.rating)}</div>
                <span className="text-sm font-medium">{deal.rating}</span>
                <span className="text-sm">({deal.review_count} reviews)</span>
              </div>
            )}
          </div>
        </div>

        {/* Price Card */}
        <Card className="w-80">
          <CardContent className="p-6">
            <div className="space-y-4">
              <div>
                <p className="text-sm text-muted-foreground">From</p>
                <div className="flex items-baseline gap-2">
                  <p className="text-3xl font-bold text-primary">
                    {formatCurrency(deal.pricing?.deal_price, deal.pricing?.currency)}
                  </p>
                  <span className="text-sm text-muted-foreground">/{deal.pricing?.per}</span>
                </div>
                {deal.pricing?.original_price > deal.pricing?.deal_price && (
                  <div className="flex items-center gap-2 mt-1">
                    <p className="text-sm text-muted-foreground line-through">
                      {formatCurrency(deal.pricing.original_price)}
                    </p>
                    <Badge variant="default" className="text-xs">
                      Save {deal.pricing.discount_percent}%
                    </Badge>
                  </div>
                )}
              </div>

              {deal.pricing?.includes && (
                <div className="space-y-1">
                  <p className="text-xs font-semibold">Includes:</p>
                  {deal.pricing.includes.map((item: string) => (
                    <div key={item} className="flex items-center gap-1 text-xs">
                      <Check size={12} className="text-green-600" />
                      <span className="capitalize">{item.replace('_', ' ')}</span>
                    </div>
                  ))}
                </div>
              )}

              <Button onClick={onAddToCart} className="w-full" size="lg">
                Add to Cart
              </Button>
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Room Types */}
      {deal.rooms && deal.rooms.length > 0 && (
        <Card>
          <CardContent className="p-6">
            <h2 className="text-xl font-bold mb-4">Available Rooms</h2>
            <div className="grid gap-4">
              {deal.rooms.map((room: any, idx: number) => (
                <div key={idx} className="flex items-start gap-4 p-4 border rounded-lg hover:bg-muted/50 transition">
                  <div className="flex-1">
                    <h3 className="font-semibold text-lg">{room.name}</h3>
                    <div className="flex items-center gap-4 text-sm text-muted-foreground mt-2">
                      <div className="flex items-center gap-1">
                        <Maximize2 size={14} />
                        <span>{room.size_sqm} m²</span>
                      </div>
                      <div className="flex items-center gap-1">
                        <Bed size={14} />
                        <span>{room.beds}</span>
                      </div>
                      <div className="flex items-center gap-1">
                        <Users size={14} />
                        <span>Up to {room.max_guests} guests</span>
                      </div>
                    </div>
                    <div className="flex flex-wrap gap-1 mt-3">
                      {room.features?.map((feature: string) => (
                        <Badge key={feature} variant="secondary" className="text-xs">
                          {feature}
                        </Badge>
                      ))}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      )}

      {/* Amenities */}
      {deal.detailed_amenities && (
        <Card>
          <CardContent className="p-6">
            <h2 className="text-xl font-bold mb-4">Amenities & Facilities</h2>
            <div className="grid md:grid-cols-2 gap-6">
              {Object.entries(deal.detailed_amenities).map(([category, items]: [string, any]) => (
                <div key={category}>
                  <h3 className="font-semibold mb-2 capitalize">{category.replace('_', ' ')}</h3>
                  <div className="space-y-1">
                    {items.map((item: string) => (
                      <div key={item} className="flex items-center gap-2 text-sm">
                        <Check size={14} className="text-green-600" />
                        <span className="capitalize">{item.replace('_', ' ')}</span>
                      </div>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      )}

      {/* Reviews */}
      {deal.reviews && deal.reviews.length > 0 && (
        <Card>
          <CardContent className="p-6">
            <h2 className="text-xl font-bold mb-4">Guest Reviews</h2>
            <div className="space-y-4">
              {deal.reviews.map((review: any, idx: number) => (
                <div key={idx} className="border-b last:border-0 pb-4 last:pb-0">
                  <div className="flex items-center justify-between mb-2">
                    <div>
                      <p className="font-semibold">{review.title}</p>
                      <p className="text-sm text-muted-foreground">{review.author} • {review.date}</p>
                    </div>
                    <div className="flex">{renderStars(review.rating)}</div>
                  </div>
                  <p className="text-sm text-muted-foreground">{review.text}</p>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      )}

      {/* Contact & Location */}
      <Card>
        <CardContent className="p-6">
          <h2 className="text-xl font-bold mb-4">Contact & Location</h2>
          <div className="grid md:grid-cols-2 gap-6">
            <div>
              <h3 className="font-semibold mb-2">Address</h3>
              <p className="text-sm text-muted-foreground">
                {deal.address?.street}<br />
                {deal.address?.postal_code} {deal.address?.city}<br />
                {deal.address?.country}
              </p>
            </div>
            {deal.contact && (
              <div>
                <h3 className="font-semibold mb-2">Contact</h3>
                <div className="space-y-2 text-sm">
                  {deal.contact.phone && (
                    <div className="flex items-center gap-2">
                      <Phone size={14} />
                      <span>{deal.contact.phone}</span>
                    </div>
                  )}
                  {deal.contact.email && (
                    <div className="flex items-center gap-2">
                      <Mail size={14} />
                      <span>{deal.contact.email}</span>
                    </div>
                  )}
                  {deal.contact.website && (
                    <div className="flex items-center gap-2">
                      <Globe size={14} />
                      <span>{deal.contact.website}</span>
                    </div>
                  )}
                </div>
              </div>
            )}
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
