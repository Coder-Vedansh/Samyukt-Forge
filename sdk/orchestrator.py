from abc import ABC, abstractmethod
from typing import Any, Dict, List

class IOrchestrator(ABC):
    """
    Interface for workflow/agent orchestration engines (e.g., LangGraph, CrewAI).
    """
    @property
    @abstractmethod
    def engine_name(self) -> str:
        pass

    @abstractmethod
    async def compile_workflow(self, workflow_definition: Dict[str, Any]) -> Any:
        """Parses a generic workflow definition into the engine's specific format."""
        pass

    @abstractmethod
    async def execute_workflow(self, compiled_workflow: Any, inputs: Dict[str, Any]) -> Any:
        """Runs the compiled workflow and returns the result."""
        pass
