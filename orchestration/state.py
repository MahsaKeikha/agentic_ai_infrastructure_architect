from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class InfrastructureState:
    case: dict[str, Any]
    analyses: dict[str, dict[str, Any]] = field(default_factory=dict)
    evidence: list[dict[str, Any]] = field(default_factory=list)
    trace: list[dict[str, Any]] = field(default_factory=list)
    escalations: list[dict[str, Any]] = field(default_factory=list)
    assumptions: list[str] = field(default_factory=list)
    conflicts: list[dict[str, Any]] = field(default_factory=list)
    unresolved_questions: list[str] = field(default_factory=list)
    open_risks: list[dict[str, Any]] = field(default_factory=list)
    approval: dict[str, Any] = field(default_factory=lambda: {"required": True, "approved": False})

    def record(self, actor: str, payload: dict[str, Any]) -> None:
        self.analyses[actor] = payload
        self.trace.append({"step": len(self.trace) + 1, "actor": actor, "event": "completed"})
        self.evidence.append({"source": actor, "payload": payload, "provenance": "derived"})

    def escalate(self, source: str, reason: str, severity: str = "high") -> None:
        item = {"source": source, "reason": reason, "severity": severity}
        self.escalations.append(item)
        self.open_risks.append(item)
