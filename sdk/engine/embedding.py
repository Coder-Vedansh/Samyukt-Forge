from abc import abstractmethod
from typing import Any, Dict, List, Union

from pydantic import BaseModel

from sdk.engine.provider import IProvider


class EmbeddingResponse(BaseModel):
    embeddings: List[List[float]]
    usage: Dict[str, int]
    model_name: str


class IEmbedding(IProvider):
    """Interface for generating vector embeddings from text or multi-modal inputs."""

    @abstractmethod
    async def embed(
        self, model: str, input_data: Union[str, List[str]], **kwargs: Any
    ) -> EmbeddingResponse:
        """Generate vector embeddings for the given input(s)."""
        pass
