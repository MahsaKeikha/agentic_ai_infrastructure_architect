# Agentic AI Infrastructure Architect (F40)

**Maturity:** L3 Gold Standard  
**Version:** 1.0.0

A multi-agent reference implementation for designing, reviewing, and governing AI infrastructure across platform topology, capacity planning, reliability engineering, cost governance, and deployment readiness.

F40 is intended for engineers, architects, researchers, students, platform teams, and technical leaders studying how infrastructure decisions can be decomposed into specialist reasoning roles while keeping deterministic analysis, shared evidence, explicit failure states, and human approval visible.

It is a reference architecture and decision-support system. It does not autonomously create cloud resources, modify production infrastructure, approve budgets, change network or IAM policy, promote deployments, or replace accountable infrastructure, security, SRE, finance, compliance, or platform teams.

## Why this repository exists

AI infrastructure decisions combine several kinds of engineering judgment that should not be collapsed into one opaque recommendation.

A platform can have a plausible topology and still be underprovisioned. It can have enough capacity and still lack tested recovery. It can be technically resilient and still violate cost or security constraints. A deployment package can look complete while upstream assumptions remain unresolved.

F40 separates these concerns so each stage can challenge the others and leave auditable evidence.

## Multi-agent workflow

```text
infrastructure case + requirements
              |
              v
 Platform Architecture Agent
              |
              v
       Capacity Agent
              |
              v
      Reliability Agent
              |
              v
   Cost Governance Agent
              |
              v
Deployment Readiness Agent
              |
              v
 fail-closed governance gates
              |
              v
     explicit human approval
```

The orchestrator records assumptions, conflicts, unresolved questions, provenance evidence, open risks, escalations, execution trace, and approval state. Human approval cannot override active technical or governance blockers.

## Agents and responsibilities

| Agent | Responsibility | Core question |
|---|---|---|
| Platform Architecture Agent | Validate required infrastructure capabilities and topology coverage | Does the proposed platform architecture cover the required services, boundaries, and dependencies? |
| Capacity Agent | Compare provisioned capacity with expected peak and growth demand | Can the system support the expected workload with appropriate headroom? |
| Reliability Agent | Review redundancy, backups, recovery, and failure handling | Can the platform continue or recover predictably when components fail? |
| Cost Governance Agent | Evaluate budget variance and cost constraints | Is the architecture financially bounded and are cost assumptions explicit? |
| Deployment Readiness Agent | Synthesize upstream evidence and apply final release gates | Is the infrastructure package technically and operationally eligible for human approval? |

Each agent owns a distinct review domain. The Deployment Readiness Agent cannot silently erase a failed reliability or capacity finding.

## Skills layer

Reusable infrastructure reasoning lives under `SKILLS/`:

```text
SKILLS/
├── topology_design.py
├── capacity_planning.py
├── reliability_design.py
├── cost_governance.py
└── deployment_readiness.py
```

### Topology design

Structures infrastructure into explicit components and dependencies. Depending on the deployment, this can include compute, model serving, data stores, queues, caches, networking, observability, identity, secrets, storage, and control-plane services.

A topology should make failure domains and trust boundaries visible rather than merely listing technologies.

### Capacity planning

Compares workload demand against available or proposed capacity. Useful inputs can include request rate, concurrency, token or batch volume, CPU, GPU, memory, storage, bandwidth, latency objectives, burst assumptions, utilization targets, and growth expectations.

Capacity planning should preserve headroom assumptions rather than hiding them inside one recommended number.

### Reliability design

Reviews redundancy, recovery, backups, failover, service dependencies, and operational ownership. Reliability should be tested against explicit failure scenarios, not inferred from the presence of multiple components.

### Cost governance

Separates technical feasibility from financial feasibility. A production-ready architecture should make major cost drivers, budget assumptions, reserved or on-demand choices, storage growth, egress, inference cost, and scaling behavior visible.

### Deployment readiness

Combines the specialist evidence into a final readiness assessment while preserving blockers. It also checks security, rollback, unresolved conflicts, unresolved questions, and human approval requirements.

## Deterministic tools

F40 includes deterministic tools under `TOOLS/`:

```text
TOOLS/
├── topology_tool.py
├── capacity_model_tool.py
├── reliability_tool.py
└── cost_model_tool.py
```

These tools demonstrate a key engineering principle: calculations and structural checks that can be performed deterministically should not depend entirely on free-form language-model judgment.

