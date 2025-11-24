"""
Simple, flexible search engine for travel deals.
LLM does the reasoning, these are just primitives.
"""
from typing import Dict, List, Optional, Any
from travel_data_catalog import TRAVEL_DEALS, CITY_COORDINATES, get_deals_by_city, get_all_cities


def search_deals(
    city: Optional[str] = None,
    budget_min: Optional[float] = None,
    budget_max: Optional[float] = None,
    deal_type: Optional[str] = None,
    suitable_for: Optional[List[str]] = None,
    min_rating: Optional[float] = None,
    min_guests: Optional[int] = None,
    pets_allowed: Optional[bool] = None,
    limit: Optional[int] = None
) -> List[Dict]:
    """
    Simple search with flexible filters.
    LLM decides how to use these filters based on conversation context.

    Args:
        city: Filter by destination city (e.g., "Warsaw", "Prague")
        budget_min: Minimum price in GBP
        budget_max: Maximum price in GBP
        deal_type: Type of deal (e.g., "hotel")
        suitable_for: List of tags (e.g., ["romantic", "beach", "families", "pets"])
        min_rating: Minimum rating (0-5)
        min_guests: Minimum guest capacity (for family/group searches)
        pets_allowed: Filter by pet-friendly properties
        limit: Max number of results to return

    Returns:
        List of matching deals
    """
    results = TRAVEL_DEALS.copy()

    # Filter by city
    if city:
        city_lower = city.strip().lower()
        results = [d for d in results if d["destination"]["city"].lower() == city_lower]

    # Filter by budget
    if budget_min is not None:
        results = [d for d in results if d["pricing"]["deal_price"] >= budget_min]

    if budget_max is not None:
        results = [d for d in results if d["pricing"]["deal_price"] <= budget_max]

    # Filter by type
    if deal_type:
        results = [d for d in results if d["type"] == deal_type]

    # Filter by suitable_for tags
    if suitable_for:
        suitable_for_lower = [tag.lower() for tag in suitable_for]
        results = [
            d for d in results
            if any(tag in suitable_for_lower for tag in d["features"].get("suitable_for", []))
        ]

    # Filter by rating
    if min_rating is not None:
        results = [d for d in results if d.get("rating", 0) >= min_rating]

    # Filter by guest capacity
    if min_guests is not None:
        results = [
            d for d in results
            if d["features"].get("capacity", {}).get("max_guests", 2) >= min_guests
        ]

    # Filter by pets allowed
    if pets_allowed is True:
        results = [
            d for d in results
            if d["features"].get("pets_allowed", False)
        ]

    # Sort by a combination of factors (deal quality)
    # Prioritize: discount, rating, urgency
    results.sort(
        key=lambda d: (
            -d["pricing"]["discount_percent"],  # Higher discount first
            -d.get("rating", 0),                 # Higher rating first
            d["urgency"].get("spots_left", 999)  # Fewer spots = more urgent
        )
    )

    # Limit results if specified
    if limit:
        results = results[:limit]

    return results


def get_deal_details(deal_id: str) -> Optional[Dict]:
    """
    Get full details for a specific deal by ID.

    Args:
        deal_id: The deal ID (e.g., "warsaw-royal-palace-hotel")

    Returns:
        Full deal object or None if not found
    """
    for deal in TRAVEL_DEALS:
        if deal["id"] == deal_id:
            return deal.copy()
    return None


def get_deals_by_urgency(ending_soon: bool = True, limit: int = 10) -> List[Dict]:
    """
    Get deals filtered by urgency.

    Args:
        ending_soon: If True, return deals ending soon; if False, return all
        limit: Max results

    Returns:
        List of deals
    """
    if ending_soon:
        results = [d for d in TRAVEL_DEALS if d["urgency"].get("ending_soon", False)]
    else:
        results = TRAVEL_DEALS.copy()

    # Sort by spots left (fewer = more urgent)
    results.sort(key=lambda d: d["urgency"].get("spots_left", 999))

    return results[:limit]


def get_deals_by_value(min_discount: int = 30, limit: int = 10) -> List[Dict]:
    """
    Get best value deals (highest discounts).

    Args:
        min_discount: Minimum discount percentage
        limit: Max results

    Returns:
        List of deals with high discounts
    """
    results = [d for d in TRAVEL_DEALS if d["pricing"]["discount_percent"] >= min_discount]
    results.sort(key=lambda d: -d["pricing"]["discount_percent"])
    return results[:limit]


def get_luxury_deals(min_stars: int = 4, limit: int = 10) -> List[Dict]:
    """
    Get luxury deals (4+ stars, high ratings).

    Args:
        min_stars: Minimum star rating (extracted from accommodation string)
        limit: Max results

    Returns:
        List of luxury deals
    """
    results = []
    for deal in TRAVEL_DEALS:
        accommodation = deal["features"].get("accommodation", "")
        # Extract star rating from accommodation string (e.g., "5-star luxury hotel")
        if "5-star" in accommodation or "4-star" in accommodation:
            if deal.get("rating", 0) >= 4.5:
                results.append(deal)

    results.sort(key=lambda d: (-d.get("rating", 0), -d["pricing"]["deal_price"]))
    return results[:limit]


def get_budget_deals(max_price: int = 400, limit: int = 10) -> List[Dict]:
    """
    Get budget-friendly deals.

    Args:
        max_price: Maximum price in GBP
        limit: Max results

    Returns:
        List of budget deals
    """
    results = [d for d in TRAVEL_DEALS if d["pricing"]["deal_price"] <= max_price]
    results.sort(key=lambda d: d["pricing"]["deal_price"])
    return results[:limit]


def get_available_cities() -> List[str]:
    """
    Get list of all cities we have deals for.

    Returns:
        List of city names
    """
    return get_all_cities()


def get_deal_count_by_city() -> Dict[str, int]:
    """
    Get count of deals per city.

    Returns:
        Dictionary mapping city name to deal count
    """
    counts = {}
    for city in get_all_cities():
        counts[city] = len(get_deals_by_city(city))
    return counts


def compare_deals(deal_ids: List[str]) -> List[Dict]:
    """
    Get multiple deals for comparison.

    Args:
        deal_ids: List of deal IDs to compare

    Returns:
        List of deal objects (maintains order)
    """
    results = []
    for deal_id in deal_ids:
        deal = get_deal_details(deal_id)
        if deal:
            results.append(deal)
    return results
