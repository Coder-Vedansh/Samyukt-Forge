import uuid
from typing import Any, Callable, Dict, List

class Event:
    def __init__(self, name: str, payload: Dict[str, Any]):
        self.id = str(uuid.uuid4())
        self.name = name
        self.payload = payload

class EventBus:
    """
    Handles publish/subscribe for asynchronous events across the Kernel and Plugins.
    """
    def __init__(self):
        self.subscribers: Dict[str, List[Callable[[Event], None]]] = {}

    def subscribe(self, event_name: str, callback: Callable[[Event], None]) -> None:
        if event_name not in self.subscribers:
            self.subscribers[event_name] = []
        self.subscribers[event_name].append(callback)

    def publish(self, event: Event) -> None:
        if event.name in self.subscribers:
            for callback in self.subscribers[event.name]:
                callback(event)

class Command:
    def __init__(self, name: str, payload: Dict[str, Any]):
        self.id = str(uuid.uuid4())
        self.name = name
        self.payload = payload

class CommandBus:
    """
    Handles 1:1 request/response commands (synchronous).
    """
    def __init__(self):
        self.handlers: Dict[str, Callable[[Command], Any]] = {}

    def register_handler(self, command_name: str, handler: Callable[[Command], Any]) -> None:
        if command_name in self.handlers:
            raise ValueError(f"Handler for command {command_name} already registered.")
        self.handlers[command_name] = handler

    def dispatch(self, command: Command) -> Any:
        if command.name not in self.handlers:
            raise ValueError(f"No handler registered for command {command.name}")
        return self.handlers[command.name](command)
