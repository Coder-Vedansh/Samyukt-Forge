from abc import ABC, abstractmethod
from typing import Any, Dict, Optional


class MemoryEntry(Dict[str, Any]):
    """Base dictionary representing a single memory item."""

    pass


class IMemoryStore(ABC):
    """
    Base interface for all hierarchical memory systems in Forge CLI.
    """

    @property
    @abstractmethod
    def scope(self) -> str:
        """The scope of this memory store (e.g. 'conversation', 'global', 'workspace')."""
        pass

    @abstractmethod
    async def get(self, key: str) -> Optional[Any]:
        """Retrieve a value by key."""
        pass

    @abstractmethod
    async def set(self, key: str, value: Any) -> None:
        """Store a value by key."""
        pass

    @abstractmethod
    async def delete(self, key: str) -> None:
        """Delete a value by key."""
        pass

    @abstractmethod
    async def clear(self) -> None:
        """Clear all entries in this memory scope."""
        pass
