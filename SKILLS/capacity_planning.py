from __future__ import annotations

from TOOLS.capacity_model_tool import model_capacity


def assess_capacity(case: dict) -> dict:
    return model_capacity(case.get("expected_peak_rps", 0), case.get("provisioned_rps", 0))
