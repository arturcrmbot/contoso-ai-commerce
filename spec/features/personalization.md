# Feature: User Preferences & Personalization

## Current State (Vodafone)
- `customer_profiles.py` - predefined test profiles (high data user, frequent traveler)
- `analyze_customer_profile` - generates recommendations

## Target State (Travel Agent)

### Simple, Modular Tools

**Preference Storage:**
- `save_preference(key, value)` - Store anything: home_location, budget_range, interests, etc.
- `get_preferences()` - Retrieve all preferences
- `update_preference(key, value)` - Modify existing

**Data Retrieval:**
- `get_past_trips()` - If user has history
- `get_trending(category)` - Popular destinations by category

### LLM Does The Intelligence

**User says:** "I'm based in London and usually spend around £1500 on trips"

**LLM reasons:**
1. Extracts: location=London, budget_typical=1500
2. Calls `save_preference("home_location", "London, UK")`
3. Calls `save_preference("budget_range", {typical: 1500})`
4. Remembers for future searches

**Later, user says:** "Show me something"

**LLM reasons:**
1. Calls `get_preferences()` → sees London, £1500 budget
2. Infers: within 3h flight from London, budget ~£1500
3. Calls `search_deals()` with these defaults
4. Presents contextual results

**User says:** "I loved Barcelona last year"

**LLM reasons:**
1. Stores: `save_preference("loved_destinations", ["Barcelona"])`
2. Analyzes: Barcelona = coastal, cultural, European
3. Future searches: suggests Valencia, Lisbon, Nice (similar vibe)
4. No rigid recommendation engine - LLM makes associations

**No `analyze_travel_profile()` tool** - LLM reasons about preferences and patterns

### Frontend Changes
**Replace:** ProfileSelector dropdown
**With:** Natural conversation that extracts preferences
- LLM asks: "Where are you based?" "What's your typical budget?" "Beach or mountains?"
- OR detects preferences from conversation organically

## Why This Works Better
- **Flexible:** Preferences emerge naturally, not forced questionnaire
- **Intelligent:** LLM makes creative connections ("loved Barcelona → try Valencia")
- **Private:** No rigid profile schema, just key-value storage
- **Agent-ready:** Specialized agents can analyze travel patterns deeply