### Topology tool

Represents required platform components and architectural coverage. Production extensions can add dependency graphs, network zones, trust boundaries, region placement, service ownership, and failure-domain modeling.

### Capacity model tool

Supports structured capacity calculations and checks. Extend it with workload-specific formulas, queueing models, accelerator utilization, memory budgets, autoscaling constraints, storage growth, and regional limits.

### Reliability tool

Provides a deterministic place for reliability evidence such as redundancy state, backups, tested recovery, and recovery objectives.

### Cost model tool

Supports explicit cost calculations and budget variance analysis. Production implementations should source current provider prices and organizational discounts from authoritative systems rather than hard-coding assumptions.

## End-to-end workflow

A typical F40 review follows this sequence:

1. Load infrastructure requirements and workload assumptions.
2. Identify required platform capabilities and dependencies.
3. Build or validate the proposed topology.
4. Check that required components and trust boundaries are represented.
5. Estimate expected peak demand and required headroom.
6. Compare expected demand with provisioned or proposed capacity.
7. Review redundancy, backup, recovery, and failure behavior.
8. Evaluate cost against budget and scaling assumptions.
9. Record conflicts, open risks, and unresolved questions.
10. Apply deployment-readiness checks for security, rollback, reliability, capacity, cost, and operational ownership.
11. Fail closed when required evidence is missing or a blocker remains.
12. Require an accountable human to approve the next deployment stage.

This sequence makes the final readiness state traceable to upstream evidence.

## Quick start

Install the repository with development dependencies:

```bash
python -m pip install -e '.[dev]'
```

Run the test suite:

```bash
pytest -q
```

Run the primary scenarios:

```bash
python evals/run_scenarios.py
```

Run the held-out evaluation:

```bash
python evals/run_heldout.py
```

Run the examples:

```bash
python examples/minimal.py
python examples/complete.py
```

Run the main entry point:

```bash
python run.py
```

The core reference workflow runs offline. CI executes the same acceptance path on Python 3.10, 3.11, and 3.12 and publishes the held-out results artifact.

## Input model

A useful infrastructure case should describe the actual workload and operating constraints. Depending on the deployment, inputs may include:

- workload type
- model or service characteristics
- expected peak traffic
- concurrency
- latency objectives
- throughput objectives
- CPU or accelerator needs
- memory requirements
- storage requirements
- network and egress expectations
- availability target
- recovery objectives
- regions or zones
- data residency requirements
- security controls
- budget limits
- deployment environments
- rollback requirements
- known dependencies
- source references

Production systems should validate these inputs against explicit schemas and preserve source provenance for material assumptions.

## Platform topology

The Platform Architecture Agent should make the system structure explicit.

A production AI topology can include:

```text
clients
  |
  v
edge / API gateway
  |
  v
application services
  |
  +--> model serving
  +--> retrieval services
  +--> feature or context stores
  +--> queues / workers
  +--> policy and guardrail services
  |
  v
data and storage layer
  |
  v
observability / security / control plane
```

The exact architecture is deployment-specific. F40 is concerned with whether required capabilities and dependencies are represented and reviewable.

## Capacity planning

Capacity should be tied to workload evidence rather than chosen from intuition.

Relevant dimensions can include:

- peak requests per second
- concurrent requests
- prompt and completion size
- batch size
- model memory footprint
- accelerator memory
- CPU preprocessing load
- storage IOPS
- network throughput
- queue depth
- autoscaling delay
- warm-up time
- regional quotas
- growth rate
- safety margin

A capacity plan should distinguish current demand, expected peak demand, projected growth, and contingency headroom.

When evidence is missing, the correct state is an explicit assumption or unresolved question, not an invented workload figure.

## Reliability engineering

Reliability review should examine both component redundancy and end-to-end recovery.

Relevant questions include:

- Are critical services redundant?
- Are failure domains independent?
- Are backups configured and restorable?
- Has restore behavior been tested?
- Are RTO and RPO defined where needed?
- Can traffic fail over safely?
- Are queues durable?
- Are stateful components protected?
- Are model and configuration artifacts reproducible?
- Are dependency failures isolated?
- Are alerts actionable?
- Is ownership clear?

Redundancy that has never been tested should not be treated as proven resilience.

## Cost governance

The Cost Governance Agent reviews whether the infrastructure remains within agreed financial constraints.

