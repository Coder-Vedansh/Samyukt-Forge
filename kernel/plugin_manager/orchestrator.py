from typing import Any
from kernel.plugin_manager.discovery import PluginDiscovery
from kernel.plugin_manager.resolver import PluginResolver
from kernel.plugin_manager.loader import DynamicLoader
from kernel.plugin_manager.sandbox import PluginSandbox
from kernel.logging.logger import Logger
from kernel.registry.module_registry import ModuleRegistry

class PluginOrchestrator:
    """
    Coordinates the entire plugin lifecycle: Discovery -> Resolution -> Loading -> Sandboxing -> Boot.
    """
    def __init__(self, 
                 logger: Logger, 
                 registry: ModuleRegistry, 
                 sandbox: PluginSandbox):
        self.discovery = PluginDiscovery()
        self.resolver = PluginResolver()
        self.loader = DynamicLoader()
        self.sandbox = sandbox
        self.logger = logger
        self.registry = registry

    def initialize_plugins(self, central_registry: Any) -> None:
        """
        Executes the full pipeline to bring plugins online.
        """
        self.logger.info("Starting Plugin Orchestration pipeline...")
        
        # 1. Discover
        raw_plugins = self.discovery.discover()
        
        # 2. Load instances (to get metadata)
        instances = []
        for p in raw_plugins:
            instance = self.loader.load_module(p["name"], p["path"])
            instances.append(instance)
            
        metas = [p.get_metadata() for p in instances]
        
        # 3. Resolve dependencies
        sorted_metas = self.resolver.resolve_load_order(metas)
        
        # Map sorted metas back to instances
        instance_map = {p.get_metadata().name: p for p in instances}
        
        # 4. Sandbox, Register, and Boot
        for meta in sorted_metas:
            plugin = instance_map[meta.name]
            
            # Evaluate Security Context
            self.sandbox.evaluate_and_sandbox(plugin)
            
            # Register with Module Registry
            self.registry.register_module(plugin)
            
            # Register tools/providers into the Service Registry
            plugin.register(central_registry)
            
            # Boot
            self.logger.debug(f"Booting sandboxed plugin: {meta.name}")
            plugin.on_boot()
            
        self.logger.info("Plugin Orchestration complete.")
