from __future__ import annotations

from TOOLS.topology_tool import validate_topology


def assess_topology(case: dict) -> dict:
    result = validate_topology(case.get("required_capabilities", []), case.get("components", []))
    result["single_region"] = bool(case.get("single_region", False))
    return result