Important cost drivers can include:

- accelerator hours
- CPU and memory
- storage growth
- database throughput
- vector database capacity
- egress
- logging and observability
- backup retention
- regional duplication
- reserved capacity
- autoscaling behavior
- model invocation volume

Cost models should separate fixed, variable, and growth-sensitive costs. Material pricing assumptions should be versioned and periodically refreshed.

## Deployment readiness

A technically plausible design is not automatically deployment-ready.

The Deployment Readiness Agent should confirm that the required upstream evidence exists and that no active blockers remain.

Typical readiness checks include:

- architecture coverage
- capacity sufficiency
- reliability evidence
- backup and recovery readiness
- cost compliance
- security review
- rollback readiness
- unresolved conflicts
- unresolved questions
- ownership and escalation paths
- human approval

The readiness agent synthesizes evidence. It does not create authority to deploy.

## Shared state and provenance

The orchestrator maintains structured workflow state across agents. Useful state includes:

- infrastructure requirements
- assumptions
- topology evidence
- capacity calculations
- reliability findings
- cost estimates
- conflicts
- unresolved questions
- open risks
- escalations
- execution trace
- approval state

Production systems should version this state by architecture candidate, environment, and deployment revision so reviewers can understand what changed between approvals.

## Fail-closed governance

F40 blocks progression when critical evidence is absent or a blocker remains.

Examples include:

```text
ARCHITECTURE COVERAGE INCOMPLETE
CAPACITY BELOW REQUIREMENT
RECOVERY NOT TESTED
BACKUP GAP
BUDGET LIMIT EXCEEDED
SECURITY REVIEW INCOMPLETE
ROLLBACK NOT TESTED
UNRESOLVED CONFLICT
UNRESOLVED QUESTION
HUMAN APPROVAL REQUIRED
```

Human approval cannot override failed technical or governance gates. A blocked system should request remediation or additional evidence rather than convert a failure into an approved state.

## Human authority and production boundaries

F40 must not autonomously:

- provision or destroy production resources
- deploy infrastructure changes
- modify IAM or network policy
- rotate or expose secrets
- approve security exceptions
- exceed approved budgets
- alter production quotas
- disable monitoring or backups
- approve data residency or regulatory compliance
- promote a deployment between environments
- override rollback requirements

Production execution should remain behind authenticated infrastructure-as-code, CI/CD, change-management, cloud-provider, and human approval controls.

## Security boundaries

AI infrastructure often contains high-value data, credentials, model artifacts, and production control paths. Production deployments should consider:

- least-privilege IAM
- workload identity
- secrets management
- encryption
- network segmentation
- private endpoints
- audit logging
- artifact integrity
- dependency security
- environment isolation
- data classification
- incident response

The multi-agent layer should not receive broad cloud credentials simply because it performs architecture analysis.

## Observability and SRE handoff

A deployable architecture should define what operators need to observe.

Useful telemetry includes:

- request rate
- latency
- error rate
- saturation
- queue depth
- accelerator utilization
- CPU and memory utilization
- storage usage
- retrieval latency
- dependency health
- cost rate
- autoscaling events
- deployment state

A production handoff should also identify dashboards, alerts, runbooks, owners, escalation paths, and rollback procedures.

## Benchmarks and evaluation

F40 includes scenario-based evaluation and published benchmark evidence under `benchmarks/` and `evals/`.

Evaluation should test more than whether the architecture recommendation sounds reasonable. Useful dimensions include:

- topology completeness
- missing-component detection
- capacity shortfall detection
- resilience-gap detection
- backup and recovery detection
- cost-overrun detection
- security-review enforcement
- rollback enforcement
- conflict detection
- unresolved-question handling
- approval-gate enforcement

Strong benchmark cases should include normal architectures, underprovisioned systems, single points of failure, untested recovery, excessive cost, missing security review, rollback gaps, contradictory requirements, and attempts to bypass human approval.

## L3 Gold Standard evidence

F40 is labeled **L3 Gold Standard** under the Agentic AI Library reference criteria.

The repository includes:

- substantive five-agent implementation
- explicit agents, skills, and tools separation
- shared traceable state and provenance
- fail-closed approval and escalation logic
- unit, integration, red-team, failure, approval, and end-to-end tests
- normal, failure, and held-out architecture scenarios
- deterministic offline reproducibility
- three-version CI required for promotion
- held-out evaluation artifact publication
- architecture, safety, evaluation, extension, citation, contribution, and security documentation

