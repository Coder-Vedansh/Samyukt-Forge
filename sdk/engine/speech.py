from abc import abstractmethod
from typing import Any, Optional

from pydantic import BaseModel

from sdk.engine.provider import IProvider


class SpeechResponse(BaseModel):
    audio_data: bytes
    format: str


class TranscriptionResponse(BaseModel):
    text: str
    language: Optional[str] = None


class ISpeech(IProvider):
    """Interface for text-to-speech and speech-to-text models."""

    @abstractmethod
    async def text_to_speech(self, model: str, text: str, **kwargs: Any) -> SpeechResponse:
        """Convert text into spoken audio."""
        pass

    @abstractmethod
    async def speech_to_text(
        self, model: str, audio_data: bytes, **kwargs: Any
    ) -> TranscriptionResponse:
        """Transcribe audio data into text."""
        pass
