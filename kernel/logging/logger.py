from enum import Enum
from typing import Optional
from kernel.bus.events import EventBus, Event

class LogLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

class Logger:
    """
    Centralized logging for the kernel. Hooks into EventBus to emit log events.
    """
    def __init__(self, event_bus: EventBus):
        self._event_bus = event_bus

    def _log(self, level: LogLevel, message: str, context: Optional[dict] = None) -> None:
        payload = {
            "level": level.value,
            "message": message,
            "context": context or {}
        }
        event = Event(name="kernel.log", payload=payload)
        self._event_bus.publish(event)
        
        # Fallback console print for the most critical kernel failures
        if level in (LogLevel.ERROR, LogLevel.CRITICAL):
            print(f"[{level.value}] {message}")

    def debug(self, message: str, context: Optional[dict] = None) -> None:
        self._log(LogLevel.DEBUG, message, context)

    def info(self, message: str, context: Optional[dict] = None) -> None:
        self._log(LogLevel.INFO, message, context)

    def warning(self, message: str, context: Optional[dict] = None) -> None:
        self._log(LogLevel.WARNING, message, context)

    def error(self, message: str, context: Optional[dict] = None) -> None:
        self._log(LogLevel.ERROR, message, context)

    def critical(self, message: str, context: Optional[dict] = None) -> None:
        self._log(LogLevel.CRITICAL, message, context)
