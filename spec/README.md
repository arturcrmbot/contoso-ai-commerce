# AI Travel Agent - Specification Documents

## Overview

This folder contains the complete specification for transforming the Vodafone Three AI Commerce platform into an AI-powered conversational travel agent.

## Documents

### Strategic Planning
- **[TRANSFORMATION_PLAN.md](./TRANSFORMATION_PLAN.md)** - High-level roadmap, what changes, what stays, timeline ⭐ **START HERE**
- **[PRD.md](./PRD.md)** - Product requirements, user stories, success metrics
- **[architecture.md](./architecture.md)** - Technical architecture, system design
- **[improvements.md](./improvements.md)** - Current codebase optimization recommendations

### Technical Specs
- **[frontend.md](./frontend.md)** - Frontend architecture, component structure, React setup
- **[backend.md](./backend.md)** - Backend architecture, FastAPI structure, tool system

### Feature Requirements (FRDs)
- **[features/deal-search.md](./features/deal-search.md)** - Search tools, data model changes
- **[features/itinerary-planning.md](./features/itinerary-planning.md)** - Multi-destination trip building
- **[features/map-geospatial.md](./features/map-geospatial.md)** - Map integration, distance intelligence
- **[features/cart-checkout.md](./features/cart-checkout.md)** - Cart adaptation for travel items
- **[features/personalization.md](./features/personalization.md)** - User preferences, recommendations
- **[features/system-prompt.md](./features/system-prompt.md)** - AI conversation design, personality shift

## Quick Start

1. Read **TRANSFORMATION_PLAN.md** for the 3-4 week roadmap
2. Review individual FRDs for each major feature
3. Reference architecture docs when implementing

## Key Decisions

### What We're Keeping
- Azure OpenAI Realtime API + WebRTC (voice)
- FastAPI backend + React frontend
- Tool-calling architecture
- Dynamic visual canvas system
- Docker deployment

### What We're Replacing
- Product catalog (phones → travel deals)
- 29 tools (device search → travel search)
- Customer profiles (telecom usage → travel preferences)
- System prompt (phone sales → travel advisory)
- UI components (ProductCard → DealCard)

### What We're Adding
- Geospatial intelligence (distance, flight time)
- Multi-destination itinerary planning
- Interactive map view
- Date flexibility + calendar heatmap
- Travel-specific data models

## Timeline

**Phase 1 (Weeks 1-4):** Core transformation - data, search, itineraries, map
**Phase 2 (Weeks 5-6):** Intelligence, personalization, polish
**Total:** 3-4 weeks for MVP with 1-2 developers

## Success Criteria

- Search deals by destination, budget, dates
- AI builds multi-destination itineraries
- Map shows deals with distance from user
- Voice conversation works end-to-end
- 10+ test users complete mock bookings
- Mobile responsive

---

**Last Updated:** January 2025
**Version:** 1.0
