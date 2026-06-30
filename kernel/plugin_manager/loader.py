import importlib
import sys
from typing import Dict, Type

from kernel.errors.exceptions import PluginLoadError
from sdk.plugin import IPlugin


class DynamicLoader:
    """
    Handles hot-loading and hot-reloading of plugin modules into the Python runtime.
    """

    def __init__(self):
        self._loaded_instances: Dict[str, IPlugin] = {}

    def load_module(self, module_name: str, path: str) -> IPlugin:
        """
        Dynamically imports the module by path and instantiates the main Plugin class.
        """
        try:
            # Note: A real implementation would use importlib.util.spec_from_file_location
            # For blueprint, we assume standard import mechanism works if path is in sys.path
            if path not in sys.path:
                sys.path.insert(0, path)

            module = importlib.import_module(module_name)

            # Find the class that implements IPlugin
            plugin_class: Type[IPlugin] = None
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, type) and issubclass(attr, IPlugin) and attr is not IPlugin:
                    plugin_class = attr
                    break

            if not plugin_class:
                raise PluginLoadError(f"No IPlugin implementation found in module {module_name}")

            instance = plugin_class()
            self._loaded_instances[module_name] = instance
            return instance

        except Exception as e:
            raise PluginLoadError(f"Failed to load plugin {module_name}: {str(e)}") from e

    def reload_module(self, module_name: str) -> IPlugin:
        """
        Hot-reloads the module without restarting the process.
        """
        if module_name in sys.modules:
            module = importlib.reload(sys.modules[module_name])
            # Re-instantiate
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, type) and issubclass(attr, IPlugin) and attr is not IPlugin:
                    instance = attr()
                    self._loaded_instances[module_name] = instance
                    return instance
        raise PluginLoadError(
            f"Cannot reload module {module_name} as it was not previously loaded."
        )
