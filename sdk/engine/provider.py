from abc import ABC, abstractmethod
from typing import List


class IProvider(ABC):
    """
    Base interface for all AI Engine Providers.
    Any provider plugin (e.g. OpenAI, Anthropic, Local) must implement this to register with the kernel.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """The canonical name of the provider."""
        pass

    @abstractmethod
    def get_supported_models(self) -> List[str]:
        """Returns a list of model strings supported by this provider instance."""
        pass
