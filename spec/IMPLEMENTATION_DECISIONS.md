# Implementation Decisions
**Answers to key questions before coding**

---

## 1. Mock Travel Data ✅

**Quantity:** 20-30 deals (not 100+)

**Locations (4 cities):**
- Warsaw (Poland capital - cultural/business)
- Prague (Czech - historic/romantic)
- Zakopane (Poland mountains - skiing/hiking)
- Sopot (Poland coast - beach/spa)

**Hotel Names:** Completely made up (fictional)

**Features:** Varied - different amenities, ratings, suitable_for tags

**Pricing:** Realistic European hotel rates

**Images:** Unsplash URLs (stable links, high-quality destination/city photos)
- Warsaw: Old Town, Palace of Culture, Royal Castle
- Prague: Charles Bridge, Old Town Square, Prague Castle
- Zakopane: Tatra Mountains, mountain resorts, winter scenes
- Sopot: Sopot Pier, beach views, Baltic coast

**Deal Types:** Just "hotel" for MVP (no packages or experiences yet)

---

## 2. Search Implementation Detail ✅

**Question:** `search_deals(query, filters)` - how should the "query" free text work?

**Your answer:** Keep it simple - basic filters only (budget, dates, location, deal_type). Return matching deals. Let LLM decide what to show to the user.

**Implementation:**
- Tool does simple filtering (budget_max, budget_min, city match, deal_type)
- Returns all matching deals
- LLM picks best ones to show based on context/conversation
- No fancy text search needed for MVP

---

## 3. Visual Types & Canvas Communication ✅

**Question:** How does LLM tell frontend what visual to show?

**Your answer:** Tool returns visual hint as part of result. Keeps it fast, not janky.

**Implementation:**
```python
return {
  "deals": [...],
  "visual": {
    "type": "deal_grid",  # or "deal_hero", "map_view", "itinerary_timeline"
    "data": deals  # formatted for that visual type
  }
}
```

Tool decides appropriate visual based on:
- Number of results (1 deal → hero, multiple → grid)
- Tool type (route_info → itinerary_timeline)
- Context (if applicable)

Frontend receives and renders immediately.

---

## 4. Geospatial Caching Strategy ✅

**Question:** Distance calculations - when/how to compute?

**Your answer:** Keep it basic. Customers are from the 4 deal locations (Warsaw, Prague, Zakopane, Sopot).

**Implementation:**
- Pre-compute distances between the 4 cities on startup
- Just 6 pairs total: Warsaw↔Prague, Warsaw↔Zakopane, Warsaw↔Sopot, Prague↔Zakopane, Prague↔Sopot, Zakopane↔Sopot
- Hardcode coordinates for these 4 cities
- Store in simple dict: `{("Warsaw", "Prague"): 515.3, ...}`
- No external API needed, just geopy library for calculations
- User selects their home city from dropdown or conversation

**No need for:**
- London, Paris, Berlin, etc. (not for MVP)
- Lazy caching (only 4 cities)
- Complex geocoding (hardcoded coords)

---

## 5. Phase Execution Order ✅

**Question:** Should implementation be strictly sequential or parallel?

**Your answer:** Option B - Build backend + frontend together in parallel.

**Implementation approach:**
- Work on tool AND its UI component simultaneously
- Example: Build `search_deals()` tool + `DealCard` component together
- Can test end-to-end sooner
- Faster feedback loop

**Order:**
1. Data models + mock catalog + basic search tool + DealCard
2. Geospatial tools + DistanceIndicator component
3. Route tools + ItineraryTimeline component
4. Cart tools + CartDrawer updates
5. Map integration (tool + MapView component)
6. Polish + testing

---

## 6. Preferences Storage (MVP) ✅

**Question:** `save_preference(key, value)` - where to store?

**Your answer:** Option A - Simple in-memory dict.

**Implementation:**
```python
user_preferences = {}  # Global dict in backend

def save_preference(session_id, key, value):
    if session_id not in user_preferences:
        user_preferences[session_id] = {}
    user_preferences[session_id][key] = value

def get_preferences(session_id):
    return user_preferences.get(session_id, {})
```

**Notes:**
- Lost on server restart (acceptable for MVP)
- No file I/O overhead
- Simple and fast

---

## 7. System Prompt Personality ✅

**Question:** Any specific tone beyond plan (enthusiastic, practical travel advisor)?

**Your answer:** Casual, friendly, funny/relatable.

**Implementation:**
- Conversational tone (not formal)
- Light humor where appropriate
- Relatable references ("perfect for escaping the office")
- Enthusiastic but not salesy
- Keep 2-3 sentences still (concise)
- Proactive suggestions welcomed

**Examples of tone:**
- ❌ "I would be delighted to assist you in finding suitable accommodations"
- ✅ "Let me find you some amazing deals!"
- ❌ "This property offers exceptional value"
- ✅ "This place is a steal - you're saving 40%!"
- ✅ "Warsaw in spring? Chef's kiss 👌"

---

## 8. Error Handling Philosophy ✅

**Question:** When things fail (geocoding fails, no deals found) - how should tools behave?

**Your answer:** Option A - Return empty/null, let LLM handle gracefully.

**Implementation:**
- No deals found? Return `[]`
- No data? Return `None` or `{}`
- LLM interprets and responds naturally
- Tools stay simple, don't need error handling logic

**Examples:**
```python
def search_deals(filters):
    results = [d for d in DEALS if matches(d, filters)]
    return results  # Could be [] if nothing matches

def get_route_info(locations):
    if not locations or len(locations) < 2:
        return []  # LLM handles it
    # ... calculate routes
```

**LLM responses:**
- Empty deals: "Hmm, no deals match that. Want to try nearby cities or different dates?"
- Missing data: "I don't have info on that yet. Let me show you what I do have!"

---

## 9. [Future questions as needed]

**Question:**

**Your answer:**
