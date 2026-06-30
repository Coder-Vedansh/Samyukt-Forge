from abc import abstractmethod
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from sdk.engine.provider import IProvider


class ChatMessage(BaseModel):
    role: str = Field(..., description="E.g., system, user, assistant")
    content: str


class ChatResponse(BaseModel):
    message: ChatMessage
    usage: Dict[str, int]
    model_name: str
    finish_reason: Optional[str] = None


class IChat(IProvider):
    """Interface for multi-turn conversational models."""

    @abstractmethod
    async def chat(self, model: str, messages: List[ChatMessage], **kwargs: Any) -> ChatResponse:
        """Asynchronously send a list of messages and receive an assistant response."""
        pass

    @abstractmethod
    async def stream_chat(self, model: str, messages: List[ChatMessage], **kwargs: Any) -> Any:
        """Stream the chat response."""
        pass
