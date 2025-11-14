# Feature: Cart & Checkout

## Current State (Vodafone)
- Shopping cart for devices, plans, accessories
- In-memory storage
- Tools: `add_to_cart`, `remove_from_cart`, `get_cart_summary`

## Target State (Travel Agent)

### Simple, Modular Tools

**Cart Operations:**
- `add_to_cart(deal_id, metadata)` - metadata: {check_in, check_out, guests}
- `update_cart_item(item_id, changes)` - Modify existing item
- `remove_from_cart(item_id)`
- `get_cart()` - Return current cart state
- `clear_cart()`

**Checkout:**
- `calculate_cart_total()` - Sum everything
- `apply_promo(code)` - Add discount
- `checkout(traveler_info, payment_info)` - Complete booking (mock for MVP)

### LLM Does The Intelligence

**User says:** "Add the Santorini deal to my cart"

**LLM reasons:**
1. Knows which deal from context (user was just looking at it)
2. Prompts: "When would you like to check in?"
3. User: "June 15th for 4 nights"
4. Calls `add_to_cart("deal-santorini-123", {check_in: "2025-06-15", nights: 4, guests: 2})`
5. Confirms: "Added! 4 nights in Santorini (June 15-19) for 2 guests. Your cart total is £749"

**User says:** "Actually make it 5 nights"

**LLM reasons:**
1. Finds cart item
2. Calls `update_cart_item(item_id, {nights: 5})`
3. Recalculates price automatically

**No complex "add_deal_with_validation_and_pricing" tool** - simple operations + LLM reasoning

### Frontend Changes
- `CartDrawer` shows trips with dates/guests (not device contracts)
- `CartItem` flexible to whatever LLM adds (1 destination or multi-city itinerary)

## Why This Works Better
- **Flexible:** LLM can add partial items ("add to cart, I'll decide dates later")
- **Conversational:** Natural modifications ("change check-in to the 20th")
- **Simple:** Tools just do CRUD, LLM handles logic
