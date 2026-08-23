"""Fail-closed governance for F128 Agentic PR and Communications."""

PROTECTED_ACTIONS = {
    "publish_statement",
    "send_media_outreach",
    "issue_press_release",
    "respond_on_record",
    "activate_crisis_response",
    "external_distribution",
}

REQUIRED_REVIEWS = (
    "research_reviewed",
    "narrative_reviewed",
    "stakeholder_reviewed",
    "risk_reviewed",
    "claims_reviewed",
    "privacy_confidentiality_reviewed",
    "evidence_provenance_reviewed",
    "qualified_communications_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {"allowed": False, "reason": "binding communications action is outside reference-system scope"}
    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required communications review", "missing": missing}
    checks = {
        "unsupported_claim": "public claim exceeds reviewed evidence",
        "impersonation_risk": "identity, attribution, or spokesperson authority unresolved",
        "deceptive_outreach": "deceptive media or stakeholder outreach detected",
        "privacy_confidentiality_gap": "privacy, consent, embargo, or confidentiality gap unresolved",
        "legal_reputation_risk": "legal, defamation, or reputational risk unresolved",
        "crisis_escalation_required": "crisis or material incident requires authorized escalation",
        "stakeholder_harm_risk": "material stakeholder-harm risk unresolved",
        "evidence_provenance_gap": "evidence provenance incomplete",
    }
    blockers = [message for key, message in checks.items() if context.get(key)]
    if blockers:
        return {"allowed": False, "reason": "communications governance blocker", "blockers": blockers}
    return {"allowed": True, "reason": "communications support package approved after qualified human review"}


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS
