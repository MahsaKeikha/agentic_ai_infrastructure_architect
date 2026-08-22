# Extending F40

Add a new infrastructure agent only when it owns a distinct decision responsibility. The agent should accept `InfrastructureState`, emit structured analysis, record evidence, and escalate conditions that should block deployment.

When adding a new readiness dimension, update the Deployment Readiness Agent, behavioral tests, offline scenarios, README, and architecture documentation together.

Useful extensions include network architecture, data residency, GPU scheduling, model-serving latency, carbon accounting, policy-as-code, disaster recovery objectives, supply-chain integrity, and cloud-provider adapters.

Do not introduce an integration that can mutate production infrastructure without an explicit authorization boundary and auditable human approval.
