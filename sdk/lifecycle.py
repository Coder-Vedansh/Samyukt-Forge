from abc import ABC, abstractmethod


class ILifecycleAware(ABC):
    """
    Interface for components that need to hook into the kernel's lifecycle.
    """

    @abstractmethod
    def on_install(self) -> None:
        """Called once when the plugin is first installed via the Package Manager."""
        pass

    @abstractmethod
    def on_boot(self) -> None:
        """Called every time the Forge Kernel boots."""
        pass

    @abstractmethod
    def on_shutdown(self) -> None:
        """Called when the Forge Kernel is terminating."""
        pass
