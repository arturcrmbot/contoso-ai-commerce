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
      <DialogContent className="max-w-md border-0 shadow-2xl rounded-2xl overflow-hidden p-0 gap-0">
        <DialogHeader className="p-6 bg-gradient-to-r from-teal-500 to-cyan-600 text-white">
          <DialogTitle className="text-xl font-bold flex items-center gap-2">
            Your Trip Itinerary
          </DialogTitle>
        </DialogHeader>

        <div className="p-6 space-y-6">
          {items.length === 0 ? (
            <div className="text-center py-12 space-y-3">
              <div className="w-16 h-16 bg-gray-100 rounded-full flex items-center justify-center mx-auto text-gray-400">
                <X size={32} />
              </div>
              <p className="text-lg font-medium text-gray-900">Your itinerary is empty</p>
              <p className="text-sm text-muted-foreground">Start exploring to add flights, hotels, and more.</p>
            </div>
          ) : (
            <>
              {/* Cart Items */}
              <div className="space-y-4 max-h-[400px] overflow-y-auto pr-2 -mr-2">
                {items.map((item) => (
                  <div
                    key={item.id}
                    className="flex items-start justify-between p-4 border border-gray-100 rounded-xl bg-gray-50/50 hover:bg-gray-50 transition-colors group"
                  >
                    <div className="flex-1">
                      <div className="flex items-center gap-2 mb-1">
                        <Badge variant="outline" className="bg-white text-[10px] uppercase tracking-wider font-semibold border-gray-200">
                          {item.type}
                        </Badge>
                      </div>
                      <p className="font-bold text-gray-900 mb-1">{item.name}</p>
                      <div className="text-sm text-gray-600">
                        {item.price_monthly && (
                          <span className="font-semibold text-teal-600">£{item.price_monthly}/mo</span>
                        )}
                        {item.price_upfront && item.price_upfront > 0 && (
                          <span className="text-muted-foreground ml-2">
                            + £{item.price_upfront} upfront
                          </span>
                        )}
                        {item.price && (
                          <span className="font-semibold text-teal-600">£{item.price}</span>
                        )}
                      </div>
                    </div>
                    <Button
                      variant="ghost"
                      size="sm"
                      onClick={() => onRemoveItem(item.id)}
                      className="h-8 w-8 p-0 text-gray-400 hover:text-red-500 hover:bg-red-50 rounded-full opacity-0 group-hover:opacity-100 transition-all"
                    >
                      <X size={16} />
                    </Button>
                  </div>
                ))}
              </div>

              {/* Pricing Summary */}
              <div className="border-t pt-6 space-y-3">
                <div className="flex justify-between text-sm text-gray-600">
                  <span>Upfront cost</span>
                  <span className="font-medium text-gray-900">£{totalUpfront.toFixed(2)}</span>
                </div>
                <div className="flex justify-between text-sm text-gray-600">
                  <span>Monthly cost</span>
                  <span className="font-medium text-gray-900">£{totalMonthly.toFixed(2)}/mo</span>
                </div>
                <div className="flex justify-between text-lg font-bold pt-4 border-t border-dashed">
                  <span>Total (24 months)</span>
                  <span className="text-teal-600">£{total24Months.toFixed(2)}</span>
                </div>
              </div>

              {/* Checkout Button */}
              <Button
                onClick={onCheckout}
                className="w-full h-12 text-lg font-bold bg-gradient-to-r from-teal-500 to-cyan-600 hover:from-teal-600 hover:to-cyan-700 shadow-lg hover:shadow-xl transition-all rounded-xl"
              >
                Confirm Booking
              </Button>
            </>
          )}
        </div>
      </DialogContent>
    </Dialog>
  );
}
