from typing import Dict, List

from sdk.plugin import IPlugin, PluginMetadata


class ModuleRegistry:
    """
    Keeps track of all loaded plugins/modules and their metadata.
    """

    def __init__(self):
        self._modules: Dict[str, IPlugin] = {}
        self._metadata: Dict[str, PluginMetadata] = {}

    def register_module(self, plugin: IPlugin) -> None:
        meta = plugin.get_metadata()
        if meta.name in self._modules:
            raise ValueError(f"Module {meta.name} is already registered.")

        self._modules[meta.name] = plugin
        self._metadata[meta.name] = meta

    def get_module(self, name: str) -> IPlugin:
        return self._modules.get(name)

    def get_all_metadata(self) -> List[PluginMetadata]:
        return list(self._metadata.values())