See `docs/L3_AUDIT.md` for the promotion record and `docs/EVALUATION.md` for benchmark interpretation.

L3 describes the quality and reproducibility of this reference implementation. It does not mean universal production fitness or provider-specific certification.

## CI and reproducibility

GitHub Actions workflows under `.github/workflows/` exercise the repository across supported Python versions.

When extending F40, CI should cover:

- import and syntax integrity
- deterministic tool tests
- agent contract tests
- orchestrator integration tests
- fail-closed gate tests
- red-team cases
- scenario regressions
- held-out evaluation
- example execution from a clean checkout

Provider-specific production systems should add sandbox deployment tests, infrastructure-policy checks, IaC validation, security scanning, disaster-recovery tests, and rollback verification.

## Extending F40

Common extensions include:

- cloud-provider adapters
- Kubernetes architecture review
- accelerator scheduling analysis
- inference-serving topology agents
- multi-region architecture analysis
- data-platform integration
- vector database sizing
- network cost modeling
- carbon or energy analysis
- SLA and SLO modeling
- chaos-testing evidence
- infrastructure-as-code validation
- FinOps policy checks
- security architecture review
- capacity forecasting
- provider quota analysis

New agents should remain narrowly scoped, emit structured evidence, use minimum required permissions, and have explicit escalation paths.

## Example use cases

F40 can serve as a reference architecture for:

- AI inference platforms
- RAG infrastructure
- model-serving systems
- ML platform architecture
- GPU cluster planning
- enterprise AI platform reviews
- multi-region resilience planning
- FinOps reviews
- deployment-readiness assessments
- architecture review boards
- teaching multi-agent infrastructure reasoning

Regulated or safety-critical environments should add the corresponding domain controls and qualified review.

## Repository map

```text
.github/
├── ISSUE_TEMPLATE/
├── pull_request_template.md
└── workflows/
    ├── ci.yml
    └── tests.yml
AGENTS/
├── platform_architecture_agent.py
├── capacity_agent.py
├── reliability_agent.py
├── cost_governance_agent.py
└── deployment_readiness_agent.py
SKILLS/
├── topology_design.py
├── capacity_planning.py
├── reliability_design.py
├── cost_governance.py
└── deployment_readiness.py
TOOLS/
├── topology_tool.py
├── capacity_model_tool.py
├── reliability_tool.py
└── cost_model_tool.py
benchmarks/
config/
docs/
evals/
examples/
tests/
run.py
pyproject.toml
CHANGELOG.md
CITATION.cff
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
```

See `docs/ARCHITECTURE.md`, `docs/AGENTS.md`, `docs/EVALUATION.md`, `docs/EXTENDING.md`, `docs/SAFETY.md`, and `docs/L3_AUDIT.md` for deeper implementation and audit detail.

## Design principles

1. Separate topology, capacity, reliability, cost, and readiness concerns.
2. Use deterministic tools for deterministic calculations.
3. Preserve assumptions and provenance across every stage.
4. Treat capacity headroom as an explicit engineering decision.
5. Treat tested recovery as distinct from theoretical redundancy.
6. Keep financial constraints visible alongside technical constraints.
7. Fail closed when critical deployment evidence is missing.
8. Keep production credentials and side-effecting tools outside analytical agent authority.
9. Require authenticated human approval for consequential infrastructure changes.
10. Evaluate architecture behavior against failure scenarios, not only normal cases.

## Limitations

F40 is a reference implementation, not an autonomous production deployment engine. Organization-specific infrastructure, threat models, regulations, cloud-provider semantics, pricing, quotas, and SRE policies require independent validation.

## Citation and contribution

The repository includes `CITATION.cff`, `CONTRIBUTING.md`, `SECURITY.md`, and `CHANGELOG.md` for citation, contribution, security reporting, and version history.

## Parent library

Agentic AI Library: https://github.com/MahsaKeikha/agentic_ai_library

## Responsible use

Use F40 as an AI infrastructure architecture and multi-agent decision-support reference. Validate workload assumptions, provider limits, capacity models, reliability design, security controls, recovery procedures, cost estimates, and operational requirements against the real deployment environment. Final infrastructure and deployment decisions remain the responsibility of authorized engineers and organizational owners.