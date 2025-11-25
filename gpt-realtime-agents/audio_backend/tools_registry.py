"""
Travel Agent Tools Registry
Simple, flexible tools for conversational travel discovery.
LLM does the reasoning, these are just primitives.
"""
import asyncio
from typing import Any, Dict, List
import search_engine
from search_engine import (
    search_deals,
    get_deal_details,
    get_deals_by_urgency,
    get_deals_by_value,
    get_luxury_deals,
    get_budget_deals,
    get_available_cities,
    compare_deals
)

# Simple in-memory preference storage
user_preferences = {}


# =============================================================================
# DEAL SEARCH & DISCOVERY TOOLS
# =============================================================================

async def tool_search_deals(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    Search for travel deals with flexible filters.
    LLM interprets user intent and applies appropriate filters.
    """
    city = arguments.get("city")
    budget_min = arguments.get("budget_min")
    budget_max = arguments.get("budget_max")
    deal_type = arguments.get("deal_type", "hotel")
    suitable_for = arguments.get("suitable_for")  # List of tags
    min_rating = arguments.get("min_rating")
    min_guests = arguments.get("min_guests")
    pets_allowed = arguments.get("pets_allowed")
    limit = arguments.get("limit", 10)

    results = search_deals(
        city=city,
        budget_min=budget_min,
        budget_max=budget_max,
        deal_type=deal_type,
        suitable_for=suitable_for,
        min_rating=min_rating,
        min_guests=min_guests,
        pets_allowed=pets_allowed,
        limit=limit
    )

    # Determine visual type based on number of results
    if len(results) == 0:
        visual_type = "empty_state"
    elif len(results) == 1:
        visual_type = "deal_hero"
    else:
        visual_type = "deal_grid"

    return {
        "deals": results,
        "count": len(results),
        "filters_applied": {
            k: v for k, v in arguments.items()
            if v is not None and k != "limit"
        },
        "_visual": {
            "type": visual_type,
            "data": {"deals": results}
        }
    }


async def tool_get_deal_details(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Get detailed information about a specific deal."""
    deal_id = arguments.get("deal_id")

    deal = get_deal_details(deal_id)

    if not deal:
        return {
            "error": "Deal not found",
            "deal_id": deal_id
        }

    return {
        "deal": deal,
        "_visual": {
            "type": "deal_detail_page",
            "data": {"deal": deal}
        }
    }


async def tool_get_urgent_deals(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Get deals that are ending soon or have limited availability."""
    limit = arguments.get("limit", 10)

    results = get_deals_by_urgency(ending_soon=True, limit=limit)

    return {
        "deals": results,
        "count": len(results),
        "urgency_filter": "ending_soon",
        "_visual": {
            "type": "deal_grid",
            "data": {"deals": results, "highlight_urgency": True}
        }
    }


async def tool_get_best_value_deals(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Get deals with highest discounts (best value for money)."""
    min_discount = arguments.get("min_discount", 30)
    limit = arguments.get("limit", 10)

    results = get_deals_by_value(min_discount=min_discount, limit=limit)

    return {
        "deals": results,
        "count": len(results),
        "min_discount": min_discount,
        "_visual": {
            "type": "deal_grid",
            "data": {"deals": results, "highlight_savings": True}
        }
    }


async def tool_get_luxury_deals(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Get premium/luxury hotel deals (4-5 star)."""
    limit = arguments.get("limit", 10)

    results = get_luxury_deals(min_stars=4, limit=limit)

    return {
        "deals": results,
        "count": len(results),
        "_visual": {
            "type": "deal_grid",
            "data": {"deals": results}
        }
    }


async def tool_get_budget_deals(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Get budget-friendly deals under a price threshold."""
    max_price = arguments.get("max_price", 400)
    limit = arguments.get("limit", 10)

    results = get_budget_deals(max_price=max_price, limit=limit)

    return {
        "deals": results,
        "count": len(results),
        "max_price": max_price,
        "_visual": {
            "type": "deal_grid",
            "data": {"deals": results}
        }
    }


async def tool_compare_deals(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    Compare multiple deals side by side with flexible comparison aspects.
    Agent decides what to compare (rooms, facilities, ratings, pricing, etc.)
    """
    deal_ids = arguments.get("deal_ids", [])
    aspects = arguments.get("aspects", ["overview", "ratings", "rooms", "facilities"])
    price_params = arguments.get("price_params", {})

    if not deal_ids or len(deal_ids) < 2:
        return {"error": "Need at least 2 deal IDs to compare"}

    if len(deal_ids) > 2:
        deal_ids = deal_ids[:2]  # Limit to 2 hotels for side-by-side comparison

    # Fetch deal details
    deals = compare_deals(deal_ids)

    if len(deals) < 2:
        return {"error": "Could not find enough deals to compare"}

    # Build comparison data structure
    comparison_data = {
        "hotels": [],
        "aspects": aspects,
        "has_price_calculation": bool(price_params)
    }

    for deal in deals:
        hotel_data = {
            "id": deal["id"],
            "name": deal["title"],
            "city": deal["destination"]["city"],
            "stars": deal.get("stars", 0),
            "rating": deal.get("rating", 0),
            "ratings": deal.get("ratings", {}),
            "price_per_night": deal["pricing"]["deal_price"],
            "image": deal["images"][0] if deal.get("images") else None
        }

        # Include rooms if requested
        if "rooms" in aspects:
            hotel_data["rooms"] = deal.get("rooms", [])

        # Include facilities if requested
        if "facilities" in aspects:
            detailed_amenities = deal.get("detailed_amenities", {})
            hotel_data["facilities"] = {
                "wellness": detailed_amenities.get("wellness", []),
                "dining": detailed_amenities.get("dining", []),
                "activities": detailed_amenities.get("activities", []),
                "business": detailed_amenities.get("business", [])
            }

        # Calculate total price if params provided
        if price_params:
            nights = price_params.get("nights", 1)
            guests = price_params.get("guests", 2)
            base_price = deal["pricing"]["deal_price"] * nights
            hotel_data["price_calculation"] = {
                "nights": nights,
                "guests": guests,
                "price_per_night": deal["pricing"]["deal_price"],
                "base_price": base_price,
                "total": base_price  # Simplified - could add taxes/fees later
            }

        comparison_data["hotels"].append(hotel_data)

    return {
        "comparison": comparison_data,
        "count": len(comparison_data["hotels"]),
        "_visual": {
            "type": "deal_comparison",
            "data": comparison_data
        }
    }


# =============================================================================
# CART & BOOKING TOOLS
# =============================================================================

# Simple in-memory cart storage
carts = {}


async def tool_add_to_cart(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Add a deal to the shopping cart."""
    session_id = arguments.get("session_id", "default")
    deal_id = arguments.get("deal_id")
    check_in = arguments.get("check_in")  # YYYY-MM-DD
    nights = arguments.get("nights", 3)
    guests = arguments.get("guests", 2)

    if session_id not in carts:
        carts[session_id] = []

    # Get deal details
    deal = get_deal_details(deal_id)
    if not deal:
        return {"error": "Deal not found"}

    # Calculate total price
    total_price = deal["pricing"]["deal_price"] * nights

    cart_item = {
        "id": f"cart_{len(carts[session_id]) + 1}",
        "deal_id": deal_id,
        "deal_name": deal["title"],
        "destination": deal["destination"]["city"],
        "check_in": check_in,
        "nights": nights,
        "guests": guests,
        "price_per_night": deal["pricing"]["deal_price"],
        "total_price": total_price,
        "image": deal["images"][0] if deal["images"] else None
    }

    carts[session_id].append(cart_item)

    return {
        "success": True,
        "cart_item": cart_item,
        "cart_count": len(carts[session_id]),
        "cart_total": sum(item["total_price"] for item in carts[session_id]),
        "_visual": {
            "type": "cart_confirmation",
            "data": {"item": cart_item, "cart_count": len(carts[session_id])}
        }
    }


async def tool_view_cart(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """View all items in the shopping cart."""
    session_id = arguments.get("session_id", "default")

    cart_items = carts.get(session_id, [])
    cart_total = sum(item["total_price"] for item in cart_items)

    return {
        "items": cart_items,
        "count": len(cart_items),
        "total": cart_total,
        "_visual": {
            "type": "cart_drawer",
            "data": {"items": cart_items, "total": cart_total}
        }
    }


async def tool_remove_from_cart(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Remove an item from the cart."""
    session_id = arguments.get("session_id", "default")
    cart_item_id = arguments.get("cart_item_id")

    if session_id not in carts:
        return {"error": "Cart not found"}

    carts[session_id] = [item for item in carts[session_id] if item["id"] != cart_item_id]

    cart_items = carts[session_id]
    cart_total = sum(item["total_price"] for item in cart_items)

    return {
        "success": True,
        "items": cart_items,
        "count": len(cart_items),
        "total": cart_total,
        "_visual": {
            "type": "cart_drawer",
            "data": {"items": cart_items, "total": cart_total}
        }
    }


async def tool_clear_cart(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Clear all items from the cart."""
    session_id = arguments.get("session_id", "default")

    carts[session_id] = []

    return {
        "success": True,
        "message": "Cart cleared",
        "count": 0,
        "total": 0
    }


# =============================================================================
# PERSONALIZATION & PREFERENCES
# =============================================================================

async def tool_save_preference(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Save a user preference (budget, interests, home city, etc.)."""
    session_id = arguments.get("session_id", "default")
    key = arguments.get("key")
    value = arguments.get("value")

    if session_id not in user_preferences:
        user_preferences[session_id] = {}

    user_preferences[session_id][key] = value

    return {
        "success": True,
        "key": key,
        "value": value,
        "all_preferences": user_preferences[session_id]
    }


async def tool_get_preferences(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Get all saved user preferences."""
    session_id = arguments.get("session_id", "default")

    prefs = user_preferences.get(session_id, {})

    return {
        "preferences": prefs,
        "has_preferences": len(prefs) > 0
    }


# =============================================================================
# UTILITY TOOLS
# =============================================================================

async def tool_get_available_cities(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Get list of all cities we have deals for."""
    cities = get_available_cities()

    return {
        "cities": cities,
        "count": len(cities)
    }


async def tool_customise_visual(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    AI composes custom visual layouts.
    Allows flexible combination of multiple visual sections.
    """
    return {
        "success": True,
        "message": "Visual updated",
        "_visual": arguments  # Pass through AI's composition
    }


# =============================================================================
# TOOLS CATALOG (Registry)
# =============================================================================

TOOLS_CATALOG = {
    "search_deals": {
        "definition": {
            "type": "function",
            "name": "search_deals",
            "description": "Search for travel deals with flexible filters. Use this for most search queries. LLM interprets user intent and applies appropriate filters.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "Filter by destination city (Warsaw, Prague, Zakopane, or Sopot)"
                    },
                    "budget_min": {
                        "type": "number",
                        "description": "Minimum price in GBP"
                    },
                    "budget_max": {
                        "type": "number",
                        "description": "Maximum price in GBP"
                    },
                    "deal_type": {
                        "type": "string",
                        "enum": ["hotel"],
                        "description": "Type of deal (currently only hotel)"
                    },
                    "suitable_for": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Tags like 'romantic', 'beach', 'skiing', 'families', 'pets', 'budget', 'luxury', 'business'"
                    },
                    "min_rating": {
                        "type": "number",
                        "description": "Minimum rating (0-5)"
                    },
                    "min_guests": {
                        "type": "number",
                        "description": "Minimum guest capacity needed (use for family/group searches, e.g. 3 for a family of 3)"
                    },
                    "pets_allowed": {
                        "type": "boolean",
                        "description": "Set to true to filter for pet-friendly properties only"
                    },
                    "limit": {
                        "type": "number",
                        "description": "Max results to return (default: 10)"
                    }
                }
            }
        },
        "executor": tool_search_deals
    },

    "get_deal_details": {
        "definition": {
            "type": "function",
            "name": "get_deal_details",
            "description": "Get full details about a specific deal",
            "parameters": {
                "type": "object",
                "properties": {
                    "deal_id": {
                        "type": "string",
                        "description": "The deal ID (e.g., 'warsaw-royal-palace-hotel')"
                    }
                },
                "required": ["deal_id"]
            }
        },
        "executor": tool_get_deal_details
    },

    "get_urgent_deals": {
        "definition": {
            "type": "function",
            "name": "get_urgent_deals",
            "description": "Get deals that are ending soon or have limited spots left",
            "parameters": {
                "type": "object",
                "properties": {
                    "limit": {
                        "type": "number",
                        "description": "Max results (default: 10)"
                    }
                }
            }
        },
        "executor": tool_get_urgent_deals
    },

    "get_best_value_deals": {
        "definition": {
            "type": "function",
            "name": "get_best_value_deals",
            "description": "Get deals with highest discounts (30%+ savings)",
            "parameters": {
                "type": "object",
                "properties": {
                    "min_discount": {
                        "type": "number",
                        "description": "Minimum discount percentage (default: 30)"
                    },
                    "limit": {
                        "type": "number",
                        "description": "Max results (default: 10)"
                    }
                }
            }
        },
        "executor": tool_get_best_value_deals
    },

    "get_luxury_deals": {
        "definition": {
            "type": "function",
            "name": "get_luxury_deals",
            "description": "Get premium 4-5 star hotel deals",
            "parameters": {
                "type": "object",
                "properties": {
                    "limit": {
                        "type": "number",
                        "description": "Max results (default: 10)"
                    }
                }
            }
        },
        "executor": tool_get_luxury_deals
    },

    "get_budget_deals": {
        "definition": {
            "type": "function",
            "name": "get_budget_deals",
            "description": "Get budget-friendly deals under a price threshold",
            "parameters": {
                "type": "object",
                "properties": {
                    "max_price": {
                        "type": "number",
                        "description": "Maximum price in GBP (default: 400)"
                    },
                    "limit": {
                        "type": "number",
                        "description": "Max results (default: 10)"
                    }
                }
            }
        },
        "executor": tool_get_budget_deals
    },

    "compare_deals": {
        "definition": {
            "type": "function",
            "name": "compare_deals",
            "description": "Compare 2 hotels side by side with flexible comparison aspects. You decide what to compare based on user needs: rooms, facilities, ratings, pricing, etc.",
            "parameters": {
                "type": "object",
                "properties": {
                    "deal_ids": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Array of 2 deal IDs to compare side by side"
                    },
                    "aspects": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "What to compare: 'overview', 'ratings', 'rooms', 'facilities', 'pricing'. Include what's relevant to the user's question. Defaults to all."
                    },
                    "price_params": {
                        "type": "object",
                        "description": "Optional: If comparing total prices, specify nights and guests to calculate totals",
                        "properties": {
                            "nights": {"type": "number", "description": "Number of nights"},
                            "guests": {"type": "number", "description": "Number of guests"}
                        }
                    }
                },
                "required": ["deal_ids"]
            }
        },
        "executor": tool_compare_deals
    },

    "add_to_cart": {
        "definition": {
            "type": "function",
            "name": "add_to_cart",
            "description": "Add a deal to the shopping cart with travel details",
            "parameters": {
                "type": "object",
                "properties": {
                    "session_id": {
                        "type": "string",
                        "description": "Session identifier"
                    },
                    "deal_id": {
                        "type": "string",
                        "description": "The deal ID to add"
                    },
                    "check_in": {
                        "type": "string",
                        "description": "Check-in date (YYYY-MM-DD format)"
                    },
                    "nights": {
                        "type": "number",
                        "description": "Number of nights"
                    },
                    "guests": {
                        "type": "number",
                        "description": "Number of guests"
                    }
                },
                "required": ["deal_id", "check_in", "nights"]
            }
        },
        "executor": tool_add_to_cart
    },

    "view_cart": {
        "definition": {
            "type": "function",
            "name": "view_cart",
            "description": "View all items in the shopping cart",
            "parameters": {
                "type": "object",
                "properties": {
                    "session_id": {
                        "type": "string",
                        "description": "Session identifier"
                    }
                }
            }
        },
        "executor": tool_view_cart
    },

    "remove_from_cart": {
        "definition": {
            "type": "function",
            "name": "remove_from_cart",
            "description": "Remove an item from the cart",
            "parameters": {
                "type": "object",
                "properties": {
                    "session_id": {
                        "type": "string",
                        "description": "Session identifier"
                    },
                    "cart_item_id": {
                        "type": "string",
                        "description": "The cart item ID to remove"
                    }
                },
                "required": ["cart_item_id"]
            }
        },
        "executor": tool_remove_from_cart
    },

    "clear_cart": {
        "definition": {
            "type": "function",
            "name": "clear_cart",
            "description": "Clear all items from the cart",
            "parameters": {
                "type": "object",
                "properties": {
                    "session_id": {
                        "type": "string",
                        "description": "Session identifier"
                    }
                }
            }
        },
        "executor": tool_clear_cart
    },

    "save_preference": {
        "definition": {
            "type": "function",
            "name": "save_preference",
            "description": "Save a user preference extracted from conversation (budget range, interests, home city, travel style, etc.)",
            "parameters": {
                "type": "object",
                "properties": {
                    "session_id": {
                        "type": "string",
                        "description": "Session identifier"
                    },
                    "key": {
                        "type": "string",
                        "description": "Preference key (e.g., 'budget_max', 'home_city', 'interests')"
                    },
                    "value": {
                        "description": "Preference value (any type)"
                    }
                },
                "required": ["key", "value"]
            }
        },
        "executor": tool_save_preference
    },

    "get_preferences": {
        "definition": {
            "type": "function",
            "name": "get_preferences",
            "description": "Get all saved user preferences",
            "parameters": {
                "type": "object",
                "properties": {
                    "session_id": {
                        "type": "string",
                        "description": "Session identifier"
                    }
                }
            }
        },
        "executor": tool_get_preferences
    },

    "get_available_cities": {
        "definition": {
            "type": "function",
            "name": "get_available_cities",
            "description": "Get list of all cities we have deals for",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        },
        "executor": tool_get_available_cities
    },

    "customise_visual": {
        "definition": {
            "type": "function",
            "name": "customise_visual",
            "description": "Compose custom visual layouts with multiple sections. Use to create rich, multi-component displays.",
            "parameters": {
                "type": "object",
                "properties": {
                    "layout": {
                        "type": "string",
                        "enum": ["single_column", "two_column", "hero_with_grid", "comparison_view"],
                        "description": "Overall layout structure"
                    },
                    "sections": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "type": {
                                    "type": "string",
                                    "enum": [
                                        "deal_hero", "deal_grid", "deal_card", "deal_comparison",
                                        "cart_drawer", "cart_confirmation",
                                        "info_callout", "section_header"
                                    ]
                                },
                                "data": {"type": "object"}
                            },
                            "required": ["type", "data"]
                        }
                    }
                },
                "required": ["layout", "sections"]
            }
        },
        "executor": tool_customise_visual
    }
}

# Alias for backward compatibility
TOOLS_REGISTRY = TOOLS_CATALOG
