# Contoso Bet - AI Football Betting Assistant

Azure OpenAI Realtime-powered betting assistant that combines voice and chat to help customers discover football matches, build accumulators, and place bets responsibly. The AI proactively suggests complementary bets while displaying live odds and matches visually.

**Originally:** E-commerce phone sales assistant
**Transformed to:** Football betting consultant with responsible gambling controls

**Based on:** [gpt-realtime-agents](https://github.com/samelhousseini/gpt-realtime-agents) by samelhousseini

---

## 🎯 What Makes This Special

### Proactive Bet Building
Unlike passive betting interfaces, this AI **actively guides** bet slip construction:
- After you add a bet, AI immediately suggests complementary matches
- Calculates combined odds in real-time ("Add Man City for 3.57x odds!")
- Builds accumulators conversationally through natural dialogue
- Shows suggestions visually on screen, not just verbally

### Responsible Gambling Built-In
- **Mandatory budget checkpoint** at 3+ bets in slip
- Betting limits tracked and enforced
- Age verification required (18+)
- Risk warnings for high-stake accumulators
- Stops suggesting at 4+ legs to prevent excessive risk

### Conversational Flow Example
```
User: "Bet on Arsenal to win"
AI: [Adds to slip] → [Searches Premier League matches] → SHOWS them visually
    "Arsenal at 2.10 is in! I'm showing other Premier League matches -
     Man City are favorites at 1.85. Combine for 3.57x odds?"

User: "Add Man City"
AI: [Adds] → [Calculates slip] → [Shows more matches]
    "Two selections, 4.83x odds! Chelsea plays later at 2.20 -
     that makes it 10.63x (£106 on £10). Want it?"

User: "Add Chelsea"
AI: "Three bets! Before I suggest more - what's your budget today?
    Want to bet responsibly."

User: "£20 total"
AI: "Got it. Your slip is £10 stake. Ready to place this 3-leg acca?"
```

---

## 🏗️ Architecture

- **Backend:** FastAPI serving API endpoints and static frontend
- **Frontend:** React 19 + Vite single-page application
- **AI:** Azure OpenAI Realtime API with function calling (21 betting tools)
- **Real-time:** WebRTC for voice/text conversation
- **Deployment:** Docker container (frontend + backend bundled)

---

## ⚡ Key Features

### Betting Features
- **8 Mock Football Events:** Premier League, Champions League, La Liga, Bundesliga, Serie A
- **10 Bet Types:** Match Result, Over/Under, BTTS, Double Chance, Accumulators, First Goalscorer, etc.
- **21 Betting Tools:** Search events, get odds, calculate returns, place bets, cash out, etc.
- **Live Match Support:** In-play betting with real-time odds
- **Accumulator Builder:** Proactive suggestions for multi-leg bets
- **Player Props:** Goalscorer markets with odds

### Conversational AI
- **Voice & Text:** Speak or type naturally
- **Visual Display:** Matches, odds, bet slip shown on left panel (70% width)
- **Proactive Suggestions:** AI recommends bets after each addition
- **Context Tracking:** Remembers if you added AI's suggestion vs your own choice
- **Odds Calculation:** Real-time combined odds for accumulators

### Responsible Gambling
- **Age Verification:** Must be 18+ to bet
- **Betting Limits:** Daily/weekly/monthly limits enforced
- **Budget Checkpoints:** Mandatory at 3+ bets in slip
- **Risk Warnings:** Clear communication about accumulator risk
- **Cash Out:** Early settlement option for active bets
- **Betting History:** Track wins, losses, patterns

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 20+
- Docker (for containerized deployment)
- Azure OpenAI Realtime API access

### 1. Configure Environment

```bash
cp .env.sample .env
```

Edit `.env` with your Azure OpenAI credentials:
```env
AZURE_GPT_REALTIME_URL=https://<resource>.openai.azure.com/openai/realtimeapi/sessions?api-version=2025-04-01-preview
WEBRTC_URL=https://<region>.realtimeapi-preview.ai.azure.com/v1/realtimertc
AZURE_GPT_REALTIME_KEY=<your-key>
AZURE_GPT_REALTIME_DEPLOYMENT=gpt-realtime-2
AZURE_GPT_REALTIME_VOICE=verse
```

### 2. Install Dependencies

**Using uv (recommended):**
```bash
uv venv
uv pip install -e .
```

**Using pip:**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e .
```

### 3. Build Frontend

```bash
cd frontend
npm ci
npm run build
cd ..
```

### 4. Copy Frontend to Backend

```bash
rm -rf audio_backend/frontend_dist
cp -r frontend/dist audio_backend/frontend_dist
```

### 5. Run Backend

```bash
uv run uvicorn audio_backend.backend:app --host 0.0.0.0 --port 8080
```

### 6. Access Application

Open browser to: **http://localhost:8080**

---

## 🐳 Docker Deployment

### Build and Run Locally

```bash
docker build -t contoso-bet .
docker run -p 8080:8080 --env-file .env contoso-bet
```

Access at `http://localhost:8080`

### Deploy to Azure Container Apps

See `deploy/README.md` for Azure deployment instructions.

---

## 🎮 How to Use

### Starting a Session
1. Open the application in your browser
2. Click "Start Session" to begin
3. Choose from suggestion cards or ask naturally:
   - "What Premier League matches are on this weekend?"
   - "Show me live matches now"
   - "Help me build an accumulator"

### Building Your Bet Slip
1. **Ask about matches:** "Show me Arsenal matches"
2. **Get details:** "Tell me about Arsenal vs Chelsea"
3. **Add to slip:** "Put £10 on Arsenal to win"
4. **AI suggests next bet:** Shows complementary matches with combined odds
5. **Build accumulator:** Keep adding as AI guides you
6. **Place bet:** Confirm and place when ready

### Responsible Gambling
- Set your budget when asked (at 3+ bets)
- Check betting limits anytime: "What's my daily limit?"
- View betting history: "Show my betting stats"
- Cash out early: "What's the cash out value for bet CB-123456?"

---

## 🔧 API Endpoints

- `POST /api/session` - Create ephemeral WebRTC session with Azure OpenAI
- `GET /api/tools` - List available function tools (21 betting tools)
- `POST /api/function-call` - Execute function and return result
- `GET /healthz` - Health check
- `GET /runtime-config.js` - Runtime configuration for frontend
- `GET /` - Serve React frontend

---

## 🛠️ Project Structure

```
gpt-realtime-agents/
├── audio_backend/                 # FastAPI backend
│   ├── backend.py                # Main application (294 lines)
│   ├── tools_registry.py         # 21 betting tools (1,784 lines)
│   ├── backend_acs.py            # Optional PSTN integration
│   ├── acs/                      # Azure Communication Services
│   └── frontend_dist/            # Built frontend (auto-generated)
│
├── frontend/                      # React application
│   ├── src/
│   │   ├── components/
│   │   │   ├── contoso/         # Business components
│   │   │   │   ├── DynamicVisualCanvas.tsx
│   │   │   │   ├── ProductShowcase.tsx
│   │   │   │   ├── CartIcon.tsx
│   │   │   │   └── CartSummary.tsx
│   │   │   ├── visual-primitives/  # Flexible visual system
│   │   │   │   ├── FlexibleRenderer.tsx
│   │   │   │   ├── ProductHero.tsx
│   │   │   │   ├── PriceBreakdown.tsx
│   │   │   │   └── types.ts
│   │   │   ├── ui/              # Shadcn UI components
│   │   │   ├── CallControls.tsx
│   │   │   ├── ChatComposer.tsx
│   │   │   ├── MessageBubble.tsx
│   │   │   └── SuggestionCards.tsx
│   │   ├── hooks/
│   │   │   └── use-realtime-session.ts  # WebRTC logic
│   │   ├── lib/
│   │   │   ├── constants.ts     # System prompt, suggestions
│   │   │   ├── types.ts         # TypeScript interfaces
│   │   │   └── utils.ts
│   │   ├── App.tsx              # Root component (70/30 split)
│   │   └── main.tsx             # Entry point
│   ├── package.json             # 70+ dependencies
│   └── vite.config.ts
│
├── prompts/
│   └── system_prompt.txt        # 330+ line betting consultant guide
│
├── deploy/                       # Azure deployment
│   ├── main.bicep               # Infrastructure as Code
│   ├── deploy-all-fixed.ps1     # Deployment scripts
│   └── README.md
│
├── Dockerfile                    # Multi-stage Docker build
├── .env.sample                   # Environment template
├── pyproject.toml                # Python dependencies
└── README.md                     # This file
```

---

## 📊 Mock Data Catalogs

### 8 Football Events
- **Premier League:** Arsenal vs Chelsea, Man City vs Liverpool, Man Utd vs Tottenham, Newcastle vs Aston Villa (live)
- **La Liga:** Real Madrid vs Barcelona
- **Bundesliga:** Bayern Munich vs Borussia Dortmund
- **Serie A:** Juventus vs Inter Milan
- **Champions League:** PSG vs Bayern Munich

Each event includes:
- Kick-off time, venue, status
- Match odds (home/draw/away, over/under, BTTS, double chance)
- Team form (last 5 results)
- Head-to-head stats
- Player odds (goalscorer markets)

### 10 Bet Types
1. **Match Result (1X2)** - Home/Draw/Away
2. **Over/Under Goals** - Total goals over/under 2.5
3. **Both Teams to Score (BTTS)** - Yes/No
4. **Double Chance** - Two outcomes covered
5. **Correct Score** - Exact final score (high risk)
6. **First Goalscorer** - Player to score first
7. **Anytime Goalscorer** - Player scores anytime
8. **Half-Time/Full-Time** - HT and FT results
9. **Asian Handicap** - Virtual advantage/disadvantage
10. **Accumulator/Parlay** - Multiple bets combined

### Bonus Codes
- `WELCOME50` - £50 free bet for new customers
- `ACCA10` - 10% odds boost on accumulators
- `CASHBACK20` - 20% cashback on losses (up to £20)
- `DOUBLE` - Double winnings on first bet

---

## 🧠 AI System Prompt Logic

### Proactive Suggestion Flow

**After EVERY `add_to_bet_slip()` success:**

#### 1 bet in slip:
- Call `search_events()` to find complementary matches
- OR call `get_related_bets()` for same event
- SHOW 2-3 options visually
- Calculate combined odds
- Example: "Arsenal at 2.10 is in! Man City at 1.85 combines for 3.57x"

#### 2-3 bets in slip:
- Call `get_bet_slip_summary()` for current odds
- Call `search_events()` for one more match
- SHOW suggestions visually
- Example: "You're at 5.2x odds. Liverpool at 1.90 pushes to 9.88x (£98 on £10)"

#### 3+ bets (CHECKPOINT):
- **MANDATORY:** Ask "What's your budget today?"
- Call `check_betting_limits()`
- Suggest ONE more bet maximum if under budget
- Example: "Before I suggest more, what's your budget? Let's bet responsibly."

#### 4+ bets:
- STOP suggesting more bets
- Warn about risk: "4-leg acca - all must win. High odds but risky."
- Guide to placement: "Ready to place this bet?"

### Context Tracking
- If user added **AI's suggestion** → Don't suggest again (user is driving)
- If user added **their own choice** → Immediately suggest complementary bets

---

## 🎲 Betting Tools (21 Total)

### Event Discovery (8 tools)
- `search_events` - Find matches by league, team, date, status
- `get_event_details` - Complete match info with odds and stats
- `compare_odds` - Compare odds across multiple matches
- `get_similar_events` - Find similar matches
- `recommend_bet_types` - Suggest bets based on risk appetite
- `get_related_bets` - Accumulator combo suggestions
- `calculate_bet_returns` - Calculate potential returns and profit
- `check_event_status` - Check if betting is available

### Customer & Account (5 tools)
- `check_betting_limits` - View daily/weekly/monthly limits
- `get_betting_history` - Win rate, profit/loss, statistics
- `verify_age_identity` - Age verification (18+ required)
- `check_account_balance` - Available funds
- `check_cashout_value` - Early settlement value

### Bet Slip Management (5 tools)
- `add_to_bet_slip` - Add selection to slip
- `remove_from_bet_slip` - Remove selection
- `get_bet_slip_summary` - Current slip with returns
- `apply_bonus` - Apply promo code
- `place_bet` - Confirm and place bet

### Support & Engagement (3 tools)
- `get_available_markets` - Browse all bet types
- `get_active_promotions` - Current offers and bonuses
- `transfer_to_human_agent` - Escalate to specialist
- `send_bet_confirmation` - Email bet confirmation
- `customise_webpage` - Custom visual layouts

---

## 📝 How We Built This

### Transformation Process

This started as an **e-commerce phone sales assistant** and was transformed into a **betting platform** through systematic domain mapping:

#### 1. Data Model Transformation
```
E-commerce → Betting
------------------
Devices     → Football Events (matches)
Plans       → Bet Types (match result, over/under, etc.)
Accessories → Bet Modifiers (related bets, combos)
Cart        → Bet Slip
Checkout    → Place Bet
```

#### 2. Tool Transformation (29 → 21 tools)
```
search_devices_by_attributes → search_events
get_device_details           → get_event_details
compare_devices              → compare_odds
get_customer_usage           → get_betting_history
check_upgrade_eligibility    → check_betting_limits
run_credit_check             → verify_age_identity
add_to_cart                  → add_to_bet_slip
process_payment              → place_bet
check_trade_in_value         → check_cashout_value
```

#### 3. System Prompt Rewrite
**Before (E-commerce):**
- "Consultative selling: DISCOVER → RECOMMEND → CONFIGURE → CLOSE"
- Focus on device features, plans, accessories
- Credit checks and delivery

**After (Betting):**
- "Betting consultation: DISCOVER → INFORM → RECOMMEND → EXPLAIN → CONFIRM"
- Focus on odds, risk, responsible gambling
- Age verification and betting limits

#### 4. Proactive Logic Addition
**New behavior not in original:**
- After every `add_to_bet_slip()`, AI proactively suggests complementary bets
- Slip size-based suggestion strategy (1, 2-3, 3+, 4+ bets)
- Mandatory responsible gambling checkpoints
- Real-time odds calculation and risk warnings

#### 5. Frontend Updates
- Updated suggestion cards (Premier League, Live Matches, Build Accumulator)
- Changed welcome message: "Welcome to Contoso Bet"
- Cart → Bet Slip terminology throughout
- Visual display still uses same flexible renderer (works for both domains!)

### Key Design Decisions

1. **Generic tools over specific ones**
   - Instead of `suggest_next_bet_for_slip()`, use `search_events()` + AI logic
   - Let AI figure out strategy rather than hardcoding tool behavior
   - More flexible, easier to maintain

2. **Visual-first approach maintained**
   - After tool calls, always SHOW results on screen
   - Don't just describe verbally - display matches, odds, slip visually
   - Leverages existing flexible visual system from e-commerce version

3. **Responsible gambling as first-class feature**
   - Not an afterthought - built into core conversation flow
   - Mandatory checkpoints at 3+ bets
   - Age verification required before any betting
   - Clear risk communication throughout

4. **Context tracking without state management**
   - Rely on AI's conversation memory to track if last bet was a suggestion
   - No complex state management needed
   - Simpler architecture, more maintainable

---

## 🔍 Example Conversations

### Beginner User - Learning to Bet
```
User: "I'm new to betting. Can you help?"
AI: [Shows bet types] "Absolutely! I'm showing you the main bet types.
    The simplest is Match Result - just pick who wins. Let me show
    you today's matches..."
AI: [Shows Premier League matches] "Arsenal vs Chelsea looks good.
    Arsenal are favorites at 2.10 - that means £10 becomes £21 if
    they win. Want to try?"
```

### Experienced User - Building Accumulator
```
User: "Show me Premier League matches"
AI: [Shows 4 matches] "Here are this weekend's fixtures..."

User: "I like Arsenal to win"
AI: [Adds to slip] [Shows more matches] "Arsenal at 2.10 is in!
    Man City play later at 1.85. Combine for 3.57x odds?"

User: "Add Man City"
AI: [Adds] [Shows more] "Two selections, 4.83x odds. Chelsea at 2.20
    makes it 10.63x (£106 on £10). Interested?"

User: "Add Chelsea"
AI: "Three bets! What's your budget today? Let's bet responsibly."

User: "£20"
AI: [Checks limits] "Perfect. Your slip is £10 stake, 10.63x odds.
    Ready to place?"

User: "Yes"
AI: [Places bet] "Bet placed! CB-789456. Good luck - all three need
    to win for £106 return!"
```

### Live Betting
```
User: "What's live now?"
AI: [Shows live match] "Newcastle vs Aston Villa is 1-1 in the 67th
    minute. Live odds: Newcastle 2.20, Draw 3.20, Aston Villa 3.30.
    Over 2.5 goals is 1.75. What interests you?"

User: "Both teams to score"
AI: "BTTS Yes is 1.62 - likely given both have scored. Want it?"
```

---

## 🧪 Testing Locally

### Manual Test Scenarios

1. **Proactive Suggestion Flow**
   - Add Arsenal to win → Does AI suggest Man City?
   - Add Man City → Does AI calculate combined odds correctly?
   - Add 3rd bet → Does AI ask about budget?

2. **Responsible Gambling**
   - Try adding 4+ bets → Does AI stop suggesting and warn about risk?
   - Ask "What's my daily limit?" → Does it call `check_betting_limits()`?

3. **Context Tracking**
   - User adds AI's suggestion → Does AI stop suggesting immediately after?
   - User adds own choice → Does AI resume suggestions?

4. **Visual Display**
   - After `search_events()` → Are matches shown on left panel?
   - After `add_to_bet_slip()` → Does bet slip appear?
   - After `place_bet()` → Is confirmation shown with bet ID?

5. **Age Verification**
   - Try placing bet without verification → Does it require age check?
   - Provide DOB under 18 → Does it reject?

---

## 🐛 Troubleshooting

### "Module not found" errors
```bash
pip install -e .
```

### Frontend not updating
```bash
cd frontend
npm run build
cd ..
rm -rf audio_backend/frontend_dist
cp -r frontend/dist audio_backend/frontend_dist
```

### Docker build fails
- Ensure Docker Desktop is running
- Check `.env` file exists with Azure credentials
- Try: `docker build --no-cache -t contoso-bet .`

### WebRTC connection fails
- Check `WEBRTC_URL` is correct for your region
- Verify `AZURE_GPT_REALTIME_KEY` is valid
- Ensure deployment name matches `AZURE_GPT_REALTIME_DEPLOYMENT`

### AI not following proactive suggestions
- Check `prompts/system_prompt.txt` was updated
- Rebuild frontend and restart backend
- Verify `constants.ts` has updated SYSTEM_PROMPT

### Tools not working
- Check `audio_backend/tools_registry.py` has betting tools
- Verify tool names match between prompt and registry
- Look at backend console logs for tool execution errors

---

## 📈 Future Enhancements

### Potential Additions
- **More sports:** Basketball, tennis, cricket betting
- **Live odds updates:** Real-time odds changes during matches
- **Betting strategies:** Suggest betting systems (Martingale, Kelly Criterion)
- **Social betting:** Share bet slips with friends
- **Statistics dashboard:** Win rate trends, profit charts
- **Cash out automation:** Auto cash out at specified thresholds
- **Multi-currency support:** Beyond GBP
- **Bet builder:** More complex custom bets (e.g., "Arsenal to win + Saka to score + Over 2.5")

### Architecture Improvements
- **Persistent bet slip:** Save to database instead of in-memory
- **User accounts:** Authentication and profile management
- **Real odds API:** Integrate with actual bookmaker APIs
- **Bet tracking:** Automatic settlement when matches finish
- **Push notifications:** Alert when matches start or odds change significantly

---

## 🙏 Credits

### Original Project
Based on [gpt-realtime-agents](https://github.com/samelhousseini/gpt-realtime-agents) by [samelhousseini](https://github.com/samelhousseini) - an incredible foundation for building AI-powered sales assistants.

### Transformation
E-commerce → Betting platform transformation demonstrates how the architecture can be adapted to any consultative domain where:
- AI guides users through complex decisions
- Visual display enhances understanding
- Function calling enables real actions
- Natural conversation feels human-like

### Technology Stack
- Azure OpenAI Realtime API
- React 19 + Vite
- FastAPI (Python)
- WebRTC for real-time communication
- Radix UI + Tailwind CSS

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

## ⚠️ Disclaimer

This is a **demonstration/prototype** built for educational purposes. It uses:
- Mock football events and odds (not real betting data)
- Simulated betting transactions (no real money involved)
- Mock age verification (90% approval rate)
- In-memory bet slip (lost on restart)

**For production betting platform:**
- Integrate real sportsbook APIs
- Implement actual payment processing
- Use production-grade KYC/age verification
- Add comprehensive responsible gambling controls
- Comply with gambling regulations (UK Gambling Commission, etc.)
- Implement fraud detection and prevention
- Add proper audit logging and compliance reporting

**Gambling should be treated responsibly. Never bet more than you can afford to lose.**

---

## 📞 Support

For questions or issues:
- Open an issue on GitHub
- Check Azure OpenAI Realtime API documentation
- Review `deploy/README.md` for deployment help

**Built with:** ❤️ and Azure OpenAI Realtime API
