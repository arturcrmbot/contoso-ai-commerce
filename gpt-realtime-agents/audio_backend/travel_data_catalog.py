"""
Mock travel deals catalog for MVP.
20-30 curated deals across 4 cities: Warsaw, Prague, Zakopane, Sopot
"""

# Hardcoded coordinates for our 4 cities
CITY_COORDINATES = {
    "Warsaw": {"lat": 52.2297, "lon": 21.0122},
    "Prague": {"lat": 50.0755, "lon": 14.4378},
    "Zakopane": {"lat": 49.2992, "lon": 19.9496},
    "Sopot": {"lat": 54.4419, "lon": 18.5602}
}

# Mock travel deals
TRAVEL_DEALS = [
    # WARSAW (7 deals - Cultural/Business)
    {
        "id": "warsaw-royal-palace-hotel",
        "type": "hotel",
        "title": "Royal Palace Boutique Hotel",
        "destination": {
            "city": "Warsaw",
            "country": "Poland",
            "region": "Mazovia",
            "coordinates": CITY_COORDINATES["Warsaw"]
        },
        "dates": {
            "available_from": "2025-03-01",
            "available_to": "2025-10-31",
            "blackout_dates": [],
            "min_nights": 2,
            "max_nights": 14
        },
        "pricing": {
            "original_price": 980,
            "deal_price": 649,
            "discount_percent": 34,
            "currency": "GBP",
            "per": "room",
            "includes": ["breakfast", "wifi", "gym_access"]
        },
        "images": [
            "https://images.unsplash.com/photo-1609137144813-7d9921338f24?w=800",
            "https://images.unsplash.com/photo-1601853895209-3a8a0b9f27a9?w=800"
        ],
        "rating": 4.7,
        "review_count": 342,
        "features": {
            "accommodation": "4-star boutique hotel",
            "amenities": ["restaurant", "spa", "conference_room", "bar", "parking"],
            "room_type": "Deluxe Room with Old Town View",
            "suitable_for": ["business", "couples", "culture"],
            "accessibility": ["elevator", "wheelchair_friendly"]
        },
        "urgency": {
            "ending_soon": False,
            "spots_left": 8,
            "last_booked": "3 hours ago"
        }
    },
    {
        "id": "warsaw-modern-loft",
        "type": "hotel",
        "title": "City Center Modern Loft Hotel",
        "destination": {
            "city": "Warsaw",
            "country": "Poland",
            "region": "Mazovia",
            "coordinates": CITY_COORDINATES["Warsaw"]
        },
        "dates": {
            "available_from": "2025-04-01",
            "available_to": "2025-12-20",
            "blackout_dates": ["2025-07-15:2025-08-15"],
            "min_nights": 1,
            "max_nights": 10
        },
        "pricing": {
            "original_price": 520,
            "deal_price": 349,
            "discount_percent": 33,
            "currency": "GBP",
            "per": "room",
            "includes": ["breakfast", "wifi"]
        },
        "images": [
            "https://images.unsplash.com/photo-1581104478174-e041b34e1729?w=800"
        ],
        "rating": 4.4,
        "review_count": 189,
        "features": {
            "accommodation": "3-star modern hotel",
            "amenities": ["gym", "24h_reception", "kitchenette"],
            "room_type": "Studio Loft",
            "suitable_for": ["solo", "business", "budget"],
            "accessibility": ["elevator"]
        },
        "urgency": {
            "ending_soon": False,
            "spots_left": 15,
            "last_booked": "1 day ago"
        }
    },
    {
        "id": "warsaw-palace-garden",
        "type": "hotel",
        "title": "Palace Garden Luxury Suites",
        "destination": {
            "city": "Warsaw",
            "country": "Poland",
            "region": "Mazovia",
            "coordinates": CITY_COORDINATES["Warsaw"]
        },
        "dates": {
            "available_from": "2025-05-01",
            "available_to": "2025-09-30",
            "blackout_dates": [],
            "min_nights": 3,
            "max_nights": 14
        },
        "pricing": {
            "original_price": 1450,
            "deal_price": 989,
            "discount_percent": 32,
            "currency": "GBP",
            "per": "room",
            "includes": ["breakfast", "spa_access", "airport_transfer", "minibar"]
        },
        "images": [
            "https://images.unsplash.com/photo-1609137144813-7d9921338f24?w=800"
        ],
        "rating": 4.9,
        "review_count": 567,
        "features": {
            "accommodation": "5-star luxury hotel",
            "amenities": ["spa", "pool", "restaurant", "concierge", "parking", "bar"],
            "room_type": "Executive Suite",
            "suitable_for": ["luxury", "honeymoon", "couples"],
            "accessibility": ["elevator", "wheelchair_friendly", "accessible_bathroom"]
        },
        "urgency": {
            "ending_soon": True,
            "spots_left": 3,
            "last_booked": "30 minutes ago"
        }
    },
    {
        "id": "warsaw-riverside-inn",
        "type": "hotel",
        "title": "Vistula Riverside Inn",
        "destination": {
            "city": "Warsaw",
            "country": "Poland",
            "region": "Mazovia",
            "coordinates": CITY_COORDINATES["Warsaw"]
        },
        "dates": {
            "available_from": "2025-03-15",
            "available_to": "2025-11-30",
            "blackout_dates": [],
            "min_nights": 2,
            "max_nights": 7
        },
        "pricing": {
            "original_price": 620,
            "deal_price": 429,
            "discount_percent": 31,
            "currency": "GBP",
            "per": "room",
            "includes": ["breakfast", "wifi", "bike_rental"]
        },
        "images": [
            "https://images.unsplash.com/photo-1601853895209-3a8a0b9f27a9?w=800"
        ],
        "rating": 4.5,
        "review_count": 223,
        "features": {
            "accommodation": "3-star riverside hotel",
            "amenities": ["restaurant", "terrace", "bike_rental", "river_view"],
            "room_type": "River View Room",
            "suitable_for": ["families", "couples", "nature"],
            "accessibility": ["elevator"]
        },
        "urgency": {
            "ending_soon": False,
            "spots_left": 12,
            "last_booked": "5 hours ago"
        }
    },
    {
        "id": "warsaw-culture-hub",
        "type": "hotel",
        "title": "Culture Hub Design Hotel",
        "destination": {
            "city": "Warsaw",
            "country": "Poland",
            "region": "Mazovia",
            "coordinates": CITY_COORDINATES["Warsaw"]
        },
        "dates": {
            "available_from": "2025-04-01",
            "available_to": "2025-10-31",
            "blackout_dates": [],
            "min_nights": 2,
            "max_nights": 10
        },
        "pricing": {
            "original_price": 750,
            "deal_price": 525,
            "discount_percent": 30,
            "currency": "GBP",
            "per": "room",
            "includes": ["breakfast", "wifi", "art_gallery_access"]
        },
        "images": [
            "https://images.unsplash.com/photo-1581104478174-e041b34e1729?w=800"
        ],
        "rating": 4.6,
        "review_count": 298,
        "features": {
            "accommodation": "4-star design hotel",
            "amenities": ["restaurant", "gallery", "rooftop_bar", "library"],
            "room_type": "Designer Room",
            "suitable_for": ["culture", "art_lovers", "couples"],
            "accessibility": ["elevator"]
        },
        "urgency": {
            "ending_soon": False,
            "spots_left": 7,
            "last_booked": "2 hours ago"
        }
    },
    {
        "id": "warsaw-airport-hotel",
        "type": "hotel",
        "title": "Warsaw Airport Express Hotel",
        "destination": {
            "city": "Warsaw",
            "country": "Poland",
            "region": "Mazovia",
            "coordinates": CITY_COORDINATES["Warsaw"]
        },
        "dates": {
            "available_from": "2025-02-01",
            "available_to": "2025-12-31",
            "blackout_dates": [],
            "min_nights": 1,
            "max_nights": 5
        },
        "pricing": {
            "original_price": 320,
            "deal_price": 229,
            "discount_percent": 28,
            "currency": "GBP",
            "per": "room",
            "includes": ["breakfast", "wifi", "airport_shuttle"]
        },
        "images": [
            "https://images.unsplash.com/photo-1609137144813-7d9921338f24?w=800"
        ],
        "rating": 4.2,
        "review_count": 456,
        "features": {
            "accommodation": "3-star airport hotel",
            "amenities": ["restaurant", "24h_reception", "free_shuttle", "parking"],
            "room_type": "Standard Room",
            "suitable_for": ["business", "transit", "solo"],
            "accessibility": ["elevator", "wheelchair_friendly"]
        },
        "urgency": {
            "ending_soon": False,
            "spots_left": 20,
            "last_booked": "1 hour ago"
        }
    },
    {
        "id": "warsaw-family-nest",
        "type": "hotel",
        "title": "Family Nest Apartments",
        "destination": {
            "city": "Warsaw",
            "country": "Poland",
            "region": "Mazovia",
            "coordinates": CITY_COORDINATES["Warsaw"]
        },
        "dates": {
            "available_from": "2025-03-01",
            "available_to": "2025-11-30",
            "blackout_dates": [],
            "min_nights": 3,
            "max_nights": 14
        },
        "pricing": {
            "original_price": 890,
            "deal_price": 599,
            "discount_percent": 33,
            "currency": "GBP",
            "per": "room",
            "includes": ["wifi", "kitchen", "parking"]
        },
        "images": [
            "https://images.unsplash.com/photo-1601853895209-3a8a0b9f27a9?w=800"
        ],
        "rating": 4.8,
        "review_count": 178,
        "features": {
            "accommodation": "4-star apartment hotel",
            "amenities": ["kitchen", "washing_machine", "parking", "playground"],
            "room_type": "2-Bedroom Apartment",
            "suitable_for": ["families", "long_stay", "groups"],
            "accessibility": ["elevator"]
        },
        "urgency": {
            "ending_soon": False,
            "spots_left": 5,
            "last_booked": "4 hours ago"
        }
    },

    # PRAGUE (8 deals - Historic/Romantic)
    {
        "id": "prague-castle-view",
        "type": "hotel",
        "title": "Castle View Heritage Hotel",
        "destination": {
            "city": "Prague",
            "country": "Czech Republic",
            "region": "Prague",
            "coordinates": CITY_COORDINATES["Prague"]
        },
        "dates": {
            "available_from": "2025-03-01",
            "available_to": "2025-10-31",
            "blackout_dates": [],
            "min_nights": 2,
            "max_nights": 10
        },
        "pricing": {
            "original_price": 1120,
            "deal_price": 749,
            "discount_percent": 33,
            "currency": "GBP",
            "per": "room",
            "includes": ["breakfast", "wifi", "castle_tour"]
        },
        "images": [
            "https://images.unsplash.com/photo-1541849546-216549ae216d?w=800",
            "https://images.unsplash.com/photo-1587974928442-77dc3e0dba72?w=800"
        ],
        "rating": 4.8,
        "review_count": 892,
        "features": {
            "accommodation": "5-star heritage hotel",
            "amenities": ["spa", "restaurant", "bar", "concierge", "parking"],
            "room_type": "Castle View Suite",
            "suitable_for": ["romantic", "luxury", "honeymoon"],
            "accessibility": ["elevator"]
        },
        "urgency": {
            "ending_soon": True,
            "spots_left": 4,
            "last_booked": "15 minutes ago"
        }
    },
    {
        "id": "prague-charles-bridge",
        "type": "hotel",
        "title": "Charles Bridge Boutique Inn",
        "destination": {
            "city": "Prague",
            "country": "Czech Republic",
            "region": "Prague",
            "coordinates": CITY_COORDINATES["Prague"]
        },
        "dates": {
            "available_from": "2025-04-01",
            "available_to": "2025-11-30",
            "blackout_dates": ["2025-08-01:2025-08-20"],
            "min_nights": 2,
            "max_nights": 7
        },
        "pricing": {
            "original_price": 820,
            "deal_price": 549,
            "discount_percent": 33,
            "currency": "GBP",
            "per": "room",
            "includes": ["breakfast", "wifi"]
        },
        "images": [
            "https://images.unsplash.com/photo-1592906209472-a36b1f3782ef?w=800"
        ],
        "rating": 4.6,
        "review_count": 534,
        "features": {
            "accommodation": "4-star boutique hotel",
            "amenities": ["restaurant", "bar", "historic_building"],
            "room_type": "Bridge View Room",
            "suitable_for": ["romantic", "couples", "culture"],
            "accessibility": []
        },
        "urgency": {
            "ending_soon": False,
            "spots_left": 9,
            "last_booked": "2 hours ago"
        }
    },
    {
        "id": "prague-old-town-square",
        "type": "hotel",
        "title": "Old Town Square Palace",
        "destination": {
            "city": "Prague",
            "country": "Czech Republic",
            "region": "Prague",
            "coordinates": CITY_COORDINATES["Prague"]
        },
        "dates": {
            "available_from": "2025-03-15",
            "available_to": "2025-10-15",
            "blackout_dates": [],
            "min_nights": 3,
            "max_nights": 14
        },
        "pricing": {
            "original_price": 1350,
            "deal_price": 899,
            "discount_percent": 33,
            "currency": "GBP",
            "per": "room",
            "includes": ["breakfast", "minibar", "spa_access", "champagne"]
        },
        "images": [
            "https://images.unsplash.com/photo-1587974928442-77dc3e0dba72?w=800"
        ],
        "rating": 4.9,
        "review_count": 1023,
        "features": {
            "accommodation": "5-star palace hotel",
            "amenities": ["spa", "restaurant", "bar", "concierge", "rooftop_terrace"],
            "room_type": "Royal Suite",
            "suitable_for": ["luxury", "honeymoon", "special_occasion"],
            "accessibility": ["elevator", "wheelchair_friendly"]
        },
        "urgency": {
            "ending_soon": True,
            "spots_left": 2,
            "last_booked": "45 minutes ago"
        }
    },
    {
        "id": "prague-art-nouveau",
        "type": "hotel",
        "title": "Art Nouveau Design Hotel",
        "destination": {
            "city": "Prague",
            "country": "Czech Republic",
            "region": "Prague",
            "coordinates": CITY_COORDINATES["Prague"]
        },
        "dates": {
            "available_from": "2025-04-01",
            "available_to": "2025-10-31",
            "blackout_dates": [],
            "min_nights": 2,
            "max_nights": 10
        },
        "pricing": {
            "original_price": 720,
            "deal_price": 489,
            "discount_percent": 32,
            "currency": "GBP",
            "per": "room",
            "includes": ["breakfast", "wifi", "art_gallery"]
        },
        "images": [
            "https://images.unsplash.com/photo-1541849546-216549ae216d?w=800"
        ],
        "rating": 4.7,
        "review_count": 412,
        "features": {
            "accommodation": "4-star design hotel",
            "amenities": ["restaurant", "bar", "art_gallery", "library"],
            "room_type": "Art Deco Room",
            "suitable_for": ["art_lovers", "culture", "couples"],
            "accessibility": ["elevator"]
        },
        "urgency": {
            "ending_soon": False,
            "spots_left": 11,
            "last_booked": "3 hours ago"
        }
    },
    {
        "id": "prague-beer-spa",
        "type": "hotel",
        "title": "Czech Beer Spa Hotel",
        "destination": {
            "city": "Prague",
            "country": "Poland",
            "region": "Prague",
            "coordinates": CITY_COORDINATES["Prague"]
        },
        "dates": {
            "available_from": "2025-03-01",
            "available_to": "2025-12-20",
            "blackout_dates": [],
            "min_nights": 2,
            "max_nights": 7
        },
        "pricing": {
            "original_price": 580,
            "deal_price": 399,
            "discount_percent": 31,
            "currency": "GBP",
            "per": "room",
            "includes": ["breakfast", "wifi", "beer_spa_treatment"]
        },
        "images": [
            "https://images.unsplash.com/photo-1592906209472-a36b1f3782ef?w=800"
        ],
        "rating": 4.5,
        "review_count": 687,
        "features": {
            "accommodation": "3-star spa hotel",
            "amenities": ["beer_spa", "restaurant", "bar", "sauna"],
            "room_type": "Spa Room",
            "suitable_for": ["unique_experience", "groups", "couples"],
            "accessibility": ["elevator"]
        },
        "urgency": {
            "ending_soon": False,
            "spots_left": 14,
            "last_booked": "1 hour ago"
        }
    },
    {
        "id": "prague-jewish-quarter",
        "type": "hotel",
        "title": "Jewish Quarter Historic Hotel",
        "destination": {
            "city": "Prague",
            "country": "Czech Republic",
            "region": "Prague",
            "coordinates": CITY_COORDINATES["Prague"]
        },
        "dates": {
            "available_from": "2025-04-01",
            "available_to": "2025-11-15",
            "blackout_dates": [],
            "min_nights": 2,
            "max_nights": 10
        },
        "pricing": {
            "original_price": 690,
            "deal_price": 469,
            "discount_percent": 32,
            "currency": "GBP",
            "per": "room",
            "includes": ["breakfast", "wifi", "walking_tour"]
        },
        "images": [
            "https://images.unsplash.com/photo-1587974928442-77dc3e0dba72?w=800"
        ],
        "rating": 4.6,
        "review_count": 378,
        "features": {
            "accommodation": "4-star historic hotel",
            "amenities": ["restaurant", "library", "courtyard", "historic_tours"],
            "room_type": "Heritage Room",
            "suitable_for": ["culture", "history", "solo"],
            "accessibility": []
        },
        "urgency": {
            "ending_soon": False,
            "spots_left": 8,
            "last_booked": "4 hours ago"
        }
    },
    {
        "id": "prague-budget-hostel",
        "type": "hotel",
        "title": "Prague City Hostel & Hotel",
        "destination": {
            "city": "Prague",
            "country": "Czech Republic",
            "region": "Prague",
            "coordinates": CITY_COORDINATES["Prague"]
        },
        "dates": {
            "available_from": "2025-02-01",
            "available_to": "2025-12-31",
            "blackout_dates": [],
            "min_nights": 1,
            "max_nights": 14
        },
        "pricing": {
            "original_price": 280,
            "deal_price": 189,
            "discount_percent": 33,
            "currency": "GBP",
            "per": "room",
            "includes": ["wifi", "common_kitchen"]
        },
        "images": [
            "https://images.unsplash.com/photo-1541849546-216549ae216d?w=800"
        ],
        "rating": 4.3,
        "review_count": 923,
        "features": {
            "accommodation": "2-star hostel",
            "amenities": ["common_room", "kitchen", "bar", "laundry"],
            "room_type": "Private Room",
            "suitable_for": ["budget", "solo", "backpackers"],
            "accessibility": []
        },
        "urgency": {
            "ending_soon": False,
            "spots_left": 25,
            "last_booked": "30 minutes ago"
        }
    },
    {
        "id": "prague-river-cruise",
        "type": "hotel",
        "title": "Vltava River Hotel & Cruises",
        "destination": {
            "city": "Prague",
            "country": "Czech Republic",
            "region": "Prague",
            "coordinates": CITY_COORDINATES["Prague"]
        },
        "dates": {
            "available_from": "2025-05-01",
            "available_to": "2025-09-30",
            "blackout_dates": [],
            "min_nights": 2,
            "max_nights": 7
        },
        "pricing": {
            "original_price": 850,
            "deal_price": 579,
            "discount_percent": 32,
            "currency": "GBP",
            "per": "room",
            "includes": ["breakfast", "wifi", "river_cruise"]
        },
        "images": [
            "https://images.unsplash.com/photo-1592906209472-a36b1f3782ef?w=800"
        ],
        "rating": 4.7,
        "review_count": 445,
        "features": {
            "accommodation": "4-star riverside hotel",
            "amenities": ["restaurant", "terrace", "river_view", "boat_tours"],
            "room_type": "River View Room",
            "suitable_for": ["romantic", "couples", "families"],
            "accessibility": ["elevator"]
        },
        "urgency": {
            "ending_soon": False,
            "spots_left": 10,
            "last_booked": "2 hours ago"
        }
    },

    # ZAKOPANE (7 deals - Mountains/Skiing)
    {
        "id": "zakopane-tatra-lodge",
        "type": "hotel",
        "title": "Tatra Mountain Lodge",
        "destination": {
            "city": "Zakopane",
            "country": "Poland",
            "region": "Lesser Poland",
            "coordinates": CITY_COORDINATES["Zakopane"]
        },
        "dates": {
            "available_from": "2025-01-01",
            "available_to": "2025-03-31",
            "blackout_dates": [],
            "min_nights": 3,
            "max_nights": 14
        },
        "pricing": {
            "original_price": 950,
            "deal_price": 629,
            "discount_percent": 34,
            "currency": "GBP",
            "per": "room",
            "includes": ["breakfast", "ski_pass", "wifi", "sauna"]
        },
        "images": [
            "https://images.unsplash.com/photo-1605640840605-14ac1855827b?w=800",
            "https://images.unsplash.com/photo-1551582045-6ec9c11d8697?w=800"
        ],
        "rating": 4.8,
        "review_count": 567,
        "features": {
            "accommodation": "4-star mountain lodge",
            "amenities": ["spa", "sauna", "restaurant", "ski_storage", "parking"],
            "room_type": "Mountain View Room",
            "suitable_for": ["skiing", "families", "nature", "adventure"],
            "accessibility": ["elevator"]
        },
        "urgency": {
            "ending_soon": True,
            "spots_left": 5,
            "last_booked": "1 hour ago"
        }
    },
    {
        "id": "zakopane-ski-resort",
        "type": "hotel",
        "title": "Grand Ski Resort & Spa",
        "destination": {
            "city": "Zakopane",
            "country": "Poland",
            "region": "Lesser Poland",
            "coordinates": CITY_COORDINATES["Zakopane"]
        },
        "dates": {
            "available_from": "2024-12-15",
            "available_to": "2025-04-15",
            "blackout_dates": ["2024-12-24:2025-01-02"],
            "min_nights": 4,
            "max_nights": 14
        },
        "pricing": {
            "original_price": 1280,
            "deal_price": 849,
            "discount_percent": 34,
            "currency": "GBP",
            "per": "room",
            "includes": ["breakfast", "dinner", "ski_pass", "spa_access", "ski_lessons"]
        },
        "images": [
            "https://images.unsplash.com/photo-1605181379317-d6a5de8f2056?w=800"
        ],
        "rating": 4.9,
        "review_count": 892,
        "features": {
            "accommodation": "5-star ski resort",
            "amenities": ["spa", "pool", "restaurant", "ski_school", "equipment_rental", "parking"],
            "room_type": "Suite with Balcony",
            "suitable_for": ["skiing", "luxury", "families", "groups"],
            "accessibility": ["elevator", "wheelchair_friendly"]
        },
        "urgency": {
            "ending_soon": True,
            "spots_left": 3,
            "last_booked": "20 minutes ago"
        }
    },
    {
        "id": "zakopane-wooden-cottage",
        "type": "hotel",
        "title": "Traditional Wooden Cottage Hotel",
        "destination": {
            "city": "Zakopane",
            "country": "Poland",
            "region": "Lesser Poland",
            "coordinates": CITY_COORDINATES["Zakopane"]
        },
        "dates": {
            "available_from": "2025-01-01",
            "available_to": "2025-12-20",
            "blackout_dates": [],
            "min_nights": 2,
            "max_nights": 10
        },
        "pricing": {
            "original_price": 620,
            "deal_price": 419,
            "discount_percent": 32,
            "currency": "GBP",
            "per": "room",
            "includes": ["breakfast", "wifi", "fireplace"]
        },
        "images": [
            "https://images.unsplash.com/photo-1551582045-6ec9c11d8697?w=800"
        },
        "rating": 4.7,
        "review_count": 334,
        "features": {
            "accommodation": "3-star traditional cottage",
            "amenities": ["restaurant", "fireplace", "garden", "parking"],
            "room_type": "Rustic Room with Fireplace",
            "suitable_for": ["romantic", "couples", "nature", "authentic"],
            "accessibility": []
        },
        "urgency": {
            "ending_soon": False,
            "spots_left": 7,
            "last_booked": "3 hours ago"
        }
    },
    {
        "id": "zakopane-hiking-base",
        "type": "hotel",
        "title": "Hiking Base Mountain Hotel",
        "destination": {
            "city": "Zakopane",
            "country": "Poland",
            "region": "Lesser Poland",
            "coordinates": CITY_COORDINATES["Zakopane"]
        },
        "dates": {
            "available_from": "2025-05-01",
            "available_to": "2025-10-31",
            "blackout_dates": [],
            "min_nights": 2,
            "max_nights": 10
        },
        "pricing": {
            "original_price": 480,
            "deal_price": 329,
            "discount_percent": 31,
            "currency": "GBP",
            "per": "room",
            "includes": ["breakfast", "wifi", "hiking_guide"]
        },
        "images": [
            "https://images.unsplash.com/photo-1605640840605-14ac1855827b?w=800"
        ],
        "rating": 4.6,
        "review_count": 289,
        "features": {
            "accommodation": "3-star mountain hotel",
            "amenities": ["restaurant", "parking", "bike_rental", "hiking_maps"],
            "room_type": "Mountain View Room",
            "suitable_for": ["hiking", "adventure", "nature", "families"],
            "accessibility": []
        },
        "urgency": {
            "ending_soon": False,
            "spots_left": 12,
            "last_booked": "5 hours ago"
        }
    },
    {
        "id": "zakopane-wellness-retreat",
        "type": "hotel",
        "title": "Mountain Wellness Retreat",
        "destination": {
            "city": "Zakopane",
            "country": "Poland",
            "region": "Lesser Poland",
            "coordinates": CITY_COORDINATES["Zakopane"]
        },
        "dates": {
            "available_from": "2025-02-01",
            "available_to": "2025-11-30",
            "blackout_dates": [],
            "min_nights": 3,
            "max_nights": 14
        },
        "pricing": {
            "original_price": 1050,
            "deal_price": 699,
            "discount_percent": 33,
            "currency": "GBP",
            "per": "room",
            "includes": ["breakfast", "spa_treatments", "yoga_classes", "healthy_meals"]
        },
        "images": [
            "https://images.unsplash.com/photo-1605181379317-d6a5de8f2056?w=800"
        ],
        "rating": 4.8,
        "review_count": 423,
        "features": {
            "accommodation": "4-star wellness hotel",
            "amenities": ["spa", "yoga_studio", "pool", "restaurant", "meditation_room"],
            "room_type": "Wellness Suite",
            "suitable_for": ["wellness", "relaxation", "couples", "solo"],
            "accessibility": ["elevator", "wheelchair_friendly"]
        },
        "urgency": {
            "ending_soon": False,
            "spots_left": 8,
            "last_booked": "2 hours ago"
        }
    },
    {
        "id": "zakopane-family-chalet",
        "type": "hotel",
        "title": "Family Chalet Apartments",
        "destination": {
            "city": "Zakopane",
            "country": "Poland",
            "region": "Lesser Poland",
            "coordinates": CITY_COORDINATES["Zakopane"]
        },
        "dates": {
            "available_from": "2025-01-01",
            "available_to": "2025-12-20",
            "blackout_dates": [],
            "min_nights": 3,
            "max_nights": 14
        },
        "pricing": {
            "original_price": 780,
            "deal_price": 529,
            "discount_percent": 32,
            "currency": "GBP",
            "per": "room",
            "includes": ["wifi", "kitchen", "parking", "playground"]
        },
        "images": [
            "https://images.unsplash.com/photo-1551582045-6ec9c11d8697?w=800"
        ],
        "rating": 4.7,
        "review_count": 267,
        "features": {
            "accommodation": "4-star chalet apartments",
            "amenities": ["kitchen", "fireplace", "parking", "playground", "bbq"],
            "room_type": "2-Bedroom Chalet",
            "suitable_for": ["families", "groups", "long_stay"],
            "accessibility": []
        },
        "urgency": {
            "ending_soon": False,
            "spots_left": 6,
            "last_booked": "4 hours ago"
        }
    },
    {
        "id": "zakopane-budget-hostel",
        "type": "hotel",
        "title": "Mountain Budget Hostel",
        "destination": {
            "city": "Zakopane",
            "country": "Poland",
            "region": "Lesser Poland",
            "coordinates": CITY_COORDINATES["Zakopane"]
        },
        "dates": {
            "available_from": "2025-01-01",
            "available_to": "2025-12-31",
            "blackout_dates": [],
            "min_nights": 1,
            "max_nights": 10
        },
        "pricing": {
            "original_price": 240,
            "deal_price": 169,
            "discount_percent": 30,
            "currency": "GBP",
            "per": "room",
            "includes": ["wifi", "common_kitchen"]
        },
        "images": [
            "https://images.unsplash.com/photo-1605640840605-14ac1855827b?w=800"
        ],
        "rating": 4.4,
        "review_count": 512,
        "features": {
            "accommodation": "2-star hostel",
            "amenities": ["common_room", "kitchen", "parking", "ski_storage"],
            "room_type": "Private Room",
            "suitable_for": ["budget", "backpackers", "solo", "groups"],
            "accessibility": []
        },
        "urgency": {
            "ending_soon": False,
            "spots_left": 18,
            "last_booked": "1 hour ago"
        }
    },

    # SOPOT (8 deals - Beach/Spa)
    {
        "id": "sopot-grand-hotel",
        "type": "hotel",
        "title": "Grand Baltic Hotel & Spa",
        "destination": {
            "city": "Sopot",
            "country": "Poland",
            "region": "Pomerania",
            "coordinates": CITY_COORDINATES["Sopot"]
        },
        "dates": {
            "available_from": "2025-05-01",
            "available_to": "2025-09-30",
            "blackout_dates": [],
            "min_nights": 3,
            "max_nights": 14
        },
        "pricing": {
            "original_price": 1320,
            "deal_price": 879,
            "discount_percent": 33,
            "currency": "GBP",
            "per": "room",
            "includes": ["breakfast", "spa_access", "beach_access", "minibar"]
        },
        "images": [
            "https://images.unsplash.com/photo-1598970434795-0c54fe7c0648?w=800",
            "https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=800"
        ],
        "rating": 4.9,
        "review_count": 1234,
        "features": {
            "accommodation": "5-star grand hotel",
            "amenities": ["spa", "pool", "restaurant", "beach_club", "casino", "pier_access"],
            "room_type": "Sea View Suite",
            "suitable_for": ["luxury", "romantic", "spa", "beach"],
            "accessibility": ["elevator", "wheelchair_friendly", "accessible_bathroom"]
        },
        "urgency": {
            "ending_soon": True,
            "spots_left": 4,
            "last_booked": "25 minutes ago"
        }
    },
    {
        "id": "sopot-pier-view",
        "type": "hotel",
        "title": "Sopot Pier View Hotel",
        "destination": {
            "city": "Sopot",
            "country": "Poland",
            "region": "Pomerania",
            "coordinates": CITY_COORDINATES["Sopot"]
        },
        "dates": {
            "available_from": "2025-04-15",
            "available_to": "2025-10-15",
            "blackout_dates": [],
            "min_nights": 2,
            "max_nights": 10
        },
        "pricing": {
            "original_price": 720,
            "deal_price": 489,
            "discount_percent": 32,
            "currency": "GBP",
            "per": "room",
            "includes": ["breakfast", "wifi", "beach_access"]
        },
        "images": [
            "https://images.unsplash.com/photo-1598970434795-0c54fe7c0648?w=800"
        ],
        "rating": 4.6,
        "review_count": 567,
        "features": {
            "accommodation": "4-star beachfront hotel",
            "amenities": ["restaurant", "bar", "terrace", "pier_view"],
            "room_type": "Pier View Room",
            "suitable_for": ["beach", "couples", "families"],
            "accessibility": ["elevator"]
        },
        "urgency": {
            "ending_soon": False,
            "spots_left": 11,
            "last_booked": "2 hours ago"
        }
    },
    {
        "id": "sopot-spa-wellness",
        "type": "hotel",
        "title": "Baltic Spa & Wellness Resort",
        "destination": {
            "city": "Sopot",
            "country": "Poland",
            "region": "Pomerania",
            "coordinates": CITY_COORDINATES["Sopot"]
        },
        "dates": {
            "available_from": "2025-03-01",
            "available_to": "2025-11-30",
            "blackout_dates": [],
            "min_nights": 3,
            "max_nights": 14
        },
        "pricing": {
            "original_price": 980,
            "deal_price": 649,
            "discount_percent": 34,
            "currency": "GBP",
            "per": "room",
            "includes": ["breakfast", "spa_treatments", "pool_access", "massage"]
        },
        "images": [
            "https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=800"
        ],
        "rating": 4.8,
        "review_count": 789,
        "features": {
            "accommodation": "4-star spa resort",
            "amenities": ["spa", "pool", "sauna", "restaurant", "wellness_programs"],
            "room_type": "Wellness Suite",
            "suitable_for": ["spa", "wellness", "relaxation", "couples"],
            "accessibility": ["elevator", "wheelchair_friendly"]
        },
        "urgency": {
            "ending_soon": False,
            "spots_left": 9,
            "last_booked": "3 hours ago"
        }
    },
    {
        "id": "sopot-beach-bungalow",
        "type": "hotel",
        "title": "Beach Bungalow Resort",
        "destination": {
            "city": "Sopot",
            "country": "Poland",
            "region": "Pomerania",
            "coordinates": CITY_COORDINATES["Sopot"]
        },
        "dates": {
            "available_from": "2025-06-01",
            "available_to": "2025-09-15",
            "blackout_dates": [],
            "min_nights": 3,
            "max_nights": 10
        },
        "pricing": {
            "original_price": 850,
            "deal_price": 579,
            "discount_percent": 32,
            "currency": "GBP",
            "per": "room",
            "includes": ["breakfast", "beach_access", "bbq", "bikes"]
        },
        "images": [
            "https://images.unsplash.com/photo-1601892546722-f9cb29c554b9?w=800"
        ],
        "rating": 4.7,
        "review_count": 445,
        "features": {
            "accommodation": "3-star beach bungalows",
            "amenities": ["beach_access", "bbq", "bike_rental", "terrace", "garden"],
            "room_type": "Beach Bungalow",
            "suitable_for": ["beach", "families", "groups", "summer"],
            "accessibility": []
        },
        "urgency": {
            "ending_soon": False,
            "spots_left": 7,
            "last_booked": "4 hours ago"
        }
    },
    {
        "id": "sopot-family-resort",
        "type": "hotel",
        "title": "Family Beach Resort Sopot",
        "destination": {
            "city": "Sopot",
            "country": "Poland",
            "region": "Pomerania",
            "coordinates": CITY_COORDINATES["Sopot"]
        },
        "dates": {
            "available_from": "2025-05-15",
            "available_to": "2025-09-15",
            "blackout_dates": [],
            "min_nights": 3,
            "max_nights": 14
        },
        "pricing": {
            "original_price": 1120,
            "deal_price": 749,
            "discount_percent": 33,
            "currency": "GBP",
            "per": "room",
            "includes": ["breakfast", "kids_club", "pool_access", "entertainment"]
        },
        "images": [
            "https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=800"
        ],
        "rating": 4.8,
        "review_count": 923,
        "features": {
            "accommodation": "4-star family resort",
            "amenities": ["kids_club", "pool", "playground", "restaurant", "animation"],
            "room_type": "Family Room",
            "suitable_for": ["families", "children", "beach"],
            "accessibility": ["elevator", "wheelchair_friendly"]
        },
        "urgency": {
            "ending_soon": False,
            "spots_left": 12,
            "last_booked": "1 hour ago"
        }
    },
    {
        "id": "sopot-boutique-villa",
        "type": "hotel",
        "title": "Seaside Boutique Villa",
        "destination": {
            "city": "Sopot",
            "country": "Poland",
            "region": "Pomerania",
            "coordinates": CITY_COORDINATES["Sopot"]
        },
        "dates": {
            "available_from": "2025-05-01",
            "available_to": "2025-10-31",
            "blackout_dates": [],
            "min_nights": 2,
            "max_nights": 10
        },
        "pricing": {
            "original_price": 620,
            "deal_price": 419,
            "discount_percent": 32,
            "currency": "GBP",
            "per": "room",
            "includes": ["breakfast", "wifi", "garden_access"]
        },
        "images": [
            "https://images.unsplash.com/photo-1598970434795-0c54fe7c0648?w=800"
        ],
        "rating": 4.7,
        "review_count": 278,
        "features": {
            "accommodation": "3-star boutique villa",
            "amenities": ["garden", "terrace", "library", "bikes"],
            "room_type": "Garden View Room",
            "suitable_for": ["romantic", "couples", "quiet"],
            "accessibility": []
        },
        "urgency": {
            "ending_soon": False,
            "spots_left": 5,
            "last_booked": "5 hours ago"
        }
    },
    {
        "id": "sopot-surfing-hostel",
        "type": "hotel",
        "title": "Surfing Paradise Hostel",
        "destination": {
            "city": "Sopot",
            "country": "Poland",
            "region": "Pomerania",
            "coordinates": CITY_COORDINATES["Sopot"]
        },
        "dates": {
            "available_from": "2025-05-01",
            "available_to": "2025-09-30",
            "blackout_dates": [],
            "min_nights": 2,
            "max_nights": 14
        },
        "pricing": {
            "original_price": 320,
            "deal_price": 219,
            "discount_percent": 32,
            "currency": "GBP",
            "per": "room",
            "includes": ["wifi", "surf_lessons", "beach_access"]
        },
        "images": [
            "https://images.unsplash.com/photo-1601892546722-f9cb29c554b9?w=800"
        ],
        "rating": 4.5,
        "review_count": 634,
        "features": {
            "accommodation": "2-star surf hostel",
            "amenities": ["surf_school", "common_room", "bbq", "beach_bar"],
            "room_type": "Private Room",
            "suitable_for": ["surfing", "adventure", "solo", "groups"],
            "accessibility": []
        },
        "urgency": {
            "ending_soon": False,
            "spots_left": 16,
            "last_booked": "2 hours ago"
        }
    },
    {
        "id": "sopot-jazz-hotel",
        "type": "hotel",
        "title": "Sopot Jazz Club Hotel",
        "destination": {
            "city": "Sopot",
            "country": "Poland",
            "region": "Pomerania",
            "coordinates": CITY_COORDINATES["Sopot"]
        },
        "dates": {
            "available_from": "2025-04-01",
            "available_to": "2025-10-31",
            "blackout_dates": [],
            "min_nights": 2,
            "max_nights": 7
        },
        "pricing": {
            "original_price": 580,
            "deal_price": 389,
            "discount_percent": 33,
            "currency": "GBP",
            "per": "room",
            "includes": ["breakfast", "wifi", "jazz_concert_tickets"]
        },
        "images": [
            "https://images.unsplash.com/photo-1598970434795-0c54fe7c0648?w=800"
        ],
        "rating": 4.6,
        "review_count": 389,
        "features": {
            "accommodation": "3-star music hotel",
            "amenities": ["jazz_club", "restaurant", "bar", "terrace"],
            "room_type": "Music Themed Room",
            "suitable_for": ["music_lovers", "culture", "nightlife"],
            "accessibility": ["elevator"]
        },
        "urgency": {
            "ending_soon": False,
            "spots_left": 8,
            "last_booked": "3 hours ago"
        }
    }
]

# Helper function to get deals by city
def get_deals_by_city(city: str):
    return [deal for deal in TRAVEL_DEALS if deal["destination"]["city"] == city]

# Helper function to get all cities
def get_all_cities():
    return list(CITY_COORDINATES.keys())
