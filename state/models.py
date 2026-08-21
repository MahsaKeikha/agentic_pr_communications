from dataclasses import dataclass, field

@dataclass
class CommunicationState:
    evidence: list = field(default_factory=list)
    risks: list = field(default_factory=list)
    human_approval: bool = False
