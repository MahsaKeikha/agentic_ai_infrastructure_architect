from __future__ import annotations

from TOOLS.reliability_tool import assess_reliability


def design_reliability(case: dict) -> dict:
    result = assess_reliability(
        case.get("replicas", 1),
        case.get("zones", 1),
        case.get("backups", False),
        case.get("restore_tested", False),
    )
    result["availability_target"] = float(case.get("availability_target", 0.999))
    return result
