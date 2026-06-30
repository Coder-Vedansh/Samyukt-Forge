from abc import ABC, abstractmethod
from typing import Any, Dict, List

from sdk.tool import ITool


class IAgent(ABC):
    """
    Interface representing a discrete agentic entity.
    """

    @property
    @abstractmethod
    def agent_id(self) -> str:
        pass

    @property
    @abstractmethod
    def role(self) -> str:
        pass

    @property
    @abstractmethod
    def goal(self) -> str:
        pass

    @abstractmethod
    def get_registered_tools(self) -> List[ITool]:
        pass

    @abstractmethod
    async def invoke(self, prompt: str, context: Dict[str, Any] = None) -> str:
        """Prompts the agent to perform an action toward its goal."""
        pass
