from typing import List

from pydantic import BaseModel


class AgentPolicies(BaseModel):
    """
    Behavioral Guardrails enforced by the Orchestrator.
    """

    dos: List[str]
    donts: List[str]
    ethical_constraints: List[str]
