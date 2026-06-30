from typing import TypeVar, Type, Dict, Any, Callable, Optional
from kernel.errors.exceptions import DependencyInjectionError

T = TypeVar('T')

class DIContainer:
    """
    Lightweight Dependency Injection Container for the Kernel.
    Supports singletons and transient factory registrations.
    """
    def __init__(self):
        self._singletons: Dict[Type, Any] = {}
        self._factories: Dict[Type, Callable[[], Any]] = {}

    def register_singleton(self, interface: Type[T], instance: T) -> None:
        self._singletons[interface] = instance

    def register_factory(self, interface: Type[T], factory: Callable[[], T]) -> None:
        self._factories[interface] = factory

    def resolve(self, interface: Type[T]) -> T:
        if interface in self._singletons:
            return self._singletons[interface]
        
        if interface in self._factories:
            return self._factories[interface]()
            
        raise DependencyInjectionError(f"No registration found for interface {interface.__name__}")
