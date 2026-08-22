from __future__ import annotations

from TOOLS.cost_model_tool import assess_cost


def govern_cost(case: dict) -> dict:
    return assess_cost(case.get("estimated_monthly_cost", 0), case.get("monthly_budget", 0))
