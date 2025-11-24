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
    <div className="max-w-7xl mx-auto space-y-8 pb-12 animate-in fade-in duration-500">
      {/* Image Gallery - Modern Grid Layout */}
      <div className="grid grid-cols-4 grid-rows-2 gap-2 h-[400px] rounded-2xl overflow-hidden shadow-lg">
        <div className="col-span-2 row-span-2 relative group cursor-pointer" onClick={() => setSelectedImage(0)}>
          <img
            src={deal.images?.[0]}
            alt={deal.title}
            className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"
          />
          <div className="absolute inset-0 bg-black/10 group-hover:bg-transparent transition-colors" />
        </div>
        <div className="col-span-1 row-span-1 relative group cursor-pointer" onClick={() => setSelectedImage(1)}>
          <img src={deal.images?.[1]} alt="Gallery 2" className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" />
        </div>
        <div className="col-span-1 row-span-1 relative group cursor-pointer" onClick={() => setSelectedImage(2)}>
          <img src={deal.images?.[2]} alt="Gallery 3" className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" />
        </div>
        <div className="col-span-1 row-span-1 relative group cursor-pointer" onClick={() => setSelectedImage(3)}>
          <img src={deal.images?.[3]} alt="Gallery 4" className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" />
        </div>
        <div className="col-span-1 row-span-1 relative group cursor-pointer" onClick={() => setSelectedImage(4)}>
          <img src={deal.images?.[4]} alt="Gallery 5" className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" />
          {deal.images && deal.images.length > 5 && (
            <div className="absolute inset-0 bg-black/50 flex items-center justify-center text-white font-bold text-lg backdrop-blur-[2px] group-hover:backdrop-blur-none transition-all">
              +{deal.images.length - 5} photos
            </div>
          )}
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Main Content */}
        <div className="lg:col-span-2 space-y-8">
          {/* Header Info */}
          <div>
            <div className="flex items-center gap-3 mb-2">
              <h1 className="text-3xl md:text-4xl font-bold text-gray-900 tracking-tight">{deal.title}</h1>
              {deal.features?.accommodation && (
                <Badge variant="secondary" className="text-sm px-3 py-1 bg-blue-50 text-blue-700 hover:bg-blue-100 border-blue-100">
                  {deal.features.accommodation}
                </Badge>
              )}
            </div>
            <div className="flex flex-wrap items-center gap-4 text-muted-foreground">
              <div className="flex items-center gap-1.5 text-gray-600">
                <MapPin size={18} weight="fill" className="text-teal-500" />
                <span className="font-medium">
                  {deal.address?.street}, {deal.destination?.city}, {deal.destination?.country}
                </span>
              </div>
              <div className="w-1 h-1 rounded-full bg-gray-300" />
              {deal.rating && (
                <div className="flex items-center gap-1.5">
                  <div className="flex text-yellow-400">{renderStars(deal.rating)}</div>
                  <span className="font-bold text-gray-900">{deal.rating}</span>
                  <span className="text-sm underline decoration-gray-300 underline-offset-4">({deal.review_count} reviews)</span>
                </div>
              )}
            </div>
          </div>

          <div className="h-px bg-gray-100" />

          {/* Description / Amenities Highlights */}
          {deal.detailed_amenities && (
            <div className="space-y-4">
              <h2 className="text-xl font-bold text-gray-900">What this place offers</h2>
              <div className="grid grid-cols-2 gap-4">
                {Object.entries(deal.detailed_amenities).slice(0, 6).map(([category, items]: [string, any]) => (
                  <div key={category} className="flex items-start gap-3">
                    <div className="mt-1 p-2 bg-gray-50 rounded-lg text-gray-600">
                      <Check size={16} weight="bold" />
                    </div>
                    <div>
                      <h3 className="font-semibold text-sm capitalize mb-1">{category.replace('_', ' ')}</h3>
                      <p className="text-sm text-muted-foreground line-clamp-1">
                        {items.slice(0, 3).join(', ')}
                      </p>
                    </div>
                  </div>
                ))}
              </div>
              <Button variant="outline" className="mt-4">Show all amenities</Button>
            </div>
          )}

          <div className="h-px bg-gray-100" />

          {/* Room Types */}
          {deal.rooms && deal.rooms.length > 0 && (
            <div className="space-y-4">
              <h2 className="text-xl font-bold text-gray-900">Where you'll sleep</h2>
              <div className="grid gap-4">
                {deal.rooms.map((room: any, idx: number) => (
                  <Card key={idx} className="border-0 shadow-sm bg-gray-50/50 hover:bg-gray-50 transition-colors">
                    <CardContent className="p-5 flex gap-4">
                      <div className="bg-white p-3 rounded-xl shadow-sm h-fit">
                        <Bed size={24} className="text-teal-600" weight="duotone" />
                      </div>
                      <div className="flex-1">
                        <div className="flex justify-between items-start">
                          <h3 className="font-bold text-lg text-gray-900">{room.name}</h3>
                          <Badge variant="outline" className="bg-white">
                            {room.size_sqm} m²
                          </Badge>
                        </div>
                        <div className="flex items-center gap-4 text-sm text-muted-foreground mt-2 mb-3">
                          <div className="flex items-center gap-1.5">
                            <Users size={16} />
                            <span>Up to {room.max_guests} guests</span>
                          </div>
                          <div className="flex items-center gap-1.5">
                            <Bed size={16} />
                            <span>{room.beds}</span>
                          </div>
                        </div>
                        <div className="flex flex-wrap gap-2">
                          {room.features?.map((feature: string) => (
                            <span key={feature} className="text-xs bg-white px-2 py-1 rounded border text-gray-600 font-medium">
                              {feature}
                            </span>
                          ))}
                        </div>
                      </div>
                    </CardContent>
                  </Card>
                ))}
              </div>
            </div>
          )}

          <div className="h-px bg-gray-100" />

          {/* Reviews Preview */}
          {deal.reviews && deal.reviews.length > 0 && (
            <div className="space-y-4">
              <div className="flex items-center gap-2">
                <Star size={24} weight="fill" className="text-yellow-400" />
                <h2 className="text-xl font-bold text-gray-900">{deal.rating} · {deal.review_count} reviews</h2>
              </div>
              <div className="grid md:grid-cols-2 gap-4">
                {deal.reviews.slice(0, 4).map((review: any, idx: number) => (
                  <div key={idx} className="p-4 rounded-xl bg-gray-50 space-y-2">
                    <div className="flex items-center justify-between">
                      <div className="flex items-center gap-2">
                        <div className="w-8 h-8 rounded-full bg-gradient-to-br from-teal-400 to-blue-500 flex items-center justify-center text-white font-bold text-xs">
                          {review.author.charAt(0)}
                        </div>
                        <div>
                          <p className="font-semibold text-sm">{review.author}</p>
                          <p className="text-xs text-muted-foreground">{review.date}</p>
                        </div>
                      </div>
                    </div>
                    <p className="text-sm text-gray-600 line-clamp-3 leading-relaxed">"{review.text}"</p>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>

        {/* Sticky Sidebar */}
        <div className="lg:col-span-1">
          <div className="sticky top-6">
            <Card className="border-0 shadow-xl rounded-2xl overflow-hidden ring-1 ring-black/5">
              <CardContent className="p-6 space-y-6">
                <div className="flex items-end justify-between border-b pb-6">
                  <div>
                    <p className="text-sm text-muted-foreground mb-1 font-medium">Total price from</p>
                    <div className="flex items-baseline gap-2">
                      <span className="text-3xl font-bold text-gray-900">
                        {formatCurrency(deal.pricing?.deal_price, deal.pricing?.currency)}
                      </span>
                      <span className="text-gray-500 font-medium">/{deal.pricing?.per}</span>
                    </div>
                  </div>
                  {deal.pricing?.original_price > deal.pricing?.deal_price && (
                    <Badge className="bg-green-100 text-green-700 hover:bg-green-200 border-0 px-2 py-1">
                      Save {deal.pricing.discount_percent}%
                    </Badge>
                  )}
                </div>

                <div className="space-y-4">
                  <div className="grid grid-cols-2 gap-3">
                    <div className="p-3 border rounded-xl bg-gray-50">
                      <p className="text-xs text-muted-foreground uppercase font-bold tracking-wider mb-1">Check-in</p>
                      <p className="font-semibold text-sm">Add date</p>
                    </div>
                    <div className="p-3 border rounded-xl bg-gray-50">
                      <p className="text-xs text-muted-foreground uppercase font-bold tracking-wider mb-1">Check-out</p>
                      <p className="font-semibold text-sm">Add date</p>
                    </div>
                  </div>
                  
                  <div className="p-3 border rounded-xl bg-gray-50 flex items-center justify-between">
                    <div>
                      <p className="text-xs text-muted-foreground uppercase font-bold tracking-wider mb-1">Guests</p>
                      <p className="font-semibold text-sm">2 guests</p>
                    </div>
                    <Users size={18} className="text-gray-400" />
                  </div>
                </div>

                {deal.pricing?.includes && (
                  <div className="bg-teal-50 p-4 rounded-xl space-y-2">
                    <p className="text-xs font-bold text-teal-800 uppercase tracking-wide mb-2">Included in price</p>
                    {deal.pricing.includes.map((item: string) => (
                      <div key={item} className="flex items-center gap-2 text-sm text-teal-700">
                        <div className="bg-white p-0.5 rounded-full">
                          <Check size={10} weight="bold" className="text-teal-600" />
                        </div>
                        <span className="capitalize font-medium">{item.replace('_', ' ')}</span>
                      </div>
                    ))}
                  </div>
                )}

                <Button 
                  onClick={onAddToCart} 
                  className="w-full h-12 text-lg font-bold bg-gradient-to-r from-teal-500 to-cyan-600 hover:from-teal-600 hover:to-cyan-700 shadow-lg hover:shadow-xl transition-all rounded-xl"
                >
                  Reserve Now
                </Button>
                
                <p className="text-center text-xs text-muted-foreground">
                  You won't be charged yet
                </p>
              </CardContent>
            </Card>
          </div>
        </div>
      </div>
    </div>
  );
}
