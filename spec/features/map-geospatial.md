# Feature: Map & Geospatial Intelligence

## Current State (Vodafone)
- No map functionality
- No location awareness

## Target State (Travel Agent)

### Simple, Modular Tools

**Geospatial Primitives:**
- `geocode(location)` → {lat, lon}
- `calculate_distance(location1, location2)` → km
- `estimate_travel_time(location1, location2, mode)` → hours

**Location Search:**
- `find_deals_near(coordinates, radius_km)` → deals within radius

### LLM Does The Intelligence

**User says:** "Show me deals within 3 hours flight from London"

**LLM reasons:**
1. Calls `geocode("London")` → {lat: 51.5074, lon: -0.1278}
2. Knows: 3 hours flight ≈ 2,400 km radius
3. Calls `find_deals_near({lat: 51.5074, lon: -0.1278}, 2400)`
4. Gets deals, enriches each with `calculate_distance()`
5. Presents: "Here are beach deals within 3h flight: Lisbon (2.5h), Barcelona (2h), Dubrovnik (2.5h)..."

**User says:** "Actually, what about train-accessible destinations?"

**LLM reasons:**
1. Knows: trains go ~600 km in 3-4 hours
2. Calls `find_deals_near(London, 600)`
3. Filters to: Paris, Amsterdam, Brussels
4. Calls `estimate_travel_time(London, Paris, "train")` for each
5. Presents with travel times

### Frontend Component
**New:** `MapView`
- Shows whatever the LLM returns (any number of pins)
- User location + deal locations
- Interactive (click pin → show deal)
- Flexible distance circles (LLM decides radius based on context)

### Caching Strategy
- Geocoding cached (city → coords, 30 days)
- Distance calculations cached (common pairs)
- LLM-agnostic (just fast primitives)

## Why This Works Better
- **Context-aware:** LLM interprets "close by" based on conversation (train vs flight)
- **Flexible queries:** "Within 500km of Paris and Barcelona" → LLM figures out the logic
- **Agent-ready:** Complex geospatial analysis can be delegated
