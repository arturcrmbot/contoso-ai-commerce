import random
import asyncio
from datetime import datetime, timedelta
from typing import Any, Dict, List

# =============================================================================
# MOCK DATA CATALOGS - FOOTBALL BETTING
# =============================================================================

MOCK_EVENTS = [
    {
        "id": "epl-arsenal-chelsea",
        "sport": "Football",
        "league": "Premier League",
        "home_team": "Arsenal",
        "away_team": "Chelsea",
        "kick_off": (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d %H:%M"),
        "venue": "Emirates Stadium",
        "status": "upcoming",
        "odds": {
            "match_result": {"home": 2.10, "draw": 3.40, "away": 3.60},
            "over_under": {"over_2_5": 1.85, "under_2_5": 1.95},
            "both_teams_score": {"yes": 1.70, "no": 2.10},
            "double_chance": {"home_draw": 1.30, "home_away": 1.40, "draw_away": 1.80}
        },
        "form": {"home": "WWDWL", "away": "LDWDW"},
        "head_to_head": "Last 5: Arsenal 2 wins, Chelsea 2 wins, 1 draw"
    },
    {
        "id": "epl-man-city-liverpool",
        "sport": "Football",
        "league": "Premier League",
        "home_team": "Manchester City",
        "away_team": "Liverpool",
        "kick_off": (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d %H:%M"),
        "venue": "Etihad Stadium",
        "status": "upcoming",
        "odds": {
            "match_result": {"home": 2.30, "draw": 3.20, "away": 3.10},
            "over_under": {"over_2_5": 1.65, "under_2_5": 2.20},
            "both_teams_score": {"yes": 1.55, "no": 2.40},
            "double_chance": {"home_draw": 1.35, "home_away": 1.45, "draw_away": 1.70}
        },
        "form": {"home": "WWWWW", "away": "WWDWW"},
        "head_to_head": "Last 5: Man City 3 wins, Liverpool 1 win, 1 draw"
    },
    {
        "id": "epl-man-utd-tottenham",
        "sport": "Football",
        "league": "Premier League",
        "home_team": "Manchester United",
        "away_team": "Tottenham",
        "kick_off": (datetime.now() + timedelta(days=4)).strftime("%Y-%m-%d %H:%M"),
        "venue": "Old Trafford",
        "status": "upcoming",
        "odds": {
            "match_result": {"home": 2.50, "draw": 3.30, "away": 2.80},
            "over_under": {"over_2_5": 1.90, "under_2_5": 1.90},
            "both_teams_score": {"yes": 1.65, "no": 2.20},
            "double_chance": {"home_draw": 1.45, "home_away": 1.50, "draw_away": 1.60}
        },
        "form": {"home": "WDLWD", "away": "WWLWD"},
        "head_to_head": "Last 5: Man Utd 2 wins, Tottenham 2 wins, 1 draw"
    },
    {
        "id": "laliga-real-madrid-barcelona",
        "sport": "Football",
        "league": "La Liga",
        "home_team": "Real Madrid",
        "away_team": "Barcelona",
        "kick_off": (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d %H:%M"),
        "venue": "Santiago Bernabéu",
        "status": "upcoming",
        "odds": {
            "match_result": {"home": 2.40, "draw": 3.10, "away": 3.00},
            "over_under": {"over_2_5": 1.80, "under_2_5": 2.00},
            "both_teams_score": {"yes": 1.60, "no": 2.30},
            "double_chance": {"home_draw": 1.40, "home_away": 1.45, "draw_away": 1.75}
        },
        "form": {"home": "WWWDW", "away": "WWWLW"},
        "head_to_head": "Last 5: Real Madrid 2 wins, Barcelona 2 wins, 1 draw"
    },
    {
        "id": "bundesliga-bayern-dortmund",
        "sport": "Football",
        "league": "Bundesliga",
        "home_team": "Bayern Munich",
        "away_team": "Borussia Dortmund",
        "kick_off": (datetime.now() + timedelta(days=6)).strftime("%Y-%m-%d %H:%M"),
        "venue": "Allianz Arena",
        "status": "upcoming",
        "odds": {
            "match_result": {"home": 1.85, "draw": 3.60, "away": 4.20},
            "over_under": {"over_2_5": 1.70, "under_2_5": 2.10},
            "both_teams_score": {"yes": 1.65, "no": 2.20},
            "double_chance": {"home_draw": 1.25, "home_away": 1.30, "draw_away": 1.95}
        },
        "form": {"home": "WWWWW", "away": "WWDLD"},
        "head_to_head": "Last 5: Bayern 4 wins, Dortmund 1 win"
    },
    {
        "id": "seriea-juventus-inter",
        "sport": "Football",
        "league": "Serie A",
        "home_team": "Juventus",
        "away_team": "Inter Milan",
        "kick_off": (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d %H:%M"),
        "venue": "Allianz Stadium",
        "status": "upcoming",
        "odds": {
            "match_result": {"home": 2.60, "draw": 3.00, "away": 2.80},
            "over_under": {"over_2_5": 2.00, "under_2_5": 1.80},
            "both_teams_score": {"yes": 1.75, "no": 2.05},
            "double_chance": {"home_draw": 1.50, "home_away": 1.55, "draw_away": 1.55}
        },
        "form": {"home": "WDWDW", "away": "WWWDL"},
        "head_to_head": "Last 5: Juventus 2 wins, Inter 2 wins, 1 draw"
    },
    {
        "id": "epl-newcastle-aston-villa",
        "sport": "Football",
        "league": "Premier League",
        "home_team": "Newcastle",
        "away_team": "Aston Villa",
        "kick_off": (datetime.now() + timedelta(hours=6)).strftime("%Y-%m-%d %H:%M"),
        "venue": "St James' Park",
        "status": "live",
        "live_score": {"home": 1, "away": 1, "minute": 67},
        "odds": {
            "match_result": {"home": 2.20, "draw": 3.20, "away": 3.30},
            "over_under": {"over_2_5": 1.75, "under_2_5": 2.05},
            "both_teams_score": {"yes": 1.62, "no": 2.25}
        },
        "form": {"home": "WWDLW", "away": "DWWDL"},
        "head_to_head": "Last 5: Newcastle 3 wins, Aston Villa 1 win, 1 draw"
    },
    {
        "id": "champions-league-psg-bayern",
        "sport": "Football",
        "league": "Champions League",
        "home_team": "PSG",
        "away_team": "Bayern Munich",
        "kick_off": (datetime.now() + timedelta(days=8)).strftime("%Y-%m-%d %H:%M"),
        "venue": "Parc des Princes",
        "status": "upcoming",
        "odds": {
            "match_result": {"home": 2.70, "draw": 3.20, "away": 2.60},
            "over_under": {"over_2_5": 1.75, "under_2_5": 2.05},
            "both_teams_score": {"yes": 1.58, "no": 2.35},
            "double_chance": {"home_draw": 1.50, "home_away": 1.50, "draw_away": 1.55}
        },
        "form": {"home": "WWWDW", "away": "WWWWW"},
        "head_to_head": "Last 5: PSG 1 win, Bayern 3 wins, 1 draw"
    }
]

MOCK_BET_TYPES = [
    {
        "id": "match-result",
        "name": "Match Result",
        "description": "Predict the final result: Home win, Draw, or Away win",
        "category": "main",
        "popularity": "high",
        "risk_level": "medium"
    },
    {
        "id": "over-under",
        "name": "Over/Under Goals",
        "description": "Bet on whether total goals will be over or under a specific number (usually 2.5)",
        "category": "main",
        "popularity": "high",
        "risk_level": "medium"
    },
    {
        "id": "both-teams-score",
        "name": "Both Teams to Score",
        "description": "Will both teams score at least one goal?",
        "category": "main",
        "popularity": "high",
        "risk_level": "medium"
    },
    {
        "id": "double-chance",
        "name": "Double Chance",
        "description": "Cover two of three possible outcomes (Home/Draw, Home/Away, Draw/Away)",
        "category": "main",
        "popularity": "medium",
        "risk_level": "low"
    },
    {
        "id": "correct-score",
        "name": "Correct Score",
        "description": "Predict the exact final score",
        "category": "advanced",
        "popularity": "medium",
        "risk_level": "high"
    },
    {
        "id": "first-goalscorer",
        "name": "First Goalscorer",
        "description": "Which player will score the first goal",
        "category": "player",
        "popularity": "high",
        "risk_level": "high"
    },
    {
        "id": "anytime-goalscorer",
        "name": "Anytime Goalscorer",
        "description": "Which player will score at any time during the match",
        "category": "player",
        "popularity": "high",
        "risk_level": "medium"
    },
    {
        "id": "half-time-full-time",
        "name": "Half Time/Full Time",
        "description": "Predict result at half-time and full-time",
        "category": "advanced",
        "popularity": "low",
        "risk_level": "high"
    },
    {
        "id": "asian-handicap",
        "name": "Asian Handicap",
        "description": "Level the playing field by giving virtual advantage/disadvantage",
        "category": "advanced",
        "popularity": "medium",
        "risk_level": "medium"
    },
    {
        "id": "accumulator",
        "name": "Accumulator/Parlay",
        "description": "Combine multiple bets - all must win for payout",
        "category": "combo",
        "popularity": "very_high",
        "risk_level": "high"
    }
]

MOCK_MARKETS = {
    "match_result": ["Home Win", "Draw", "Away Win"],
    "over_under": ["Over 0.5", "Over 1.5", "Over 2.5", "Over 3.5", "Under 0.5", "Under 1.5", "Under 2.5", "Under 3.5"],
    "both_teams_score": ["Yes", "No"],
    "double_chance": ["Home or Draw", "Home or Away", "Draw or Away"],
    "correct_score": ["0-0", "1-0", "1-1", "2-0", "2-1", "2-2", "3-0", "3-1", "3-2", "Other"],
    "halftime_result": ["Home", "Draw", "Away"]
}

MOCK_PLAYERS = {
    "Arsenal": ["Bukayo Saka", "Gabriel Jesus", "Martin Ødegaard", "Leandro Trossard"],
    "Chelsea": ["Cole Palmer", "Nicolas Jackson", "Raheem Sterling", "Christopher Nkunku"],
    "Manchester City": ["Erling Haaland", "Phil Foden", "Kevin De Bruyne", "Julian Alvarez"],
    "Liverpool": ["Mohamed Salah", "Darwin Núñez", "Luis Díaz", "Cody Gakpo"],
    "Manchester United": ["Marcus Rashford", "Bruno Fernandes", "Rasmus Højlund", "Alejandro Garnacho"],
    "Tottenham": ["Son Heung-min", "Richarlison", "Dejan Kulusevski", "James Maddison"],
    "Real Madrid": ["Vinícius Júnior", "Jude Bellingham", "Rodrygo", "Joselu"],
    "Barcelona": ["Robert Lewandowski", "Raphinha", "Ferran Torres", "João Félix"],
    "Bayern Munich": ["Harry Kane", "Jamal Musiala", "Leroy Sané", "Thomas Müller"],
    "Borussia Dortmund": ["Donyell Malen", "Karim Adeyemi", "Niclas Füllkrug", "Marco Reus"],
    "default": ["Player A", "Player B", "Player C"]
}

# Bet slip (in-memory - will be lost on restart)
BET_SLIP = {}

# =============================================================================
# CONTOSO BET TOOLS
# =============================================================================

async def search_events(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Search for football events/matches based on criteria."""
    league = arguments.get("league")
    team = arguments.get("team")
    date_range = arguments.get("date_range", "upcoming")  # "today", "tomorrow", "week", "upcoming"
    status = arguments.get("status", "upcoming")  # "upcoming", "live", "all"

    filtered_events = []
    for event in MOCK_EVENTS:
        # Status filter
        if status != "all" and event["status"] != status:
            continue

        # League filter
        if league and league.lower() not in event["league"].lower():
            continue

        # Team filter
        if team:
            team_lower = team.lower()
            if (team_lower not in event["home_team"].lower() and
                team_lower not in event["away_team"].lower()):
                continue

        filtered_events.append(event)

    # Sort by kick-off time
    filtered_events.sort(key=lambda e: e.get("kick_off", ""))

    title = "Upcoming Matches" if status == "upcoming" else "Live Matches" if status == "live" else "Football Matches"

    return {
        "events": filtered_events[:10],
        "count": len(filtered_events),
        "filters_applied": {"league": league, "team": team, "status": status},
        "_visual": {
            "layout": "flow",
            "header": {
                "title": title,
                "subtitle": f"Found {len(filtered_events)} matches"
            },
            "sections": [
                {
                    "type": "match_grid",
                    "title": title,
                    "subtitle": f"Found {len(filtered_events)} matches",
                    "data": {
                        "matches": [
                            {
                                "id": e["id"],
                                "home_team": e["home_team"],
                                "away_team": e["away_team"],
                                "league": e["league"],
                                "kick_off": e.get("kick_off", "TBD"),
                                "venue": e.get("venue", ""),
                                "status": e.get("status", "upcoming"),
                                "odds": {
                                    "home": e["odds"]["match_result"]["home"],
                                    "draw": e["odds"]["match_result"]["draw"],
                                    "away": e["odds"]["match_result"]["away"]
                                },
                                "live_score": e.get("live_score")
                            }
                            for e in filtered_events[:10]
                        ]
                    }
                }
            ]
        }
    }


async def get_event_details(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Get complete details for a specific match including odds and stats."""
    event_id = arguments.get("event_id")

    event = next((e for e in MOCK_EVENTS if e["id"] == event_id), None)
    if not event:
        return {"error": "Event not found"}

    # Get players for both teams
    home_players = MOCK_PLAYERS.get(event["home_team"], MOCK_PLAYERS["default"])
    away_players = MOCK_PLAYERS.get(event["away_team"], MOCK_PLAYERS["default"])

    # Enhanced details
    enhanced_event = {
        **event,
        "description": f"{event['home_team']} face {event['away_team']} at {event['venue']} in what promises to be an exciting {event['league']} clash.",
        "statistics": {
            "home_win_percentage": random.randint(35, 65),
            "draw_percentage": random.randint(20, 30),
            "away_win_percentage": random.randint(25, 45),
            "avg_goals_per_match": round(random.uniform(2.3, 3.2), 1)
        },
        "team_news": {
            "home": f"{event['home_team']} have no major injury concerns. Full squad available.",
            "away": f"{event['away_team']} will be without 1-2 key players but squad looking strong."
        },
        "top_goalscorers": {
            "home": home_players[0],
            "away": away_players[0]
        },
        "referee": random.choice(["Michael Oliver", "Anthony Taylor", "Paul Tierney", "Simon Hooper"]),
        "weather": random.choice(["Clear", "Partly cloudy", "Light rain expected"]),
        "player_odds": {
            "first_goalscorer": {
                home_players[0]: round(random.uniform(4.5, 7.5), 2),
                home_players[1]: round(random.uniform(6.0, 9.0), 2),
                away_players[0]: round(random.uniform(5.0, 8.0), 2),
                away_players[1]: round(random.uniform(6.5, 9.5), 2)
            },
            "anytime_goalscorer": {
                home_players[0]: round(random.uniform(2.2, 3.5), 2),
                home_players[1]: round(random.uniform(2.8, 4.2), 2),
                away_players[0]: round(random.uniform(2.5, 3.8), 2),
                away_players[1]: round(random.uniform(3.0, 4.5), 2)
            }
        }
    }

    return {
        **enhanced_event,
        "_visual": {
            "layout": "multi_section",
            "theme": "default",
            "sections": [
                {
                    "type": "product_hero",
                    "data": {
                        "name": f"{event['home_team']} vs {event['away_team']}",
                        "description": enhanced_event["description"],
                        "image_url": "https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=800&h=400&fit=crop",
                        "home_odds": event["odds"]["match_result"]["home"],
                        "attributes": {
                            "League": event["league"],
                            "Venue": event["venue"],
                            "Kick-off": event["kick_off"],
                            "Status": event["status"]
                        }
                    }
                },
                {
                    "type": "price_breakdown",
                    "title": "Match Odds",
                    "data": {
                        "items": [
                            {"label": f"{event['home_team']} Win", "amount": event["odds"]["match_result"]["home"], "type": "odds"},
                            {"label": "Draw", "amount": event["odds"]["match_result"]["draw"], "type": "odds"},
                            {"label": f"{event['away_team']} Win", "amount": event["odds"]["match_result"]["away"], "type": "odds"}
                        ]
                    }
                }
            ]
        }
    }


async def compare_odds(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Compare odds for multiple events or markets."""
    event_ids = arguments.get("event_ids", [])
    bet_type = arguments.get("bet_type", "match_result")

    events = [e for e in MOCK_EVENTS if e["id"] in event_ids]

    if not events:
        return {"error": "No events found"}

    comparison = {
        "events": events,
        "bet_type": bet_type,
        "odds_comparison": [],
        "_visual": {
            "type": "comparison_table",
            "title": f"Odds Comparison - {bet_type.replace('_', ' ').title()}",
            "devices": [
                {
                    "id": e["id"],
                    "name": f"{e['home_team']} vs {e['away_team']}",
                    "brand": e["league"],
                    "home_odds": e["odds"]["match_result"]["home"],
                    "attributes": {
                        "home_odds": e["odds"]["match_result"]["home"],
                        "draw_odds": e["odds"]["match_result"]["draw"],
                        "away_odds": e["odds"]["match_result"]["away"]
                    }
                }
                for e in events
            ]
        }
    }

    return comparison


async def get_similar_events(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Find similar matches (same league, same teams, similar odds)."""
    event_id = arguments.get("event_id")

    current = next((e for e in MOCK_EVENTS if e["id"] == event_id), None)
    if not current:
        return {"error": "Event not found"}

    # Find events in same league
    same_league = [e for e in MOCK_EVENTS if e["league"] == current["league"] and e["id"] != event_id]

    # Find events with same teams
    same_teams = [
        e for e in MOCK_EVENTS
        if (e["home_team"] in [current["home_team"], current["away_team"]] or
            e["away_team"] in [current["home_team"], current["away_team"]])
        and e["id"] != event_id
    ]

    all_similar = list({e["id"]: e for e in (same_league[:3] + same_teams[:2])}.values())

    return {
        "current_event": current,
        "similar_events": all_similar,
        "_visual": {
            "type": "product_grid",
            "title": f"Similar to {current['home_team']} vs {current['away_team']}",
            "items": [
                {
                    "id": e["id"],
                    "name": f"{e['home_team']} vs {e['away_team']}",
                    "brand": e["league"],
                    "home_odds": e["odds"]["match_result"]["home"],
                    "image_url": "https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=400&h=300&fit=crop"
                }
                for e in all_similar
            ]
        }
    }


async def recommend_bet_types(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Recommend bet types based on user preferences and risk appetite."""
    event_id = arguments.get("event_id")
    risk_level = arguments.get("risk_level", "medium")  # "low", "medium", "high"
    budget = arguments.get("budget", 20)

    event = next((e for e in MOCK_EVENTS if e["id"] == event_id), None)

    if not event:
        return {"error": "Event not found"}

    # Filter bet types by risk level
    suitable_bet_types = [bt for bt in MOCK_BET_TYPES if bt["risk_level"] == risk_level or risk_level == "all"]

    recommendations = []
    for bet_type in suitable_bet_types[:5]:
        potential_return = round(budget * random.uniform(1.5, 8.0), 2)
        recommendations.append({
            "bet_type": bet_type,
            "event": f"{event['home_team']} vs {event['away_team']}",
            "stake": budget,
            "potential_return": potential_return,
            "profit": round(potential_return - budget, 2)
        })

    return {
        "event_id": event_id,
        "event_name": f"{event['home_team']} vs {event['away_team']}",
        "recommendations": recommendations,
        "_visual": {
            "type": "plan_cards",
            "title": f"Recommended Bets for {event['home_team']} vs {event['away_team']}",
            "items": [
                {
                    "id": rec["bet_type"]["id"],
                    "name": rec["bet_type"]["name"],
                    "type": rec["bet_type"]["category"],
                    "potential_return": round(rec["potential_return"], 2),
                    "highlights": [
                        f"Stake: £{rec['stake']}",
                        f"Potential return: £{rec['potential_return']}",
                        f"Profit: £{rec['profit']}"
                    ]
                }
                for rec in recommendations
            ]
        }
    }


async def get_related_bets(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Get related bet suggestions for accumulator/parlay opportunities."""
    event_id = arguments.get("event_id")

    event = next((e for e in MOCK_EVENTS if e["id"] == event_id), None)
    if not event:
        return {"error": "Event not found"}

    # Suggest popular accumulator combinations
    related_bets = [
        {
            "id": "combo-1",
            "name": f"{event['home_team']} to Win + Over 2.5 Goals",
            "type": "combo",
            "odds": round(event["odds"]["match_result"]["home"] * event["odds"]["over_under"]["over_2_5"], 2),
            "description": "Higher risk, higher reward combination"
        },
        {
            "id": "combo-2",
            "name": f"Both Teams to Score + Over 2.5 Goals",
            "type": "combo",
            "odds": round(event["odds"]["both_teams_score"]["yes"] * event["odds"]["over_under"]["over_2_5"], 2),
            "description": "Popular combo for attacking teams"
        },
        {
            "id": "combo-3",
            "name": f"{event['home_team']} Win or Draw + Under 3.5 Goals",
            "type": "combo",
            "odds": round(event["odds"]["double_chance"]["home_draw"] * 1.4, 2),
            "description": "Safer option with decent returns"
        }
    ]

    return {
        "event_id": event_id,
        "related_bets": related_bets,
        "bundle_bonus": "Add to accumulator for 10% odds boost!",
        "_visual": {
            "type": "accessory_grid",
            "title": f"Bet Combos for {event['home_team']} vs {event['away_team']}",
            "items": [
                {
                    "id": bet["id"],
                    "name": bet["name"],
                    "type": bet["type"],
                    "price": bet["odds"],
                    "in_stock": True,
                    "image_url": "https://images.unsplash.com/photo-1508970259924-5fbe90befa5a?w=400&h=300&fit=crop"
                }
                for bet in related_bets
            ]
        }
    }


async def calculate_bet_returns(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Calculate potential returns for a bet or accumulator."""
    bets = arguments.get("bets", [])  # List of {event_id, market, selection, stake, odds}
    bet_type = arguments.get("bet_type", "single")  # "single", "accumulator", "system"
    total_stake = arguments.get("total_stake", 10)

    if not bets:
        return {"error": "No bets provided"}

    if bet_type == "single":
        # Single bet calculation
        bet = bets[0]
        potential_return = round(bet.get("stake", total_stake) * bet.get("odds", 2.0), 2)
        profit = round(potential_return - bet.get("stake", total_stake), 2)

        return {
            "bet_type": "single",
            "total_stake": bet.get("stake", total_stake),
            "potential_return": potential_return,
            "profit": profit,
            "_visual": {
                "type": "price_breakdown",
                "data": {
                    "items": [
                        {"label": "Stake", "amount": bet.get("stake", total_stake), "type": "upfront"},
                        {"label": f"Odds: {bet.get('odds', 2.0)}", "amount": potential_return, "type": "return"}
                    ],
                    "total_upfront": bet.get("stake", total_stake),
                    "total_monthly": 0,
                    "total_24m": potential_return
                }
            }
        }

    elif bet_type == "accumulator":
        # Accumulator calculation - all odds multiplied
        combined_odds = 1.0
        for bet in bets:
            combined_odds *= bet.get("odds", 2.0)

        combined_odds = round(combined_odds, 2)
        potential_return = round(total_stake * combined_odds, 2)
        profit = round(potential_return - total_stake, 2)

        return {
            "bet_type": "accumulator",
            "num_selections": len(bets),
            "total_stake": total_stake,
            "combined_odds": combined_odds,
            "potential_return": potential_return,
            "profit": profit,
            "warning": "All selections must win for payout",
            "_visual": {
                "type": "price_breakdown",
                "data": {
                    "items": [
                        {"label": f"Selection {i+1}: {bet.get('selection', 'N/A')}", "amount": bet.get("odds", 2.0), "type": "odds"}
                        for i, bet in enumerate(bets)
                    ] + [
                        {"label": f"Combined Odds ({len(bets)} selections)", "amount": combined_odds, "type": "odds"},
                        {"label": "Total Stake", "amount": total_stake, "type": "upfront"},
                        {"label": "Potential Return", "amount": potential_return, "type": "return"}
                    ],
                    "total_upfront": total_stake,
                    "total_monthly": 0,
                    "total_24m": potential_return
                }
            }
        }


async def check_event_status(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Check if event is available for betting (live odds, suspended, etc.)."""
    event_id = arguments.get("event_id")

    event = next((e for e in MOCK_EVENTS if e["id"] == event_id), None)
    if not event:
        return {"error": "Event not found"}

    betting_status = {
        "upcoming": "Available for betting",
        "live": "Live betting available - odds updating in real-time",
        "suspended": "Betting temporarily suspended",
        "finished": "Event finished - no longer available"
    }

    return {
        "event": f"{event['home_team']} vs {event['away_team']}",
        "status": event["status"],
        "betting_status": betting_status.get(event["status"], "Unknown"),
        "markets_available": len(event.get("odds", {})),
        "live_score": event.get("live_score") if event["status"] == "live" else None
    }


# Customer & Account Tools

async def check_betting_limits(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Check customer's betting limits and responsible gambling status."""
    await asyncio.sleep(0.5)

    account_number = arguments.get("account_number", "MOCK")

    # Mock limits
    daily_limit = random.randint(50, 500)
    weekly_limit = daily_limit * 5
    current_daily_spend = random.randint(0, int(daily_limit * 0.7))

    return {
        "account_number": account_number,
        "limits": {
            "daily_limit": daily_limit,
            "weekly_limit": weekly_limit,
            "monthly_limit": weekly_limit * 4,
            "single_bet_limit": int(daily_limit * 0.5)
        },
        "current_spend": {
            "today": current_daily_spend,
            "this_week": current_daily_spend * 3,
            "this_month": current_daily_spend * 10
        },
        "remaining_today": daily_limit - current_daily_spend,
        "responsible_gambling": {
            "self_exclusion": False,
            "timeout_active": False,
            "reality_check_enabled": True
        },
        "_visual": {
            "type": "info_callout",
            "data": {
                "message": f"✓ Daily limit: £{daily_limit} | Remaining today: £{daily_limit - current_daily_spend}"
            }
        }
    }


async def get_betting_history(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Get customer's betting history and statistics."""
    await asyncio.sleep(0.5)

    account_number = arguments.get("account_number", "MOCK")
    timeframe = arguments.get("timeframe", "month")  # "week", "month", "year"

    # Mock betting history
    num_bets = random.randint(15, 50)
    win_rate = random.randint(35, 55)
    total_staked = random.randint(200, 1000)
    total_returns = int(total_staked * random.uniform(0.85, 1.15))
    profit_loss = total_returns - total_staked

    return {
        "account_number": account_number,
        "timeframe": timeframe,
        "summary": {
            "total_bets": num_bets,
            "bets_won": int(num_bets * win_rate / 100),
            "bets_lost": int(num_bets * (100 - win_rate) / 100),
            "win_rate_percentage": win_rate,
            "total_staked": total_staked,
            "total_returns": total_returns,
            "profit_loss": profit_loss
        },
        "favorite_bet_types": ["Match Result", "Over/Under 2.5", "Both Teams to Score"],
        "favorite_leagues": ["Premier League", "Champions League", "La Liga"],
        "biggest_win": {
            "event": "Liverpool vs Manchester City",
            "stake": 20,
            "return": 180,
            "odds": 9.0
        }
    }


async def verify_age_identity(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Verify customer age and identity for betting compliance."""
    customer_name = arguments.get("customer_name")
    date_of_birth = arguments.get("date_of_birth")
    id_type = arguments.get("id_type")
    address = arguments.get("address")
    postcode = arguments.get("postcode")

    if not all([customer_name, date_of_birth, address, postcode]):
        return {
            "error": "Missing required information",
            "message": "We need your full name, date of birth, address, and postcode for age verification",
            "_visual": {
                "type": "info_callout",
                "data": {"message": "📋 Age verification required - must be 18+ to bet"}
            }
        }

    # Simulate verification
    await asyncio.sleep(2)

    # Calculate age from DOB
    try:
        dob_date = datetime.strptime(date_of_birth, "%Y-%m-%d")
        age = (datetime.now() - dob_date).days // 365
    except:
        age = 18  # Default for mock

    if age < 18:
        return {
            "verified": False,
            "status": "underage",
            "message": "You must be 18 or older to place bets",
            "_visual": {
                "type": "info_callout",
                "data": {"message": "❌ Age verification failed - must be 18+"}
            }
        }

    # Mock verification success
    verified = random.random() > 0.1  # 90% success rate

    if verified:
        return {
            "verified": True,
            "customer_name": customer_name,
            "age": age,
            "status": "verified",
            "message": "Identity verified successfully. You can now place bets!",
            "_visual": {
                "layout": "multi_section",
                "theme": "success",
                "sections": [
                    {
                        "type": "info_callout",
                        "data": {
                            "message": f"✅ Identity Verified\n👤 {customer_name}\n📍 {postcode}"
                        },
                        "style": "emphasized"
                    }
                ]
            }
        }
    else:
        return {
            "verified": False,
            "status": "verification_failed",
            "message": "Unable to verify identity. Please contact support.",
            "_visual": {
                "type": "info_callout",
                "data": {"message": "⚠️ Verification failed - please contact support"}
            }
        }


async def check_account_balance(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Check customer's account balance and available funds."""
    account_number = arguments.get("account_number", "MOCK")

    await asyncio.sleep(0.3)

    balance = round(random.uniform(10, 500), 2)
    pending_bets = round(random.uniform(0, 50), 2)
    available = round(balance - pending_bets, 2)

    return {
        "account_number": account_number,
        "balance": balance,
        "pending_bets": pending_bets,
        "available_to_bet": available,
        "currency": "GBP",
        "bonus_balance": round(random.uniform(0, 25), 2),
        "message": f"Available balance: £{available}",
        "_visual": {
            "type": "info_callout",
            "data": {
                "message": f"💰 Balance: £{balance}\n🎯 Available: £{available}\n🎁 Bonus: £{round(random.uniform(0, 25), 2)}"
            }
        }
    }


async def check_cashout_value(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Check cash-out value for active bet."""
    bet_id = arguments.get("bet_id", "BET-12345")

    await asyncio.sleep(1)

    # Mock cash-out calculation
    original_stake = random.randint(10, 50)
    potential_return = original_stake * random.uniform(3, 10)
    cashout_value = round(original_stake * random.uniform(1.2, 2.5), 2)
    profit_if_cashout = round(cashout_value - original_stake, 2)

    return {
        "bet_id": bet_id,
        "original_stake": original_stake,
        "potential_return": round(potential_return, 2),
        "cashout_value": cashout_value,
        "profit_if_cashout": profit_if_cashout,
        "cashout_available": True,
        "message": f"Cash out now for £{cashout_value} (£{profit_if_cashout} profit)",
        "_visual": {
            "layout": "single_focus",
            "theme": "info",
            "sections": [
                {
                    "type": "trade_in_value",
                    "data": {
                        "device_model": f"Bet #{bet_id}",
                        "condition": "Active",
                        "trade_in_value": cashout_value,
                        "original_price": original_stake,
                        "factors": {
                            "Original Stake": f"£{original_stake}",
                            "Current Value": f"£{cashout_value}",
                            "Potential Return": f"£{round(potential_return, 2)}"
                        },
                        "bonus_offer": "Cash out now to secure your profit!",
                        "next_steps": [
                            "Click 'Cash Out' to confirm",
                            "Funds credited immediately",
                            "Bet will be settled"
                        ]
                    },
                    "emphasis": "high"
                }
            ]
        }
    }


# Bet Slip Management

async def add_to_bet_slip(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Add selection to bet slip."""
    session_id = arguments.get("session_id", "default")
    event_id = arguments.get("event_id")
    market = arguments.get("market")  # "match_result", "over_under", etc.
    selection = arguments.get("selection")  # "home", "away", "over_2_5", etc.
    odds = arguments.get("odds", 2.0)

    if session_id not in BET_SLIP:
        BET_SLIP[session_id] = {"selections": [], "created_at": datetime.now()}

    # Get event details
    event = next((e for e in MOCK_EVENTS if e["id"] == event_id), None)

    bet_item = {
        "id": f"bet_{len(BET_SLIP[session_id]['selections'])}",
        "event_id": event_id,
        "event_name": f"{event['home_team']} vs {event['away_team']}" if event else "Unknown Event",
        "market": market,
        "selection": selection,
        "odds": odds,
        "added_at": datetime.now().isoformat()
    }

    BET_SLIP[session_id]["selections"].append(bet_item)

    # Get bet slip summary
    slip_summary = await get_bet_slip_summary({"session_id": session_id})

    return {
        "success": True,
        "bet_id": bet_item["id"],
        "bet_slip_count": len(BET_SLIP[session_id]["selections"]),
        "message": f"Added {selection} to bet slip",
        "selections": slip_summary.get("selections", []),
        "combined_odds": slip_summary.get("combined_odds", 0),
        "potential_return": slip_summary.get("potential_return", 0),
        "_visual": {
            "type": "bet_slip_preview",
            "title": "Bet Slip Updated",
            "data": {
                "selections": slip_summary.get("selections", []),
                "combined_odds": slip_summary.get("combined_odds", 0),
                "stake": 10,
                "potential_return": slip_summary.get("potential_return", 0)
            }
        }
    }


async def remove_from_bet_slip(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Remove selection from bet slip."""
    session_id = arguments.get("session_id", "default")
    bet_id = arguments.get("bet_id")

    if session_id in BET_SLIP:
        BET_SLIP[session_id]["selections"] = [
            bet for bet in BET_SLIP[session_id]["selections"]
            if bet["id"] != bet_id
        ]

    slip_summary = await get_bet_slip_summary({"session_id": session_id})

    return {
        "success": True,
        "bet_slip_count": len(BET_SLIP.get(session_id, {}).get("selections", [])),
        "message": "Selection removed from bet slip",
        "selections": slip_summary.get("selections", []),
        "combined_odds": slip_summary.get("combined_odds", 0),
        "potential_return": slip_summary.get("potential_return", 0),
        "_visual": {
            "type": "bet_slip_preview",
            "title": "Bet Slip Updated",
            "data": {
                "selections": slip_summary.get("selections", []),
                "combined_odds": slip_summary.get("combined_odds", 0),
                "stake": 10,
                "potential_return": slip_summary.get("potential_return", 0)
            }
        }
    }


async def get_bet_slip_summary(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Get complete bet slip with potential returns."""
    session_id = arguments.get("session_id", "default")

    if session_id not in BET_SLIP:
        return {"selections": [], "total_stake": 0, "potential_return": 0}

    slip = BET_SLIP[session_id]
    selections = slip["selections"]

    # Default stake per bet
    stake_per_bet = 10
    total_stake = stake_per_bet * len(selections) if selections else 0

    # Calculate potential returns (accumulator style)
    if selections:
        combined_odds = 1.0
        for bet in selections:
            combined_odds *= bet.get("odds", 2.0)
        potential_return = round(stake_per_bet * combined_odds, 2)
    else:
        potential_return = 0

    return {
        "selections": selections,
        "num_selections": len(selections),
        "total_stake": total_stake,
        "combined_odds": round(combined_odds, 2) if selections else 0,
        "potential_return": potential_return,
        "potential_profit": round(potential_return - total_stake, 2) if selections else 0,
        "_visual": {
            "type": "bet_slip_preview",
            "title": "Your Bet Slip",
            "data": {
                "selections": selections,
                "combined_odds": round(combined_odds, 2) if selections else 0,
                "stake": stake_per_bet,
                "potential_return": potential_return
            }
        }
    }


async def apply_bonus(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Apply bonus or promotion code."""
    code = arguments.get("code", "").upper()
    bet_value = arguments.get("bet_value", 0)

    # Mock bonus codes
    valid_codes = {
        "WELCOME50": {"type": "free_bet", "value": 50, "description": "£50 free bet for new customers"},
        "ACCA10": {"type": "odds_boost", "value": 10, "description": "10% odds boost on accumulators"},
        "CASHBACK20": {"type": "cashback", "value": 20, "description": "20% cashback on losses (up to £20)"},
        "DOUBLE": {"type": "multiplier", "value": 2, "description": "Double your winnings on first bet"}
    }

    if code in valid_codes:
        bonus = valid_codes[code]
        return {
            "valid": True,
            "code": code,
            "bonus_type": bonus["type"],
            "bonus_value": bonus["value"],
            "description": bonus["description"],
            "message": f"Bonus applied! {bonus['description']}"
        }

    return {
        "valid": False,
        "code": code,
        "message": "Invalid bonus code"
    }


async def place_bet(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Place bet and process transaction."""
    await asyncio.sleep(2)

    session_id = arguments.get("session_id", "default")
    bet_type = arguments.get("bet_type", "accumulator")  # "single", "accumulator", "system"

    # Get bet slip
    slip_summary = await get_bet_slip_summary({"session_id": session_id})

    if not slip_summary.get("selections"):
        return {"error": "Bet slip is empty"}

    bet_id = f"CB-{random.randint(100000, 999999)}"
    settlement_time = "After all events complete" if bet_type == "accumulator" else "After event completion"

    selections = slip_summary.get("selections", [])

    confirmation_number = f"CONF-{random.randint(1000000, 9999999)}"
    stake = slip_summary.get("total_stake", 0) / len(selections) if selections else 10

    # Clear the bet slip after placing
    if session_id in BET_SLIP:
        BET_SLIP[session_id]["selections"] = []

    return {
        "success": True,
        "bet_id": bet_id,
        "bet_type": bet_type,
        "confirmation_number": confirmation_number,
        "status": "accepted",
        "total_stake": slip_summary.get("total_stake", 0),
        "potential_return": slip_summary.get("potential_return", 0),
        "combined_odds": slip_summary.get("combined_odds", 0),
        "num_selections": len(selections),
        "settlement_time": settlement_time,
        "message": "Bet placed successfully! Good luck!",
        "selections": [],  # Clear selections in response
        "_visual": {
            "layout": "flow",
            "theme": "success",
            "sections": [
                {
                    "type": "bet_confirmation",
                    "data": {
                        "betId": bet_id,
                        "confirmationNumber": confirmation_number,
                        "selections": [
                            {
                                "event_name": sel["event_name"],
                                "market": sel["market"],
                                "selection": sel["selection"],
                                "odds": sel["odds"]
                            }
                            for sel in selections
                        ],
                        "stake": stake,
                        "combinedOdds": slip_summary.get("combined_odds", 0),
                        "potentialReturn": slip_summary.get("potential_return", 0)
                    }
                }
            ],
            "animation": "scale"
        }
    }


async def get_available_markets(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Browse all available betting markets/bet types."""
    category = arguments.get("category")  # "main", "player", "advanced", "combo", "all"

    if category and category != "all":
        filtered = [bt for bt in MOCK_BET_TYPES if bt["category"] == category]
    else:
        filtered = MOCK_BET_TYPES

    return {
        "bet_types": filtered,
        "count": len(filtered),
        "category": category or "all",
        "_visual": {
            "type": "plan_cards",
            "title": "Available Bet Types",
            "items": [
                {
                    "id": bt["id"],
                    "name": bt["name"],
                    "type": bt["category"],
                    "highlights": [
                        bt["description"],
                        f"Risk: {bt['risk_level']}",
                        f"Popularity: {bt['popularity']}"
                    ]
                }
                for bt in filtered
            ]
        }
    }


async def get_active_promotions(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Get current betting promotions and offers."""
    customer_type = arguments.get("customer_type", "new")  # "new", "existing"

    promotions = {
        "new": [
            {"title": "Welcome Bonus", "description": "Bet £10, Get £50 in Free Bets", "code": "WELCOME50"},
            {"title": "Risk Free First Bet", "description": "Money back as a free bet if your first bet loses (up to £25)", "code": "RISKFREE"},
            {"title": "Odds Boost", "description": "Enhanced odds on selected Premier League matches", "auto_apply": True}
        ],
        "existing": [
            {"title": "Acca Insurance", "description": "Get your stake back if one leg lets you down (5+ selections)", "auto_apply": True},
            {"title": "Cashback Fridays", "description": "10% cashback on all football bets placed on Fridays", "code": "FRIDAY10"},
            {"title": "Refer a Friend", "description": "£25 for you and your friend when they place first bet", "code": "REFER25"}
        ]
    }

    promos = promotions.get(customer_type, promotions["existing"])

    return {
        "customer_type": customer_type,
        "available_promotions": promos,
        "expires_date": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d"),
        "_visual": {
            "type": "promo_banner",
            "title": f"{customer_type.title()} Customer Offers",
            "items": promos
        }
    }


async def transfer_to_human_agent(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Transfer to human betting specialist."""
    reason = arguments.get("reason", "customer_request")
    context = arguments.get("context", {})

    return {
        "transfer_initiated": True,
        "estimated_wait_time_minutes": random.randint(2, 8),
        "agent_type": "betting_specialist",
        "reference_number": f"TRF-{random.randint(100000, 999999)}",
        "message": "Connecting you to a betting specialist. Please hold..."
    }


async def send_bet_confirmation(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Email bet confirmation to customer."""
    email = arguments.get("email")
    bet_id = arguments.get("bet_id", f"BET-{random.randint(100000, 999999)}")

    return {
        "sent": True,
        "email": email,
        "bet_id": bet_id,
        "message": f"Bet confirmation sent to {email}"
    }


async def customise_webpage(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """AI composes the visual display based on conversation context."""
    return {
        "success": True,
        "message": "Visual updated",
        "_visual": arguments
    }


# =============================================================================
# TOOLS REGISTRY
# =============================================================================

TOOLS_REGISTRY = {
    # Event Discovery & Information
    "search_events": {
        "definition": {
            "type": "function",
            "name": "search_events",
            "description": "Search for football matches/events based on league, team, date, or status. Use this when customer asks about upcoming matches or specific teams.",
            "parameters": {
                "type": "object",
                "properties": {
                    "league": {
                        "type": "string",
                        "description": "League name (e.g., Premier League, La Liga, Champions League)"
                    },
                    "team": {
                        "type": "string",
                        "description": "Team name to search for"
                    },
                    "date_range": {
                        "type": "string",
                        "enum": ["today", "tomorrow", "week", "upcoming"],
                        "description": "When to search for matches"
                    },
                    "status": {
                        "type": "string",
                        "enum": ["upcoming", "live", "all"],
                        "description": "Match status filter"
                    }
                }
            }
        },
        "executor": search_events
    },

    "get_event_details": {
        "definition": {
            "type": "function",
            "name": "get_event_details",
            "description": "Get complete details for a specific match including odds, team stats, form, and player information.",
            "parameters": {
                "type": "object",
                "properties": {
                    "event_id": {
                        "type": "string",
                        "description": "Event/match identifier"
                    }
                },
                "required": ["event_id"]
            }
        },
        "executor": get_event_details
    },

    "compare_odds": {
        "definition": {
            "type": "function",
            "name": "compare_odds",
            "description": "Compare odds across multiple matches or markets to find best value.",
            "parameters": {
                "type": "object",
                "properties": {
                    "event_ids": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of event IDs to compare"
                    },
                    "bet_type": {
                        "type": "string",
                        "description": "Type of bet to compare (match_result, over_under, etc.)"
                    }
                },
                "required": ["event_ids"]
            }
        },
        "executor": compare_odds
    },

    "get_similar_events": {
        "definition": {
            "type": "function",
            "name": "get_similar_events",
            "description": "Find similar matches (same league, same teams, similar odds).",
            "parameters": {
                "type": "object",
                "properties": {
                    "event_id": {
                        "type": "string",
                        "description": "Reference event ID"
                    }
                },
                "required": ["event_id"]
            }
        },
        "executor": get_similar_events
    },

    "recommend_bet_types": {
        "definition": {
            "type": "function",
            "name": "recommend_bet_types",
            "description": "Recommend suitable bet types based on customer preferences and risk appetite.",
            "parameters": {
                "type": "object",
                "properties": {
                    "event_id": {
                        "type": "string",
                        "description": "Event ID"
                    },
                    "risk_level": {
                        "type": "string",
                        "enum": ["low", "medium", "high", "all"],
                        "description": "Customer's risk appetite"
                    },
                    "budget": {
                        "type": "number",
                        "description": "Budget for betting"
                    }
                },
                "required": ["event_id"]
            }
        },
        "executor": recommend_bet_types
    },

    "get_related_bets": {
        "definition": {
            "type": "function",
            "name": "get_related_bets",
            "description": "Get related betting suggestions for accumulator/parlay opportunities.",
            "parameters": {
                "type": "object",
                "properties": {
                    "event_id": {
                        "type": "string",
                        "description": "Event ID"
                    }
                },
                "required": ["event_id"]
            }
        },
        "executor": get_related_bets
    },

    "calculate_bet_returns": {
        "definition": {
            "type": "function",
            "name": "calculate_bet_returns",
            "description": "Calculate potential returns for single bet or accumulator with detailed breakdown.",
            "parameters": {
                "type": "object",
                "properties": {
                    "bets": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "event_id": {"type": "string"},
                                "market": {"type": "string"},
                                "selection": {"type": "string"},
                                "odds": {"type": "number"},
                                "stake": {"type": "number"}
                            }
                        },
                        "description": "List of bets with details"
                    },
                    "bet_type": {
                        "type": "string",
                        "enum": ["single", "accumulator", "system"],
                        "description": "Type of bet"
                    },
                    "total_stake": {
                        "type": "number",
                        "description": "Total stake amount"
                    }
                },
                "required": ["bets"]
            }
        },
        "executor": calculate_bet_returns
    },

    "check_event_status": {
        "definition": {
            "type": "function",
            "name": "check_event_status",
            "description": "Check if event is available for betting, live odds status, or if suspended.",
            "parameters": {
                "type": "object",
                "properties": {
                    "event_id": {
                        "type": "string",
                        "description": "Event ID"
                    }
                },
                "required": ["event_id"]
            }
        },
        "executor": check_event_status
    },

    # Customer & Account Management
    "check_betting_limits": {
        "definition": {
            "type": "function",
            "name": "check_betting_limits",
            "description": "Check customer's betting limits and responsible gambling settings.",
            "parameters": {
                "type": "object",
                "properties": {
                    "account_number": {
                        "type": "string",
                        "description": "Customer account number"
                    }
                }
            }
        },
        "executor": check_betting_limits
    },

    "get_betting_history": {
        "definition": {
            "type": "function",
            "name": "get_betting_history",
            "description": "Get customer's betting history, win rate, and statistics.",
            "parameters": {
                "type": "object",
                "properties": {
                    "account_number": {
                        "type": "string",
                        "description": "Customer account number"
                    },
                    "timeframe": {
                        "type": "string",
                        "enum": ["week", "month", "year"],
                        "description": "Timeframe for history"
                    }
                }
            }
        },
        "executor": get_betting_history
    },

    "verify_age_identity": {
        "definition": {
            "type": "function",
            "name": "verify_age_identity",
            "description": "Verify customer age and identity for betting compliance (must be 18+).",
            "parameters": {
                "type": "object",
                "properties": {
                    "customer_name": {"type": "string", "description": "Full name"},
                    "date_of_birth": {"type": "string", "description": "Date of birth (YYYY-MM-DD)"},
                    "id_type": {
                        "type": "string",
                        "enum": ["passport", "drivers_license", "national_id"],
                        "description": "ID document type"
                    },
                    "address": {"type": "string", "description": "Full address"},
                    "postcode": {"type": "string", "description": "Postcode"}
                },
                "required": ["customer_name", "date_of_birth", "address", "postcode"]
            }
        },
        "executor": verify_age_identity
    },

    "check_account_balance": {
        "definition": {
            "type": "function",
            "name": "check_account_balance",
            "description": "Check customer's account balance and available funds for betting.",
            "parameters": {
                "type": "object",
                "properties": {
                    "account_number": {"type": "string"}
                }
            }
        },
        "executor": check_account_balance
    },

    "check_cashout_value": {
        "definition": {
            "type": "function",
            "name": "check_cashout_value",
            "description": "Check current cash-out value for an active bet.",
            "parameters": {
                "type": "object",
                "properties": {
                    "bet_id": {
                        "type": "string",
                        "description": "Bet identifier"
                    }
                },
                "required": ["bet_id"]
            }
        },
        "executor": check_cashout_value
    },

    # Bet Slip Management
    "add_to_bet_slip": {
        "definition": {
            "type": "function",
            "name": "add_to_bet_slip",
            "description": "Add a betting selection to the bet slip.",
            "parameters": {
                "type": "object",
                "properties": {
                    "session_id": {"type": "string"},
                    "event_id": {"type": "string", "description": "Event/match ID"},
                    "market": {
                        "type": "string",
                        "description": "Betting market (match_result, over_under, etc.)"
                    },
                    "selection": {
                        "type": "string",
                        "description": "Selection (home, away, over_2_5, etc.)"
                    },
                    "odds": {
                        "type": "number",
                        "description": "Current odds for this selection"
                    }
                },
                "required": ["event_id", "market", "selection", "odds"]
            }
        },
        "executor": add_to_bet_slip
    },

    "remove_from_bet_slip": {
        "definition": {
            "type": "function",
            "name": "remove_from_bet_slip",
            "description": "Remove a selection from bet slip.",
            "parameters": {
                "type": "object",
                "properties": {
                    "session_id": {"type": "string"},
                    "bet_id": {"type": "string", "description": "Bet slip item ID"}
                },
                "required": ["bet_id"]
            }
        },
        "executor": remove_from_bet_slip
    },

    "get_bet_slip_summary": {
        "definition": {
            "type": "function",
            "name": "get_bet_slip_summary",
            "description": "Get current bet slip with all selections and potential returns.",
            "parameters": {
                "type": "object",
                "properties": {
                    "session_id": {"type": "string"}
                }
            }
        },
        "executor": get_bet_slip_summary
    },

    "apply_bonus": {
        "definition": {
            "type": "function",
            "name": "apply_bonus",
            "description": "Apply bonus or promotional code to bet.",
            "parameters": {
                "type": "object",
                "properties": {
                    "code": {"type": "string", "description": "Bonus/promo code"},
                    "bet_value": {"type": "number", "description": "Current bet value"}
                },
                "required": ["code"]
            }
        },
        "executor": apply_bonus
    },

    "place_bet": {
        "definition": {
            "type": "function",
            "name": "place_bet",
            "description": "Place bet and confirm transaction. Use after customer confirms they want to place the bet.",
            "parameters": {
                "type": "object",
                "properties": {
                    "session_id": {"type": "string"},
                    "bet_type": {
                        "type": "string",
                        "enum": ["single", "accumulator", "system"],
                        "description": "Type of bet to place"
                    }
                }
            }
        },
        "executor": place_bet
    },

    "get_available_markets": {
        "definition": {
            "type": "function",
            "name": "get_available_markets",
            "description": "Browse all available betting markets and bet types.",
            "parameters": {
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "enum": ["main", "player", "advanced", "combo", "all"],
                        "description": "Filter by bet type category"
                    }
                }
            }
        },
        "executor": get_available_markets
    },

    "get_active_promotions": {
        "definition": {
            "type": "function",
            "name": "get_active_promotions",
            "description": "Get current betting promotions and bonus offers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "customer_type": {
                        "type": "string",
                        "enum": ["new", "existing"],
                        "description": "Customer type"
                    }
                }
            }
        },
        "executor": get_active_promotions
    },

    # Support & Engagement
    "transfer_to_human_agent": {
        "definition": {
            "type": "function",
            "name": "transfer_to_human_agent",
            "description": "Transfer customer to human betting specialist for complex queries or high-value bets.",
            "parameters": {
                "type": "object",
                "properties": {
                    "reason": {"type": "string"},
                    "context": {"type": "object"}
                }
            }
        },
        "executor": transfer_to_human_agent
    },

    "send_bet_confirmation": {
        "definition": {
            "type": "function",
            "name": "send_bet_confirmation",
            "description": "Email bet confirmation to customer.",
            "parameters": {
                "type": "object",
                "properties": {
                    "email": {"type": "string"},
                    "bet_id": {"type": "string"}
                },
                "required": ["email"]
            }
        },
        "executor": send_bet_confirmation
    },

    "customise_webpage": {
        "definition": {
            "type": "function",
            "name": "customise_webpage",
            "description": "Update the left-side visual display for betting interface. Use to show matches, odds, bet slip, live scores, or any betting content.",
            "parameters": {
                "type": "object",
                "properties": {
                    "layout": {
                        "type": "string",
                        "enum": ["single_focus", "two_column", "multi_section", "grid", "flow", "wizard"]
                    },
                    "header": {
                        "type": "object",
                        "properties": {
                            "title": {"type": "string"},
                            "subtitle": {"type": "string"},
                            "badge": {"type": "string"}
                        }
                    },
                    "sections": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "type": {"type": "string"},
                                "data": {"type": "object"},
                                "title": {"type": "string"},
                                "emphasis": {"type": "string"}
                            }
                        }
                    },
                    "theme": {"type": "string"},
                    "animation": {"type": "string"}
                },
                "required": ["layout", "sections"]
            }
        },
        "executor": customise_webpage
    }
}
