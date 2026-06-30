import uuid
import time
from typing import Any, Callable, Dict
from pydantic import BaseModel, Field
from kernel.errors.exceptions import CommandNotRegisteredError

class Command(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    payload: Dict[str, Any]
    timestamp: float = Field(default_factory=time.time)

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
            raise CommandNotRegisteredError(f"No handler registered for command: {command.name}")
        return self.handlers[command.name](command)
