import json
import sys
from typing import Any, Callable, Dict


class StdioTransport:
    """
    Standard I/O transport layer for local MCP interactions.
    Reads JSON-RPC messages from stdin and writes to stdout.
    """

    def __init__(self):
        self._on_message: Callable[[Dict[str, Any]], None] = None

    def set_handler(self, handler: Callable[[Dict[str, Any]], None]) -> None:
        self._on_message = handler

    def send(self, message: Dict[str, Any]) -> None:
        sys.stdout.write(json.dumps(message) + "\n")
        sys.stdout.flush()

    def listen(self) -> None:
        for line in sys.stdin:
            if not line.strip():
                continue
            try:
                msg = json.loads(line)
                if self._on_message:
                    self._on_message(msg)
            except json.JSONDecodeError:
                # Log error or send JSON-RPC parse error back
                pass
