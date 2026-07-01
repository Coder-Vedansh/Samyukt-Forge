from typing import Optional

from pydantic import BaseModel


class AgentIdentity(BaseModel):
    """
    Defines who the agent is and how it presents itself.
    """

    id: str
    name: str
    role: str
    backstory: Optional[str] = None
    system_prompt_override: Optional[str] = None
