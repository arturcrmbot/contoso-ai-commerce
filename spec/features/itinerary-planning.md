# Feature: Multi-Destination Itinerary Planning

## Current State (Vodafone)
- No equivalent (single product focus)

## Target State (Travel Agent)

### Simple, Modular Tools

**Route Analysis:**
- `get_route_info(locations[])`
  - Returns: distances between each pair, travel times, suggested transport modes
  - Example: ["Athens", "Santorini", "Mykonos"] → distances, ferry/flight options

**Cost Calculations:**
- `calculate_trip_cost(deals[], transport_between[])` - Sum up total cost
- `estimate_transport_cost(from, to, mode)` - Inter-city travel cost

**Activity Data:**
- `get_destination_activities(location, interests[])` - Suggest things to do

### LLM Does The Intelligence

**User says:** "Plan me a 10-day Greek islands trip"

**LLM reasons:**
1. Understands: Greece, islands, 10 days → needs multi-destination
2. Calls `search_deals("Greek islands", {})` to see what's available
3. Picks 3 destinations: Athens (gateway), Santorini (iconic), Mykonos (beaches)
4. Calls `get_route_info(["Athens", "Santorini", "Mykonos"])`
5. Sees: Athens→Santorini (ferry 5h), Santorini→Mykonos (ferry 3h) ✅ logical
6. Allocates nights: 2 Athens (short stay), 4 Santorini (main attraction), 3 Mykonos
7. Calls `get_deal_details()` for each city
8. Calls `calculate_trip_cost()` to verify within budget
9. Presents: "I've planned a 10-day adventure: Start in Athens (2 nights), ferry to Santorini (4 nights), then Mykonos (3 nights). Total: £1,850"

**User says:** "Can we swap Mykonos for Crete?"

**LLM reasons:**
1. Keeps Athens + Santorini
2. Calls `get_route_info(["Athens", "Santorini", "Crete"])`
3. Sees: Santorini→Crete is awkward (backtracking)
4. Suggests: Athens→Crete→Santorini is better
5. Recalculates and presents new itinerary

**No rigid `suggest_multi_destination_itinerary()` tool** - LLM orchestrates simple tools + applies reasoning

### Frontend Changes
**New:** `ItineraryTimeline` component
- Displays whatever structure the LLM creates
- Flexible layout (2 cities, 5 cities, doesn't matter)
- Shows: nights per stop, transport between, activities, costs

## Why This Works Better
- **Creative:** LLM can handle "show me an off-the-beaten-path route" without hardcoded logic
- **Adaptive:** "I only have 5 days" → LLM adjusts on the fly
- **Conversational:** User can iterate ("swap X for Y", "add a beach day")
- **Agent-ready:** Complex planning can be delegated to specialized agent
