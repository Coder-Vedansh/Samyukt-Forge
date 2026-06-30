import time
import uuid
from typing import Any, Callable, Dict, List

from pydantic import BaseModel, Field


class Event(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    payload: Dict[str, Any]
    timestamp: float = Field(default_factory=time.time)


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
                # In a robust implementation, this could be async/await or queue-based
                callback(event)
