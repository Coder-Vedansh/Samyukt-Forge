from abc import ABC, abstractmethod

from sdk.tools.schema import InputSchema, OutputSchema


class IToolLifecycle(ABC):
    """
    Defines the distinct execution phases of a Tool.
    """

    @abstractmethod
    async def on_init(self) -> None:
        """Setup connections or resources required by the tool."""
        pass

    @abstractmethod
    async def pre_execute(self, inputs: InputSchema) -> None:
        """Validation or permission checks before execution."""
        pass

    @abstractmethod
    async def post_execute(self, outputs: OutputSchema) -> OutputSchema:
        """Output sanitation or transformation after execution."""
        pass

    @abstractmethod
    async def on_teardown(self) -> None:
        """Resource cleanup (e.g. closing network connections, deleting tmp files)."""
        pass
