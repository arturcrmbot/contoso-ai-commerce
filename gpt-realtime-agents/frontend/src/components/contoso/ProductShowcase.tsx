import { ProductCard } from './ProductCard';

interface Device {
  id: string;
  name: string;
  brand: string;
  price_upfront: number;
  price_monthly: number;
  image_url?: string;
  attributes?: any;
  rating?: number;
  reviews_count?: number;
}

interface ProductShowcaseProps {
  products: Device[];
  highlightedId: string | null;
  onProductClick: (device: Device) => void;
}

export function ProductShowcase({
  products,
  highlightedId,
  onProductClick
}: ProductShowcaseProps) {
  return (
    <div className="h-full flex flex-col px-6 pb-6">
      {/* Header */}
      <div className="mb-6 flex-shrink-0">
        <h2 className="text-2xl font-bold text-foreground tracking-tight">Recommended Phones</h2>
        <p className="text-base text-muted-foreground">
          {products.length} {products.length === 1 ? 'device' : 'devices'} found
        </p>
      </div>

      {/* Product Grid */}
      <div className="flex-1 overflow-y-auto min-h-0 pr-2 -mr-2">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 pb-8">
          {products.map((device) => (
            <ProductCard
              key={device.id}
              device={device}
              isHighlighted={device.id === highlightedId}
              onClick={() => onProductClick(device)}
            />
          ))}
        </div>

        {products.length === 0 && (
          <div className="flex flex-col items-center justify-center h-64 text-muted-foreground bg-gray-50 rounded-xl border-2 border-dashed">
            <p className="text-lg font-medium">No products found</p>
            <p className="text-sm">Try adjusting your search criteria</p>
          </div>
        )}
      </div>
    </div>
  );
}
