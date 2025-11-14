# Product Requirements Document (PRD)
## AI-Powered Conversational Travel Agent

**Version:** 1.0
**Date:** January 2025
**Status:** Draft
**Owner:** Product Team

---

## Executive Summary

Transform the existing Vodafone Three AI Commerce platform into an AI-powered conversational travel agent that revolutionizes how users discover and book travel deals through natural conversation, intelligent recommendations, and visual discovery.

Unlike traditional travel deal websites (Secret Escapes, Zlavomat) that rely on manual filtering, our platform will offer:
- **Conversational Discovery**: Natural language search ("Find me a beach getaway in May under £1,000")
- **Intelligent Recommendations**: Distance-aware, date-flexible, interest-based suggestions
- **Multi-Destination Planning**: AI-built itineraries with optimized routing
- **Voice Interaction**: Hands-free travel planning
- **Visual Intelligence**: Maps, timelines, and dynamic showcases

---

## Problem Statement

### Current Pain Points in Travel Deal Discovery

1. **Filter Fatigue**: Users must manually set multiple filters (destination, dates, price, amenities) across hundreds of deals
2. **No Context Awareness**: Sites don't consider user location, travel time, or practical logistics
3. **Single-Destination Bias**: Difficult to plan multi-city trips with deal combinations
4. **Rigid Date Searches**: Must know exact dates; no "flexible in May" option
5. **No Personalization**: Generic deal lists; no learning from preferences or past trips
6. **Static Experience**: Click, scroll, filter; no interactive guidance

### User Needs

**Primary Personas:**

1. **Busy Professional (Sarah, 32)**
   - Limited time to research
   - Wants quick, personalized recommendations
   - Values convenience and quality over cheapest price
   - Prefers voice interaction while multitasking

2. **Budget Traveler (James, 25)**
   - Flexible dates, seeking best value
   - Wants to maximize experiences per budget
   - Interested in multi-destination trips
   - Needs complete cost transparency

3. **Family Planner (Emma, 40)**
   - Specific dates (school holidays)
   - Multiple constraints (kid-friendly, accessibility)
   - Wants curated options, not overwhelming choices
   - Values detailed information and reassurance

---

## Product Vision

**Vision Statement:**
"Make travel planning as simple as talking to a knowledgeable friend who knows every deal, every destination, and exactly what you're looking for."

**Mission:**
Enable anyone to discover and book their perfect trip through natural conversation, powered by AI that understands context, preferences, and practical constraints.

**Key Differentiators:**
1. Conversational interface (voice + text)
2. Distance and travel-time intelligence
3. AI-generated multi-destination itineraries
4. Flexible date matching with visual calendars
5. Proactive recommendations based on user profile
6. Real-time visual updates during conversation

---

## Success Metrics

### Primary KPIs

| Metric | Target | Measurement |
|--------|--------|-------------|
| Conversation-to-Booking Rate | 15% | Completed checkouts / total sessions |
| Average Session Duration | 8-12 min | Time from start to cart add/exit |
| Deals Viewed per Session | 5-8 | Number of deals explored |
| Multi-Deal Bookings | 25% | Bookings with >1 destination |
| Voice Interaction Rate | 30% | Sessions using voice |
| User Satisfaction (NPS) | 50+ | Post-booking survey |

### Secondary Metrics

- Average cart value (target: £1,200)
- Return user rate (target: 40% within 6 months)
- Deal comparison usage (target: 60% of sessions)
- Itinerary builder usage (target: 35% of sessions)
- Email save rate (target: 20%)

---

## Scope

### In Scope (MVP - Phase 1)

**Core Features:**
- ✅ Conversational deal search (destination, dates, budget, interests)
- ✅ Visual deal presentation (cards, hero views, comparisons)
- ✅ Distance and flight time calculations
- ✅ Cart and checkout flow
- ✅ Deal comparison (side-by-side)
- ✅ Basic user preference collection
- ✅ Mock travel deal catalog (100+ deals)
- ✅ Voice and text interaction
- ✅ Proactive recommendations

**Technical:**
- ✅ Azure OpenAI Realtime API integration
- ✅ WebRTC voice streaming
- ✅ React frontend with dynamic visuals
- ✅ FastAPI backend with tool calling
- ✅ Azure Container Apps deployment

### Out of Scope (MVP)

