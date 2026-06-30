from typing import Dict, List, Set

from kernel.errors.exceptions import PluginLoadError
from sdk.plugin import PluginMetadata


class PluginResolver:
    """
    Resolves plugin dependency graphs using Topological Sort.
    """

    def __init__(self):
        pass

    def resolve_load_order(self, plugins_meta: List[PluginMetadata]) -> List[PluginMetadata]:
        """
        Takes a list of metadata and returns a sorted list where dependencies come first.
        Raises PluginLoadError if a circular dependency is detected.
        """
        graph: Dict[str, List[str]] = {p.name: p.dependencies for p in plugins_meta}
        meta_map = {p.name: p for p in plugins_meta}

        visited: Set[str] = set()
        temp_mark: Set[str] = set()
        sorted_order: List[PluginMetadata] = []

        def visit(node_name: str):
            if node_name in temp_mark:
                raise PluginLoadError(f"Circular dependency detected involving plugin: {node_name}")
            if node_name not in visited:
                temp_mark.add(node_name)
                for dep in graph.get(node_name, []):
                    # Ignore optional or missing dependencies for now
                    if dep in meta_map:
                        visit(dep)
                temp_mark.remove(node_name)
                visited.add(node_name)
                sorted_order.append(meta_map[node_name])

        for p in plugins_meta:
            if p.name not in visited:
                visit(p.name)

        return sorted_order
