from abc import abstractmethod
from typing import Any, Optional

from pydantic import BaseModel

from sdk.engine.provider import IProvider


class VideoGenerationResponse(BaseModel):
    url: Optional[str] = None
    b64_data: Optional[str] = None


class IVideo(IProvider):
    """Interface for Video Generation and Analysis models."""

    @abstractmethod
    async def generate_video(
        self, model: str, prompt: str, **kwargs: Any
    ) -> VideoGenerationResponse:
        """Generates a video from a text prompt or image."""
        pass
