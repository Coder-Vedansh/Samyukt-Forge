from abc import abstractmethod
from typing import Any, List

from sdk.memory.core import IMemoryStore


class IConversationMemory(IMemoryStore):
    """
    Scope: Short-term history of the current interaction.
    Stores conversational turns.
    """

    @abstractmethod
    async def append_message(self, role: str, content: str, **kwargs: Any) -> None:
        """Appends a new message to the conversation history."""
        pass

    @abstractmethod
    async def get_history(self, limit: int = 50) -> List[Any]:
        """Retrieves the recent conversation history."""
        pass