**Phase 2 Features:**
- ⏭️ Real-time API integration (Amadeus, Skyscanner)
- ⏭️ Flight search and booking
- ⏭️ Interactive map view with deal pins
- ⏭️ Calendar availability heatmap
- ⏭️ Multi-destination itinerary builder
- ⏭️ User accounts and saved trips
- ⏭️ Social sharing features

**Future Considerations:**
- 🔮 Activity and attraction booking
- 🔮 Restaurant recommendations
- 🔮 Travel insurance
- 🔮 Loyalty program
- 🔮 Mobile native app
- 🔮 Integration with calendar/email

---

## User Stories

### Epic 1: Deal Discovery

**US-1.1: Basic Search**
As a user, I want to search for travel deals by destination so that I can find hotels in places I want to visit.

**Acceptance Criteria:**
- Can specify city, country, or region
- Results show within 3 seconds
- Each deal shows: image, title, price, discount, rating
- Deals sorted by relevance (match quality + price)

**US-1.2: Budget-Aware Search**
As a budget-conscious traveler, I want to specify my maximum budget so that I only see deals I can afford.

**Acceptance Criteria:**
- Can set budget range (min/max)
- Budget includes accommodation only (flights separate)
- Results respect budget constraints
- Can see "slightly over budget" options with clear indicator

**US-1.3: Date-Flexible Search**
As a flexible traveler, I want to search for deals available in a general timeframe (e.g., "May") so that I can find the best deals across multiple dates.

**Acceptance Criteria:**
- Can specify month or date range
- Can indicate flexibility ("anytime in summer")
- Results show best dates for each deal
- Can see price variations by date

**US-1.4: Interest-Based Search**
As an adventure seeker, I want to find deals matching my interests (beach, culture, adventure) so that I discover destinations I'll enjoy.

**Acceptance Criteria:**
- Can select multiple interests
- Deals tagged with appropriate categories
- Results prioritize interest matches
- Can see why each deal was recommended

**US-1.5: Proximity Search**
As a user, I want to find deals near me or within a certain travel distance so that I minimize flight time.

**Acceptance Criteria:**
- System detects or asks for home location
- Can filter by max flight hours (e.g., "within 3 hours")
- Each deal shows distance and flight duration
- Results sorted by proximity + deal quality

### Epic 2: Deal Exploration

**US-2.1: Deal Details**
As a user, I want to see comprehensive details about a deal so that I can make an informed decision.

**Acceptance Criteria:**
- High-quality images (5+ photos)
- Full description of accommodation
- Amenities list with icons
- Location on map
- Reviews and ratings
- Available dates calendar
- What's included/excluded
- Cancellation policy

**US-2.2: Deal Comparison**
As an indecisive user, I want to compare multiple deals side-by-side so that I can easily see differences.

**Acceptance Criteria:**
- Can compare 2-4 deals simultaneously
- Comparison includes: price, location, amenities, ratings, distance
- Highlights differences
- Can swap deals in comparison view

**US-2.3: Similar Deals**
As a user considering a deal, I want to see similar alternatives so that I explore all options before deciding.

**Acceptance Criteria:**
- Shows 3-5 similar deals
- Variations include: cheaper, more luxury, different dates, nearby locations
- Can easily switch focus to similar deal

### Epic 3: Trip Planning

**US-3.1: Multi-Destination Itinerary**
As an adventurous traveler, I want AI to suggest multi-city itineraries so that I can visit multiple places in one trip.

**Acceptance Criteria:**
- AI suggests logical routes (no backtracking)
- Shows inter-city transport options and duration
- Calculates total trip cost
- Displays visual timeline of the trip
- Can modify number of nights per destination

**US-3.2: Cost Estimation**
As a budget planner, I want to see total trip cost including flights and activities so that I can budget accurately.

**Acceptance Criteria:**
- Breaks down: accommodation, estimated flights, activities
- Shows savings vs. non-deal prices
- Can toggle flights on/off
- Displays in user's currency

**US-3.3: Itinerary Customization**
As a user, I want to modify AI-suggested itineraries so that I can tailor the trip to my preferences.

**Acceptance Criteria:**
- Can add/remove destinations
- Can adjust nights per location
- Can swap hotels in each destination
- Can add activities
- Cost updates in real-time

### Epic 4: Booking & Cart

**US-4.1: Add to Cart**
As a user, I want to add deals to a cart so that I can book multiple items together.

**Acceptance Criteria:**
- One-click add to cart
- Cart shows item count indicator
- Can add multiple deals (multi-destination)
- Can add activities/extras

