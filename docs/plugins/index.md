# Plugin Documentation

Everything in Forge is a plugin. If you want to extend the Kernel, you build a plugin.

## The IPlugin Interface

Every plugin must implement the `IPlugin` interface from the Forge SDK:

```python
from forge_cli.sdk.plugin import IPlugin, PluginContext

class MyPlugin(IPlugin):
    @property
    def name(self) -> str:
        return "my_plugin"
        
    @property
    def version(self) -> str:
        return "1.0.0"
        
    async def on_load(self, context: PluginContext) -> None:
        print("Plugin loaded!")
```

## Sandboxing
Plugins are executed in isolation. Direct access to host memory or file systems outside the designated `.forge/workspace` will result in a `PermissionDeniedError`.
