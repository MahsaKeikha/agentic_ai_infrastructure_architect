# Safety Policy

F40 provides infrastructure decision support only. It does not execute deployments, mutate cloud resources, rotate credentials, alter firewalls, or approve production changes autonomously.

Deployment approval requires all technical readiness gates plus explicit human authorization. Architecture gaps, capacity shortfalls, inadequate redundancy or recovery, budget violations, missing security review, untested rollback, conflicting inputs, and unresolved questions fail closed to `review_required`.

Adapters that add external execution must implement separate authorization, least privilege, audit logging, rollback, and environment-specific security review.