**US-4.2: Cart Management**
As a user, I want to review and modify my cart so that I can finalize my booking.

**Acceptance Criteria:**
- See all cart items with images
- Remove items
- Modify dates/guests
- See total cost with breakdown
- Apply promo codes

**US-4.3: Checkout**
As a user, I want to complete my booking with clear steps so that I can secure my trip.

**Acceptance Criteria:**
- Collect traveler details (name, passport, contact)
- Secure payment processing
- Booking confirmation email
- Downloadable itinerary PDF

### Epic 5: Personalization

**US-5.1: Preference Learning**
As a returning user, I want the system to remember my preferences so that I get better recommendations.

**Acceptance Criteria:**
- Asks about preferences on first visit
- Saves: budget range, travel style, interests, home location
- Uses preferences to filter results
- Can update preferences anytime

**US-5.2: Proactive Recommendations**
As a user, I want to receive personalized deal suggestions so that I discover opportunities I might miss.

**Acceptance Criteria:**
- Recommendations based on past searches
- Trending destinations matching my interests
- Deals near me or in favorite regions
- "You might like" section with explanations

**US-5.3: Save for Later**
As a user researching multiple trips, I want to save deals for later so that I can compare them over time.

**Acceptance Criteria:**
- Save individual deals
- Save complete itineraries
- Email saved trips to myself
- Access saved trips on return visit (if logged in)

### Epic 6: Voice Interaction

**US-6.1: Voice Search**
As a busy user, I want to search for deals using voice so that I can multitask.

**Acceptance Criteria:**
- Activate voice with button press
- Clear voice input recognition
- Spoken responses from AI
- Can switch between voice and text seamlessly

**US-6.2: Voice Navigation**
As a hands-free user, I want to navigate deals and cart using voice so that I never need to touch the screen.

**Acceptance Criteria:**
- "Show me deal details"
- "Compare with similar deals"
- "Add to cart"
- "Go back to search results"

---

## Functional Requirements

See individual Feature Requirements Documents (FRDs) in `/spec/features/`:

1. [Deal Search & Discovery](./features/deal-search.md)
2. [Deal Presentation & Visualization](./features/deal-presentation.md)
3. [Itinerary Planning](./features/itinerary-planning.md)
4. [Cart & Checkout](./features/cart-checkout.md)
5. [User Preferences & Personalization](./features/personalization.md)
6. [Voice Interaction](./features/voice-interaction.md)
7. [Map & Geospatial Features](./features/map-geospatial.md)

---

## Non-Functional Requirements

### Performance

- **Page Load**: < 2 seconds on 4G connection
- **Search Results**: < 3 seconds for query execution
- **Voice Latency**: < 500ms for AI response start
- **Tool Execution**: < 1 second for most tools
- **Concurrent Users**: Support 100+ simultaneous sessions

### Scalability

- Horizontal scaling via Azure Container Apps (1-10 replicas)
- Stateless backend design
- Cache frequently accessed data (geocoding, distances)
- CDN for images and static assets

### Security

- HTTPS only
- Secure WebRTC with ephemeral tokens
- PCI DSS compliance for payment processing
- No storage of payment details
- Rate limiting on API endpoints
- Input validation and sanitization

### Accessibility

- WCAG 2.1 AA compliance
- Screen reader support
- Keyboard navigation
- Voice as alternative input method
- High contrast mode
- Text scaling support

### Reliability

- 99.5% uptime SLA
- Graceful degradation (fallback to text if voice fails)
- Error handling with user-friendly messages
- Session recovery on disconnect
- Health monitoring and alerts

### Compatibility

**Browsers:**
- Chrome 120+ (primary)
- Firefox 121+
- Safari 17+
- Edge 120+

**Devices:**
- Desktop (1920x1080 primary)
- Tablet (1024x768)
- Mobile (375x667 minimum)

**Voice:**
- Microphone permission required
- WebRTC support required
- Fallback to text-only mode

---

## Technical Constraints

### Current Infrastructure (Reuse)

- Azure OpenAI Realtime API (GPT-4 Realtime)
- Azure Container Apps for hosting
- Azure Container Registry
- FastAPI backend (Python 3.11+)
- React 19 frontend
- WebRTC for real-time communication

### New Dependencies Required

**Frontend:**
- Map library (react-leaflet or mapbox-gl)
- Date handling (date-fns)
- Chart library (recharts for heatmaps)

**Backend:**
- Geospatial calculations (geopy)
- Travel API clients (Amadeus SDK - Phase 2)
- Date utilities (python-dateutil)

