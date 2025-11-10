import random
import asyncio
from datetime import datetime, timedelta
from typing import Any, Dict, List
from customer_profiles import get_profile

# =============================================================================
# MOCK DATA CATALOGS
# =============================================================================

MOCK_DEVICES = [
    {
        "id": "iphone-15-pro",
        "name": "iPhone 15 Pro",
        "brand": "Apple",
        "price_upfront": 199,
        "price_monthly": 47,
        "image_url": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-1inch-bluetitanium?wid=5120&hei=2880&fmt=p-jpg&qlt=80&.v=1692845699220",
        "attributes": {
            "battery_life": "excellent",  # 5000mAh+
            "camera_quality": "excellent",  # 48MP+
            "storage_options": [128, 256, 512, 1024],
            "screen_size": 6.1,
            "5g": True,
            "use_cases": ["photography", "gaming", "business", "everyday"]
        },
        "rating": 4.8,
        "reviews_count": 2341
    },
    {
        "id": "samsung-s24-ultra",
        "name": "Samsung Galaxy S24 Ultra",
        "brand": "Samsung",
        "price_upfront": 149,
        "price_monthly": 45,
        "image_url": "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=400&h=400&fit=crop",
        "attributes": {
            "battery_life": "excellent",
            "camera_quality": "excellent",
            "storage_options": [256, 512, 1024],
            "screen_size": 6.8,
            "5g": True,
            "use_cases": ["photography", "gaming", "content_creation", "business"]
        },
        "rating": 4.7,
        "reviews_count": 1823
    },
    {
        "id": "pixel-8-pro",
        "name": "Google Pixel 8 Pro",
        "brand": "Google",
        "price_upfront": 99,
        "price_monthly": 42,
        "image_url": "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400&h=400&fit=crop",
        "attributes": {
            "battery_life": "very_good",
            "camera_quality": "excellent",
            "storage_options": [128, 256, 512],
            "screen_size": 6.7,
            "5g": True,
            "use_cases": ["photography", "everyday", "ai_features"]
        },
        "rating": 4.6,
        "reviews_count": 1456
    },
    {
        "id": "iphone-15",
        "name": "iPhone 15",
        "brand": "Apple",
        "price_upfront": 99,
        "price_monthly": 39,
        "image_url": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-finish-select-202309-6-1inch-blue?wid=5120&hei=2880&fmt=p-jpg&qlt=80&.v=1692923781972",
        "attributes": {
            "battery_life": "good",
            "camera_quality": "very_good",
            "storage_options": [128, 256, 512],
            "screen_size": 6.1,
            "5g": True,
            "use_cases": ["everyday", "photography", "business"]
        },
        "rating": 4.7,
        "reviews_count": 3421
    },
    {
        "id": "samsung-s24",
        "name": "Samsung Galaxy S24",
        "brand": "Samsung",
        "price_upfront": 79,
        "price_monthly": 37,
        "image_url": "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=400&h=400&fit=crop",
        "attributes": {
            "battery_life": "very_good",
            "camera_quality": "very_good",
            "storage_options": [128, 256],
            "screen_size": 6.2,
            "5g": True,
            "use_cases": ["everyday", "photography", "gaming"]
        },
        "rating": 4.6,
        "reviews_count": 2103
    },
    {
        "id": "xiaomi-14",
        "name": "Xiaomi 14",
        "brand": "Xiaomi",
        "price_upfront": 49,
        "price_monthly": 32,
        "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400&h=400&fit=crop",
        "attributes": {
            "battery_life": "excellent",
            "camera_quality": "very_good",
            "storage_options": [256, 512],
            "screen_size": 6.36,
            "5g": True,
            "use_cases": ["everyday", "gaming", "budget_premium"]
        },
        "rating": 4.5,
        "reviews_count": 876
    },
    {
        "id": "oneplus-12",
        "name": "OnePlus 12",
        "brand": "OnePlus",
        "price_upfront": 69,
        "price_monthly": 35,
        "image_url": "https://images.unsplash.com/photo-1592286927505-decd0cb4084d?w=400&h=400&fit=crop",
        "attributes": {
            "battery_life": "excellent",
            "camera_quality": "very_good",
            "storage_options": [256, 512],
            "screen_size": 6.7,
            "5g": True,
            "use_cases": ["gaming", "everyday", "fast_charging"]
        },
        "rating": 4.5,
        "reviews_count": 1234
    },
    {
        "id": "iphone-14",
        "name": "iPhone 14",
        "brand": "Apple",
        "price_upfront": 49,
        "price_monthly": 32,
        "image_url": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-14-finish-select-202209-6-1inch-blue?wid=5120&hei=2880&fmt=p-jpg&qlt=80&.v=1661027336558",
        "attributes": {
            "battery_life": "good",
            "camera_quality": "good",
            "storage_options": [128, 256],
            "screen_size": 6.1,
            "5g": True,
            "use_cases": ["everyday", "budget_apple"]
        },
        "rating": 4.6,
        "reviews_count": 5234
    },
    {
        "id": "samsung-a54",
        "name": "Samsung Galaxy A54",
        "brand": "Samsung",
        "price_upfront": 0,
        "price_monthly": 25,
        "image_url": "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400&h=400&fit=crop",
        "attributes": {
            "battery_life": "very_good",
            "camera_quality": "good",
            "storage_options": [128, 256],
            "screen_size": 6.4,
            "5g": True,
            "use_cases": ["everyday", "budget"]
        },
        "rating": 4.4,
        "reviews_count": 2876
    },
    {
        "id": "pixel-8a",
        "name": "Google Pixel 8a",
        "brand": "Google",
        "price_upfront": 0,
        "price_monthly": 28,
        "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400&h=400&fit=crop",
        "attributes": {
            "battery_life": "good",
            "camera_quality": "very_good",
            "storage_options": [128],
            "screen_size": 6.1,
            "5g": True,
            "use_cases": ["everyday", "photography", "budget"]
        },
        "rating": 4.5,
        "reviews_count": 1543
    }
]

MOCK_PLANS = [
    {
        "id": "unlimited-max",
        "name": "Unlimited Max",
        "type": "unlimited",
        "data": "Unlimited",
        "minutes": "Unlimited",
        "texts": "Unlimited",
        "international_roaming": True,
        "5g": True,
        "price_monthly": 35,
        "highlights": ["5G speeds", "Roaming in 81 countries", "Unlimited hotspot"]
    },
    {
        "id": "unlimited-lite",
        "name": "Unlimited Lite",
        "type": "unlimited",
        "data": "Unlimited (2Mbps after 50GB)",
        "minutes": "Unlimited",
        "texts": "Unlimited",
        "international_roaming": False,
        "5g": True,
        "price_monthly": 25,
        "highlights": ["5G speeds", "Entertainment apps included"]
    },
    {
        "id": "data-100gb",
        "name": "Essential 100GB",
        "type": "capped",
        "data": "100GB",
        "minutes": "Unlimited",
        "texts": "Unlimited",
        "international_roaming": False,
        "5g": True,
        "price_monthly": 20,
        "highlights": ["Perfect for most users", "5G ready"]
    },
    {
        "id": "data-50gb",
        "name": "Essential 50GB",
        "type": "capped",
        "data": "50GB",
        "minutes": "Unlimited",
        "texts": "Unlimited",
        "international_roaming": False,
        "5g": False,
        "price_monthly": 15,
        "highlights": ["Great value", "4G speeds"]
    },
    {
        "id": "data-20gb",
        "name": "Essential 20GB",
        "type": "capped",
        "data": "20GB",
        "minutes": "Unlimited",
        "texts": "Unlimited",
        "international_roaming": False,
        "5g": False,
        "price_monthly": 10,
        "highlights": ["Budget friendly", "Perfect for light users"]
    }
]

