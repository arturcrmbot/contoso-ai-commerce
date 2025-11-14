# Feature: Deal Search & Discovery

## Current State (Vodafone)
- `search_devices_by_attributes` - filters phones by battery, camera, price, brand
- Product catalog with ~20 mock devices
- Visual grid shows phone cards

## Target State (Travel Agent)

### Simple, Modular Tools

**Core Search (flexible):**
- `search_deals(query, filters)`
  - query: free text ("beach hotels Greece", "Santorini")
  - filters: {budget_max, budget_min, deal_type, available_from, available_to}
  - Returns: list of deals with metadata

**Detail Fetching:**
- `get_deal_details(deal_id)` - Full info for one deal
- `get_deals_batch(deal_ids[])` - Multiple deals at once

**Basic Operations:**
- `filter_deals(deals[], criteria)` - Apply additional filtering
- `sort_deals(deals[], sort_by)` - Reorder results

### LLM Does The Intelligence

**User says:** "Find me beach deals in Greece under £1000"

**LLM reasons:**
1. Calls `search_deals("Greece beach", {budget_max: 1000, deal_type: "hotel"})`
2. Gets results, analyzes them
3. Decides which to show first based on ratings, urgency, variety
4. Generates contextual response: "I found 12 stunning beach hotels in Greece! Here are the top 5..."
5. If user location known, enriches with distance (calls geospatial tools)

**User says:** "Which one has the best reviews?"

**LLM reasons:**
1. Already has deals in context
2. Sorts by rating: `sort_deals(deals, "rating")`
3. Highlights top-rated option

**No rigid "search_by_destination" vs "search_by_interests"** - just flexible search + LLM reasoning

### Data Model Changes
**From:** `Device` (id, name, brand, price_upfront, price_monthly, attributes)
**To:** `TravelDeal` (id, title, destination, dates, pricing, images, rating, features, urgency)

### Frontend Changes
**From:** ProductCard → **To:** DealCard
- Add: Distance badge (if location known), urgency tags, climate info
- Remove: Device-specific specs

## Why This Works Better
- **Flexible:** LLM can handle "find me something romantic" without needing a `search_by_vibe` tool
- **Composable:** Chain simple tools for complex queries
- **Adaptive:** Easy to add new search criteria without new tools
- **Agent-ready:** Future agents can orchestrate multi-step searches
