from __future__ import annotations


def validate_topology(required: list[str], components: list[str]) -> dict[str, list[str] | bool]:
    normalized_required = sorted({str(x).strip() for x in required if str(x).strip()})
    normalized_components = sorted({str(x).strip() for x in components if str(x).strip()})
    missing = sorted(set(normalized_required) - set(normalized_components))
    return {
        "required_capabilities": normalized_required,
        "components": normalized_components,
        "missing_capabilities": missing,
        "architecture_valid": not missing,
    }
