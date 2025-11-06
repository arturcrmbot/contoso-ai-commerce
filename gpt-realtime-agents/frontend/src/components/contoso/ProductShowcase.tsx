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
    <div className="h-full flex flex-col">
      {/* Header */}
      <div className="mb-4 flex-shrink-0">
        <h2 className="text-xl font-bold text-foreground">Recommended Phones</h2>
        <p className="text-sm text-muted-foreground">
          {products.length} {products.length === 1 ? 'device' : 'devices'} found
        </p>
      </div>

      {/* Product Grid */}
      <div className="flex-1 overflow-y-auto min-h-0">
        <div className="grid grid-cols-2 gap-4 pb-4">
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
          <div className="flex items-center justify-center h-full text-muted-foreground">
            <p className="text-sm">No products to display yet</p>
          </div>
        )}
      </div>
    </div>
  );
}
