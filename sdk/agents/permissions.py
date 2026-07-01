from typing import List

from pydantic import BaseModel

from sdk.tools.permission import ToolPermission


class AgentPermissions(BaseModel):
    """
    Defines the absolute security boundaries for this agent instance.
    """

    allowed_grants: List[ToolPermission]
    max_tools_per_step: int = 5
    allow_unsupervised_execution: bool = False
