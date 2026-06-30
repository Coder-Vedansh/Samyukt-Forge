import os
from pathlib import Path
from typing import List, Dict

class PluginDiscovery:
    """
    Scans the filesystem and Python entry points to find installed plugins.
    """
    def __init__(self, plugins_dir: str = ".forge/plugins"):
        self.plugins_dir = Path(plugins_dir)

    def discover(self) -> List[Dict[str, str]]:
        """
        Returns a list of discovered plugins with their physical paths.
        """
        plugins = []
        if not self.plugins_dir.exists():
            return plugins

        for item in self.plugins_dir.iterdir():
            if item.is_dir() and (item / "__init__.py").exists():
                plugins.append({
                    "name": item.name,
                    "path": str(item)
                })
                
        # Future: Also scan standard python `importlib.metadata.entry_points` 
        # looking for the 'forge.plugins' group.
        return plugins
