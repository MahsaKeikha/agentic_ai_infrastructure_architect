from __future__ import annotations


def assess_cost(monthly: float, budget: float) -> dict[str, float | bool]:
    monthly = max(0.0, float(monthly))
    budget = max(0.0, float(budget))
    variance = monthly - budget if budget > 0 else 0.0
    over_budget = budget > 0 and monthly > budget
    variance_pct = (variance / budget) if budget > 0 else 0.0
    return {
        "estimated_monthly_cost": monthly,
        "monthly_budget": budget,
        "variance": round(variance, 2),
        "variance_pct": round(variance_pct, 4),
        "over_budget": over_budget,
    }
