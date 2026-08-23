from AGENTS import narrative_agent, research_agent, review_agent, risk_agent, stakeholder_agent
from safety.policy import authorize


def run(case: dict) -> dict:
    result = {
        "research": research_agent.run(case),
        "narrative": narrative_agent.run(case),
        "stakeholder": stakeholder_agent.run(case),
        "risk": risk_agent.run(case),
        "review": review_agent.run(case),
    }
    governance = authorize("release_support_package", case.get("governance", {}))
    result["governance"] = governance
    result["released"] = governance["allowed"]
    return result
