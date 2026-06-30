from abc import ABC, abstractmethod
from typing import Any, AsyncGenerator, Dict, List

from pydantic import BaseModel


class ModelMessage(BaseModel):
    role: str
    content: str


class ModelResponse(BaseModel):
    content: str
    usage: Dict[str, int]
    model_name: str


class IModelProvider(ABC):
    """
    Interface for AI Model Providers (LLMs, Embeddings, Multimodal).
    """

    @abstractmethod
    def get_provider_name(self) -> str:
        pass

    @abstractmethod
    def get_supported_models(self) -> List[str]:
        pass

    @abstractmethod
    async def generate_async(
        self, model: str, messages: List[ModelMessage], **kwargs: Any
    ) -> ModelResponse:
        pass

    @abstractmethod
    async def stream_async(
        self, model: str, messages: List[ModelMessage], **kwargs: Any
    ) -> AsyncGenerator[str, None]:
        pass
