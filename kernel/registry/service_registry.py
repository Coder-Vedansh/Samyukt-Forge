from typing import Any, Dict, List, Type


class ServiceRegistry:
    """
    Maps SDK interfaces (e.g., ILLMProvider) to concrete implementations provided by plugins.
    Allows the Kernel to query "What provides ILLMProvider?".
    """

    def __init__(self):
        # Maps Interface Type -> List of Concrete Instances
        self._services: Dict[Type, List[Any]] = {}

    def register_service(self, interface: Type, implementation: Any) -> None:
        if interface not in self._services:
            self._services[interface] = []
        self._services[interface].append(implementation)

    def get_services(self, interface: Type) -> List[Any]:
        """Returns all implementations registered for a given interface."""
        return self._services.get(interface, [])

    def get_service(self, interface: Type) -> Any:
        """Returns the first registered implementation for an interface."""
        services = self.get_services(interface)
        if services:
            return services[0]
        return None
