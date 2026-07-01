from abc import ABC, abstractmethod
from typing import Any


class ISandbox(ABC):
    """
    Defines the isolation boundary in which a tool executes.
    Prevents arbitrary code execution or side effects on the host OS.
    """

    @abstractmethod
    async def run_isolated(self, executable: Any, *args: Any, **kwargs: Any) -> Any:
        """Executes the given logic inside the sandbox boundary."""
        pass


class ProcessSandbox(ISandbox):
    """Isolates execution to a separate OS-level process with restricted privileges."""

    async def run_isolated(self, executable: Any, *args: Any, **kwargs: Any) -> Any:
        pass


class WasmSandbox(ISandbox):
    """Executes code compiled to WebAssembly (Wasm) with zero host access."""

    async def run_isolated(self, executable: Any, *args: Any, **kwargs: Any) -> Any:
        pass


class DockerSandbox(ISandbox):
    """Executes logic inside an ephemeral Docker container."""

    async def run_isolated(self, executable: Any, *args: Any, **kwargs: Any) -> Any:
        pass
