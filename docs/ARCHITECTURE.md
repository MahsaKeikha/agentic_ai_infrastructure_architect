# Architecture

F40 uses a deterministic five-agent pipeline over a shared `InfrastructureState`.

## State contract

The state carries the input case, per-agent analyses, evidence records, execution trace, escalation records, and explicit human approval state.

## Decision flow

Platform Architecture validates component coverage. Capacity checks expected peak load against provisioned throughput. Reliability checks redundancy and recoverability. Cost Governance checks budget variance. Deployment Readiness synthesizes those results with security-review and rollback-test evidence.

A plan can be `approved` only when every readiness gate passes and a human has explicitly approved it. A technically ready plan without human approval remains `awaiting_human_approval`. Any failed gate produces `review_required`.

## Design principle

Agents have distinct responsibilities and write traceable evidence into shared state. No downstream agent can silently erase an upstream escalation.
