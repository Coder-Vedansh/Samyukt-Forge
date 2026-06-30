from abc import abstractmethod
from typing import Any, Dict, List

from pydantic import BaseModel

from sdk.engine.chat import ChatMessage
from sdk.engine.provider import IProvider


class ReasoningStep(BaseModel):
    thought: str
    tokens: int


class ReasoningResponse(BaseModel):
    message: ChatMessage
    reasoning_steps: List[ReasoningStep]
    usage: Dict[str, int]
    model_name: str


class IReasoning(IProvider):
    """Interface for advanced reasoning models that return chain-of-thought traces."""

    @abstractmethod
    async def reason(
        self, model: str, messages: List[ChatMessage], **kwargs: Any
    ) -> ReasoningResponse:
        """Execute a prompt that requires internal reflection or chain of thought."""
        pass
