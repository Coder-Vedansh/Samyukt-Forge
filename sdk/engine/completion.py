from abc import abstractmethod
from typing import Any, Dict, Optional

from pydantic import BaseModel

from sdk.engine.provider import IProvider


class CompletionResponse(BaseModel):
    text: str
    usage: Dict[str, int]
    model_name: str
    finish_reason: Optional[str] = None


class ICompletion(IProvider):
    """Interface for legacy text-in, text-out completion models."""

    @abstractmethod
    async def complete(self, model: str, prompt: str, **kwargs: Any) -> CompletionResponse:
        """Generate a text completion for the given prompt."""
        pass
