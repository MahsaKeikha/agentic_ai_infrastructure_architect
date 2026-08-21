from __future__ import annotations


def assess_reliability(replicas: int, zones: int, backups: bool, restore_tested: bool) -> dict[str, int | bool]:
    replicas = max(0, int(replicas))
    zones = max(0, int(zones))
    resilient = replicas >= 2 and zones >= 2 and bool(backups) and bool(restore_tested)
    return {
        "replicas": replicas,
        "zones": zones,
        "backups": bool(backups),
        "restore_tested": bool(restore_tested),
        "resilient": resilient,
    }
