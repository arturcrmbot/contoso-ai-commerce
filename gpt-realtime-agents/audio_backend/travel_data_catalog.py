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
            "https://images.unsplash.com/photo-1601853895209-3a8a0b9f27a9?w=800",
            "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=800",
            "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800",
            "https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=800"
        ],
        "rating": 4.7,
        "review_count": 342,
        "address": {
            "street": "ul. Krakowskie Przedmieście 87/89",
            "city": "Warsaw",
            "postal_code": "00-079",
            "country": "Poland"
        },
        "contact": {
            "phone": "+48 22 826 1234",
            "email": "reservations@royalpalacehotel.pl",
            "website": "www.royalpalacehotel-warsaw.pl"
        },
        "features": {
            "accommodation": "4-star boutique hotel",
            "amenities": ["restaurant", "spa", "conference_room", "bar", "parking"],
            "room_type": "Deluxe Room with Old Town View",
            "room_types_available": ["Standard Double", "Deluxe Room", "Junior Suite", "Executive Suite"],
            "capacity": {"max_guests": 2, "max_adults": 2, "max_children": 1},
            "pets_allowed": False,
            "suitable_for": ["business", "couples", "culture"],
            "accessibility": ["elevator", "wheelchair_friendly"]
        },
        "detailed_amenities": {
            "general": ["free_wifi", "24h_reception", "concierge", "luggage_storage", "room_service"],
            "business": ["conference_room", "meeting_rooms", "business_center", "printing_service"],
            "wellness": ["spa", "gym", "massage_service", "sauna"],
            "dining": ["restaurant", "bar", "breakfast_buffet", "room_service"],
            "room": ["minibar", "safe", "air_conditioning", "flat_screen_tv", "coffee_maker"]
        },
        "rooms": [
            {
                "name": "Standard Double",
                "size_sqm": 28,
                "beds": "1 Queen Bed",
                "max_guests": 2,
                "features": ["AC", "City view", "Minibar", "Safe", "Work desk"]
            },
            {
                "name": "Deluxe Room with Old Town View",
                "size_sqm": 35,
                "beds": "1 King Bed",
                "max_guests": 2,
                "features": ["AC", "Old Town view", "Minibar", "Safe", "Seating area", "Coffee maker"]
            },
            {
                "name": "Junior Suite",
                "size_sqm": 45,
                "beds": "1 King Bed + Sofa bed",
                "max_guests": 3,
                "features": ["AC", "Old Town view", "Minibar", "Safe", "Living area", "Coffee maker", "Bathrobe"]
            },
            {
                "name": "Executive Suite",
                "size_sqm": 60,
                "beds": "1 King Bed + Sofa bed",
                "max_guests": 3,
                "features": ["AC", "Panoramic view", "Minibar", "Safe", "Separate living room", "Coffee machine", "Bathrobe", "Spa access"]
            }
        ],
        "reviews": [
            {
                "author": "Michael B.",
                "rating": 5,
                "date": "2025-02-10",
                "title": "Perfect location in Old Town",
                "text": "Stunning boutique hotel right in the heart of Warsaw's Old Town. The rooms are elegantly decorated with modern amenities. The spa was excellent and the restaurant serves outstanding Polish cuisine. Staff went above and beyond to make our stay memorable."
            },
            {
                "author": "Catherine L.",
                "rating": 5,
                "date": "2025-01-28",
                "title": "Business trip made luxurious",
                "text": "Stayed here for a conference and was thoroughly impressed. The conference facilities are top-notch, the room was spacious and quiet, and the breakfast buffet had excellent variety. Perfect for business travelers."
            },
            {
                "author": "James T.",
                "rating": 4,
                "date": "2025-01-15",
                "title": "Beautiful hotel with great service",
                "text": "Lovely hotel with a historic charm. The Old Town views from our room were spectacular. Only minor issue was occasional noise from the busy street below, but overall an excellent stay. Would definitely recommend."
            }
        ],
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
            "https://images.unsplash.com/photo-1581104478174-e041b34e1729?w=800",
            "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=800",
            "https://images.unsplash.com/photo-1595526114035-0d45ed16cfbf?w=800",
            "https://images.unsplash.com/photo-1578683010236-d716f9a3f461?w=800"
        ],
        "rating": 4.4,
        "review_count": 189,
        "address": {
            "street": "ul. Twarda 52",
            "city": "Warsaw",
            "postal_code": "00-831",
            "country": "Poland"
        },
        "contact": {
            "phone": "+48 22 654 7890",
            "email": "hello@modernloft-warsaw.pl",
            "website": "www.modernloft-warsaw.com"
        },
        "features": {
            "accommodation": "3-star modern hotel",
            "amenities": ["gym", "24h_reception", "kitchenette"],
            "room_type": "Studio Loft",
            "suitable_for": ["solo", "business", "budget"],
            "accessibility": ["elevator"]
        },
        "detailed_amenities": {
            "general": ["free_wifi", "24h_reception", "luggage_storage", "express_checkout"],
            "wellness": ["gym", "fitness_center"],
            "dining": ["breakfast_room", "coffee_bar", "vending_machines"],
            "room": ["kitchenette", "microwave", "mini_fridge", "flat_screen_tv", "work_desk"]
        },
        "rooms": [
            {
                "name": "Studio Loft",
                "size_sqm": 25,
                "beds": "1 Queen Bed",
                "max_guests": 2,
                "features": ["AC", "City view", "Kitchenette", "Work desk", "Smart TV"]
            },
            {
                "name": "Superior Studio",
                "size_sqm": 30,
                "beds": "1 King Bed",
                "max_guests": 2,
                "features": ["AC", "Skylight", "Kitchenette", "Dining table", "Work desk", "Premium bedding"]
            },
            {
                "name": "Deluxe Loft",
                "size_sqm": 38,
                "beds": "1 King Bed + Sofa bed",
                "max_guests": 3,
                "features": ["AC", "High ceiling", "Full kitchenette", "Living area", "Work desk", "Balcony"]
            }
        ],
        "reviews": [
            {
                "author": "David S.",
                "rating": 4,
                "date": "2025-02-18",
                "title": "Great value in city center",
                "text": "Perfect for a business trip. The location is excellent, just minutes from the central station. The loft-style room was modern and clean, and the kitchenette was very handy. Great value for money in such a central location."
            },
            {
                "author": "Emma W.",
                "rating": 5,
                "date": "2025-02-05",
                "title": "Modern and convenient",
                "text": "Loved the contemporary design and the kitchenette was perfect for preparing quick meals. The gym was well-equipped and the 24-hour reception was helpful when I had a late check-in. Would stay again!"
            },
            {
                "author": "Robert K.",
                "rating": 4,
                "date": "2025-01-22",
                "title": "Good for solo travelers",
                "text": "Clean, modern room with everything you need. The kitchenette saved me money on meals. Only downside is that the room can feel a bit small if you have large luggage, but overall a solid choice for the price."
            }
        ],
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
            "https://images.unsplash.com/photo-1609137144813-7d9921338f24?w=800",
            "https://images.unsplash.com/photo-1564501049412-61c2a3083791?w=800",
            "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=800",
            "https://images.unsplash.com/photo-1596394516093-501ba68a0ba6?w=800",
            "https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=800"
        ],
        "rating": 4.9,
        "review_count": 567,
        "address": {
            "street": "ul. Senatorska 29",
            "city": "Warsaw",
            "postal_code": "00-099",
            "country": "Poland"
        },
        "contact": {
            "phone": "+48 22 556 9000",
            "email": "reservations@palacegarden.pl",
            "website": "www.palacegardenwarsaw.com"
        },
        "features": {
            "accommodation": "5-star luxury hotel",
            "amenities": ["spa", "pool", "restaurant", "concierge", "parking", "bar"],
            "room_type": "Executive Suite",
            "suitable_for": ["luxury", "honeymoon", "couples"],
            "accessibility": ["elevator", "wheelchair_friendly", "accessible_bathroom"]
        },
        "detailed_amenities": {
            "general": ["free_wifi", "24h_concierge", "valet_parking", "luggage_storage", "room_service"],
            "luxury": ["limousine_service", "butler_service", "private_check_in", "turndown_service"],
            "wellness": ["luxury_spa", "indoor_pool", "sauna", "steam_room", "massage_service", "beauty_salon"],
            "dining": ["fine_dining_restaurant", "lobby_bar", "in_room_dining", "champagne_bar"],
            "room": ["premium_minibar", "nespresso_machine", "smart_tv", "safe", "bathrobe_slippers", "luxury_toiletries"]
        },
        "rooms": [
            {
                "name": "Deluxe Room",
                "size_sqm": 42,
                "beds": "1 King Bed",
                "max_guests": 2,
                "features": ["AC", "Garden view", "Marble bathroom", "Walk-in shower", "Premium minibar", "Nespresso"]
            },
            {
                "name": "Executive Suite",
                "size_sqm": 65,
                "beds": "1 King Bed",
                "max_guests": 2,
                "features": ["AC", "Palace view", "Marble bathroom", "Separate living room", "Premium minibar", "Nespresso", "Bathtub"]
            },
            {
                "name": "Royal Suite",
                "size_sqm": 85,
                "beds": "1 King Bed + Sofa bed",
                "max_guests": 3,
                "features": ["AC", "Panoramic view", "Luxury bathroom", "Separate living room", "Dining area", "Premium minibar", "Butler service"]
            },
            {
                "name": "Presidential Suite",
                "size_sqm": 120,
                "beds": "1 King Bed + Extra room",
                "max_guests": 4,
                "features": ["AC", "360° views", "Master bathroom", "Guest bathroom", "Private terrace", "Full kitchen", "Butler service", "Piano"]
            }
        ],
        "reviews": [
            {
                "author": "Alexandra M.",
                "rating": 5,
                "date": "2025-02-12",
                "title": "Unparalleled luxury experience",
                "text": "This hotel exceeded all expectations. From the moment we arrived, we were treated like royalty. The Executive Suite was breathtaking with palace views. The spa is world-class and the fine dining restaurant deserves its Michelin recognition. Perfect for our anniversary."
            },
            {
                "author": "William H.",
                "rating": 5,
                "date": "2025-01-30",
                "title": "Best hotel in Warsaw",
                "text": "Simply the finest hotel I've stayed at in Poland. The attention to detail is remarkable, from the luxurious rooms to the exceptional service. The indoor pool and spa are stunning. Airport transfer was seamless. Worth every penny."
            },
            {
                "author": "Sophie D.",
                "rating": 5,
                "date": "2025-01-18",
                "title": "Honeymoon perfection",
                "text": "We spent our honeymoon here and it was magical. The staff arranged champagne and roses in our suite. The spa treatments were incredible and the restaurant served the best meal we had in Warsaw. Cannot recommend highly enough for special occasions."
            }
        ],
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
            "https://images.unsplash.com/photo-1601853895209-3a8a0b9f27a9?w=800",
            "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800",
            "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?w=800",
            "https://images.unsplash.com/photo-1445019980597-93fa8acb246c?w=800"
        ],
        "rating": 4.5,
        "review_count": 223,
        "address": {
            "street": "ul. Wybrzeże Kościuszkowskie 31",
            "city": "Warsaw",
            "postal_code": "00-379",
            "country": "Poland"
        },
        "contact": {
            "phone": "+48 22 443 2100",
            "email": "stay@riversideinn.pl",
            "website": "www.vistulariversideinn.pl"
        },
        "features": {
            "accommodation": "3-star riverside hotel",
            "amenities": ["restaurant", "terrace", "bike_rental", "river_view"],
            "room_type": "River View Room",
            "suitable_for": ["families", "couples", "nature"],
            "accessibility": ["elevator"]
        },
        "detailed_amenities": {
            "general": ["free_wifi", "24h_reception", "luggage_storage", "free_parking"],
            "recreation": ["bike_rental", "river_terrace", "jogging_path", "boat_tours"],
            "dining": ["riverside_restaurant", "terrace_bar", "breakfast_buffet"],
            "room": ["flat_screen_tv", "coffee_maker", "safe", "air_conditioning", "river_view"]
        },
        "rooms": [
            {
                "name": "Standard Room",
                "size_sqm": 24,
                "beds": "1 Queen Bed",
                "max_guests": 2,
                "features": ["AC", "City view", "Coffee maker", "Work desk", "Smart TV"]
            },
            {
                "name": "River View Room",
                "size_sqm": 28,
                "beds": "1 Queen Bed",
                "max_guests": 2,
                "features": ["AC", "River view", "Balcony", "Coffee maker", "Mini fridge"]
            },
            {
                "name": "Family River View",
                "size_sqm": 38,
                "beds": "1 Queen + 2 Singles",
                "max_guests": 4,
                "features": ["AC", "River view", "Balcony", "Seating area", "Coffee maker", "Mini fridge"]
            }
        ],
        "reviews": [
            {
                "author": "Jennifer L.",
                "rating": 5,
                "date": "2025-02-15",
                "title": "Beautiful riverside location",
                "text": "The river views are absolutely stunning, especially at sunset. The bike rental was perfect for exploring the riverside paths. Restaurant serves great Polish food and the terrace is lovely. Very peaceful despite being in the city."
            },
            {
                "author": "Mark P.",
                "rating": 4,
                "date": "2025-02-03",
                "title": "Great for families",
                "text": "Wonderful hotel for a family stay. The kids loved being by the river and the bikes were a huge hit. The family room was spacious and comfortable. Good breakfast selection. Only small issue was limited parking, but overall excellent value."
            },
            {
                "author": "Lisa K.",
                "rating": 5,
                "date": "2025-01-20",
                "title": "Relaxing retreat",
                "text": "Perfect escape from the busy city center while still being easily accessible. The river terrace is so relaxing and the staff arranged a boat tour for us. Clean rooms, friendly service, and great breakfast. Highly recommend!"
            }
        ],
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
            "https://images.unsplash.com/photo-1581104478174-e041b34e1729?w=800",
            "https://images.unsplash.com/photo-1590073844006-33379778ae09?w=800",
            "https://images.unsplash.com/photo-1618773928121-c32242e63f39?w=800",
            "https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=800"
        ],
        "rating": 4.6,
        "review_count": 298,
        "address": {
            "street": "ul. Marszałkowska 115",
            "city": "Warsaw",
            "postal_code": "00-102",
            "country": "Poland"
        },
        "contact": {
            "phone": "+48 22 333 4567",
            "email": "contact@culturehub-warsaw.pl",
            "website": "www.culturehubhotel.com"
        },
        "features": {
            "accommodation": "4-star design hotel",
            "amenities": ["restaurant", "gallery", "rooftop_bar", "library"],
            "room_type": "Designer Room",
            "suitable_for": ["culture", "art_lovers", "couples"],
            "accessibility": ["elevator"]
        },
        "detailed_amenities": {
            "general": ["free_wifi", "24h_reception", "concierge", "luggage_storage"],
            "culture": ["art_gallery", "library", "cultural_events", "artist_workshops", "exhibition_space"],
            "dining": ["restaurant", "rooftop_bar", "breakfast_buffet", "coffee_lounge"],
            "room": ["designer_furniture", "smart_tv", "bluetooth_speaker", "coffee_maker", "safe"]
        },
        "rooms": [
            {
                "name": "Designer Room",
                "size_sqm": 30,
                "beds": "1 Queen Bed",
                "max_guests": 2,
                "features": ["AC", "City view", "Custom artwork", "Designer furniture", "Smart lighting"]
            },
            {
                "name": "Gallery Suite",
                "size_sqm": 42,
                "beds": "1 King Bed",
                "max_guests": 2,
                "features": ["AC", "Gallery view", "Original artworks", "Designer furniture", "Seating area", "Vinyl player"]
            },
            {
                "name": "Artist Loft",
                "size_sqm": 55,
                "beds": "1 King Bed + Sofa bed",
                "max_guests": 3,
                "features": ["AC", "Skylight", "Art studio setup", "Custom furniture", "Living area", "Work desk", "Balcony"]
            }
        ],
        "reviews": [
            {
                "author": "Isabella R.",
                "rating": 5,
                "date": "2025-02-08",
                "title": "A cultural gem",
                "text": "This hotel is a work of art itself! Every room features unique pieces from Polish artists. The gallery hosts fantastic exhibitions and the rooftop bar has amazing city views. Perfect for art enthusiasts. The staff are knowledgeable and passionate about culture."
            },
            {
                "author": "Daniel M.",
                "rating": 5,
                "date": "2025-01-25",
                "title": "Unique and inspiring",
                "text": "Stayed in the Artist Loft and loved every minute. The design is impeccable and the cultural events they organize are wonderful. Library has a great collection. Restaurant serves creative cuisine. This is more than a hotel, it's an experience."
            },
            {
                "author": "Rachel T.",
                "rating": 4,
                "date": "2025-01-12",
                "title": "Design lovers paradise",
                "text": "Beautiful hotel with incredible attention to design details. The art gallery access is a great bonus. Rooftop bar is trendy and serves excellent cocktails. Room was stylish and comfortable. Breakfast could have more variety but overall a wonderful stay."
            }
        ],
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
            "https://images.unsplash.com/photo-1609137144813-7d9921338f24?w=800",
            "https://images.unsplash.com/photo-1590490360182-c33d57733427?w=800",
            "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?w=800",
            "https://images.unsplash.com/photo-1578683010236-d716f9a3f461?w=800"
        ],
        "rating": 4.2,
        "review_count": 456,
        "address": {
            "street": "ul. Komitetu Obrony Robotników 49",
            "city": "Warsaw",
            "postal_code": "02-146",
            "country": "Poland"
        },
        "contact": {
            "phone": "+48 22 123 9876",
            "email": "reservations@airportexpress.pl",
            "website": "www.warsawairporthotel.com"
        },
        "features": {
            "accommodation": "3-star airport hotel",
            "amenities": ["restaurant", "24h_reception", "free_shuttle", "parking"],
            "room_type": "Standard Room",
            "suitable_for": ["business", "transit", "solo"],
            "accessibility": ["elevator", "wheelchair_friendly"]
        },
        "detailed_amenities": {
            "general": ["free_wifi", "24h_reception", "luggage_storage", "express_checkout", "currency_exchange"],
            "business": ["business_center", "meeting_room", "printing_service"],
            "transport": ["free_airport_shuttle", "free_parking", "car_rental_desk", "taxi_service"],
            "dining": ["restaurant", "24h_snack_bar", "breakfast_buffet"],
            "room": ["soundproof_windows", "blackout_curtains", "flat_screen_tv", "coffee_maker", "safe"]
        },
        "rooms": [
            {
                "name": "Standard Room",
                "size_sqm": 22,
                "beds": "1 Queen Bed or 2 Singles",
                "max_guests": 2,
                "features": ["AC", "Soundproof", "Blackout curtains", "Work desk", "Coffee maker"]
            },
            {
                "name": "Business Room",
                "size_sqm": 26,
                "beds": "1 King Bed",
                "max_guests": 2,
                "features": ["AC", "Soundproof", "Large work desk", "Ergonomic chair", "Coffee maker", "Iron"]
            },
            {
                "name": "Family Room",
                "size_sqm": 32,
                "beds": "1 Queen + 2 Singles",
                "max_guests": 4,
                "features": ["AC", "Soundproof", "Seating area", "Mini fridge", "Coffee maker", "Extra space"]
            }
        ],
        "reviews": [
            {
                "author": "Thomas B.",
                "rating": 4,
                "date": "2025-02-20",
                "title": "Perfect for airport layover",
                "text": "Exactly what you need for an airport hotel. Free shuttle runs every 20 minutes, room was quiet despite proximity to airport. Check-in was quick, breakfast was good. Ideal for early flights or layovers."
            },
            {
                "author": "Sandra M.",
                "rating": 4,
                "date": "2025-02-07",
                "title": "Convenient and efficient",
                "text": "Great for business travelers. The shuttle service is reliable and the room had everything I needed for work. Soundproofing is excellent. Restaurant stays open late which is helpful for evening arrivals. Good value."
            },
            {
                "author": "Kevin P.",
                "rating": 5,
                "date": "2025-01-28",
                "title": "Stress-free transit stay",
                "text": "Stayed here between connecting flights and it was perfect. Super close to airport, free parking, comfortable bed, and good breakfast. Staff were helpful with arranging early shuttle. Would definitely use again for layovers."
            }
        ],
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
            "https://images.unsplash.com/photo-1601853895209-3a8a0b9f27a9?w=800",
            "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=800",
            "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800",
            "https://images.unsplash.com/photo-1502672260066-6bc35f0a1f80?w=800"
        ],
        "rating": 4.8,
        "review_count": 178,
        "address": {
            "street": "ul. Żurawia 24",
            "city": "Warsaw",
            "postal_code": "00-515",
            "country": "Poland"
        },
        "contact": {
            "phone": "+48 22 789 4321",
            "email": "booking@familynest.pl",
            "website": "www.familynest-warsaw.com"
        },
        "features": {
            "accommodation": "4-star apartment hotel",
            "amenities": ["kitchen", "washing_machine", "parking", "playground"],
            "room_type": "2-Bedroom Apartment",
            "suitable_for": ["families", "long_stay", "groups"],
            "accessibility": ["elevator"]
        },
        "detailed_amenities": {
            "general": ["free_wifi", "free_parking", "reception", "luggage_storage", "concierge"],
            "family": ["playground", "kids_playroom", "high_chairs", "baby_cots_available", "family_activities"],
            "apartment": ["full_kitchen", "washing_machine", "dishwasher", "dining_table", "living_room"],
            "room": ["flat_screen_tv", "coffee_maker", "safe", "iron", "air_conditioning"]
        },
        "rooms": [
            {
                "name": "1-Bedroom Apartment",
                "size_sqm": 55,
                "beds": "1 King Bed + Sofa bed",
                "max_guests": 4,
                "features": ["AC", "Full kitchen", "Living room", "Washing machine", "Balcony", "Dining area"]
            },
            {
                "name": "2-Bedroom Apartment",
                "size_sqm": 75,
                "beds": "1 King + 2 Singles",
                "max_guests": 5,
                "features": ["AC", "Full kitchen", "Living room", "Washing machine", "2 bathrooms", "Balcony", "Dining area"]
            },
            {
                "name": "3-Bedroom Family Apartment",
                "size_sqm": 95,
                "beds": "1 King + 2 Queens",
                "max_guests": 7,
                "features": ["AC", "Full kitchen", "Large living room", "Washing machine", "2 bathrooms", "Balcony", "Play area"]
            }
        ],
        "reviews": [
            {
                "author": "Patricia G.",
                "rating": 5,
                "date": "2025-02-14",
                "title": "Perfect for families with children",
                "text": "We stayed for a week with our two kids and it was wonderful. The apartment had everything we needed - full kitchen, washing machine, plenty of space. The playground kept the kids entertained and the location is convenient. Felt like home away from home."
            },
            {
                "author": "James F.",
                "rating": 5,
                "date": "2025-01-30",
                "title": "Excellent for longer stays",
                "text": "Stayed here for 10 days while working in Warsaw. Having a kitchen saved so much money on meals and the apartment was spacious and comfortable. Free parking is a huge plus in Warsaw. Staff were helpful and responsive. Highly recommended for families or longer visits."
            },
            {
                "author": "Maria S.",
                "rating": 4,
                "date": "2025-01-17",
                "title": "Great value for groups",
                "text": "Booked the 3-bedroom apartment for our family reunion. Plenty of space for everyone and having multiple bathrooms was convenient. Kitchen was well-equipped. Kids loved the playroom. Only minor issue was Wi-Fi could be faster, but overall excellent value for the price."
            }
        ],
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
            "https://images.unsplash.com/photo-1587974928442-77dc3e0dba72?w=800",
            "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?w=800",
            "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800",
            "https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=800"
        ],
        "rating": 4.8,
        "review_count": 892,
        "address": {
            "street": "Nerudova 211/44",
            "city": "Prague",
            "postal_code": "118 00",
            "country": "Czech Republic"
        },
        "contact": {
            "phone": "+420 257 532 088",
            "email": "reservations@castleviewheritage.cz",
            "website": "www.castleviewprague.com"
        },
        "features": {
            "accommodation": "5-star heritage hotel",
            "amenities": ["spa", "restaurant", "bar", "concierge", "parking"],
            "room_type": "Castle View Suite",
            "suitable_for": ["romantic", "luxury", "honeymoon"],
            "accessibility": ["elevator"]
        },
        "detailed_amenities": {
            "general": ["free_wifi", "24h_concierge", "valet_parking", "luggage_storage", "room_service"],
            "luxury": ["private_castle_tours", "champagne_welcome", "butler_service", "turndown_service"],
            "wellness": ["luxury_spa", "massage_treatments", "sauna", "hot_tub"],
            "dining": ["fine_dining_restaurant", "rooftop_bar", "breakfast_terrace", "in_room_dining"],
            "room": ["premium_minibar", "nespresso_machine", "smart_tv", "safe", "luxury_toiletries", "bathrobe"]
        },
        "rooms": [
            {
                "name": "Superior Room",
                "size_sqm": 35,
                "beds": "1 King Bed",
                "max_guests": 2,
                "features": ["AC", "City view", "Marble bathroom", "Minibar", "Nespresso", "Safe"]
            },
            {
                "name": "Castle View Suite",
                "size_sqm": 55,
                "beds": "1 King Bed",
                "max_guests": 2,
                "features": ["AC", "Castle view", "Marble bathroom", "Living area", "Premium minibar", "Nespresso", "Balcony"]
            },
            {
                "name": "Royal Suite",
                "size_sqm": 75,
                "beds": "1 King Bed + Sofa bed",
                "max_guests": 3,
                "features": ["AC", "Panoramic castle view", "Luxury bathroom", "Separate living room", "Dining area", "Butler service"]
            },
            {
                "name": "Presidential Suite",
                "size_sqm": 110,
                "beds": "1 King + Extra bed",
                "max_guests": 4,
                "features": ["AC", "360° views", "Master bathroom", "Private terrace", "Full bar", "Piano", "Butler service"]
            }
        ],
        "reviews": [
            {
                "author": "Charlotte W.",
                "rating": 5,
                "date": "2025-02-16",
                "title": "Magical castle views",
                "text": "The views of Prague Castle from our suite were absolutely breathtaking, especially at night when it's illuminated. The private castle tour arranged by the concierge was fascinating. Spa treatments were world-class. Perfect honeymoon destination!"
            },
            {
                "author": "Henry M.",
                "rating": 5,
                "date": "2025-02-01",
                "title": "Unmatched elegance",
                "text": "This heritage hotel combines historic charm with modern luxury perfectly. The Presidential Suite exceeded all expectations. Fine dining restaurant deserves its recognition. Staff attention to detail is impeccable. Best hotel experience in Prague."
            },
            {
                "author": "Victoria L.",
                "rating": 5,
                "date": "2025-01-19",
                "title": "Romantic perfection",
                "text": "Celebrated our anniversary here and it was magical. The champagne welcome, rose petals, and castle views created an unforgettable atmosphere. Breakfast on the terrace overlooking the castle is a must. Cannot recommend highly enough for special occasions."
            }
        ],
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
            "https://images.unsplash.com/photo-1592906209472-a36b1f3782ef?w=800",
            "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800",
            "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=800",
            "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?w=800"
        ],
        "rating": 4.6,
        "review_count": 534,
        "address": {
            "street": "Karlova 188/2",
            "city": "Prague",
            "postal_code": "110 00",
            "country": "Czech Republic"
        },
        "contact": {
            "phone": "+420 222 220 888",
            "email": "stay@charlesbridgeinn.cz",
            "website": "www.charlesbridgeboutique.com"
        },
        "features": {
            "accommodation": "4-star boutique hotel",
            "amenities": ["restaurant", "bar", "historic_building"],
            "room_type": "Bridge View Room",
            "suitable_for": ["romantic", "couples", "culture"],
            "accessibility": []
        },
        "detailed_amenities": {
            "general": ["free_wifi", "24h_reception", "concierge", "luggage_storage"],
            "historic": ["historic_building", "original_architecture", "heritage_tours", "period_features"],
            "dining": ["traditional_restaurant", "wine_bar", "breakfast_room"],
            "room": ["antique_furniture", "flat_screen_tv", "minibar", "safe", "coffee_maker"]
        },
        "rooms": [
            {
                "name": "Classic Room",
                "size_sqm": 26,
                "beds": "1 Queen Bed",
                "max_guests": 2,
                "features": ["Historic decor", "City view", "Antique furniture", "Minibar", "Safe"]
            },
            {
                "name": "Bridge View Room",
                "size_sqm": 32,
                "beds": "1 King Bed",
                "max_guests": 2,
                "features": ["Bridge view", "Period features", "Seating area", "Minibar", "Coffee maker"]
            },
            {
                "name": "Junior Suite",
                "size_sqm": 42,
                "beds": "1 King Bed + Sofa",
                "max_guests": 3,
                "features": ["Bridge view", "Separate sitting area", "Original beams", "Minibar", "Bathtub"]
            }
        ],
        "reviews": [
            {
                "author": "Oliver S.",
                "rating": 5,
                "date": "2025-02-11",
                "title": "Historic charm at its finest",
                "text": "This boutique hotel is housed in a beautifully preserved historic building just steps from Charles Bridge. Our room had original wooden beams and period features while still offering modern comfort. The restaurant serves excellent Czech cuisine. Perfect romantic getaway."
            },
            {
                "author": "Amelia K.",
                "rating": 5,
                "date": "2025-01-27",
                "title": "Incredible location and character",
                "text": "Waking up to views of Charles Bridge was magical. The hotel beautifully preserves its historic character with antique furniture and original architecture. Staff are knowledgeable about Prague's history. Walking distance to everything. Highly recommended for couples."
            },
            {
                "author": "Lucas M.",
                "rating": 4,
                "date": "2025-01-14",
                "title": "Charming but note the stairs",
                "text": "Beautiful historic hotel with wonderful atmosphere and great location. Rooms are cozy with authentic period details. Wine bar is excellent. Only note there's no elevator, so be prepared for stairs. But the charm and location more than make up for it."
            }
        ],
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
            "https://images.unsplash.com/photo-1587974928442-77dc3e0dba72?w=800",
            "https://images.unsplash.com/photo-1564501049412-61c2a3083791?w=800",
            "https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=800",
            "https://images.unsplash.com/photo-1596394516093-501ba68a0ba6?w=800",
            "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=800"
        ],
        "rating": 4.9,
        "review_count": 1023,
        "address": {
            "street": "Staroměstské náměstí 24",
            "city": "Prague",
            "postal_code": "110 00",
            "country": "Czech Republic"
        },
        "contact": {
            "phone": "+420 221 771 200",
            "email": "reservations@oldtownpalace.cz",
            "website": "www.oldtownsquarepalace.com"
        },
        "features": {
            "accommodation": "5-star palace hotel",
            "amenities": ["spa", "restaurant", "bar", "concierge", "rooftop_terrace"],
            "room_type": "Royal Suite",
            "suitable_for": ["luxury", "honeymoon", "special_occasion"],
            "accessibility": ["elevator", "wheelchair_friendly"]
        },
        "detailed_amenities": {
            "general": ["free_wifi", "24h_concierge", "valet_parking", "luggage_storage", "room_service"],
            "luxury": ["champagne_bar", "private_shopping", "limousine_service", "butler_service", "personal_stylist"],
            "wellness": ["luxury_spa", "indoor_pool", "sauna", "steam_room", "beauty_treatments", "fitness_center"],
            "dining": ["michelin_restaurant", "champagne_bar", "rooftop_terrace", "in_room_dining", "private_dining"],
            "room": ["premium_minibar", "nespresso_machine", "smart_tv", "safe", "luxury_linens", "designer_toiletries"]
        },
        "rooms": [
            {
                "name": "Deluxe Room",
                "size_sqm": 40,
                "beds": "1 King Bed",
                "max_guests": 2,
                "features": ["AC", "Square view", "Marble bathroom", "Walk-in closet", "Premium minibar", "Nespresso"]
            },
            {
                "name": "Executive Suite",
                "size_sqm": 70,
                "beds": "1 King Bed",
                "max_guests": 2,
                "features": ["AC", "Square view", "Luxury bathroom", "Separate living room", "Dining area", "Premium minibar"]
            },
            {
                "name": "Royal Suite",
                "size_sqm": 95,
                "beds": "1 King Bed + Sofa bed",
                "max_guests": 3,
                "features": ["AC", "Panoramic square view", "Master bathroom", "Living room", "Dining room", "Butler service", "Terrace"]
            },
            {
                "name": "Presidential Suite",
                "size_sqm": 140,
                "beds": "1 King + Extra bedroom",
                "max_guests": 4,
                "features": ["AC", "360° views", "Master suite", "Guest suite", "Private terrace", "Full kitchen", "Butler", "Grand piano"]
            }
        ],
        "reviews": [
            {
                "author": "Sebastian L.",
                "rating": 5,
                "date": "2025-02-09",
                "title": "The epitome of luxury",
                "text": "This palace hotel is absolutely magnificent. Our Royal Suite overlooking Old Town Square was breathtaking. The Michelin restaurant exceeded expectations, spa treatments were divine, and the champagne bar on the rooftop is spectacular. Flawless service throughout our stay."
            },
            {
                "author": "Gabriella R.",
                "rating": 5,
                "date": "2025-01-24",
                "title": "Unforgettable honeymoon",
                "text": "We celebrated our honeymoon here and it was perfection. The butler service anticipated our every need, the champagne welcome was elegant, and watching the Astronomical Clock from our suite was magical. The spa and indoor pool are world-class. Worth every penny!"
            },
            {
                "author": "Christopher D.",
                "rating": 5,
                "date": "2025-01-11",
                "title": "Best hotel in Prague",
                "text": "Having stayed at many luxury hotels, this is truly special. The location on Old Town Square is unbeatable, rooms are palatial, and the service is impeccable. Private dining experience was extraordinary. Perfect for celebrating special occasions."
            }
        ],
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
            "https://images.unsplash.com/photo-1541849546-216549ae216d?w=800",
            "https://images.unsplash.com/photo-1590073844006-33379778ae09?w=800",
            "https://images.unsplash.com/photo-1618773928121-c32242e63f39?w=800",
            "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800"
        ],
        "rating": 4.7,
        "review_count": 412,
        "address": {
            "street": "Na Příkopě 22",
            "city": "Prague",
            "postal_code": "110 00",
            "country": "Czech Republic"
        },
        "contact": {
            "phone": "+420 224 234 111",
            "email": "info@artnouveauprague.cz",
            "website": "www.artnouveaudesignhotel.com"
        },
        "features": {
            "accommodation": "4-star design hotel",
            "amenities": ["restaurant", "bar", "art_gallery", "library"],
            "room_type": "Art Deco Room",
            "suitable_for": ["art_lovers", "culture", "couples"],
            "accessibility": ["elevator"]
        },
        "detailed_amenities": {
            "general": ["free_wifi", "24h_reception", "concierge", "luggage_storage"],
            "art_culture": ["art_gallery", "library", "art_workshops", "curated_exhibitions", "design_store"],
            "dining": ["contemporary_restaurant", "design_bar", "breakfast_lounge"],
            "room": ["designer_furniture", "art_pieces", "smart_tv", "nespresso", "safe", "premium_linens"]
        },
        "rooms": [
            {
                "name": "Art Deco Room",
                "size_sqm": 32,
                "beds": "1 Queen Bed",
                "max_guests": 2,
                "features": ["AC", "Art Deco design", "Custom furniture", "Original artwork", "Nespresso"]
            },
            {
                "name": "Art Nouveau Suite",
                "size_sqm": 48,
                "beds": "1 King Bed",
                "max_guests": 2,
                "features": ["AC", "Art Nouveau features", "Living area", "Designer furniture", "Gallery views", "Bathtub"]
            },
            {
                "name": "Designer Loft",
                "size_sqm": 60,
                "beds": "1 King Bed + Sofa bed",
                "max_guests": 3,
                "features": ["AC", "High ceilings", "Contemporary art", "Full living area", "Designer kitchen", "Balcony"]
            }
        ],
        "reviews": [
            {
                "author": "Francesca T.",
                "rating": 5,
                "date": "2025-02-13",
                "title": "A masterpiece of design",
                "text": "This hotel is a work of art! Every room features carefully curated pieces and the Art Nouveau Suite was breathtaking. The gallery exhibitions are world-class and the art workshops were fascinating. Design bar has creative cocktails. Perfect for art and design enthusiasts."
            },
            {
                "author": "Marcus W.",
                "rating": 5,
                "date": "2025-01-29",
                "title": "Inspiring and beautiful",
                "text": "Stayed here for a design conference and was blown away. The attention to artistic detail is remarkable, from the custom furniture to the curated artwork in each room. Library has an excellent collection. Staff are knowledgeable about Prague's art scene."
            },
            {
                "author": "Nina P.",
                "rating": 4,
                "date": "2025-01-16",
                "title": "Unique cultural experience",
                "text": "Beautiful hotel that celebrates Art Nouveau heritage while being thoroughly modern. The art gallery access is fantastic and the design store has unique pieces. Restaurant serves creative cuisine. Only minor issue was some street noise, but earplugs provided. Highly recommended for culture lovers."
            }
        ],
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
            "country": "Czech Republic",
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
            "https://images.unsplash.com/photo-1592906209472-a36b1f3782ef?w=800",
            "https://images.unsplash.com/photo-1540555700478-4be289fbecef?w=800",
            "https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=800",
            "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800"
        ],
        "rating": 4.5,
        "review_count": 687,
        "address": {
            "street": "Rybná 685/7",
            "city": "Prague",
            "postal_code": "110 00",
            "country": "Czech Republic"
        },
        "contact": {
            "phone": "+420 222 333 444",
            "email": "bookings@czechbeerspa.cz",
            "website": "www.praguebeerspahotel.com"
        },
        "features": {
            "accommodation": "3-star spa hotel",
            "amenities": ["beer_spa", "restaurant", "bar", "sauna"],
            "room_type": "Spa Room",
            "suitable_for": ["unique_experience", "groups", "couples"],
            "accessibility": ["elevator"]
        },
        "detailed_amenities": {
            "general": ["free_wifi", "24h_reception", "luggage_storage"],
            "spa_wellness": ["beer_spa_baths", "hop_treatments", "sauna", "relaxation_room", "massage_service"],
            "dining": ["czech_restaurant", "beer_bar", "tasting_room", "breakfast_buffet"],
            "room": ["comfortable_beds", "flat_screen_tv", "minibar", "safe", "bathrobe_provided"]
        },
        "rooms": [
            {
                "name": "Standard Spa Room",
                "size_sqm": 24,
                "beds": "1 Queen Bed",
                "max_guests": 2,
                "features": ["AC", "City view", "Modern bathroom", "Minibar", "Coffee maker"]
            },
            {
                "name": "Superior Spa Room",
                "size_sqm": 30,
                "beds": "1 King Bed",
                "max_guests": 2,
                "features": ["AC", "City view", "Bathtub", "Seating area", "Minibar", "Bathrobe"]
            },
            {
                "name": "Deluxe Spa Suite",
                "size_sqm": 40,
                "beds": "1 King Bed + Sofa bed",
                "max_guests": 3,
                "features": ["AC", "Separate living area", "Jacuzzi tub", "Minibar", "Extra spa treatment included"]
            }
        ],
        "reviews": [
            {
                "author": "Brian H.",
                "rating": 5,
                "date": "2025-02-17",
                "title": "Unique and fun experience!",
                "text": "The beer spa is absolutely fantastic - such a unique Czech experience! Soaking in warm beer baths with hops was surprisingly relaxing and the unlimited beer while bathing was a fun touch. Restaurant serves excellent traditional Czech food. Staff are friendly and fun. Highly recommend for groups!"
            },
            {
                "author": "Elena M.",
                "rating": 4,
                "date": "2025-02-04",
                "title": "One-of-a-kind spa",
                "text": "Never thought I'd bathe in beer, but it was amazing! The hop treatments left my skin feeling wonderful. Rooms are comfortable and clean. Beer bar has great selection. Perfect for couples looking for something different. Only small downside is it can get busy, so book spa times early."
            },
            {
                "author": "Max K.",
                "rating": 5,
                "date": "2025-01-21",
                "title": "Must-try in Prague",
                "text": "This place is a blast! The beer spa concept is executed perfectly - relaxing and entertaining. Great value for what you get. Restaurant has hearty Czech dishes. Central location makes exploring Prague easy. Perfect for bachelor parties or fun couples getaway."
            }
        ],
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
            "https://images.unsplash.com/photo-1587974928442-77dc3e0dba72?w=800",
            "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800",
            "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?w=800",
            "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=800"
        ],
        "rating": 4.6,
        "review_count": 378,
        "address": {
            "street": "Maiselova 15",
            "city": "Prague",
            "postal_code": "110 00",
            "country": "Czech Republic"
        },
        "contact": {
            "phone": "+420 222 317 555",
            "email": "reception@jewishquarterhotel.cz",
            "website": "www.jewishquarterhotel.com"
        },
        "features": {
            "accommodation": "4-star historic hotel",
            "amenities": ["restaurant", "library", "courtyard", "historic_tours"],
            "room_type": "Heritage Room",
            "suitable_for": ["culture", "history", "solo"],
            "accessibility": []
        },
        "detailed_amenities": {
            "general": ["free_wifi", "24h_reception", "concierge", "luggage_storage"],
            "cultural": ["library", "historic_tours", "courtyard", "heritage_exhibits", "cultural_programs"],
            "dining": ["traditional_restaurant", "courtyard_cafe", "breakfast_room"],
            "room": ["period_furniture", "flat_screen_tv", "minibar", "safe", "coffee_maker"]
        },
        "rooms": [
            {
                "name": "Heritage Room",
                "size_sqm": 28,
                "beds": "1 Queen Bed",
                "max_guests": 2,
                "features": ["Period decor", "Courtyard view", "Antique furniture", "Minibar", "Safe"]
            },
            {
                "name": "Superior Heritage Room",
                "size_sqm": 34,
                "beds": "1 King Bed",
                "max_guests": 2,
                "features": ["Historic features", "Quarter view", "Seating area", "Minibar", "Coffee maker"]
            },
            {
                "name": "Heritage Suite",
                "size_sqm": 45,
                "beds": "1 King Bed + Sofa",
                "max_guests": 3,
                "features": ["Original architecture", "Living area", "Courtyard view", "Minibar", "Bathtub"]
            }
        ],
        "reviews": [
            {
                "author": "Benjamin R.",
                "rating": 5,
                "date": "2025-02-19",
                "title": "Rich in history and culture",
                "text": "This hotel is a treasure trove of Jewish history. The guided tours of the quarter organized by the hotel were incredibly informative. The library has fascinating historical documents. Rooms beautifully preserve period features. Perfect for history enthusiasts."
            },
            {
                "author": "Ruth S.",
                "rating": 5,
                "date": "2025-02-06",
                "title": "Authentic and educational",
                "text": "Stayed here to explore Prague's Jewish heritage and couldn't have chosen better. The hotel staff are knowledgeable historians. The courtyard is peaceful and beautiful. Restaurant serves traditional recipes. Walking distance to all synagogues and museums. Highly recommend."
            },
            {
                "author": "David L.",
                "rating": 4,
                "date": "2025-01-23",
                "title": "Wonderful historic setting",
                "text": "Beautiful hotel in the heart of the Jewish Quarter. Rooms have authentic character with modern amenities. The cultural programs and walking tours are excellent. Only note that there's no elevator due to historic building regulations. But worth it for the atmosphere and location."
            }
        ],
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
            "https://images.unsplash.com/photo-1541849546-216549ae216d?w=800",
            "https://images.unsplash.com/photo-1555854877-bab0e564b8d5?w=800",
            "https://images.unsplash.com/photo-1506057278219-795838d4c2dd?w=800",
            "https://images.unsplash.com/photo-1578683010236-d716f9a3f461?w=800"
        ],
        "rating": 4.3,
        "review_count": 923,
        "address": {
            "street": "Sokolovská 112",
            "city": "Prague",
            "postal_code": "186 00",
            "country": "Czech Republic"
        },
        "contact": {
            "phone": "+420 220 871 111",
            "email": "info@praguecityhostel.com",
            "website": "www.praguecityhostel.com"
        },
        "features": {
            "accommodation": "2-star hostel",
            "amenities": ["common_room", "kitchen", "bar", "laundry"],
            "room_type": "Private Room",
            "suitable_for": ["budget", "solo", "backpackers"],
            "accessibility": []
        },
        "detailed_amenities": {
            "general": ["free_wifi", "24h_reception", "luggage_storage", "lockers"],
            "social": ["common_room", "hostel_bar", "games_room", "terrace", "organized_events"],
            "practical": ["shared_kitchen", "laundry_facilities", "vending_machines", "bike_storage"],
            "room": ["comfortable_beds", "bedding_included", "reading_lights", "power_outlets"]
        },
        "rooms": [
            {
                "name": "Private Room",
                "size_sqm": 16,
                "beds": "2 Singles or 1 Double",
                "max_guests": 2,
                "features": ["Shared bathroom", "Lockers", "Reading lights", "Desk"]
            },
            {
                "name": "Private Triple",
                "size_sqm": 20,
                "beds": "3 Singles",
                "max_guests": 3,
                "features": ["Shared bathroom", "Lockers", "Reading lights", "Storage space"]
            },
            {
                "name": "Private Quad",
                "size_sqm": 24,
                "beds": "4 Singles",
                "max_guests": 4,
                "features": ["Shared bathroom", "Lockers", "Reading lights", "Extra space"]
            }
        ],
        "reviews": [
            {
                "author": "Sophie T.",
                "rating": 4,
                "date": "2025-02-22",
                "title": "Great budget option",
                "text": "Perfect hostel for backpackers! Clean private rooms, great common areas to meet other travelers, and the bar has cheap drinks. Kitchen is well-equipped. Staff organize fun pub crawls and city tours. Good value for Prague."
            },
            {
                "author": "Jake M.",
                "rating": 5,
                "date": "2025-02-09",
                "title": "Social and clean",
                "text": "One of the best hostels I've stayed at. The private room was clean and comfortable, common room is great for socializing, and I met awesome people. Location is decent with good tram connections. Breakfast could be better but at this price point, it's excellent value."
            },
            {
                "author": "Emma B.",
                "rating": 4,
                "date": "2025-01-26",
                "title": "Budget traveler's dream",
                "text": "Clean, safe, and affordable. Staff are friendly and helpful with recommendations. The organized events are fun. Kitchen facilities are good. Only minor downside is it's not in the absolute center, but the tram stop is nearby. Would definitely stay again."
            }
        ],
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
            "https://images.unsplash.com/photo-1592906209472-a36b1f3782ef?w=800",
            "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800",
            "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?w=800",
            "https://images.unsplash.com/photo-1445019980597-93fa8acb246c?w=800"
        ],
        "rating": 4.7,
        "review_count": 445,
        "address": {
            "street": "Dvořákovo nábřeží 12",
            "city": "Prague",
            "postal_code": "110 00",
            "country": "Czech Republic"
        },
        "contact": {
            "phone": "+420 221 984 111",
            "email": "reservations@vltavariverhotel.cz",
            "website": "www.vltavariverhotel.com"
        },
        "features": {
            "accommodation": "4-star riverside hotel",
            "amenities": ["restaurant", "terrace", "river_view", "boat_tours"],
            "room_type": "River View Room",
            "suitable_for": ["romantic", "couples", "families"],
            "accessibility": ["elevator"]
        },
        "detailed_amenities": {
            "general": ["free_wifi", "24h_reception", "concierge", "luggage_storage"],
            "river_activities": ["river_cruises", "boat_tours", "private_charters", "sunset_cruises"],
            "dining": ["riverside_restaurant", "terrace_bar", "breakfast_terrace", "river_view_dining"],
            "room": ["river_views", "balconies", "flat_screen_tv", "minibar", "safe", "coffee_maker"]
        },
        "rooms": [
            {
                "name": "Standard Room",
                "size_sqm": 26,
                "beds": "1 Queen Bed",
                "max_guests": 2,
                "features": ["AC", "City view", "Modern bathroom", "Minibar", "Coffee maker"]
            },
            {
                "name": "River View Room",
                "size_sqm": 32,
                "beds": "1 King Bed",
                "max_guests": 2,
                "features": ["AC", "River view", "Balcony", "Seating area", "Minibar", "Nespresso"]
            },
            {
                "name": "Family River Suite",
                "size_sqm": 48,
                "beds": "1 King + 2 Singles",
                "max_guests": 4,
                "features": ["AC", "Panoramic river view", "Large balcony", "Living area", "Minibar", "2 bathrooms"]
            }
        ],
        "reviews": [
            {
                "author": "Andrew C.",
                "rating": 5,
                "date": "2025-02-14",
                "title": "River cruise included was amazing!",
                "text": "The included river cruise was the highlight of our stay! Seeing Prague from the Vltava River at sunset was magical. Our river view room had a perfect balcony for morning coffee. Restaurant has excellent Czech and international cuisine. Staff arranged a private dinner cruise for our anniversary."
            },
            {
                "author": "Jessica P.",
                "rating": 5,
                "date": "2025-01-31",
                "title": "Perfect riverside location",
                "text": "Wonderful hotel right on the Vltava River. The boat tours are fantastic and great value. Family suite was spacious with amazing views. Terrace restaurant is beautiful in good weather. Kids loved watching the boats. Great for families wanting something special."
            },
            {
                "author": "Martin K.",
                "rating": 4,
                "date": "2025-01-18",
                "title": "Romantic and scenic",
                "text": "Beautiful riverside hotel with stunning views. The sunset cruise was incredibly romantic. Rooms are comfortable and well-appointed. Restaurant quality is excellent. Only minor point is the breakfast could have more variety, but overall a wonderful experience. Highly recommended for couples."
            }
        ],
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
            "https://images.unsplash.com/photo-1551582045-6ec9c11d8697?w=800",
            "https://images.unsplash.com/photo-1519904981063-b0cf448d479e?w=800",
            "https://images.unsplash.com/photo-1605181379317-d6a5de8f2056?w=800",
            "https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=800"
        ],
        "rating": 4.8,
        "review_count": 567,
        "address": {
            "street": "ul. Droga do Białego 25",
            "city": "Zakopane",
            "postal_code": "34-500",
            "country": "Poland"
        },
        "contact": {
            "phone": "+48 18 206 7890",
            "email": "reservations@tatralodge.pl",
            "website": "www.tatramountainlodge.com"
        },
        "features": {
            "accommodation": "4-star mountain lodge",
            "amenities": ["spa", "sauna", "restaurant", "ski_storage", "parking"],
            "room_type": "Mountain View Room",
            "suitable_for": ["skiing", "families", "nature", "adventure"],
            "accessibility": ["elevator"]
        },
        "detailed_amenities": {
            "general": ["free_wifi", "24h_reception", "free_parking", "luggage_storage", "ski_storage"],
            "mountain_wellness": ["spa", "sauna", "steam_room", "massage_treatments", "hot_tub"],
            "skiing": ["ski_pass_office", "ski_storage", "equipment_rental_nearby", "ski_school_bookings"],
            "dining": ["mountain_restaurant", "fireside_bar", "breakfast_buffet", "packed_lunches"],
            "room": ["mountain_views", "balconies", "flat_screen_tv", "safe", "coffee_maker", "heating"]
        },
        "rooms": [
            {
                "name": "Standard Mountain Room",
                "size_sqm": 28,
                "beds": "1 Queen Bed",
                "max_guests": 2,
                "features": ["Heating", "Mountain view", "Balcony", "Safe", "Coffee maker"]
            },
            {
                "name": "Mountain View Room",
                "size_sqm": 34,
                "beds": "1 King Bed",
                "max_guests": 2,
                "features": ["Heating", "Tatra view", "Large balcony", "Seating area", "Minibar", "Bathrobe"]
            },
            {
                "name": "Family Mountain Suite",
                "size_sqm": 50,
                "beds": "1 King + 2 Singles",
                "max_guests": 4,
                "features": ["Heating", "Panoramic view", "2 balconies", "Living area", "Fireplace", "2 bathrooms"]
            },
            {
                "name": "Alpine Chalet Room",
                "size_sqm": 45,
                "beds": "1 King Bed + Sofa bed",
                "max_guests": 3,
                "features": ["Heating", "Mountain view", "Private terrace", "Fireplace", "Kitchenette", "Hot tub access"]
            }
        ],
        "reviews": [
            {
                "author": "Piotr W.",
                "rating": 5,
                "date": "2025-01-20",
                "title": "Perfect ski vacation",
                "text": "Amazing lodge with direct access to ski slopes! The included ski pass saved us hassle. Rooms have stunning Tatra views and the sauna after skiing was heavenly. Restaurant serves hearty mountain food. Staff are knowledgeable about ski conditions. Perfect for ski enthusiasts!"
            },
            {
                "author": "Anna M.",
                "rating": 5,
                "date": "2025-01-10",
                "title": "Mountain paradise",
                "text": "Stayed here with family and loved every minute. The Family Suite was spacious with amazing views. Spa facilities are excellent - hot tub with mountain views is incredible. Breakfast buffet has great variety. Kids loved the snow activities. Highly recommend!"
            },
            {
                "author": "Marek K.",
                "rating": 4,
                "date": "2025-01-05",
                "title": "Great mountain retreat",
                "text": "Beautiful lodge in perfect location for Tatra Mountains. Rooms are cozy and well-heated. Spa is relaxing after hiking. Restaurant quality is good. Only minor issue was Wi-Fi could be stronger, but when you're in the mountains, that's expected. Would definitely return!"
            }
        ],
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
            "https://images.unsplash.com/photo-1605181379317-d6a5de8f2056?w=800",
            "https://images.unsplash.com/photo-1519904981063-b0cf448d479e?w=800",
            "https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=800",
            "https://images.unsplash.com/photo-1605640840605-14ac1855827b?w=800",
            "https://images.unsplash.com/photo-1551582045-6ec9c11d8697?w=800"
        ],
        "rating": 4.9,
        "review_count": 892,
        "address": {
            "street": "ul. Przewodników Tatrzańskich 10",
            "city": "Zakopane",
            "postal_code": "34-500",
            "country": "Poland"
        },
        "contact": {
            "phone": "+48 18 200 5000",
            "email": "reservations@grandskiResort.pl",
            "website": "www.grandskizakopane.com"
        },
        "features": {
            "accommodation": "5-star ski resort",
            "amenities": ["spa", "pool", "restaurant", "ski_school", "equipment_rental", "parking"],
            "room_type": "Suite with Balcony",
            "suitable_for": ["skiing", "luxury", "families", "groups"],
            "accessibility": ["elevator", "wheelchair_friendly"]
        },
        "detailed_amenities": {
            "general": ["free_wifi", "24h_concierge", "valet_parking", "luggage_storage", "ski_valet"],
            "luxury_ski": ["ski_in_ski_out", "private_ski_school", "equipment_rental", "ski_concierge", "heated_boot_room"],
            "wellness": ["luxury_spa", "indoor_pool", "outdoor_hot_tub", "sauna", "steam_room", "massage", "beauty_salon"],
            "dining": ["fine_dining", "apres_ski_bar", "pool_bar", "breakfast_buffet", "room_service"],
            "room": ["mountain_views", "balconies", "fireplace", "minibar", "nespresso", "bathrobe", "premium_toiletries"]
        },
        "rooms": [
            {
                "name": "Deluxe Mountain Room",
                "size_sqm": 38,
                "beds": "1 King Bed",
                "max_guests": 2,
                "features": ["Heating", "Mountain view", "Balcony", "Fireplace", "Minibar", "Bathrobe"]
            },
            {
                "name": "Suite with Balcony",
                "size_sqm": 55,
                "beds": "1 King Bed + Sofa bed",
                "max_guests": 3,
                "features": ["Heating", "Panoramic view", "Large balcony", "Living area", "Fireplace", "Jacuzzi tub"]
            },
            {
                "name": "Family Ski Suite",
                "size_sqm": 75,
                "beds": "1 King + 2 Queens",
                "max_guests": 6,
                "features": ["Heating", "Ski slope view", "2 balconies", "2 bathrooms", "Living room", "Kitchenette"]
            },
            {
                "name": "Presidential Chalet Suite",
                "size_sqm": 120,
                "beds": "2 King Beds + Extra room",
                "max_guests": 6,
                "features": ["Heating", "360° views", "Private terrace", "Hot tub", "Full kitchen", "Fireplace", "Butler service"]
            }
        ],
        "reviews": [
            {
                "author": "Katarzyna B.",
                "rating": 5,
                "date": "2025-01-18",
                "title": "Ultimate luxury ski experience",
                "text": "This resort is world-class! Ski-in/ski-out access is incredibly convenient. Private ski lessons were excellent and equipment rental was seamless. The spa is stunning with mountain views from the hot tub. Fine dining restaurant is Michelin-worthy. Worth every zloty!"
            },
            {
                "author": "Tomasz G.",
                "rating": 5,
                "date": "2025-01-08",
                "title": "Perfect for families",
                "text": "Stayed with our family and kids in the Family Ski Suite - absolutely perfect! Ski school for kids was fantastic, pool and spa kept everyone happy. Breakfast buffet has amazing variety. Staff go above and beyond. Best ski vacation we've ever had!"
            },
            {
                "author": "Magdalena S.",
                "rating": 5,
                "date": "2024-12-28",
                "title": "5-star mountain paradise",
                "text": "Everything about this resort screams luxury. From the heated boot room to the après-ski bar, every detail is perfect. Our suite had a fireplace and the most amazing Tatra views. Spa treatments are world-class. Cannot wait to return!"
            }
        ],
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
            "https://images.unsplash.com/photo-1551582045-6ec9c11d8697?w=800",
            "https://images.unsplash.com/photo-1602343168117-bb8ffe3e2e9f?w=800",
            "https://images.unsplash.com/photo-1587381420270-3e1a5b9e6904?w=800",
            "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?w=800"
        ],
        "rating": 4.7,
        "review_count": 334,
        "address": {
            "street": "ul. Krupówki 22",
            "city": "Zakopane",
            "postal_code": "34-500",
            "country": "Poland"
        },
        "contact": {
            "phone": "+48 18 201 4567",
            "email": "info@woodencottage.pl",
            "website": "www.traditionwoodencottage.com"
        },
        "features": {
            "accommodation": "3-star traditional cottage",
            "amenities": ["restaurant", "fireplace", "garden", "parking"],
            "room_type": "Rustic Room with Fireplace",
            "suitable_for": ["romantic", "couples", "nature", "authentic"],
            "accessibility": []
        },
        "detailed_amenities": {
            "general": ["free_wifi", "reception", "free_parking", "luggage_storage"],
            "traditional": ["wood_construction", "traditional_decor", "fireplaces", "mountain_garden", "highlander_atmosphere"],
            "dining": ["traditional_restaurant", "fireplace_lounge", "breakfast_room", "highland_cuisine"],
            "room": ["wooden_furnishings", "fireplaces", "mountain_views", "traditional_bedding", "heating"]
        },
        "rooms": [
            {
                "name": "Rustic Room with Fireplace",
                "size_sqm": 25,
                "beds": "1 Queen Bed",
                "max_guests": 2,
                "features": ["Heating", "Fireplace", "Mountain view", "Wood furnishings", "Traditional decor"]
            },
            {
                "name": "Highland Suite",
                "size_sqm": 35,
                "beds": "1 King Bed",
                "max_guests": 2,
                "features": ["Heating", "Large fireplace", "Tatra view", "Seating area", "Traditional bathroom"]
            },
            {
                "name": "Family Cottage Room",
                "size_sqm": 45,
                "beds": "1 Queen + 2 Singles",
                "max_guests": 4,
                "features": ["Heating", "Fireplace", "Mountain view", "Separate sleeping area", "Traditional furnishings"]
            }
        ],
        "reviews": [
            {
                "author": "Jan P.",
                "rating": 5,
                "date": "2025-01-15",
                "title": "Authentic highland experience",
                "text": "This cottage hotel is a gem! The traditional wooden architecture and authentic highland decor create such a cozy atmosphere. Our room's fireplace was perfect for romantic evenings. Restaurant serves amazing traditional food. Felt like stepping back in time in the best way!"
            },
            {
                "author": "Ewa K.",
                "rating": 5,
                "date": "2025-01-06",
                "title": "Charming and romantic",
                "text": "Perfect for a romantic mountain getaway. The fireplace in our room, the wooden beams, the mountain views - everything was magical. Staff are warm and welcoming. Traditional breakfast was delicious. Great value and authentic Zakopane experience."
            },
            {
                "author": "Michał W.",
                "rating": 4,
                "date": "2024-12-30",
                "title": "Traditional charm",
                "text": "Beautiful traditional cottage with genuine highland character. Rooms are cozy and well-heated. Love the authentic wooden construction. Restaurant has excellent regional dishes. No elevator but the rustic charm makes up for it. Recommended for couples seeking authentic atmosphere."
            }
        ],
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
            "https://images.unsplash.com/photo-1605640840605-14ac1855827b?w=800",
            "https://images.unsplash.com/photo-1551582045-6ec9c11d8697?w=800",
            "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800",
            "https://images.unsplash.com/photo-1442850473887-0fb77cd0b337?w=800"
        ],
        "rating": 4.6,
        "review_count": 289,
        "address": {
            "street": "ul. Chałubińskiego 44",
            "city": "Zakopane",
            "postal_code": "34-500",
            "country": "Poland"
        },
        "contact": {
            "phone": "+48 18 206 3333",
            "email": "info@hikingbase.pl",
            "website": "www.hikingbasezakopane.com"
        },
        "features": {
            "accommodation": "3-star mountain hotel",
            "amenities": ["restaurant", "parking", "bike_rental", "hiking_maps"],
            "room_type": "Mountain View Room",
            "suitable_for": ["hiking", "adventure", "nature", "families"],
            "accessibility": []
        },
        "detailed_amenities": {
            "general": ["free_wifi", "24h_reception", "free_parking", "luggage_storage", "drying_room"],
            "hiking": ["hiking_guides", "trail_maps", "packed_lunches", "gear_storage", "route_planning"],
            "recreation": ["bike_rental", "mountain_gear_rental", "guided_tours"],
            "dining": ["mountain_restaurant", "packed_lunch_service", "breakfast_buffet"],
            "room": ["mountain_views", "heating", "comfortable_beds", "coffee_maker", "balconies"]
        },
        "rooms": [
            {
                "name": "Standard Mountain Room",
                "size_sqm": 22,
                "beds": "1 Queen Bed or 2 Singles",
                "max_guests": 2,
                "features": ["Heating", "Mountain view", "Coffee maker", "Gear storage"]
            },
            {
                "name": "Mountain View Room",
                "size_sqm": 28,
                "beds": "1 King Bed",
                "max_guests": 2,
                "features": ["Heating", "Tatra view", "Balcony", "Seating area", "Minibar"]
            },
            {
                "name": "Family Hiking Room",
                "size_sqm": 38,
                "beds": "1 Queen + 2 Singles",
                "max_guests": 4,
                "features": ["Heating", "Mountain view", "Balcony", "Extra storage", "2 bathrooms"]
            }
        ],
        "reviews": [
            {
                "author": "Wojciech M.",
                "rating": 5,
                "date": "2025-06-15",
                "title": "Perfect hiking base",
                "text": "Ideal location for Tatra hiking! Staff are knowledgeable about trails and provided excellent route recommendations. Packed lunches were generous. Drying room was essential after rainy hikes. Restaurant has hearty meals perfect after long days. Great value for hikers!"
            },
            {
                "author": "Aleksandra N.",
                "rating": 4,
                "date": "2025-06-05",
                "title": "Great for outdoor enthusiasts",
                "text": "Perfect hotel for hiking and biking. Bike rental was convenient and gear storage secure. Staff organized guided hikes which were fantastic. Rooms are simple but comfortable with beautiful mountain views. Breakfast has good energy for hiking. Highly recommend for active travelers."
            },
            {
                "author": "Paweł R.",
                "rating": 5,
                "date": "2025-05-28",
                "title": "Hiker's paradise",
                "text": "Everything a hiker needs! Trail maps, packed lunches, early breakfasts, drying facilities. The hiking guides were professional and showed us amazing trails. Family room was perfect for us and the kids. Will definitely return for our next Tatra adventure!"
            }
        ],
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
            "https://images.unsplash.com/photo-1605181379317-d6a5de8f2056?w=800",
            "https://images.unsplash.com/photo-1544161515-4ab6ce6db874?w=800",
            "https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=800",
            "https://images.unsplash.com/photo-1540555700478-4be289fbecef?w=800"
        ],
        "rating": 4.8,
        "review_count": 423,
        "address": {
            "street": "ul. Pardałówka 17",
            "city": "Zakopane",
            "postal_code": "34-500",
            "country": "Poland"
        },
        "contact": {
            "phone": "+48 18 202 8888",
            "email": "reservations@mountainwellness.pl",
            "website": "www.wellnessretreat-zakopane.com"
        },
        "features": {
            "accommodation": "4-star wellness hotel",
            "amenities": ["spa", "yoga_studio", "pool", "restaurant", "meditation_room"],
            "room_type": "Wellness Suite",
            "suitable_for": ["wellness", "relaxation", "couples", "solo"],
            "accessibility": ["elevator", "wheelchair_friendly"]
        },
        "detailed_amenities": {
            "general": ["free_wifi", "24h_reception", "free_parking", "luggage_storage", "concierge"],
            "wellness": ["spa_treatments", "yoga_classes", "meditation_sessions", "wellness_programs", "health_consultations"],
            "spa_facilities": ["indoor_pool", "sauna", "steam_room", "hot_tub", "relaxation_lounge", "treatment_rooms"],
            "dining": ["healthy_restaurant", "juice_bar", "wellness_cafe", "organic_breakfast"],
            "room": ["mountain_views", "aromatherapy", "yoga_mats", "meditation_cushions", "premium_bedding"]
        },
        "rooms": [
            {
                "name": "Wellness Room",
                "size_sqm": 30,
                "beds": "1 King Bed",
                "max_guests": 2,
                "features": ["Heating", "Mountain view", "Yoga mat", "Aromatherapy", "Meditation cushion"]
            },
            {
                "name": "Wellness Suite",
                "size_sqm": 42,
                "beds": "1 King Bed",
                "max_guests": 2,
                "features": ["Heating", "Panoramic view", "Living area", "Hot tub", "Yoga space", "Balcony"]
            },
            {
                "name": "Detox Suite",
                "size_sqm": 50,
                "beds": "1 King Bed + Sofa bed",
                "max_guests": 3,
                "features": ["Heating", "Mountain view", "Meditation room", "Private sauna", "Yoga area", "Tea station"]
            }
        ],
        "reviews": [
            {
                "author": "Agnieszka L.",
                "rating": 5,
                "date": "2025-03-10",
                "title": "Pure relaxation and rejuvenation",
                "text": "This wellness retreat exceeded all expectations! The yoga classes with mountain views are incredible. Spa treatments are world-class and the wellness programs are expertly designed. Healthy restaurant serves delicious organic food. Left feeling completely refreshed and centered."
            },
            {
                "author": "Barbara S.",
                "rating": 5,
                "date": "2025-02-25",
                "title": "Mountain wellness paradise",
                "text": "Perfect escape from city stress. Daily yoga and meditation sessions were transformative. The Wellness Suite with hot tub and mountain views was heavenly. Staff are caring wellness professionals. Organic meals were nutritious and tasty. Highly recommend for wellness seekers!"
            },
            {
                "author": "Krzysztof T.",
                "rating": 4,
                "date": "2025-02-12",
                "title": "Excellent wellness experience",
                "text": "Great wellness hotel with professional programs. Spa facilities are excellent and treatments very relaxing. Yoga instructors are experienced. Healthy food is delicious. Only minor point is some wellness programs book up fast, so reserve early. Overall fantastic experience."
            }
        ],
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
            "https://images.unsplash.com/photo-1551582045-6ec9c11d8697?w=800",
            "https://images.unsplash.com/photo-1602343168117-bb8ffe3e2e9f?w=800",
            "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?w=800",
            "https://images.unsplash.com/photo-1519904981063-b0cf448d479e?w=800"
        ],
        "rating": 4.7,
        "review_count": 267,
        "address": {
            "street": "ul. Bogdańskiego 8",
            "city": "Zakopane",
            "postal_code": "34-500",
            "country": "Poland"
        },
        "contact": {
            "phone": "+48 18 201 9999",
            "email": "booking@familychalet.pl",
            "website": "www.familychalet-zakopane.com"
        },
        "features": {
            "accommodation": "4-star chalet apartments",
            "amenities": ["kitchen", "fireplace", "parking", "playground", "bbq"],
            "room_type": "2-Bedroom Chalet",
            "suitable_for": ["families", "groups", "long_stay"],
            "accessibility": []
        },
        "detailed_amenities": {
            "general": ["free_wifi", "free_parking", "reception", "luggage_storage"],
            "family": ["playground", "children's_play_area", "bbq_facilities", "family_activities", "garden"],
            "chalet": ["full_kitchen", "fireplace", "dining_area", "living_room", "private_entrance", "terrace"],
            "room": ["mountain_views", "heating", "flat_screen_tv", "washer", "dishwasher"]
        },
        "rooms": [
            {
                "name": "1-Bedroom Chalet",
                "size_sqm": 50,
                "beds": "1 King Bed + Sofa bed",
                "max_guests": 4,
                "features": ["Heating", "Full kitchen", "Fireplace", "Terrace", "Mountain view", "BBQ"]
            },
            {
                "name": "2-Bedroom Chalet",
                "size_sqm": 70,
                "beds": "1 King + 2 Singles",
                "max_guests": 5,
                "features": ["Heating", "Full kitchen", "Fireplace", "Large terrace", "2 bathrooms", "BBQ", "Garden access"]
            },
            {
                "name": "3-Bedroom Family Chalet",
                "size_sqm": 95,
                "beds": "1 King + 2 Queens",
                "max_guests": 7,
                "features": ["Heating", "Full kitchen", "2 fireplaces", "Large terrace", "2 bathrooms", "BBQ", "Play area"]
            }
        ],
        "reviews": [
            {
                "author": "Joanna K.",
                "rating": 5,
                "date": "2025-02-20",
                "title": "Perfect for family vacation",
                "text": "Amazing chalet for our family of 5! Full kitchen was perfect for cooking meals, fireplace created cozy evenings, and kids loved the playground. Tatra views from the terrace are stunning. Having our own space with BBQ was wonderful. Highly recommend for families!"
            },
            {
                "author": "Robert M.",
                "rating": 5,
                "date": "2025-01-28",
                "title": "Home away from home",
                "text": "Stayed for a week and felt completely at home. Chalet is spacious and well-equipped with everything you need. Fireplace and mountain views are magical. Kids played in the garden while we barbecued. Great value for families or groups. Will definitely return!"
            },
            {
                "author": "Dorota W.",
                "rating": 4,
                "date": "2025-01-14",
                "title": "Great for longer stays",
                "text": "Excellent chalet apartments for extended mountain stays. Having a kitchen saved money and the living space is comfortable. Playground kept the kids busy. Only note is limited reception hours, but staff are helpful when available. Overall great value for families."
            }
        ],
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
            "https://images.unsplash.com/photo-1605640840605-14ac1855827b?w=800",
            "https://images.unsplash.com/photo-1555854877-bab0e564b8d5?w=800",
            "https://images.unsplash.com/photo-1506057278219-795838d4c2dd?w=800",
            "https://images.unsplash.com/photo-1578683010236-d716f9a3f461?w=800"
        ],
        "rating": 4.4,
        "review_count": 512,
        "address": {
            "street": "ul. Zamoyskiego 8",
            "city": "Zakopane",
            "postal_code": "34-500",
            "country": "Poland"
        },
        "contact": {
            "phone": "+48 18 206 1234",
            "email": "info@mountainhostel.pl",
            "website": "www.zakopanebudgethostel.com"
        },
        "features": {
            "accommodation": "2-star hostel",
            "amenities": ["common_room", "kitchen", "parking", "ski_storage"],
            "room_type": "Private Room",
            "suitable_for": ["budget", "backpackers", "solo", "groups"],
            "accessibility": []
        },
        "detailed_amenities": {
            "general": ["free_wifi", "24h_reception", "free_parking", "luggage_storage", "lockers"],
            "social": ["common_room", "shared_kitchen", "terrace", "game_room", "group_activities"],
            "mountain": ["ski_storage", "drying_room", "hiking_info", "tour_bookings"],
            "room": ["comfortable_beds", "bedding_included", "heating", "reading_lights"]
        },
        "rooms": [
            {
                "name": "Private Room",
                "size_sqm": 16,
                "beds": "2 Singles or 1 Double",
                "max_guests": 2,
                "features": ["Heating", "Shared bathroom", "Lockers", "Mountain view"]
            },
            {
                "name": "Private Triple",
                "size_sqm": 20,
                "beds": "3 Singles",
                "max_guests": 3,
                "features": ["Heating", "Shared bathroom", "Lockers", "Storage space"]
            },
            {
                "name": "Family Room",
                "size_sqm": 24,
                "beds": "4 Singles",
                "max_guests": 4,
                "features": ["Heating", "Shared bathroom", "Lockers", "Mountain view", "Extra space"]
            }
        ],
        "reviews": [
            {
                "author": "Adam S.",
                "rating": 4,
                "date": "2025-01-25",
                "title": "Great budget option for mountains",
                "text": "Perfect hostel for budget travelers! Clean rooms, great common areas to meet other hikers and skiers. Kitchen is well-equipped. Ski storage and drying room are essential. Staff are friendly and helpful with mountain advice. Excellent value for Zakopane!"
            },
            {
                "author": "Karolina P.",
                "rating": 5,
                "date": "2025-01-12",
                "title": "Budget-friendly and social",
                "text": "Best budget accommodation in Zakopane! Met amazing people in the common room. Staff organized group hikes which were fun. Private room was clean and comfortable. Free parking is a bonus. Kitchen saved me lots of money. Definitely recommend for backpackers!"
            },
            {
                "author": "Marcin L.",
                "rating": 4,
                "date": "2024-12-29",
                "title": "Good value hostel",
                "text": "Clean and affordable hostel close to ski slopes. Common areas are cozy and great for socializing. Kitchen facilities are good. Staff are helpful with local tips. Only minor issue is bathrooms can get busy in the morning, but that's expected at a hostel. Good choice for budget travelers."
            }
        ],
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
            "https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=800",
            "https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=800",
            "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800",
            "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=800"
        ],
        "rating": 4.9,
        "review_count": 1234,
        "address": {
            "street": "ul. Powstańców Warszawy 12/14",
            "city": "Sopot",
            "postal_code": "81-718",
            "country": "Poland"
        },
        "contact": {
            "phone": "+48 58 520 6000",
            "email": "reservations@grandbaltic.pl",
            "website": "www.grandbaltichotel.com"
        },
        "features": {
            "accommodation": "5-star grand hotel",
            "amenities": ["spa", "pool", "restaurant", "beach_club", "casino", "pier_access"],
            "room_type": "Sea View Suite",
            "suitable_for": ["luxury", "romantic", "spa", "beach"],
            "accessibility": ["elevator", "wheelchair_friendly", "accessible_bathroom"]
        },
        "detailed_amenities": {
            "general": ["free_wifi", "24h_concierge", "valet_parking", "luggage_storage", "room_service"],
            "luxury": ["casino", "pier_access", "beach_club", "limousine_service", "butler_service"],
            "wellness": ["luxury_spa", "indoor_pool", "outdoor_pool", "sauna", "steam_room", "beauty_salon", "massage"],
            "dining": ["fine_dining", "beach_restaurant", "lobby_bar", "pool_bar", "in_room_dining"],
            "room": ["sea_views", "balconies", "premium_minibar", "nespresso", "bathrobe", "designer_toiletries"]
        },
        "rooms": [
            {
                "name": "Superior Room",
                "size_sqm": 35,
                "beds": "1 King Bed",
                "max_guests": 2,
                "features": ["AC", "Park view", "Marble bathroom", "Minibar", "Nespresso", "Balcony"]
            },
            {
                "name": "Sea View Suite",
                "size_sqm": 55,
                "beds": "1 King Bed",
                "max_guests": 2,
                "features": ["AC", "Sea view", "Large balcony", "Living area", "Premium minibar", "Bathtub"]
            },
            {
                "name": "Grand Suite",
                "size_sqm": 75,
                "beds": "1 King Bed + Sofa bed",
                "max_guests": 3,
                "features": ["AC", "Panoramic sea view", "Living room", "Dining area", "2 bathrooms", "Butler service"]
            },
            {
                "name": "Presidential Suite",
                "size_sqm": 120,
                "beds": "1 King + Extra bedroom",
                "max_guests": 4,
                "features": ["AC", "360° views", "Private terrace", "Full bar", "Master bathroom", "Grand piano", "Butler"]
            }
        ],
        "reviews": [
            {
                "author": "Monika Z.",
                "rating": 5,
                "date": "2025-07-15",
                "title": "Absolute Baltic luxury",
                "text": "This grand hotel is magnificent! Our Sea View Suite had stunning Baltic views and direct pier access. The spa is world-class with incredible treatments. Fine dining restaurant is Michelin-worthy. Beach club service was impeccable. Perfect anniversary celebration!"
            },
            {
                "author": "Grzegorz P.",
                "rating": 5,
                "date": "2025-07-05",
                "title": "Best hotel on the Baltic coast",
                "text": "Simply spectacular! Every detail screams luxury from the marble bathrooms to the butler service. Casino adds entertainment, beach club is exclusive, and spa treatments divine. Indoor and outdoor pools are stunning. Worth every zloty for a special occasion!"
            },
            {
                "author": "Natalia K.",
                "rating": 5,
                "date": "2025-06-28",
                "title": "Unforgettable luxury experience",
                "text": "Celebrated our honeymoon here and it was perfection. Presidential Suite was beyond our dreams with pier and sea views. Staff anticipated every need. Spa, restaurants, beach access - everything was five-star. The most luxurious hotel experience in Poland!"
            }
        ],
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
            "https://images.unsplash.com/photo-1598970434795-0c54fe7c0648?w=800",
            "https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=800",
            "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800",
            "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=800"
        ],
        "rating": 4.6,
        "review_count": 567,
        "address": {
            "street": "ul. Bitwy pod Płowcami 59",
            "city": "Sopot",
            "postal_code": "81-732",
            "country": "Poland"
        },
        "contact": {
            "phone": "+48 58 555 1234",
            "email": "booking@pierview-sopot.pl",
            "website": "www.pierviewhotel.com"
        },
        "features": {
            "accommodation": "4-star beachfront hotel",
            "amenities": ["restaurant", "bar", "terrace", "pier_view"],
            "room_type": "Pier View Room",
            "suitable_for": ["beach", "couples", "families"],
            "accessibility": ["elevator"]
        },
        "detailed_amenities": {
            "general": ["free_wifi", "24h_reception", "luggage_storage", "concierge"],
            "beach": ["beach_access", "beach_chairs", "beach_towels", "pier_view"],
            "dining": ["beachfront_restaurant", "pier_bar", "terrace_dining", "breakfast_buffet"],
            "room": ["sea_views", "balconies", "flat_screen_tv", "minibar", "safe", "coffee_maker"]
        },
        "rooms": [
            {
                "name": "Standard Room",
                "size_sqm": 26,
                "beds": "1 Queen Bed",
                "max_guests": 2,
                "features": ["AC", "City view", "Modern bathroom", "Coffee maker", "Safe"]
            },
            {
                "name": "Pier View Room",
                "size_sqm": 32,
                "beds": "1 King Bed",
                "max_guests": 2,
                "features": ["AC", "Pier view", "Balcony", "Seating area", "Minibar", "Coffee maker"]
            },
            {
                "name": "Family Pier View",
                "size_sqm": 45,
                "beds": "1 King + 2 Singles",
                "max_guests": 4,
                "features": ["AC", "Pier and sea view", "Large balcony", "Living area", "Minibar", "2 bathrooms"]
            }
        ],
        "reviews": [
            {
                "author": "Beata W.",
                "rating": 5,
                "date": "2025-07-12",
                "title": "Perfect beachfront location",
                "text": "Amazing hotel right by the pier! Our room had stunning views of the longest wooden pier in Europe. Beach access is direct and the restaurant terrace overlooks the sea. Staff are friendly and helpful. Perfect for beach lovers and romantic getaways!"
            },
            {
                "author": "Filip K.",
                "rating": 4,
                "date": "2025-07-03",
                "title": "Great family beach hotel",
                "text": "Excellent location for families. Family room was spacious with great pier views. Kids loved being so close to the beach and pier. Restaurant has good food. Only minor point is it can get busy during peak season but that's expected. Overall great value!"
            },
            {
                "author": "Zofia M.",
                "rating": 5,
                "date": "2025-06-25",
                "title": "Romantic seaside escape",
                "text": "Perfect for a romantic weekend. Waking up to pier and sea views was magical. Walking distance to everything in Sopot. Terrace bar is lovely for sunset drinks. Rooms are comfortable and clean. Highly recommend for couples!"
            }
        ],
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
            "https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=800",
            "https://images.unsplash.com/photo-1540555700478-4be289fbecef?w=800",
            "https://images.unsplash.com/photo-1544161515-4ab6ce6db874?w=800",
            "https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=800"
        ],
        "rating": 4.8,
        "review_count": 789,
        "address": {
            "street": "ul. Haffnera 83",
            "city": "Sopot",
            "postal_code": "81-715",
            "country": "Poland"
        },
        "contact": {
            "phone": "+48 58 550 9000",
            "email": "wellness@balticspa.pl",
            "website": "www.balticspasopot.com"
        },
        "features": {
            "accommodation": "4-star spa resort",
            "amenities": ["spa", "pool", "sauna", "restaurant", "wellness_programs"],
            "room_type": "Wellness Suite",
            "suitable_for": ["spa", "wellness", "relaxation", "couples"],
            "accessibility": ["elevator", "wheelchair_friendly"]
        },
        "detailed_amenities": {
            "general": ["free_wifi", "24h_reception", "free_parking", "luggage_storage", "concierge"],
            "spa_wellness": ["luxury_spa", "wellness_programs", "massage_treatments", "beauty_treatments", "health_consultations"],
            "facilities": ["indoor_pool", "outdoor_pool", "sauna", "steam_room", "hot_tub", "relaxation_lounge"],
            "dining": ["wellness_restaurant", "juice_bar", "healthy_cafe", "breakfast_buffet"],
            "room": ["sea_views", "balconies", "aromatherapy", "premium_bedding", "bathrobe"]
        },
        "rooms": [
            {
                "name": "Wellness Room",
                "size_sqm": 30,
                "beds": "1 King Bed",
                "max_guests": 2,
                "features": ["AC", "Park view", "Balcony", "Aromatherapy", "Bathrobe", "Tea station"]
            },
            {
                "name": "Wellness Suite",
                "size_sqm": 42,
                "beds": "1 King Bed",
                "max_guests": 2,
                "features": ["AC", "Sea view", "Large balcony", "Living area", "Hot tub", "Premium spa products"]
            },
            {
                "name": "Spa Suite with Terrace",
                "size_sqm": 55,
                "beds": "1 King Bed + Sofa bed",
                "max_guests": 3,
                "features": ["AC", "Sea view", "Private terrace", "Outdoor hot tub", "Treatment room", "Yoga space"]
            }
        ],
        "reviews": [
            {
                "author": "Iwona S.",
                "rating": 5,
                "date": "2025-07-10",
                "title": "Ultimate spa relaxation",
                "text": "This spa resort is paradise! Wellness programs are expertly designed and treatments are world-class. Both pools are beautiful, sauna facilities excellent. Healthy restaurant serves delicious food. Our Wellness Suite was heavenly. Left feeling completely rejuvenated!"
            },
            {
                "author": "Andrzej T.",
                "rating": 5,
                "date": "2025-06-30",
                "title": "Best spa on the Baltic",
                "text": "Incredible wellness experience! Massage treatments were professional, spa facilities top-notch. The outdoor pool with sea views is stunning. Wellness programs include yoga and meditation. Staff are caring professionals. Perfect for couples seeking relaxation."
            },
            {
                "author": "Marta L.",
                "rating": 4,
                "date": "2025-06-18",
                "title": "Excellent wellness retreat",
                "text": "Great spa resort with comprehensive wellness offerings. Spa Suite with hot tub was amazing. Treatments are high quality and wellness consultations helpful. Healthy food is tasty. Only minor point is spa can book up, so reserve treatments early. Highly recommended!"
            }
        ],
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
            "https://images.unsplash.com/photo-1601892546722-f9cb29c554b9?w=800",
            "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=800",
            "https://images.unsplash.com/photo-1584132967334-10e028bd69f7?w=800",
            "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800",
            "https://images.unsplash.com/photo-1602002418082-a4443e081dd1?w=800",
            "https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=800"
        ],
        "rating": 4.7,
        "review_count": 445,
        "address": {
            "street": "ul. Morska 15",
            "city": "Sopot",
            "postal_code": "81-704",
            "country": "Poland"
        },
        "contact": {
            "phone": "+48 58 123 4567",
            "email": "info@beachbungalow.pl",
            "website": "www.beachbungalow-sopot.pl"
        },
        "features": {
            "accommodation": "3-star beach bungalows",
            "amenities": ["beach_access", "bbq", "bike_rental", "terrace", "garden", "pet_bowls", "dog_park"],
            "room_type": "Beach Bungalow",
            "room_types_available": ["Standard Bungalow", "Family Bungalow", "Deluxe Bungalow with Terrace"],
            "capacity": {"max_guests": 4, "max_adults": 2, "max_children": 3},
            "pets_allowed": True,
            "pet_fee": 15,
            "suitable_for": ["beach", "families", "groups", "summer", "pets"],
            "accessibility": []
        },
        "detailed_amenities": {
            "general": ["free_wifi", "free_parking", "24h_reception", "luggage_storage", "concierge"],
            "beach": ["beach_chairs", "beach_umbrellas", "beach_towels", "water_sports"],
            "food": ["breakfast_buffet", "bbq_facilities", "shared_kitchen", "picnic_area"],
            "recreation": ["bike_rental", "playground", "beach_volleyball", "ping_pong"],
            "pet_friendly": ["dog_park", "pet_bowls", "pet_beds_available", "dog_walking_area"]
        },
        "rooms": [
            {
                "name": "Standard Bungalow",
                "size_sqm": 35,
                "beds": "1 Queen Bed",
                "max_guests": 2,
                "features": ["AC", "Private terrace", "Garden view", "Mini fridge", "Coffee maker"]
            },
            {
                "name": "Family Bungalow",
                "size_sqm": 50,
                "beds": "1 Queen + 2 Singles",
                "max_guests": 4,
                "features": ["AC", "Private terrace", "Sea view", "Kitchenette", "Living area", "BBQ"]
            },
            {
                "name": "Deluxe Bungalow with Terrace",
                "size_sqm": 60,
                "beds": "1 King + 2 Singles",
                "max_guests": 4,
                "features": ["AC", "Large terrace", "Direct beach access", "Full kitchen", "Outdoor shower", "BBQ"]
            }
        ],
        "reviews": [
            {
                "author": "Sarah M.",
                "rating": 5,
                "date": "2025-05-15",
                "title": "Perfect family getaway with our dog!",
                "text": "Amazing place for families with pets! The dog park was fantastic and our golden retriever loved the beach access. Bungalows are spacious and the BBQ facilities were great for family dinners."
            },
            {
                "author": "Tom K.",
                "rating": 5,
                "date": "2025-05-10",
                "title": "Beach paradise",
                "text": "Direct beach access is a game changer. Bikes included made exploring Sopot super easy. Staff was incredibly friendly and helpful."
            },
            {
                "author": "Anna P.",
                "rating": 4,
                "date": "2025-05-05",
                "title": "Great value for money",
                "text": "Excellent location right on the beach. Bungalows are cozy and well-equipped. Only minor downside is it can get a bit noisy during peak hours but that's expected at a beach resort."
            }
        ],
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
            "https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=800",
            "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800",
            "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800",
            "https://images.unsplash.com/photo-1502672260066-6bc35f0a1f80?w=800"
        ],
        "rating": 4.8,
        "review_count": 923,
        "address": {
            "street": "ul. Grunwaldzka 74",
            "city": "Sopot",
            "postal_code": "81-771",
            "country": "Poland"
        },
        "contact": {
            "phone": "+48 58 556 7000",
            "email": "family@beachresortsopot.pl",
            "website": "www.familybeachresort.com"
        },
        "features": {
            "accommodation": "4-star family resort",
            "amenities": ["kids_club", "pool", "playground", "restaurant", "animation", "pet_area"],
            "room_type": "Family Room",
            "room_types_available": ["Standard Family Room", "Family Suite", "Connecting Rooms", "Family Apartment"],
            "capacity": {"max_guests": 5, "max_adults": 2, "max_children": 3},
            "pets_allowed": True,
            "pet_fee": 20,
            "suitable_for": ["families", "children", "beach", "pets"],
            "accessibility": ["elevator", "wheelchair_friendly"]
        },
        "detailed_amenities": {
            "general": ["free_wifi", "24h_reception", "free_parking", "luggage_storage", "concierge"],
            "family": ["kids_club", "playground", "childrens_pool", "baby_cots", "high_chairs", "animation_team"],
            "beach": ["beach_access", "beach_toys", "beach_volleyball", "water_activities"],
            "dining": ["family_restaurant", "kids_menu", "poolside_bar", "ice_cream_bar", "breakfast_buffet"],
            "pet_friendly": ["pet_area", "dog_walking_space", "pet_bowls", "pet_beds_available"],
            "room": ["sea_views", "balconies", "family_amenities", "flat_screen_tv", "minibar"]
        },
        "rooms": [
            {
                "name": "Standard Family Room",
                "size_sqm": 35,
                "beds": "1 Queen + 1 Single + Sofa bed",
                "max_guests": 4,
                "features": ["AC", "Park view", "Balcony", "Kids area", "Minibar", "Safe"]
            },
            {
                "name": "Family Suite",
                "size_sqm": 50,
                "beds": "1 King + 2 Singles",
                "max_guests": 5,
                "features": ["AC", "Sea view", "Large balcony", "Separate kids room", "Kitchenette", "2 bathrooms"]
            },
            {
                "name": "Family Apartment",
                "size_sqm": 70,
                "beds": "1 King + 2 Queens",
                "max_guests": 6,
                "features": ["AC", "Sea view", "Living room", "Full kitchen", "2 bathrooms", "Washing machine", "Terrace"]
            }
        ],
        "reviews": [
            {
                "author": "Kamila R.",
                "rating": 5,
                "date": "2025-07-08",
                "title": "Perfect for families with kids",
                "text": "Amazing family resort! Kids club kept our children entertained for hours. Animation team was fantastic. Pool area is great with separate kids pool. Restaurant has excellent kids menu. Beach access is easy. Our family had a wonderful vacation!"
            },
            {
                "author": "Tomasz D.",
                "rating": 5,
                "date": "2025-06-27",
                "title": "Family paradise with pets",
                "text": "Excellent resort that welcomes families and pets! Our dog loved the pet area and beach walks. Kids enjoyed playground and pool. Family Suite was spacious and comfortable. Staff are family-friendly and helpful. Highly recommend for families!"
            },
            {
                "author": "Justyna P.",
                "rating": 4,
                "date": "2025-06-15",
                "title": "Great family vacation",
                "text": "Wonderful resort for families. Kids club and entertainment kept children busy. Pool area is nice and beach access convenient. Family Apartment was perfect with full kitchen. Only minor point is restaurant can get crowded during peak times but overall excellent experience!"
            }
        ],
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
            "https://images.unsplash.com/photo-1598970434795-0c54fe7c0648?w=800",
            "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=800",
            "https://images.unsplash.com/photo-1587381420270-3e1a5b9e6904?w=800",
            "https://images.unsplash.com/photo-1602343168117-bb8ffe3e2e9f?w=800"
        ],
        "rating": 4.7,
        "review_count": 278,
        "address": {
            "street": "ul. Chopina 32",
            "city": "Sopot",
            "postal_code": "81-786",
            "country": "Poland"
        },
        "contact": {
            "phone": "+48 58 344 5555",
            "email": "stay@seasidevilla.pl",
            "website": "www.seasideboutiquevilla.com"
        },
        "features": {
            "accommodation": "3-star boutique villa",
            "amenities": ["garden", "terrace", "library", "bikes"],
            "room_type": "Garden View Room",
            "suitable_for": ["romantic", "couples", "quiet"],
            "accessibility": []
        },
        "detailed_amenities": {
            "general": ["free_wifi", "reception", "luggage_storage", "concierge"],
            "boutique": ["garden", "terrace", "library", "bike_rental", "peaceful_atmosphere"],
            "dining": ["breakfast_terrace", "tea_lounge", "garden_dining"],
            "room": ["elegant_decor", "quality_bedding", "flat_screen_tv", "safe", "coffee_maker"]
        },
        "rooms": [
            {
                "name": "Garden View Room",
                "size_sqm": 24,
                "beds": "1 Queen Bed",
                "max_guests": 2,
                "features": ["AC", "Garden view", "Elegant decor", "Coffee maker", "Bathrobe"]
            },
            {
                "name": "Superior Garden Room",
                "size_sqm": 30,
                "beds": "1 King Bed",
                "max_guests": 2,
                "features": ["AC", "Garden view", "Balcony", "Seating area", "Premium bedding", "Tea station"]
            },
            {
                "name": "Romantic Suite",
                "size_sqm": 40,
                "beds": "1 King Bed",
                "max_guests": 2,
                "features": ["AC", "Garden and partial sea view", "Private terrace", "Living area", "Bathtub", "Champagne on arrival"]
            }
        ],
        "reviews": [
            {
                "author": "Sylwia K.",
                "rating": 5,
                "date": "2025-07-05",
                "title": "Romantic and peaceful",
                "text": "Perfect boutique villa for a romantic getaway! The garden is beautiful and peaceful. Our room was elegantly decorated with attention to detail. Breakfast on the terrace was lovely. Bikes provided were great for exploring quiet Sopot streets. Highly recommend for couples!"
            },
            {
                "author": "Michał B.",
                "rating": 5,
                "date": "2025-06-22",
                "title": "Charming hideaway",
                "text": "What a charming place! The villa has character and the garden is a tranquil oasis. Library has interesting books. Romantic Suite was perfect for our anniversary. Staff are attentive and service personal. A hidden gem in Sopot!"
            },
            {
                "author": "Kasia W.",
                "rating": 4,
                "date": "2025-06-10",
                "title": "Quiet boutique experience",
                "text": "Beautiful boutique villa away from the busy beach crowds. Garden is peaceful and well-maintained. Rooms are cozy with quality furnishings. Breakfast is simple but fresh. No elevator but the intimate atmosphere makes up for it. Perfect for couples seeking tranquility."
            }
        ],
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
