from abc import abstractmethod
from typing import Any, List, Optional

from pydantic import BaseModel

from sdk.engine.provider import IProvider


class ImageResult(BaseModel):
    url: Optional[str] = None
    b64_json: Optional[str] = None


class ImageGenerationResponse(BaseModel):
    created: int
    data: List[ImageResult]


class IImage(IProvider):
    """Interface for Image Generation models (e.g. DALL-E, Stable Diffusion)."""

    @abstractmethod
    async def generate_image(
        self, model: str, prompt: str, **kwargs: Any
    ) -> ImageGenerationResponse:
        """Generates an image from a text prompt."""
        pass

    @abstractmethod
    async def edit_image(
        self, model: str, image_data: bytes, prompt: str, **kwargs: Any
    ) -> ImageGenerationResponse:
        """Edits an existing image based on a prompt."""
        pass
