from abc import ABC, abstractmethod
from typing import Type

from pydantic import BaseModel


class IConfigurable(ABC):
    """
    Interface for plugins that require their own configuration schemas (e.g. API keys).
    """

    @abstractmethod
    def get_config_schema(self) -> Type[BaseModel]:
        """Returns a Pydantic BaseModel class representing the expected config."""
        pass

    @abstractmethod
    def load_config(self, config_instance: BaseModel) -> None:
        """Injects the instantiated config into the plugin."""
        pass
