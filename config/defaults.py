DEFAULTS = {
    "min_zones": 2,
    "min_replicas": 2,
    "require_backups": True,
    "require_restore_test": True,
    "require_security_review": True,
    "require_rollback_test": True,
    "require_human_approval": True,
}


def get_defaults() -> dict:
    return dict(DEFAULTS)
