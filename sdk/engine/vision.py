from abc import abstractmethod
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel

from sdk.engine.chat import ChatMessage
from sdk.engine.provider import IProvider


class VisionContent(BaseModel):
    type: str  # e.g., 'image_url' or 'text'
    text: Optional[str] = None
    image_url: Optional[Dict[str, str]] = None


class VisionMessage(BaseModel):
    role: str
    content: Union[str, List[VisionContent]]


class VisionResponse(BaseModel):
    message: ChatMessage
    usage: Dict[str, int]
    model_name: str


class IVision(IProvider):
    """Interface for models capable of processing visual inputs."""

    @abstractmethod
    async def analyze_vision(
        self, model: str, messages: List[VisionMessage], **kwargs: Any
    ) -> VisionResponse:
        """Analyze multi-modal messages containing images and text."""
        pass
