"""
Mock Customer Profiles for Proactive Nudging Demo
"""

CUSTOMER_PROFILES = {
    "VF001_HIGH_DATA_USER": {
        "account_number": "VF001_HIGH_DATA_USER",
        "name": "Sarah Chen",
        "usage_history": [
            {"month": "2024-10", "data_gb": 88, "minutes": 450, "texts": 200},
            {"month": "2024-09", "data_gb": 92, "minutes": 520, "texts": 180},
            {"month": "2024-08", "data_gb": 95, "minutes": 480, "texts": 220},
            {"month": "2024-07", "data_gb": 87, "minutes": 410, "texts": 195},
            {"month": "2024-06", "data_gb": 90, "minutes": 470, "texts": 210},
            {"month": "2024-05", "data_gb": 85, "minutes": 440, "texts": 185}
        ],
        "travel_history": [],
        "billing_history": [
            {"month": "2024-10", "amount": 50, "status": "paid", "late": False, "overage_charge": 15},
            {"month": "2024-09", "amount": 53, "status": "paid", "late": False, "overage_charge": 18},
            {"month": "2024-08", "amount": 55, "status": "paid", "late": False, "overage_charge": 20}
        ],
        "current_plan": {
            "plan_id": "essential-50gb",
            "plan_name": "Essential 50GB",
            "data_allowance": 50,
            "price_monthly": 35,
            "international_roaming": False
        },
        "current_device": {
            "model": "Samsung Galaxy S22",
            "purchase_date": "2022-11-15",
            "age_months": 24,
            "trade_in_value": 180
        },
        "contract": {
            "start_date": "2022-11-15",
            "end_date": "2024-11-15",
            "months_remaining": 0,
            "eligible_for_upgrade": True
        },
        "preferences": {
            "brand_affinity": "Samsung",
            "price_sensitivity": "medium",
            "feature_priorities": ["data_allowance", "5g"],
            "last_interaction": "2024-10-15"
        }
    },

    "VF002_FREQUENT_TRAVELER": {
        "account_number": "VF002_FREQUENT_TRAVELER",
        "name": "James Mitchell",
        "usage_history": [
            {"month": "2024-10", "data_gb": 35, "minutes": 650, "texts": 120},
            {"month": "2024-09", "data_gb": 42, "minutes": 720, "texts": 140},
            {"month": "2024-08", "data_gb": 38, "minutes": 680, "texts": 130},
            {"month": "2024-07", "data_gb": 40, "minutes": 700, "texts": 125},
            {"month": "2024-06", "data_gb": 36, "minutes": 640, "texts": 115},
            {"month": "2024-05", "data_gb": 39, "minutes": 660, "texts": 135}
        ],
        "travel_history": [
            {"country": "France", "dates": ["2024-10-05", "2024-10-12"], "roaming_used": False, "roaming_charges": 45},
            {"country": "Germany", "dates": ["2024-08-15", "2024-08-22"], "roaming_used": False, "roaming_charges": 38},
            {"country": "Spain", "dates": ["2024-06-10", "2024-06-17"], "roaming_used": False, "roaming_charges": 42},
            {"country": "Italy", "dates": ["2024-04-05", "2024-04-10"], "roaming_used": False, "roaming_charges": 35}
        ],
        "billing_history": [
            {"month": "2024-10", "amount": 65, "status": "paid", "late": False, "overage_charge": 0, "roaming_charge": 45},
            {"month": "2024-09", "amount": 20, "status": "paid", "late": False, "overage_charge": 0, "roaming_charge": 0},
            {"month": "2024-08", "amount": 58, "status": "paid", "late": False, "overage_charge": 0, "roaming_charge": 38}
        ],
        "current_plan": {
            "plan_id": "essential-50gb",
            "plan_name": "Essential 50GB",
            "data_allowance": 50,
            "price_monthly": 20,
            "international_roaming": False
        },
        "current_device": {
            "model": "iPhone 14",
            "purchase_date": "2023-09-20",
            "age_months": 14,
            "trade_in_value": 350
        },
        "contract": {
            "start_date": "2023-09-20",
            "end_date": "2025-09-20",
            "months_remaining": 10,
            "eligible_for_upgrade": False
        },
        "preferences": {
            "brand_affinity": "Apple",
            "price_sensitivity": "low",
            "feature_priorities": ["international_roaming", "camera_quality"],
            "last_interaction": "2024-10-20"
        }
    },

    "VF003_OLD_DEVICE": {
        "account_number": "VF003_OLD_DEVICE",
        "name": "Michael Brown",
        "usage_history": [
            {"month": "2024-10", "data_gb": 25, "minutes": 300, "texts": 150},
            {"month": "2024-09", "data_gb": 28, "minutes": 320, "texts": 160},
            {"month": "2024-08", "data_gb": 22, "minutes": 280, "texts": 140},
            {"month": "2024-07", "data_gb": 26, "minutes": 310, "texts": 155},
            {"month": "2024-06", "data_gb": 24, "minutes": 290, "texts": 145},
            {"month": "2024-05", "data_gb": 27, "minutes": 305, "texts": 152}
        ],
        "travel_history": [],
        "billing_history": [
            {"month": "2024-10", "amount": 25, "status": "paid", "late": False, "overage_charge": 0},
            {"month": "2024-09", "amount": 25, "status": "paid", "late": False, "overage_charge": 0},
            {"month": "2024-08", "amount": 25, "status": "paid", "late": False, "overage_charge": 0}
        ],
        "current_plan": {
            "plan_id": "essential-30gb",
            "plan_name": "Essential 30GB",
            "data_allowance": 30,
            "price_monthly": 25,
            "international_roaming": False
        },
        "current_device": {
            "model": "iPhone 11",
            "purchase_date": "2020-10-15",
            "age_months": 49,
            "trade_in_value": 120
        },
        "contract": {
            "start_date": "2020-10-15",
            "end_date": "2022-10-15",
            "months_remaining": 0,
            "eligible_for_upgrade": True
        },
        "preferences": {
            "brand_affinity": "Apple",
            "price_sensitivity": "high",
            "feature_priorities": ["battery_life", "price"],
            "last_interaction": "2024-09-10"
        }
    },

    "VF004_PAYMENT_ISSUES": {
        "account_number": "VF004_PAYMENT_ISSUES",
        "name": "Emma Wilson",
        "usage_history": [
            {"month": "2024-10", "data_gb": 45, "minutes": 520, "texts": 180},
            {"month": "2024-09", "data_gb": 48, "minutes": 540, "texts": 190},
            {"month": "2024-08", "data_gb": 42, "minutes": 510, "texts": 175},
            {"month": "2024-07", "data_gb": 46, "minutes": 530, "texts": 185},
            {"month": "2024-06", "data_gb": 44, "minutes": 515, "texts": 182},
            {"month": "2024-05", "data_gb": 47, "minutes": 525, "texts": 188}
        ],
        "travel_history": [],
        "billing_history": [
            {"month": "2024-10", "amount": 35, "status": "paid", "late": True, "overage_charge": 0, "late_fee": 10},
            {"month": "2024-09", "amount": 35, "status": "paid", "late": True, "overage_charge": 0, "late_fee": 10},
            {"month": "2024-08", "amount": 35, "status": "paid", "late": False, "overage_charge": 0},
            {"month": "2024-07", "amount": 35, "status": "paid", "late": True, "overage_charge": 0, "late_fee": 10}
        ],
        "current_plan": {
            "plan_id": "essential-50gb",
            "plan_name": "Essential 50GB",
            "data_allowance": 50,
            "price_monthly": 35,
            "international_roaming": False
        },
        "current_device": {
            "model": "Samsung Galaxy A54",
            "purchase_date": "2023-04-10",
            "age_months": 19,
            "trade_in_value": 150
        },
        "contract": {
            "start_date": "2023-04-10",
            "end_date": "2025-04-10",
            "months_remaining": 5,
            "eligible_for_upgrade": False
        },
        "preferences": {
            "brand_affinity": "Samsung",
            "price_sensitivity": "very_high",
            "feature_priorities": ["price", "battery_life"],
            "last_interaction": "2024-10-25"
        }
    },

    "VF005_PREMIUM_CUSTOMER": {
        "account_number": "VF005_PREMIUM_CUSTOMER",
        "name": "David Lee",
        "usage_history": [
            {"month": "2024-10", "data_gb": 120, "minutes": 850, "texts": 220},
            {"month": "2024-09", "data_gb": 115, "minutes": 820, "texts": 210},
            {"month": "2024-08", "data_gb": 125, "minutes": 880, "texts": 230},
            {"month": "2024-07", "data_gb": 118, "minutes": 840, "texts": 215},
            {"month": "2024-06", "data_gb": 122, "minutes": 860, "texts": 225},
            {"month": "2024-05", "data_gb": 119, "minutes": 830, "texts": 218}
        ],
        "travel_history": [
            {"country": "USA", "dates": ["2024-09-01", "2024-09-15"], "roaming_used": True, "roaming_charges": 0},
            {"country": "Japan", "dates": ["2024-07-10", "2024-07-20"], "roaming_used": True, "roaming_charges": 0},
            {"country": "Dubai", "dates": ["2024-05-05", "2024-05-12"], "roaming_used": True, "roaming_charges": 0}
        ],
        "billing_history": [
            {"month": "2024-10", "amount": 50, "status": "paid", "late": False, "overage_charge": 0},
            {"month": "2024-09", "amount": 50, "status": "paid", "late": False, "overage_charge": 0},
            {"month": "2024-08", "amount": 50, "status": "paid", "late": False, "overage_charge": 0}
        ],
        "current_plan": {
            "plan_id": "unlimited-max",
            "plan_name": "Unlimited Max",
            "data_allowance": 999999,
            "price_monthly": 50,
            "international_roaming": True
        },
        "current_device": {
            "model": "iPhone 15 Pro Max",
            "purchase_date": "2023-10-01",
            "age_months": 13,
            "trade_in_value": 650
        },
        "contract": {
            "start_date": "2023-10-01",
            "end_date": "2025-10-01",
            "months_remaining": 11,
            "eligible_for_upgrade": False
        },
        "preferences": {
            "brand_affinity": "Apple",
            "price_sensitivity": "very_low",
            "feature_priorities": ["5g", "international_roaming", "premium_support"],
            "last_interaction": "2024-11-01"
        }
    }
}


def get_profile(account_number: str):
    """Get customer profile by account number"""
    return CUSTOMER_PROFILES.get(account_number)


def list_profiles():
    """List all available customer profiles"""
    return [
        {
            "account_number": profile["account_number"],
            "name": profile["name"],
            "scenario": _get_scenario_description(account_number)
        }
        for account_number, profile in CUSTOMER_PROFILES.items()
    ]


def _get_scenario_description(account_number: str) -> str:
    """Get human-readable scenario description"""
    scenarios = {
        "VF001_HIGH_DATA_USER": "High data user (90GB avg on 50GB plan) - needs unlimited",
        "VF002_FREQUENT_TRAVELER": "Travels 4x/year without roaming - needs roaming pass",
        "VF003_OLD_DEVICE": "iPhone 11 (4 years old) - needs device upgrade",
        "VF004_PAYMENT_ISSUES": "Late payments (3 of last 4 months) - needs payment plan",
        "VF005_PREMIUM_CUSTOMER": "Premium customer on Unlimited Max - accessory upsell"
    }
    return scenarios.get(account_number, "Unknown scenario")