### External APIs (Phase 2)

- Amadeus Travel API (hotels, flights)
- Mapbox or Google Maps API
- OpenWeather API (climate data)
- Geocoding API (Geoapify/OpenCage)

### Budget Constraints

- **Development**: 10-12 weeks (2-3 developers)
- **Monthly Hosting**: $50-100 (Azure services)
- **API Costs**: $100-200/month (Amadeus, Maps, Weather)
- **Total MVP**: ~$15K-25K

---

## Assumptions & Dependencies

### Assumptions

1. Users have microphone access for voice features
2. Users are comfortable with AI-powered recommendations
3. Majority of users will be from UK/EU initially
4. Mock data sufficient for MVP validation
5. Users prefer curated deals over exhaustive search
6. Mobile web is acceptable (no native app needed initially)

### Dependencies

1. Azure OpenAI Realtime API availability and pricing
2. Travel deal data sources (manual curation for MVP)
3. Payment gateway integration (Stripe or similar)
4. Email service for confirmations (SendGrid or similar)
5. Image hosting and CDN (Azure Blob Storage + CDN)

### Risks

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Azure OpenAI API pricing changes | High | Medium | Budget buffer, usage monitoring |
| Voice recognition accuracy issues | Medium | Medium | Robust fallback to text mode |
| Travel API rate limits/costs | High | Medium | Aggressive caching, start with mock data |
| User adoption of voice interface | Medium | Low | Make text mode equally powerful |
| Complex itineraries confuse AI | Medium | Medium | Start with single-destination, iterate |
| Regulatory (travel booking licensing) | High | Low | Legal review, partner with licensed OTA |

---

## Release Plan

### Phase 1: MVP (Weeks 1-10)

**Goal:** Validate conversational travel planning concept with mock data

**Deliverables:**
- Conversational deal search (text + voice)
- 100+ curated mock travel deals
- Visual deal presentation (cards, hero, comparison)
- Basic cart and checkout
- Distance calculations
- Single-destination focus
- Deployed on Azure

**Success Criteria:**
- 10+ test users complete bookings
- Average session: 8-12 minutes
- Voice usage: 30%+ of interactions
- User feedback: 4+/5 satisfaction

### Phase 2: Intelligence (Weeks 11-16)

**Goal:** Add advanced planning and personalization

**Deliverables:**
- Multi-destination itinerary builder
- Interactive map view
- Calendar availability heatmap
- User preference profiles
- Save trips for later
- Real travel API integration (Amadeus)

**Success Criteria:**
- 25% of bookings are multi-destination
- 40% users return within 30 days
- Map usage: 50%+ of sessions

### Phase 3: Scale (Weeks 17-24)

**Goal:** Production-ready with real inventory

**Deliverables:**
- Full Amadeus/Skyscanner integration
- Flight search and booking
- Activity/attraction booking
- Payment processing (Stripe)
- Email confirmations and itineraries
- User accounts and authentication
- Mobile optimization

**Success Criteria:**
- 100+ bookings per week
- <3% booking failure rate
- 50+ NPS score

---

## Stakeholder Sign-off

| Stakeholder | Role | Approval | Date |
|-------------|------|----------|------|
| Product Owner | Vision & Requirements | ☐ | |
| Engineering Lead | Technical Feasibility | ☐ | |
| Design Lead | UX/UI Approach | ☐ | |
| Business Owner | Budget & Timeline | ☐ | |

---

## Appendix

### Competitive Analysis

**Secret Escapes:**
- Strengths: Curated luxury deals, member exclusivity, strong brand
- Weaknesses: Manual filtering, no personalization, single-destination only
- Our Edge: Conversational discovery, multi-destination planning, voice

**Zlavomat:**
- Strengths: Broad deal categories, local market knowledge
- Weaknesses: Overwhelming choice, generic UI, no travel intelligence
- Our Edge: AI-curated recommendations, distance-aware, itinerary building

**Traditional OTAs (Booking.com, Expedia):**
- Strengths: Comprehensive inventory, established trust
- Weaknesses: Filter fatigue, no conversational interface, transaction-focused
- Our Edge: Consultative experience, proactive recommendations, voice

### References

- Azure OpenAI Realtime API: https://learn.microsoft.com/azure/ai-services/openai/realtime-audio
- Travel Industry Trends 2025: [Market Research]
- Conversational Commerce Study: [User Research]
