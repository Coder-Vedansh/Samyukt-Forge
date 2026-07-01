from abc import ABC, abstractmethod
from typing import Any, Dict

from sdk.orchestration.core import Workflow


class IOrchestratorAdapter(ABC):
    """
    Interface for third-party orchestration engines (CrewAI, LangGraph, AutoGen).
    Adapters translate the native Forge DAG/Workflow into the backend-specific format.
    """

    @property
    @abstractmethod
    def engine_name(self) -> str:
        pass

    @abstractmethod
    async def compile(self, workflow: Workflow) -> Any:
        """Parses a native Forge Workflow into the engine's specific format."""
        pass

    @abstractmethod
    async def execute(self, compiled_workflow: Any, inputs: Dict[str, Any]) -> Any:
        """Runs the compiled workflow and returns the result."""
        pass


class CrewAIAdapter(IOrchestratorAdapter):
    """Adapter for CrewAI execution."""

    @property
    def engine_name(self) -> str:
        return "crewai"

    async def compile(self, workflow: Workflow) -> Any:
        pass

    async def execute(self, compiled_workflow: Any, inputs: Dict[str, Any]) -> Any:
        pass


class LangGraphAdapter(IOrchestratorAdapter):
    """Adapter for LangGraph execution."""

    @property
    def engine_name(self) -> str:
        return "langgraph"

    async def compile(self, workflow: Workflow) -> Any:
        pass

    async def execute(self, compiled_workflow: Any, inputs: Dict[str, Any]) -> Any:
        pass


class AutoGenAdapter(IOrchestratorAdapter):
    """Adapter for AutoGen execution."""

    @property
    def engine_name(self) -> str:
        return "autogen"

    async def compile(self, workflow: Workflow) -> Any:
        pass

    async def execute(self, compiled_workflow: Any, inputs: Dict[str, Any]) -> Any:
        pass
