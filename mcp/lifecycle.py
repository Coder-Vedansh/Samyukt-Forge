from typing import Any, Dict


class CapabilityNegotiator:
    """
    Handles the MCP `initialize` request to negotiate capabilities.
    """

    def __init__(self, version: str = "1.0.0"):
        self.version = version

    def handle_initialize(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """
        Processes client capabilities and returns the Server capabilities.
        """
        # A real implementation would parse request["params"]["capabilities"]

        return {
            "protocolVersion": "2024-11-05",  # Standard MCP version
            "serverInfo": {"name": "forge-cli-mcp", "version": self.version},
            "capabilities": {"tools": {"listChanged": True}, "resources": {}, "prompts": {}},
        }
