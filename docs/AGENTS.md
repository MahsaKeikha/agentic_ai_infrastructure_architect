# Agents

## Platform Architecture Agent
Validates that declared infrastructure components satisfy the required capability set and records architectural gaps.

## Capacity Agent
Compares expected peak throughput with provisioned throughput and records headroom and capacity ratio.

## Reliability Agent
Evaluates redundancy and recoverability through replica count, zone count, backups, and tested restores.

## Cost Governance Agent
Compares estimated monthly cost with the declared budget and records variance.

## Deployment Readiness Agent
Synthesizes all upstream evidence with security-review and rollback-readiness gates. It cannot approve a design; it only determines technical readiness. Final approval remains human-controlled.
