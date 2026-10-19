"""Shipping Rate and Delivery Estimate Calculator.

Provides modular calculation functions for weight-based tiers,
shipping speed multipliers, destination zones, and sales tax application.
"""

# Base rate constants
BASE_FLAT_FEE = 5.00  # Minimum handling fee in USD
TAX_RATE = 0.0825     # Standard sales tax rate (8.25%)

# Speed multipliers
SHIPPING_METHODS = {
    "standard": 1.0,
    "express": 1.5,
    "overnight": 2.25
}

# Regional destination adjustments (multipliers on base calculation)
ZONE_RATES = {
    "zone_1": 1.0,   # Local / In-state
    "zone_2": 1.25,  # Regional / Domestic
    "zone_3": 1.75   # Remote / Long-distance
}


def calculate_weight_tier_cost(weight_lbs: float) -> float:
    """Calculate the tiered rate based on package weight.

    Tier Breakdown:
      - 0 to 2 lbs: $1.50 per lb
      - >2 to 6 lbs: $3.00 per lb
      - >6 to 10 lbs: $4.00 per lb
      - Over 10 lbs: $4.75 per lb
    """
    if weight_lbs <= 0:
        raise ValueError("Package weight must be greater than zero.")

    if weight_lbs <= 2.0:
        rate_per_lb = 1.50
    elif weight_lbs <= 6.0:
        rate_per_lb = 3.00
    elif weight_lbs <= 10.0:
        rate_per_lb = 4.00
    else:
        rate_per_lb = 4.75

    return weight_lbs * rate_per_lb


def calculate_shipping_cost(
    weight_lbs: float,
    method: str = "standard",
    zone: str = "zone_1",
    include_tax: bool = True
) -> dict:
    """Compute the subtotal, tax amount, and total final shipping cost.

    Returns a structured dictionary with line-item breakdowns.
    """
    method_key = method.lower()
    zone_key = zone.lower()

    if method_key not in SHIPPING_METHODS:
        raise ValueError(
            f"Invalid shipping method '{method}'. Valid options: {list(SHIPPING_METHODS.keys())}"
        )

    if zone_key not in ZONE_RATES:
        raise ValueError(
            f"Invalid destination zone '{zone}'. Valid options: {list(ZONE_RATES.keys())}"
        )

    # 1. Base cost calculation
    weight_cost = calculate_weight_tier_cost(weight_lbs)
    method_multiplier = SHIPPING_METHODS[method_key]
    zone_multiplier = ZONE_RATES[zone_key]

    subtotal = (BASE_FLAT_FEE + weight_cost) * method_multiplier * zone_multiplier

    # 2. Tax calculation
    tax_amount = (subtotal * TAX_RATE) if include_tax else 0.00
    total = subtotal + tax_amount

    return {
        "weight_lbs": weight_lbs,
        "method": method_key,
        "zone": zone_key,
        "base_flat_fee": round(BASE_FLAT_FEE, 2),
        "weight_cost": round(weight_cost, 2),
        "subtotal": round(subtotal, 2),
        "tax_amount": round(tax_amount, 2),
        "total_cost": round(total, 2)
    }


def main():
    """CLI demonstration and quick validation."""
    print("=== Logistics Shipping Rate Calculator ===")
    test_weights = [1.5, 4.0, 8.5, 12.0]

    for weight in test_weights:
        result = calculate_shipping_cost(weight, method="express", zone="zone_2")
        print(
            f"Weight: {result['weight_lbs']:>4} lbs | "
            f"Subtotal: ${result['subtotal']:>6.2f} | "
            f"Tax: ${result['tax_amount']:>5.2f} | "
            f"Total: ${result['total_cost']:>6.2f}"
        )


if __name__ == "__main__":
    main()
