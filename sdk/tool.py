from abc import ABC, abstractmethod
from typing import Any, Dict

from pydantic import BaseModel


class ToolParameter(BaseModel):
    name: str
    type: str
    description: str
    required: bool = True


class ITool(ABC):
    """
    Interface for capabilities/tools that can be executed by Agents or the User.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass

    @abstractmethod
    def get_parameters(self) -> Dict[str, ToolParameter]:
        """Returns the schema of expected parameters."""
        pass

    @abstractmethod
    async def execute_async(self, **kwargs: Any) -> Any:
        """Executes the tool asynchronously."""
        pass
