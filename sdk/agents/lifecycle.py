from abc import ABC, abstractmethod


class IAgentLifecycle(ABC):
    """
    Hooks for agent state transitions.
    """

    @abstractmethod
    async def on_spawn(self) -> None:
        pass

    @abstractmethod
    async def on_pause(self) -> None:
        pass

    @abstractmethod
    async def on_resume(self) -> None:
        pass

    @abstractmethod
    async def on_terminate(self) -> None:
        pass
