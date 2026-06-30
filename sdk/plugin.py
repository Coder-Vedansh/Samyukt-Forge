from abc import ABC, abstractmethod
from typing import List, Any
from pydantic import BaseModel
from sdk.lifecycle import ILifecycleAware
from sdk.security import ISecurityContext
from sdk.config import IConfigurable

class PluginMetadata(BaseModel):
    name: str
    version: str
    author: str
    description: str
    dependencies: List[str] = []

class IPlugin(ILifecycleAware, IConfigurable, ABC):
    """
    The master interface that all Forge plugins must implement.
    It combines Lifecycle, Configuration, and Security.
    """
    @abstractmethod
    def get_metadata(self) -> PluginMetadata:
        """Returns the plugin metadata."""
        pass
        
    @abstractmethod
    def get_security_context(self) -> ISecurityContext:
        """Returns the permissions required by this plugin."""
        pass

    @abstractmethod
    def register(self, registry: Any) -> None:
        """
        Registers the plugin's capabilities (tools, providers, orchestrators) 
        with the Kernel Registry.
        """
        pass
