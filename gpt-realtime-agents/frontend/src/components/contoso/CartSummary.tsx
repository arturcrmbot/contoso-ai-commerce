import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from '@/components/ui/dialog';
import { Button } from '@/components/ui/button';
import { X } from '@phosphor-icons/react';

interface CartItem {
  id: string;
  type: 'device' | 'plan' | 'accessory';
  name: string;
  price_upfront?: number;
  price_monthly?: number;
  price?: number; // For accessories
}

interface CartSummaryProps {
  isOpen: boolean;
  onClose: () => void;
  items: CartItem[];
  onRemoveItem: (itemId: string) => void;
  onCheckout: () => void;
}

export function CartSummary({
  isOpen,
  onClose,
  items,
  onRemoveItem,
  onCheckout
}: CartSummaryProps) {
  const totalUpfront = items.reduce((sum, item) => {
    return sum + (item.price_upfront || 0) + (item.price || 0);
  }, 0);

  const totalMonthly = items.reduce((sum, item) => {
    return sum + (item.price_monthly || 0);
  }, 0);

  const total24Months = (totalMonthly * 24) + totalUpfront;

  return (
    <Dialog open={isOpen} onOpenChange={onClose}>
      <DialogContent className="max-w-md">
        <DialogHeader>
          <DialogTitle>Shopping Cart</DialogTitle>
        </DialogHeader>

        <div className="space-y-4">
          {items.length === 0 ? (
            <p className="text-muted-foreground text-sm text-center py-8">
              Your cart is empty
            </p>
          ) : (
            <>
              {/* Cart Items */}
              <div className="space-y-3 max-h-[300px] overflow-y-auto">
                {items.map((item) => (
                  <div
                    key={item.id}
                    className="flex items-start justify-between p-3 border rounded-lg"
                  >
                    <div className="flex-1">
                      <p className="font-medium text-sm">{item.name}</p>
                      <p className="text-xs text-muted-foreground capitalize">{item.type}</p>
                      <div className="mt-1 text-xs">
                        {item.price_monthly && (
                          <span className="font-semibold">£{item.price_monthly}/mo</span>
                        )}
                        {item.price_upfront && item.price_upfront > 0 && (
                          <span className="text-muted-foreground ml-2">
                            + £{item.price_upfront} upfront
                          </span>
                        )}
                        {item.price && (
                          <span className="font-semibold">£{item.price}</span>
                        )}
                      </div>
                    </div>
                    <Button
                      variant="ghost"
                      size="sm"
                      onClick={() => onRemoveItem(item.id)}
                      className="h-8 w-8 p-0"
                    >
                      <X size={16} />
                    </Button>
                  </div>
                ))}
              </div>

              {/* Pricing Summary */}
              <div className="border-t pt-4 space-y-2">
                <div className="flex justify-between text-sm">
                  <span>Upfront cost:</span>
                  <span className="font-semibold">£{totalUpfront.toFixed(2)}</span>
                </div>
                <div className="flex justify-between text-sm">
                  <span>Monthly cost:</span>
                  <span className="font-semibold">£{totalMonthly.toFixed(2)}/mo</span>
                </div>
                <div className="flex justify-between text-base font-bold pt-2 border-t">
                  <span>24-month total:</span>
                  <span>£{total24Months.toFixed(2)}</span>
                </div>
              </div>

              {/* Checkout Button */}
              <Button
                onClick={onCheckout}
                className="w-full"
                size="lg"
              >
                Proceed to Checkout
              </Button>
            </>
          )}
        </div>
      </DialogContent>
    </Dialog>
  );
}
