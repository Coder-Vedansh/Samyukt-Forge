from enum import Enum
from typing import List
from kernel.logging.logger import Logger
from kernel.registry.module_registry import ModuleRegistry
from kernel.errors.exceptions import ForgeError

class KernelState(str, Enum):
    IDLE = "IDLE"
    BOOTING = "BOOTING"
    INITIALIZING = "INITIALIZING"
    RUNNING = "RUNNING"
    SHUTTING_DOWN = "SHUTTING_DOWN"

class LifecycleManager:
    """
    Manages the overall kernel state and plugin boot sequence.
    """
    def __init__(self, logger: Logger, module_registry: ModuleRegistry):
        self._state = KernelState.IDLE
        self._logger = logger
        self._module_registry = module_registry

    @property
    def state(self) -> KernelState:
        return self._state

    def boot(self) -> None:
        if self._state != KernelState.IDLE:
            raise ForgeError(f"Cannot boot kernel from state: {self._state}")
            
        self._state = KernelState.BOOTING
        self._logger.info("Kernel is booting...")
        
        self._state = KernelState.INITIALIZING
        self._logger.info("Initializing modules...")
        
        # In a full implementation, Topological Sort would happen here
        # based on dependencies in plugin metadata
        
        plugins = self._module_registry.get_all_metadata()
        for meta in plugins:
            plugin = self._module_registry.get_module(meta.name)
            self._logger.debug(f"Booting plugin: {meta.name}")
            try:
                plugin.on_boot()
            except Exception as e:
                self._logger.error(f"Failed to boot plugin {meta.name}: {str(e)}")
                raise

        self._state = KernelState.RUNNING
        self._logger.info("Kernel is now RUNNING.")

    def shutdown(self) -> None:
        self._state = KernelState.SHUTTING_DOWN
        self._logger.info("Kernel is shutting down...")
        
        plugins = self._module_registry.get_all_metadata()
        # Teardown in reverse order ideally
        for meta in reversed(plugins):
            plugin = self._module_registry.get_module(meta.name)
            self._logger.debug(f"Shutting down plugin: {meta.name}")
            try:
                plugin.on_shutdown()
            except Exception as e:
                self._logger.error(f"Error shutting down plugin {meta.name}: {str(e)}")
                
        self._state = KernelState.IDLE
        self._logger.info("Kernel shutdown complete.")
