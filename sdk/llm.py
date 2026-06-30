from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
# pyrefly: ignore [missing-import]
from pydantic import BaseModel

class LLMMessage(BaseModel):
    role: str
    content: str

class LLMResponse(BaseModel):
    content: str
    usage: Dict[str, int]
    model_name: str

class ILLMProvider(ABC):
    """
    Interface for Large Language Model providers.
    Plugins wrapping OpenAI, Anthropic, Ollama, etc. must implement this.
    """
    
    @abstractmethod
    def get_provider_name(self) -> str:
        pass

    @abstractmethod
    def get_supported_models(self) -> List[str]:
        pass

    @abstractmethod
    def generate(self, model: str, messages: List[LLMMessage], **kwargs: Any) -> LLMResponse:
        """Synchronously generate a response from the LLM."""
        pass

    @abstractmethod
    async def generate_async(self, model: str, messages: List[LLMMessage], **kwargs: Any) -> Any:
        """Asynchronously generate a response from the LLM."""
        pass
