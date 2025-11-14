"""
Geospatial utilities for travel agent.
Simple distance calculations and travel time estimates.
"""
from typing import Dict, Tuple, Optional
from math import radians, sin, cos, sqrt, atan2

# Hardcoded coordinates for our 4 MVP cities
CITY_COORDINATES = {
    "Warsaw": {"lat": 52.2297, "lon": 21.0122},
    "Prague": {"lat": 50.0755, "lon": 14.4378},
    "Zakopane": {"lat": 49.2992, "lon": 19.9496},
    "Sopot": {"lat": 54.4419, "lon": 18.5602}
}

# Pre-computed distances between cities (in km)
# This is calculated once on module load to avoid repeated computations
CITY_DISTANCES = {}


def _haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate the great circle distance between two points on Earth.
    Returns distance in kilometers.
    """
    R = 6371  # Earth's radius in kilometers

    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c


def _precompute_city_distances():
    """Pre-compute all distances between our 4 cities on module load."""
    cities = list(CITY_COORDINATES.keys())
    for i, city1 in enumerate(cities):
        for city2 in cities[i+1:]:
            coords1 = CITY_COORDINATES[city1]
            coords2 = CITY_COORDINATES[city2]
            distance = _haversine_distance(
                coords1["lat"], coords1["lon"],
                coords2["lat"], coords2["lon"]
            )
            # Store in both directions for easy lookup
            CITY_DISTANCES[(city1, city2)] = distance
            CITY_DISTANCES[(city2, city1)] = distance


# Pre-compute on module load
_precompute_city_distances()


def geocode(location: str) -> Optional[Dict[str, float]]:
    """
    Get coordinates for a location.
    For MVP, only supports our 4 cities.
    Returns {"lat": float, "lon": float} or None if not found.
    """
    # Case-insensitive lookup
    location_lower = location.strip().lower()
    for city, coords in CITY_COORDINATES.items():
        if city.lower() == location_lower:
            return coords.copy()
    return None


def calculate_distance(location1: str, location2: str) -> Optional[float]:
    """
    Calculate distance between two locations in kilometers.
    Uses pre-computed cache for our 4 cities.
    Returns distance in km or None if locations not found.
    """
    # Try pre-computed cache first
    distance = CITY_DISTANCES.get((location1, location2))
    if distance is not None:
        return round(distance, 1)

    # Fall back to coordinate calculation if we have coords
    coords1 = geocode(location1)
    coords2 = geocode(location2)

    if coords1 and coords2:
        distance = _haversine_distance(
            coords1["lat"], coords1["lon"],
            coords2["lat"], coords2["lon"]
        )
        return round(distance, 1)

    return None


def estimate_travel_time(distance_km: float, mode: str = "flight") -> Dict[str, any]:
    """
    Estimate travel time based on distance and mode.

    Args:
        distance_km: Distance in kilometers
        mode: "flight", "car", or "train"

    Returns:
        {
            "hours": float,
            "minutes": int,
            "formatted": str (e.g., "2h 30m")
        }
    """
    if mode == "flight":
        # Average flight speed ~800 km/h + 1 hour for takeoff/landing
        hours = (distance_km / 800) + 1.0
    elif mode == "car":
        # Average highway speed ~100 km/h
        hours = distance_km / 100
    elif mode == "train":
        # Average high-speed train ~150 km/h
        hours = distance_km / 150
    else:
        # Default to flight
        hours = (distance_km / 800) + 1.0

    total_minutes = int(hours * 60)
    hours_part = total_minutes // 60
    minutes_part = total_minutes % 60

    # Format nicely
    if hours_part > 0 and minutes_part > 0:
        formatted = f"{hours_part}h {minutes_part}m"
    elif hours_part > 0:
        formatted = f"{hours_part}h"
    else:
        formatted = f"{minutes_part}m"

    return {
        "hours": round(hours, 1),
        "minutes": total_minutes,
        "formatted": formatted
    }


def get_distance_with_travel_time(location1: str, location2: str, mode: str = "flight") -> Optional[Dict]:
    """
    Convenience function that returns both distance and travel time.

    Returns:
        {
            "distance_km": float,
            "travel_time": {...}
        }
        or None if locations not found
    """
    distance = calculate_distance(location1, location2)
    if distance is None:
        return None

    travel_time = estimate_travel_time(distance, mode)

    return {
        "distance_km": distance,
        "travel_time": travel_time,
        "from": location1,
        "to": location2,
        "mode": mode
    }


def get_all_cities() -> list[str]:
    """Get list of all supported cities."""
    return list(CITY_COORDINATES.keys())


def get_city_info(city: str) -> Optional[Dict]:
    """
    Get comprehensive info about a city.

    Returns:
        {
            "name": str,
            "coordinates": {"lat": float, "lon": float},
            "distances_to_other_cities": {city: km}
        }
    """
    coords = geocode(city)
    if not coords:
        return None

    distances = {}
    for other_city in CITY_COORDINATES.keys():
        if other_city != city:
            dist = calculate_distance(city, other_city)
            if dist:
                distances[other_city] = dist

    return {
        "name": city,
        "coordinates": coords,
        "distances_to_other_cities": distances
    }
