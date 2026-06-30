from abc import ABC, abstractmethod
from typing import Any, Dict, List

class MemoryEntry(Dict[str, Any]):
    pass

class IMemoryProvider(ABC):
    """
    Interface for short-term and long-term memory systems (e.g. Vector DBs, Redis).
    """
    @property
    @abstractmethod
    def provider_name(self) -> str:
        pass

    @abstractmethod
    async def store(self, collection: str, entry: MemoryEntry) -> str:
        """Stores a memory entry and returns its ID."""
        pass

    @abstractmethod
    async def search(self, collection: str, query: str, limit: int = 5) -> List[MemoryEntry]:
        """Performs semantic or keyword search across memory."""
        pass

    @abstractmethod
    async def retrieve(self, collection: str, entry_id: str) -> MemoryEntry:
        """Retrieves a specific memory entry by ID."""
        pass