MOCK_ACCESSORIES = {
    "iphone-15-pro": [
        {"id": "case-iphone-15-pro", "name": "Apple Silicone Case", "type": "case", "price": 49, "in_stock": True, "image_url": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/MWND3?wid=400&hei=400&fmt=jpeg&qlt=90"},
        {"id": "charger-usbc-20w", "name": "20W USB-C Charger", "type": "charger", "price": 25, "in_stock": True, "image_url": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/MHJE3?wid=400&hei=400&fmt=jpeg&qlt=90"},
        {"id": "airpods-pro", "name": "AirPods Pro (2nd gen)", "type": "earbuds", "price": 229, "in_stock": True, "image_url": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/MQD83?wid=400&hei=400&fmt=jpeg&qlt=90"},
        {"id": "screen-protector", "name": "Screen Protector", "type": "screen_protector", "price": 15, "in_stock": True, "image_url": "https://m.media-amazon.com/images/I/61S+VmKJ1WL._AC_SX300_SY300_.jpg"}
    ],
    "samsung-s24-ultra": [
        {"id": "case-s24-ultra", "name": "Samsung Rugged Case", "type": "case", "price": 39, "in_stock": True, "image_url": "https://images.samsung.com/is/image/samsung/p6pim/uk/ef-ru916cbegww/gallery/uk-galaxy-s24-ultra-protective-standing-cover-ef-ru916-ef-ru916cbegww-542072913?imwidth=400"},
        {"id": "charger-45w", "name": "45W Super Fast Charger", "type": "charger", "price": 35, "in_stock": True, "image_url": "https://images.samsung.com/is/image/samsung/p6pim/uk/ep-t4510xbegww/gallery/uk-45w-usb-c-super-fast-charging-wall-charger-ep-t4510xbegww-535606456?imwidth=400"},
        {"id": "buds-pro", "name": "Galaxy Buds2 Pro", "type": "earbuds", "price": 199, "in_stock": True, "image_url": "https://images.samsung.com/is/image/samsung/p6pim/uk/2202/gallery/uk-galaxy-buds2-pro-sm-r510nlvaeua-530891235?imwidth=400"},
        {"id": "screen-protector-s24", "name": "Tempered Glass Protector", "type": "screen_protector", "price": 18, "in_stock": True, "image_url": "https://m.media-amazon.com/images/I/61S+VmKJ1WL._AC_SX300_SY300_.jpg"}
    ],
    "default": [
        {"id": "case-universal", "name": "Universal Protective Case", "type": "case", "price": 25, "in_stock": True, "image_url": "https://m.media-amazon.com/images/I/71ux+r8jC5L._AC_SX300_SY300_.jpg"},
        {"id": "charger-usbc", "name": "USB-C Charger", "type": "charger", "price": 19, "in_stock": True, "image_url": "https://m.media-amazon.com/images/I/41pBh1CEq8L._AC_SX300_SY300_.jpg"},
        {"id": "screen-protector-universal", "name": "Universal Screen Protector", "type": "screen_protector", "price": 12, "in_stock": True, "image_url": "https://m.media-amazon.com/images/I/61S+VmKJ1WL._AC_SX300_SY300_.jpg"}
    ]
}

# Shopping cart (in-memory - will be lost on restart)
SHOPPING_CART = {}

# =============================================================================
# CONTOSO SALES TOOLS
# =============================================================================

async def search_devices_by_attributes(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Intelligent device search based on customer requirements using scoring."""
    battery_pref = arguments.get("battery_life")
    camera_pref = arguments.get("camera_quality")
    price_max = arguments.get("price_max_monthly", 999)
    brand = arguments.get("brand")
    use_case = arguments.get("use_case")

    quality_levels = {"good": 1, "very_good": 2, "excellent": 3}

    # Score each device based on how well it matches criteria
    scored_devices = []
    for device in MOCK_DEVICES:
        attrs = device["attributes"]
        score = 0

        # Hard price filter - don't show devices over budget
        if device["price_monthly"] > price_max:
            continue

        # Brand match - strong preference (exact match gets big boost)
        if brand:
            if device["brand"].lower() == brand.lower():
                score += 50  # Exact brand match
            else:
                continue  # Skip non-matching brands if brand specified

        # Battery scoring (not exclusion)
        if battery_pref:
            required_level = quality_levels.get(battery_pref, 0)
            device_level = quality_levels.get(attrs.get("battery_life", "good"), 0)
            # Give points based on how close/better the device is
            if device_level >= required_level:
                score += 20 + (device_level - required_level) * 5  # Bonus for exceeding
            else:
                score += device_level * 5  # Partial credit

        # Camera scoring (not exclusion)
        if camera_pref:
            required_level = quality_levels.get(camera_pref, 0)
            device_level = quality_levels.get(attrs.get("camera_quality", "good"), 0)
            if device_level >= required_level:
                score += 20 + (device_level - required_level) * 5
            else:
                score += device_level * 5

        # Use case match
        if use_case and use_case in attrs.get("use_cases", []):
            score += 15

        # Rating contribution
        score += (device.get("rating", 0) * 5)

        # Price value - cheaper is better (within budget)
        price_score = max(0, (price_max - device["price_monthly"]) / 5)
        score += price_score

        scored_devices.append({"device": device, "score": score})

    # Sort by score descending
    scored_devices.sort(key=lambda x: -x["score"])

    # Return top devices with their scores
    top_devices = [item["device"] for item in scored_devices[:5]]

    return {
        "search_criteria": arguments,
        "results_count": len(top_devices),
        "devices": top_devices,
        "message": f"Found {len(scored_devices)} devices, showing top {len(top_devices)} matches",
        "scoring_used": True,
        "_visual": {
            "type": "product_grid",
            "title": "Recommended Phones",
            "items": top_devices
        }
    }


async def get_device_details(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Get full details for a specific device."""
    device_id = arguments.get("device_id")

    device = next((d for d in MOCK_DEVICES if d["id"] == device_id), None)
    if not device:
        return {"error": "Device not found"}

    # Enhanced details
    enhanced_device = {
        **device,
        "description": f"The {device['name']} combines cutting-edge technology with elegant design. Perfect for {', '.join(device['attributes'].get('use_cases', [])[:2])}.",
        "full_specs": {
            "processor": "Latest generation",
            "ram": "8GB",
            "weight": "195g",
            "water_resistant": True,
            "warranty": "2 years"
        },
        "customer_reviews": [
            {"rating": 5, "comment": "Best phone I've ever had!", "helpful": 234},
            {"rating": 4, "comment": "Great camera but pricey", "helpful": 123}
        ],
        "available_colors": ["Black", "Silver", "Blue"],
        "stock_status": "In stock",
        "delivery_estimate": "Next day delivery available"
    }

    return {
        **enhanced_device,
        "_visual": {
            "type": "product_hero",
            "data": enhanced_device
        }
    }


async def compare_devices(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Compare multiple devices side-by-side."""
    device_ids = arguments.get("device_ids", [])
    context = arguments.get("_context", {})

    devices = [d for d in MOCK_DEVICES if d["id"] in device_ids]

    # Determine which attributes to compare based on user priorities
    priorities = context.get("user_priorities", [])

    if priorities:
        # Show only priority attributes + price
        matrix_keys = priorities + ["price_monthly", "price_upfront"]
    else:
        # Default: show common attributes
        matrix_keys = ["battery_life", "camera_quality", "screen_size", "price_monthly", "price_upfront", "rating"]

    # Build comparison matrix
    comparison_matrix = {}
    for key in matrix_keys:
        if key in ["price_monthly", "price_upfront", "rating"]:
            comparison_matrix[key] = [d.get(key, 0) for d in devices]
        else:
            comparison_matrix[key] = [d["attributes"].get(key, "N/A") for d in devices]

    comparison = {
        "devices": devices,
        "comparison_matrix": comparison_matrix,
        "best_for": {
            "battery": devices[0]["name"] if devices else None,
            "camera": devices[0]["name"] if devices else None,
            "value": min(devices, key=lambda d: d["price_monthly"])["name"] if devices else None
        },
        "_visual": {
            "type": "comparison_table",
            "title": "Device Comparison",
            "devices": devices,
            "matrix": comparison_matrix,
            "context": context
        }
    }

    return comparison


async def get_similar_devices(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Find alternative devices at different price points."""
    device_id = arguments.get("device_id")

    current = next((d for d in MOCK_DEVICES if d["id"] == device_id), None)
    if not current:
        return {"error": "Device not found"}

    current_price = current["price_monthly"]

    # Find cheaper, similar price, and premium alternatives
    cheaper = [d for d in MOCK_DEVICES if d["price_monthly"] < current_price - 5]
    premium = [d for d in MOCK_DEVICES if d["price_monthly"] > current_price + 5]
    similar = [d for d in MOCK_DEVICES if abs(d["price_monthly"] - current_price) <= 5 and d["id"] != device_id]

    all_alternatives = (
        sorted(cheaper, key=lambda d: -d["rating"])[:2] +
        sorted(premium, key=lambda d: d["price_monthly"])[:2] +
        sorted(similar, key=lambda d: -d["rating"])[:2]
    )

    return {
        "current_device": current,
        "cheaper_options": sorted(cheaper, key=lambda d: -d["rating"])[:2],
        "premium_options": sorted(premium, key=lambda d: d["price_monthly"])[:2],
        "similar_price": sorted(similar, key=lambda d: -d["rating"])[:2],
        "_visual": {
            "type": "product_grid",
            "title": f"Alternatives to {current['name']}",
            "items": all_alternatives
        }
    }


async def recommend_plan_for_device(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Recommend plans suitable for a device and usage profile."""
    device_id = arguments.get("device_id")
    data_usage = arguments.get("estimated_data_usage_gb", 50)
    international = arguments.get("needs_international", False)

    device = next((d for d in MOCK_DEVICES if d["id"] == device_id), None)

    # Filter plans based on needs
    suitable_plans = []
    for plan in MOCK_PLANS:
        # Data requirement
        if plan["type"] == "capped":
            plan_data = int(plan["data"].replace("GB", ""))
            if plan_data < data_usage:
                continue

        # International requirement
        if international and not plan.get("international_roaming"):
            continue

        suitable_plans.append(plan)

    # Sort by price
    suitable_plans.sort(key=lambda p: p["price_monthly"])

    # Calculate total monthly cost
    recommendations = []
    if device and suitable_plans:
        for plan in suitable_plans[:3]:
            total_monthly = device["price_monthly"] + plan["price_monthly"]
            recommendations.append({
                "plan": plan,
                "device": device["name"],
                "total_monthly": total_monthly,
                "total_upfront": device["price_upfront"],
                "total_24_months": total_monthly * 24 + device["price_upfront"]
            })

    return {
        "device_id": device_id,
        "recommendations": recommendations,
        "message": f"Here are {len(recommendations)} plan options for the {device['name'] if device else 'selected device'}",
        "_visual": {
            "type": "plan_cards",
            "title": f"Plans for {device['name'] if device else 'Your Device'}",
            "items": suitable_plans[:3]
        }
    }


async def get_compatible_accessories(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Get accessories compatible with a device (upsell opportunity)."""
    device_id = arguments.get("device_id")

    accessories = MOCK_ACCESSORIES.get(device_id, MOCK_ACCESSORIES["default"])

    # Get device name for context
    device = next((d for d in MOCK_DEVICES if d["id"] == device_id), None)
    device_name = device["name"] if device else "this device"

    # Group accessories by type for better presentation
    essential = [a for a in accessories if a.get("type") in ["case", "screen_protector"]]
    optional = [a for a in accessories if a.get("type") not in ["case", "screen_protector", None]]

    return {
        "device_id": device_id,
        "accessories": accessories,
        "recommended": accessories[0] if accessories else None,
        "bundle_discount": "Save 10% when purchased together",
        "_visual": {
            "type": "accessory_grid",
            "title": f"Accessories for {device_name}",
            "items": accessories
        }
    }


async def calculate_total_cost(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Calculate complete cost breakdown for a purchase."""
    plan_id = arguments.get("plan_id")
    device_id = arguments.get("device_id")
    accessory_ids = arguments.get("accessory_ids", [])
    contract_months = arguments.get("contract_months", 24)

    device = next((d for d in MOCK_DEVICES if d["id"] == device_id), None)
    plan = next((p for p in MOCK_PLANS if p["id"] == plan_id), None)

    if not device or not plan:
        return {"error": "Invalid device or plan ID"}

    # Calculate accessories cost
    all_accessories = []
    for acc_list in MOCK_ACCESSORIES.values():
        all_accessories.extend(acc_list)

    accessories_cost = sum(
        acc["price"] for acc in all_accessories if acc["id"] in accessory_ids
    )

    # Cost breakdown
    upfront_total = device["price_upfront"] + accessories_cost
    monthly_total = device["price_monthly"] + plan["price_monthly"]
    contract_total = (monthly_total * contract_months) + upfront_total

    breakdown_data = {
        "upfront_costs": {
            "device": device["price_upfront"],
            "accessories": accessories_cost,
            "total": upfront_total
        },
        "monthly_costs": {
            "device": device["price_monthly"],
            "plan": plan["price_monthly"],
            "total": monthly_total
        },
        "contract_summary": {
            "duration_months": contract_months,
            "total_cost": contract_total,
            "monthly_payment": monthly_total
        }
    }

    return {
        "breakdown": breakdown_data,
        "device_name": device["name"],
        "plan_name": plan["name"],
        "_visual": {
            "type": "price_breakdown",
            "data": {
                "items": [
                    {"label": f"{device['name']} (device)", "amount": device["price_monthly"], "type": "monthly"},
                    {"label": f"{plan['name']} (plan)", "amount": plan["price_monthly"], "type": "monthly"}
                ],
                "total_upfront": upfront_total,
                "total_monthly": monthly_total,
                "total_24m": contract_total
            }
        }
    }


async def check_stock_availability(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Check device stock at local stores."""
    device_id = arguments.get("device_id")
    postcode = arguments.get("postcode", "SW1A 1AA")

    device = next((d for d in MOCK_DEVICES if d["id"] == device_id), None)
    if not device:
        return {"error": "Device not found"}

    # Mock store availability
    stores = [
        {"name": "Contoso Oxford Street", "distance_miles": 0.5, "stock": random.choice([0, 2, 5, 10])},
        {"name": "Contoso Westfield", "distance_miles": 2.3, "stock": random.choice([0, 1, 8])},
        {"name": "Contoso Covent Garden", "distance_miles": 1.1, "stock": random.choice([3, 7, 12])}
    ]

    online_stock = random.choice(["In stock", "Low stock - 3 remaining", "Out of stock"])

    return {
        "device": device["name"],
        "online_availability": online_stock,
        "nearby_stores": stores,
        "postcode_searched": postcode
    }


# Customer & Eligibility Tools (MOCKED)

async def check_upgrade_eligibility(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Check if customer is eligible for upgrade (MOCKED)."""
    await asyncio.sleep(0.5)  # Simulate API call

    account_number = arguments.get("account_number", "MOCK")

    eligible = random.choice([True, True, False])  # 66% eligible
    months_remaining = 0 if eligible else random.randint(1, 12)

    return {
        "account_number": account_number,
        "eligible": eligible,
        "contract_end_date": (datetime.now() + timedelta(days=months_remaining * 30)).strftime("%Y-%m-%d"),
        "months_remaining": months_remaining,
        "early_upgrade_fee": 0 if eligible else months_remaining * 15,
        "message": "You're eligible to upgrade now!" if eligible else f"Upgrade available in {months_remaining} months",
        "_visual": {
            "type": "info_callout",
            "data": {
                "message": "✓ You're eligible to upgrade now!" if eligible else f"⏳ Upgrade available in {months_remaining} months"
            }
        }
    }


async def get_customer_usage(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Get customer's historical usage to recommend appropriate plan (MOCKED)."""
    await asyncio.sleep(0.5)

    return {
        "account_number": arguments.get("account_number"),
        "average_monthly_usage": {
            "data_gb": random.randint(10, 80),
            "minutes": random.randint(100, 800),
            "texts": random.randint(50, 500)
        },
        "peak_usage_month": {
            "data_gb": random.randint(60, 120),
            "month": "August 2024"
        },
        "current_plan": random.choice(["Essential 50GB", "Unlimited Lite"]),
        "recommendation": "Based on your usage, consider upgrading to 100GB plan"
    }


async def check_coverage(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Check network coverage at customer's location."""
    postcode = arguments.get("postcode")
    service_type = arguments.get("service_type", "5g")  # "4g", "5g", "broadband"

    # Mock coverage data
    coverage_quality = random.choice(["Excellent", "Good", "Fair"])

    return {
        "postcode": postcode,
        "service_type": service_type.upper(),
        "coverage": coverage_quality,
        "signal_strength": random.randint(3, 5),
        "max_speed_mbps": random.randint(50, 300) if service_type == "5g" else random.randint(20, 80),
        "indoor_coverage": random.choice([True, True, False]),
        "nearby_towers": random.randint(2, 8)
    }


async def analyze_customer_profile(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Analyze customer profile and generate proactive recommendations based on usage, travel, billing, and device history."""
    account_number = arguments.get("account_number")

    profile = get_profile(account_number)

    if not profile:
        return {
            "account_number": account_number,
            "error": "Customer profile not found",
            "recommendations": []
        }

    recommendations = []

    # Analyze data usage patterns
    usage_history = profile.get("usage_history", [])
    if len(usage_history) >= 3:
        recent_usage = usage_history[:3]  # Last 3 months
        avg_data = sum(m["data_gb"] for m in recent_usage) / len(recent_usage)
        current_plan = profile.get("current_plan", {})
        data_allowance = current_plan.get("data_allowance", 50)

        # High data usage recommendation
        if avg_data > data_allowance * 0.85:  # Using >85% consistently
            overage_history = profile.get("billing_history", [])[:3]
            avg_overage = sum(b.get("overage_charge", 0) for b in overage_history) / len(overage_history)

            recommendations.append({
                "type": "plan_upgrade",
                "priority": "high",
                "reason": f"Using {avg_data:.0f}GB/month on average (85%+ of your {data_allowance}GB plan)",
                "customer_quote": f"You've been hitting your data limit consistently",
                "suggested_plan_id": "unlimited-max",
                "suggested_plan_name": "Unlimited Max",
                "monthly_savings": avg_overage,
                "talking_point": f"You're averaging {avg_data:.0f}GB but paying £{avg_overage:.0f}/month in overage fees. Unlimited would save you money."
            })

    # Analyze travel patterns
    travel_history = profile.get("travel_history", [])
    if len(travel_history) > 0:
        trips_without_roaming = [t for t in travel_history if not t.get("roaming_used", False)]

        if len(trips_without_roaming) > 0:
            total_roaming_charges = sum(t.get("roaming_charges", 0) for t in trips_without_roaming)
            countries = list(set(t["country"] for t in trips_without_roaming))

            recommendations.append({
                "type": "roaming_pass",
                "priority": "high",
                "reason": f"Traveled to {len(countries)} countries without roaming ({', '.join(countries[:2])})",
                "customer_quote": f"You've traveled internationally {len(trips_without_roaming)} times this year",
                "suggested_addon": "international-roaming",
                "monthly_cost": 5,
                "annual_savings": total_roaming_charges,
                "talking_point": f"You've spent £{total_roaming_charges:.0f} on roaming fees. Our roaming pass is just £5/month and covers 81 countries."
            })

    # Analyze device age
    device = profile.get("current_device", {})
    device_age_months = device.get("age_months", 0)

    if device_age_months > 24:  # Older than 2 years
        trade_in_value = device.get("trade_in_value", 0)

        recommendations.append({
            "type": "device_upgrade",
            "priority": "medium" if device_age_months > 36 else "low",
            "reason": f"{device.get('model')} is {device_age_months} months old ({device_age_months // 12} years)",
            "customer_quote": f"Your phone has been going strong for {device_age_months // 12} years",
            "trade_in_value": trade_in_value,
            "suggested_devices": ["iphone-15-pro", "samsung-s24-ultra", "pixel-8-pro"],
            "talking_point": f"Your {device.get('model')} is worth £{trade_in_value} trade-in. That could bring down the cost of a new phone significantly."
        })

    # Analyze billing patterns
    billing_history = profile.get("billing_history", [])
    late_payments = [b for b in billing_history if b.get("late", False)]

    if len(late_payments) >= 2:  # 2+ late payments
        total_late_fees = sum(b.get("late_fee", 0) for b in late_payments)

        recommendations.append({
            "type": "payment_plan",
            "priority": "low",
            "reason": f"{len(late_payments)} late payments in recent history",
            "customer_quote": "Flexible payment options available",
            "suggested_option": "direct_debit",
            "monthly_savings": total_late_fees / len(late_payments),
            "talking_point": f"You've paid £{total_late_fees:.0f} in late fees. Setting up direct debit ensures you never miss a payment."
        })

    # Sort by priority
    priority_order = {"high": 0, "medium": 1, "low": 2}
    recommendations.sort(key=lambda r: priority_order.get(r.get("priority", "low"), 2))

    # Return top recommendation as primary
    return {
        "account_number": account_number,
        "customer_name": profile.get("name"),
        "recommendations": recommendations,
        "primary_recommendation": recommendations[0] if recommendations else None,
        "profile_summary": {
            "current_plan": profile.get("current_plan", {}).get("plan_name"),
            "current_device": device.get("model"),
            "avg_monthly_data": sum(m["data_gb"] for m in usage_history[:3]) / min(3, len(usage_history)) if usage_history else 0,
            "upgrade_eligible": profile.get("contract", {}).get("eligible_for_upgrade", False)
        }
    }


async def run_credit_check(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Run credit check for contract approval. Requires customer details."""
    # Require customer information
    customer_name = arguments.get("customer_name")
    address = arguments.get("address")
    postcode = arguments.get("postcode")
    dob = arguments.get("date_of_birth")

    if not all([customer_name, address, postcode]):
        return {
            "error": "Missing required information",
            "message": "I need your full name, address, and postcode to run the credit check",
            "_visual": {
                "type": "info_callout",
                "data": {"message": "📋 Please provide your details for credit check"}
            }
        }

    # Simulate different outcomes
    await asyncio.sleep(2)  # Simulate processing time

    outcome = random.choices(
        ['approved', 'approved', 'approved', 'review_required', 'declined'],
        weights=[0.7, 0.15, 0.1, 0.04, 0.01]
    )[0]

    if outcome == 'approved':
        deposit = random.choice([0, 0, 0, 99]) if random.random() > 0.7 else 0
        return {
            "customer_name": customer_name,
            "status": "approved",
            "deposit_required": deposit,
            "credit_limit": 2500,
            "message": f"Credit check passed! {f'Deposit of £{deposit} required.' if deposit > 0 else 'No deposit needed.'}",
            "_visual": {
                "layout": "multi_section",
                "theme": "success",
                "sections": [
                    {
                        "type": "info_callout",
                        "data": {
                            "message": f"📋 Credit Check for: {customer_name}\n📍 Delivery to: {address}, {postcode}"
                        },
                        "style": "minimal"
                    },
                    {
                        "type": "credit_check_status",
                        "data": {
                            "status": "approved",
                            "message": "Great news! Your credit check has been approved.",
                            "credit_limit": 2500
                        },
                        "emphasis": "high"
                    }
                ],
                "animation": "scale"
            }
        }
    elif outcome == 'review_required':
        return {
            "customer_name": customer_name,
            "status": "review_required",
            "message": "Your application requires manual review. We'll contact you within 24 hours.",
            "_visual": {
                "type": "credit_check_status",
                "data": {
                    "status": "review_required",
                    "message": "Your application needs a quick review."
                }
            }
        }
    else:
        return {
            "customer_name": customer_name,
            "status": "declined",
            "message": "Unfortunately, we cannot approve your application at this time.",
            "reasons": [
                "Credit history requires further review",
                "Consider our pay-as-you-go options instead"
            ],
            "_visual": {
                "type": "credit_check_status",
                "data": {
                    "status": "declined",
                    "message": "We're unable to approve your application at this time."
                }
            }
        }


async def verify_identity(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Verify customer identity (MOCKED)."""
    await asyncio.sleep(1.5)

    return {
        "verified": True,
        "id_type": arguments.get("id_type"),
        "confidence": "high",
        "message": "Identity verified successfully"
    }


async def check_trade_in_value(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Estimate trade-in value for customer's old device."""
    device_model = arguments.get("device_model", "")
    condition = arguments.get("condition", "good")  # excellent, good, fair, poor

    if not device_model:
        return {
            "error": "Missing device model",
            "message": "Please tell me what phone you'd like to trade in"
        }

    # Simulate processing
    await asyncio.sleep(1)

    # Mock trade-in values based on device model and condition
    base_values = {
        "iphone 15 pro": 650,
        "iphone 15": 550,
        "iphone 14 pro": 500,
        "iphone 14": 400,
        "iphone 13": 300,
        "iphone 12": 200,
        "samsung galaxy s24 ultra": 600,
        "samsung galaxy s24": 500,
        "samsung galaxy s23": 400,
        "samsung galaxy a54": 200,
        "google pixel 8 pro": 450,
        "google pixel 8": 350,
        "google pixel 8a": 250,
    }

    # Find matching device (case insensitive, partial match)
    device_lower = device_model.lower()
    base_value = 150  # Default for unknown devices
    matched_model = device_model

    for model_key, value in base_values.items():
        if model_key in device_lower or device_lower in model_key:
            base_value = value
            matched_model = model_key.title()
            break

    # Adjust for condition
    condition_multipliers = {
        "excellent": 1.0,
        "good": 0.75,
        "fair": 0.5,
        "poor": 0.25
    }

    multiplier = condition_multipliers.get(condition.lower(), 0.75)
    trade_in_value = int(base_value * multiplier)

    # Bonus offer (random chance)
    bonus_offer = None
    if random.random() > 0.6:
        bonus_offer = f"Trade in today and get an extra £50 off your new phone!"

    # Build response with visual
    return {
        "device_model": matched_model,
        "condition": condition,
        "trade_in_value": trade_in_value,
        "original_value": base_value,
        "message": f"Your {matched_model} in {condition} condition is worth £{trade_in_value} as a trade-in.",
        "_visual": {
            "layout": "single_focus",
            "theme": "default",
            "sections": [
                {
                    "type": "trade_in_value",
                    "data": {
                        "device_model": matched_model,
                        "condition": condition,
                        "trade_in_value": trade_in_value,
                        "original_price": base_value,
                        "factors": {
                            "screen_condition": "Good" if condition != "poor" else "Cracked",
                            "battery_health": f"{random.randint(75, 95)}%" if condition in ["excellent", "good"] else f"{random.randint(50, 70)}%",
                            "physical_damage": "None" if condition == "excellent" else "Minor scratches" if condition == "good" else "Visible wear"
                        },
                        "bonus_offer": bonus_offer,
                        "next_steps": [
                            "Add your new phone to cart",
                            "Trade-in value applied at checkout",
                            "Send your old phone within 14 days"
                        ]
                    },
                    "emphasis": "high"
                }
            ],
            "animation": "fade"
        }
    }


# Cart Management Tools

async def add_to_cart(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Add item to shopping cart."""
    session_id = arguments.get("session_id", "default")
    item_type = arguments.get("item_type")  # "device", "plan", "accessory"
    item_id = arguments.get("item_id")
    config = arguments.get("config", {})  # color, storage, etc.

    if session_id not in SHOPPING_CART:
        SHOPPING_CART[session_id] = {"items": [], "created_at": datetime.now()}

    cart_item = {
        "id": f"cart_{len(SHOPPING_CART[session_id]['items'])}",
        "type": item_type,
        "item_id": item_id,
        "config": config,
        "added_at": datetime.now().isoformat()
    }

    SHOPPING_CART[session_id]["items"].append(cart_item)

    # Get full cart summary for visual
    cart_summary = await get_cart_summary({"session_id": session_id})

    return {
        "success": True,
        "cart_item_id": cart_item["id"],
        "cart_count": len(SHOPPING_CART[session_id]["items"]),
        "message": f"Added {item_type} to cart",
        "_visual": {
            "type": "cart_preview",
            "title": "Shopping Cart",
            "items": cart_summary.get("items", []),
            "summary": {
                "monthly": cart_summary.get("total_monthly", 0),
                "total_24m": cart_summary.get("total_24m", 0)
            }
        }
    }


async def remove_from_cart(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Remove item from cart."""
    session_id = arguments.get("session_id", "default")
    cart_item_id = arguments.get("cart_item_id")

    if session_id in SHOPPING_CART:
        SHOPPING_CART[session_id]["items"] = [
            item for item in SHOPPING_CART[session_id]["items"]
            if item["id"] != cart_item_id
        ]

    # Get updated cart summary for visual
    cart_summary = await get_cart_summary({"session_id": session_id})

    return {
        "success": True,
        "cart_count": len(SHOPPING_CART.get(session_id, {}).get("items", [])),
        "message": "Item removed from cart",
        "_visual": {
            "type": "cart_preview",
            "title": "Shopping Cart",
            "items": cart_summary.get("items", []),
            "summary": {
                "monthly": cart_summary.get("total_monthly", 0),
                "total_24m": cart_summary.get("total_24m", 0)
            }
        }
    }


async def get_cart_summary(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Get complete cart with pricing."""
    session_id = arguments.get("session_id", "default")

    if session_id not in SHOPPING_CART:
        return {"items": [], "total_upfront": 0, "total_monthly": 0}

    cart = SHOPPING_CART[session_id]
    items_details = []
    total_upfront = 0
    total_monthly = 0

    for item in cart["items"]:
        if item["type"] == "device":
            device = next((d for d in MOCK_DEVICES if d["id"] == item["item_id"]), None)
            if device:
                items_details.append({**device, "cart_item_id": item["id"]})
                total_upfront += device["price_upfront"]
                total_monthly += device["price_monthly"]
        elif item["type"] == "plan":
            plan = next((p for p in MOCK_PLANS if p["id"] == item["item_id"]), None)
            if plan:
                items_details.append({**plan, "cart_item_id": item["id"]})
                total_monthly += plan["price_monthly"]
        elif item["type"] == "accessory":
            # Find accessory in any list
            for acc_list in MOCK_ACCESSORIES.values():
                acc = next((a for a in acc_list if a["id"] == item["item_id"]), None)
                if acc:
                    items_details.append({**acc, "cart_item_id": item["id"]})
                    total_upfront += acc["price"]
                    break

    return {
        "items": items_details,
        "summary": {
            "upfront_total": total_upfront,
            "monthly_total": total_monthly,
            "contract_value_24m": (total_monthly * 24) + total_upfront
        },
        "item_count": len(items_details),
        "_visual": {
            "type": "cart_preview",
            "title": "Your Cart",
            "items": items_details,
            "summary": {
                "monthly": total_monthly,
                "total_24m": (total_monthly * 24) + total_upfront
            }
        }
    }


async def apply_promo_code(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Apply promotional discount code (MOCKED)."""
    code = arguments.get("code", "").upper()
    cart_value = arguments.get("cart_value", 0)

    # Mock promo codes
    valid_codes = {
        "WELCOME10": {"type": "percentage", "value": 10, "description": "10% off first month"},
        "SAVE50": {"type": "fixed", "value": 50, "description": "£50 off upfront cost"},
        "STUDENT": {"type": "percentage", "value": 15, "description": "15% student discount"},
        "UPGRADE20": {"type": "fixed", "value": 20, "description": "£20 upgrade credit"}
    }

    if code in valid_codes:
        promo = valid_codes[code]
        if promo["type"] == "percentage":
            discount = cart_value * (promo["value"] / 100)
        else:
            discount = promo["value"]

        return {
            "valid": True,
            "code": code,
            "discount_amount": discount,
            "description": promo["description"],
            "message": f"Promo code applied! You save £{discount:.2f}"
        }

    return {
        "valid": False,
        "code": code,
        "message": "Invalid promo code"
    }


async def process_payment(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Process checkout and payment (MOCKED - Always succeeds)."""
    await asyncio.sleep(2)  # Simulate payment processing

    payment_method = arguments.get("payment_method", "card")
    session_id = arguments.get("session_id", "default")

    # Get cart details for order summary
    cart_summary = await get_cart_summary({"session_id": session_id})

    order_id = f"VF-{random.randint(100000, 999999)}"
    delivery_date = (datetime.now() + timedelta(days=random.randint(1, 3))).strftime("%A, %B %d")

    # Create stunning multi-section order confirmation
    cart_items = cart_summary.get("items", [])

    return {
        "success": True,
        "order_id": order_id,
        "confirmation_number": f"CONF-{random.randint(1000000, 9999999)}",
        "payment_status": "completed",
        "delivery_estimate": delivery_date,
        "message": "Order confirmed! You'll receive a confirmation email shortly.",
        "_visual": {
            "layout": "multi_section",
            "theme": "success",
            "header": {
                "title": "🎉 Order Confirmed!",
                "subtitle": f"Order #{order_id}",
                "badge": "Payment Complete"
            },
            "sections": [
                {
                    "type": "info_callout",
                    "data": {
                        "message": f"✅ Your order has been confirmed and will be delivered on {delivery_date}"
                    },
                    "style": "emphasized"
                },
                {
                    "type": "product_grid",
                    "title": "Your New Devices & Plans",
                    "data": {"items": cart_items[:4]},  # Show up to 4 items with images
                    "emphasis": "high"
                },
                {
                    "type": "price_breakdown",
                    "data": {
                        "items": [
                            {"label": item.get("name", "Item"), "amount": item.get("price_monthly", item.get("price", 0)), "type": "monthly" if "price_monthly" in item else "upfront"}
                            for item in cart_items
                        ],
                        "total_upfront": cart_summary.get("total_upfront", 0),
                        "total_monthly": cart_summary.get("total_monthly", 0),
                        "total_24m": cart_summary.get("total_24m", 0)
                    },
                    "style": "minimal"
                },
                {
                    "type": "section_divider",
                    "title": "What's Next?"
                },
                {
                    "type": "info_callout",
                    "data": {
                        "message": f"📧 Confirmation email sent\n📦 Track your delivery online\n📱 Your service activates on delivery day"
                    }
                }
            ],
            "animation": "scale"
        }
    }


async def get_available_plans(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Browse all available plans."""
    plan_type = arguments.get("plan_type")  # "unlimited", "capped", "all"

    if plan_type and plan_type != "all":
        filtered = [p for p in MOCK_PLANS if p["type"] == plan_type]
    else:
        filtered = MOCK_PLANS

    return {
        "plans": filtered,
        "count": len(filtered),
        "plan_type": plan_type or "all",
        "_visual": {
            "type": "plan_cards",
            "title": "Available Plans",
            "items": filtered
        }
    }


async def get_active_promotions(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Get current promotions and deals."""
    customer_type = arguments.get("customer_type", "new")  # "new", "upgrade", "existing"

    promotions = {
        "new": [
            {"title": "Welcome Offer", "description": "50% off first 3 months on Unlimited plans", "code": "WELCOME50"},
            {"title": "Free Accessories", "description": "Free case and screen protector with any iPhone", "auto_apply": True}
        ],
        "upgrade": [
            {"title": "Loyalty Reward", "description": "£100 credit towards new device", "code": "LOYAL100"},
            {"title": "Trade-In Bonus", "description": "Extra £50 when you trade in your old phone", "auto_apply": True}
        ],
        "existing": [
            {"title": "Refer a Friend", "description": "£25 credit for you and your friend", "code": "REFER25"}
        ]
    }

    promos = promotions.get(customer_type, [])

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


async def schedule_store_appointment(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Schedule in-store appointment (MOCKED)."""
    store_name = arguments.get("store_name", "Contoso Oxford Street")
    preferred_date = arguments.get("preferred_date")
    preferred_time = arguments.get("preferred_time")

    return {
        "confirmed": True,
        "appointment_id": f"APT-{random.randint(10000, 99999)}",
        "store": store_name,
        "date": preferred_date or (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d"),
        "time": preferred_time or "14:00",
        "staff_member": random.choice(["Sarah", "James", "Emma", "Mohammed"]),
        "message": "Appointment confirmed! You'll receive a reminder SMS."
    }


async def transfer_to_human_agent(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Transfer to human sales agent."""
    reason = arguments.get("reason", "customer_request")
    context = arguments.get("context", {})

    return {
        "transfer_initiated": True,
        "estimated_wait_time_minutes": random.randint(2, 8),
        "agent_type": "sales_specialist",
        "reference_number": f"TRF-{random.randint(100000, 999999)}",
        "message": "Connecting you to a sales specialist. Please hold..."
    }


async def customise_webpage(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """AI composes the visual display based on conversation context."""
    # Simply return the visual structure as-is
    # The frontend will render it via FlexibleRenderer

    return {
        "success": True,
        "message": "Visual updated",
        "_visual": arguments  # Pass through AI's composition directly
    }


async def send_quote_email(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Email quote to customer (MOCKED)."""
    email = arguments.get("email")
    cart_summary = arguments.get("cart_summary", {})

    return {
        "sent": True,
        "email": email,
        "quote_id": f"QT-{random.randint(100000, 999999)}",
        "valid_until": (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d"),
        "message": f"Quote sent to {email}. Valid for 7 days."
    }


# =============================================================================
# TOOLS REGISTRY
# =============================================================================

TOOLS_REGISTRY = {
    # Device Discovery & Recommendation
    "search_devices_by_attributes": {
        "definition": {
            "type": "function",
            "name": "search_devices_by_attributes",
            "description": "Search for devices based on customer requirements like battery life, camera quality, price range, brand, or use case. Use this when customer describes what they need in a phone.",
            "parameters": {
                "type": "object",
                "properties": {
                    "battery_life": {
                        "type": "string",
                        "enum": ["good", "very_good", "excellent"],
                        "description": "Required battery performance"
                    },
                    "camera_quality": {
                        "type": "string",
                        "enum": ["good", "very_good", "excellent"],
                        "description": "Required camera quality"
                    },
                    "price_max_monthly": {
                        "type": "number",
                        "description": "Maximum monthly payment willing to pay"
                    },
                    "brand": {
                        "type": "string",
                        "description": "Preferred brand (Apple, Samsung, Google, etc.)"
                    },
                    "use_case": {
                        "type": "string",
                        "enum": ["photography", "gaming", "business", "everyday", "budget", "content_creation"],
                        "description": "Primary use case for the device"
                    }
                }
            }
        },
        "executor": search_devices_by_attributes
    },

    "get_device_details": {
        "definition": {
            "type": "function",
            "name": "get_device_details",
            "description": "Get complete details, specifications, and reviews for a specific device.",
            "parameters": {
                "type": "object",
                "properties": {
                    "device_id": {
                        "type": "string",
                        "description": "Device identifier"
                    }
                },
                "required": ["device_id"]
            }
        },
        "executor": get_device_details
    },

    "compare_devices": {
        "definition": {
            "type": "function",
            "name": "compare_devices",
            "description": "Compare multiple devices side-by-side to help customer decide.",
            "parameters": {
                "type": "object",
                "properties": {
                    "device_ids": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of device IDs to compare"
                    }
                },
                "required": ["device_ids"]
            }
        },
        "executor": compare_devices
    },

    "get_similar_devices": {
        "definition": {
            "type": "function",
            "name": "get_similar_devices",
            "description": "Find alternative devices at different price points (cheaper, similar, premium).",
            "parameters": {
                "type": "object",
                "properties": {
                    "device_id": {
                        "type": "string",
                        "description": "Reference device ID"
                    }
                },
                "required": ["device_id"]
            }
        },
        "executor": get_similar_devices
    },

    "recommend_plan_for_device": {
        "definition": {
            "type": "function",
            "name": "recommend_plan_for_device",
            "description": "Recommend suitable plans for a device based on customer usage patterns.",
            "parameters": {
                "type": "object",
                "properties": {
                    "device_id": {
                        "type": "string",
                        "description": "Device ID"
                    },
                    "estimated_data_usage_gb": {
                        "type": "number",
                        "description": "Estimated monthly data usage in GB"
                    },
                    "needs_international": {
                        "type": "boolean",
                        "description": "Whether customer needs international roaming"
                    }
                },
                "required": ["device_id"]
            }
        },
        "executor": recommend_plan_for_device
    },

    "get_compatible_accessories": {
        "definition": {
            "type": "function",
            "name": "get_compatible_accessories",
            "description": "Get accessories compatible with a device (cases, chargers, earbuds). Use for upselling.",
            "parameters": {
                "type": "object",
                "properties": {
                    "device_id": {
                        "type": "string",
                        "description": "Device ID"
                    }
                },
                "required": ["device_id"]
            }
        },
        "executor": get_compatible_accessories
    },

    "calculate_total_cost": {
        "definition": {
            "type": "function",
            "name": "calculate_total_cost",
            "description": "Calculate complete cost breakdown including upfront, monthly, and total contract value.",
            "parameters": {
                "type": "object",
                "properties": {
                    "plan_id": {
                        "type": "string",
                        "description": "Plan ID"
                    },
                    "device_id": {
                        "type": "string",
                        "description": "Device ID"
                    },
                    "accessory_ids": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of accessory IDs"
                    },
                    "contract_months": {
                        "type": "number",
                        "description": "Contract duration in months (12, 24, 36)",
                        "enum": [12, 24, 36]
                    }
                },
                "required": ["plan_id", "device_id"]
            }
        },
        "executor": calculate_total_cost
    },

    "check_stock_availability": {
        "definition": {
            "type": "function",
            "name": "check_stock_availability",
            "description": "Check if device is in stock online and at nearby stores.",
            "parameters": {
                "type": "object",
                "properties": {
                    "device_id": {
                        "type": "string",
                        "description": "Device ID"
                    },
                    "postcode": {
                        "type": "string",
                        "description": "Customer postcode to find nearby stores"
                    }
                },
                "required": ["device_id"]
            }
        },
        "executor": check_stock_availability
    },

    # Customer & Eligibility
    "check_upgrade_eligibility": {
        "definition": {
            "type": "function",
            "name": "check_upgrade_eligibility",
            "description": "Check if existing customer is eligible for upgrade (MOCKED).",
            "parameters": {
                "type": "object",
                "properties": {
                    "account_number": {
                        "type": "string",
                        "description": "Customer account number"
                    }
                },
                "required": ["account_number"]
            }
        },
        "executor": check_upgrade_eligibility
    },

    "get_customer_usage": {
        "definition": {
            "type": "function",
            "name": "get_customer_usage",
            "description": "Get customer's historical data/minute usage to recommend appropriate plan (MOCKED).",
            "parameters": {
                "type": "object",
                "properties": {
                    "account_number": {
                        "type": "string",
                        "description": "Customer account number"
                    }
                },
                "required": ["account_number"]
            }
        },
        "executor": get_customer_usage
    },

    "check_coverage": {
        "definition": {
            "type": "function",
            "name": "check_coverage",
            "description": "Check Contoso network coverage (4G/5G) at customer's location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "postcode": {
                        "type": "string",
                        "description": "UK postcode"
                    },
                    "service_type": {
                        "type": "string",
                        "enum": ["4g", "5g", "broadband"],
                        "description": "Type of service to check"
                    }
                },
                "required": ["postcode"]
            }
        },
        "executor": check_coverage
    },

    "run_credit_check": {
        "definition": {
            "type": "function",
            "name": "run_credit_check",
            "description": "Run credit check for contract approval (MOCKED - mostly approves).",
            "parameters": {
                "type": "object",
                "properties": {
                    "customer_name": {
                        "type": "string",
                        "description": "Customer full name"
                    },
                    "address": {
                        "type": "string",
                        "description": "Full delivery address"
                    },
                    "postcode": {
                        "type": "string",
                        "description": "Customer postcode"
                    },
                    "date_of_birth": {
                        "type": "string",
                        "description": "Date of birth (YYYY-MM-DD) - optional"
                    }
                },
                "required": ["customer_name", "address", "postcode"]
            }
        },
        "executor": run_credit_check
    },

    "verify_identity": {
        "definition": {
            "type": "function",
            "name": "verify_identity",
            "description": "Verify customer identity (MOCKED).",
            "parameters": {
                "type": "object",
                "properties": {
                    "id_type": {
                        "type": "string",
                        "enum": ["passport", "drivers_license", "national_id"],
                        "description": "Type of ID document"
                    },
                    "id_number": {
                        "type": "string",
                        "description": "ID number"
                    }
                },
                "required": ["id_type", "id_number"]
            }
        },
        "executor": verify_identity
    },

    "check_trade_in_value": {
        "definition": {
            "type": "function",
            "name": "check_trade_in_value",
            "description": "Estimate trade-in value for customer's old device. Use when customer asks about trading in their current phone.",
            "parameters": {
                "type": "object",
                "properties": {
                    "device_model": {
                        "type": "string",
                        "description": "Model of the device to trade in (e.g., 'iPhone 14', 'Samsung Galaxy S23')"
                    },
                    "condition": {
                        "type": "string",
                        "enum": ["excellent", "good", "fair", "poor"],
                        "description": "Condition of the device: excellent (like new), good (minor wear), fair (noticeable wear), poor (damaged)"
                    }
                },
                "required": ["device_model"]
            }
        },
        "executor": check_trade_in_value
    },

    # Cart Management
    "add_to_cart": {
        "definition": {
            "type": "function",
            "name": "add_to_cart",
            "description": "Add device, plan, or accessory to shopping cart.",
            "parameters": {
                "type": "object",
                "properties": {
                    "session_id": {"type": "string", "description": "Session identifier"},
                    "item_type": {
                        "type": "string",
                        "enum": ["device", "plan", "accessory"],
                        "description": "Type of item"
                    },
                    "item_id": {
                        "type": "string",
                        "description": "Item identifier"
                    },
                    "config": {
                        "type": "object",
                        "description": "Item configuration (color, storage, etc.)"
                    }
                },
                "required": ["item_type", "item_id"]
            }
        },
        "executor": add_to_cart
    },

    "remove_from_cart": {
        "definition": {
            "type": "function",
            "name": "remove_from_cart",
            "description": "Remove item from shopping cart.",
            "parameters": {
                "type": "object",
                "properties": {
                    "session_id": {"type": "string"},
                    "cart_item_id": {"type": "string", "description": "Cart item ID to remove"}
                },
                "required": ["cart_item_id"]
            }
        },
        "executor": remove_from_cart
    },

    "get_cart_summary": {
        "definition": {
            "type": "function",
            "name": "get_cart_summary",
            "description": "Get current shopping cart with all items and pricing.",
            "parameters": {
                "type": "object",
                "properties": {
                    "session_id": {"type": "string"}
                }
            }
        },
        "executor": get_cart_summary
    },

    "apply_promo_code": {
        "definition": {
            "type": "function",
            "name": "apply_promo_code",
            "description": "Apply promotional discount code to purchase.",
            "parameters": {
                "type": "object",
                "properties": {
                    "code": {
                        "type": "string",
                        "description": "Promo code"
                    },
                    "cart_value": {
                        "type": "number",
                        "description": "Current cart value for percentage calculations"
                    }
                },
                "required": ["code"]
            }
        },
        "executor": apply_promo_code
    },

    "process_payment": {
        "definition": {
            "type": "function",
            "name": "process_payment",
            "description": "Process checkout and payment (MOCKED - completes order).",
            "parameters": {
                "type": "object",
                "properties": {
                    "payment_method": {
                        "type": "string",
                        "enum": ["card", "paypal", "direct_debit"],
                        "description": "Payment method"
                    },
                    "billing_address": {
                        "type": "object",
                        "description": "Billing address details"
                    }
                },
                "required": ["payment_method"]
            }
        },
        "executor": process_payment
    },

    "get_available_plans": {
        "definition": {
            "type": "function",
            "name": "get_available_plans",
            "description": "Browse all available Contoso plans.",
            "parameters": {
                "type": "object",
                "properties": {
                    "plan_type": {
                        "type": "string",
                        "enum": ["unlimited", "capped", "all"],
                        "description": "Filter by plan type"
                    }
                }
            }
        },
        "executor": get_available_plans
    },

    "get_active_promotions": {
        "definition": {
            "type": "function",
            "name": "get_active_promotions",
            "description": "Get current promotions and deals available.",
            "parameters": {
                "type": "object",
                "properties": {
                    "customer_type": {
                        "type": "string",
                        "enum": ["new", "upgrade", "existing"],
                        "description": "Customer type"
                    }
                }
            }
        },
        "executor": get_active_promotions
    },

    # Support & Engagement
    "schedule_store_appointment": {
        "definition": {
            "type": "function",
            "name": "schedule_store_appointment",
            "description": "Schedule in-person appointment at Contoso store (MOCKED).",
            "parameters": {
                "type": "object",
                "properties": {
                    "store_name": {"type": "string"},
                    "preferred_date": {"type": "string", "description": "YYYY-MM-DD"},
                    "preferred_time": {"type": "string", "description": "HH:MM"}
                }
            }
        },
        "executor": schedule_store_appointment
    },

    "transfer_to_human_agent": {
        "definition": {
            "type": "function",
            "name": "transfer_to_human_agent",
            "description": "Transfer customer to human sales specialist.",
            "parameters": {
                "type": "object",
                "properties": {
                    "reason": {"type": "string", "description": "Reason for transfer"},
                    "context": {"type": "object", "description": "Conversation context"}
                }
            }
        },
        "executor": transfer_to_human_agent
    },

    "send_quote_email": {
        "definition": {
            "type": "function",
            "name": "send_quote_email",
            "description": "Email purchase quote to customer (MOCKED).",
            "parameters": {
                "type": "object",
                "properties": {
                    "email": {"type": "string", "description": "Customer email"},
                    "cart_summary": {"type": "object", "description": "Current cart details"}
                },
                "required": ["email"]
            }
        },
        "executor": send_quote_email
    },

    "customise_webpage": {
        "definition": {
            "type": "function",
            "name": "customise_webpage",
            "description": "Update the left-side visual display based on conversation context. Use this to show products, plans, comparisons, checkout progress, or any other visual content. You have complete creative control over the layout and emphasis.",
            "parameters": {
                "type": "object",
                "properties": {
                    "layout": {
                        "type": "string",
                        "enum": ["single_focus", "two_column", "multi_section", "grid", "flow", "wizard"],
                        "description": "Overall page layout structure"
                    },
                    "header": {
                        "type": "object",
                        "properties": {
                            "title": {"type": "string"},
                            "subtitle": {"type": "string"},
                            "badge": {"type": "string"}
                        },
                        "description": "Optional header for the page"
                    },
                    "sections": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "type": {
                                    "type": "string",
                                    "enum": [
                                        "product_hero", "product_grid", "product_card", "product_carousel",
                                        "accessory_grid", "accessory_carousel", "accessory_card",
                                        "plan_card", "plan_selector", "plan_comparison",
                                        "price_breakdown", "checkout_stepper", "credit_check_status",
                                        "promo_banner", "info_callout", "section_divider"
                                    ],
                                    "description": "Type of component to render"
                                },
                                "data": {
                                    "type": "object",
                                    "description": "Data for this component - use results from previous tool calls"
                                },
                                "title": {"type": "string"},
                                "emphasis": {
                                    "type": "string",
                                    "enum": ["low", "medium", "high", "critical"],
                                    "description": "Visual prominence level"
                                },
                                "size": {
                                    "type": "string",
                                    "enum": ["sm", "md", "lg", "xl"]
                                }
                            },
                            "required": ["type", "data"]
                        },
                        "description": "Array of visual sections to display"
                    },
                    "cta": {
                        "type": "object",
                        "properties": {
                            "text": {"type": "string"},
                            "action": {"type": "string"},
                            "prominence": {
                                "type": "string",
                                "enum": ["primary", "secondary", "subtle"]
                            }
                        },
                        "description": "Optional call-to-action button"
                    },
                    "theme": {
                        "type": "string",
                        "enum": ["default", "success", "warning", "info"],
                        "description": "Overall page theme/mood"
                    },
                    "animation": {
                        "type": "string",
                        "enum": ["fade", "slide", "scale", "none"],
                        "description": "Entry animation"
                    }
                },
                "required": ["layout", "sections"]
            }
        },
        "executor": customise_webpage
    },

    "analyze_customer_profile": {
        "definition": {
            "type": "function",
            "name": "analyze_customer_profile",
            "description": "Analyze customer profile to generate proactive recommendations based on usage patterns, travel history, device age, and billing. Call this IMMEDIATELY at session start if account_number available.",
            "parameters": {
                "type": "object",
                "properties": {
                    "account_number": {
                        "type": "string",
                        "description": "Customer account number (e.g. VF001_HIGH_DATA_USER)"
                    }
                },
                "required": ["account_number"]
            }
        },
        "executor": analyze_customer_profile
    }
}

async def customise_webpage(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """AI composes the visual display based on conversation context."""
    # Simply return the visual structure as-is
    # The frontend will render it via FlexibleRenderer

    return {
        "success": True,
        "message": "Visual updated",
        "_visual": arguments  # Pass through AI's composition directly
    }
