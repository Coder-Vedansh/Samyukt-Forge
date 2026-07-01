from abc import abstractmethod
from typing import Any, List

from sdk.memory.core import IMemoryStore, MemoryEntry


class IVectorMemory(IMemoryStore):
    """
    Scope: Long-term semantic/RAG memory.
    Uses vector embeddings for similarity-based search and retrieval.
    """

    @abstractmethod
    async def search_similar(self, query: str, limit: int = 5, **kwargs: Any) -> List[MemoryEntry]:
        """Perform a semantic search across the vector store based on the input query."""
        pass

    @abstractmethod
    async def add_documents(self, documents: List[str], **kwargs: Any) -> None:
        """Embed and store a list of text documents into the vector space."""
        pass
