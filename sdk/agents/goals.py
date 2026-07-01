from typing import List

from pydantic import BaseModel


class AgentGoal(BaseModel):
    """
    Defines the objective for the agent.
    """

    primary_objective: str
    sub_tasks: List[str]
    success_criteria: List[str]
