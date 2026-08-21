# Safety

F40 is a reference architecture and does not autonomously deploy infrastructure.

Consequential changes require explicit human approval. Approval cannot override failed architecture completeness, capacity, resilience, budget, security-review, or rollback-readiness gates.

The system fails closed to `review_required` when required capabilities are missing, provisioned capacity is insufficient, recoverability controls are incomplete, budget is exceeded, security review is absent, or rollback readiness is not demonstrated.

Production adoption should add organization-specific IAM, policy-as-code, change-management integration, secrets handling, environment isolation, compliance controls, and independent security review.
