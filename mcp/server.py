from typing import Dict, Any
import asyncio
from mcp.transport import StdioTransport
from mcp.registry import MCPToolRegistry
from mcp.lifecycle import CapabilityNegotiator
from mcp.auth import MCPAuthenticator

class MCPServer:
    """
    Exposes Forge CLI tools to external clients via the Model Context Protocol.
    """
    def __init__(self, registry: MCPToolRegistry, auth: MCPAuthenticator):
        self.transport = StdioTransport()
        self.registry = registry
        self.auth = auth
        self.negotiator = CapabilityNegotiator()
        
        self.transport.set_handler(self._handle_message)

    def _handle_message(self, message: Dict[str, Any]) -> None:
        # JSON-RPC standard handling
        msg_id = message.get("id")
        method = message.get("method")
        
        if method == "initialize":
            result = self.negotiator.handle_initialize(message)
            self.transport.send({"jsonrpc": "2.0", "id": msg_id, "result": result})
            
        elif method == "notifications/initialized":
            # Handshake complete
            pass
            
        elif method == "tools/list":
            tools = self.registry.list_tools_mcp_format()
            self.transport.send({"jsonrpc": "2.0", "id": msg_id, "result": {"tools": tools}})
            
        elif method == "tools/call":
            params = message.get("params", {})
            name = params.get("name")
            args = params.get("arguments", {})
            
            tool = self.registry.get_tool(name)
            if not tool:
                self.transport.send({
                    "jsonrpc": "2.0", 
                    "id": msg_id, 
                    "error": {"code": -32601, "message": f"Tool {name} not found"}
                })
                return
                
            # Note: A true async execution would happen in the event loop.
            # We simulate a sync response for the blueprint.
            # In production: asyncio.create_task(self._async_execute(msg_id, tool, args))
            try:
                # Simulated result
                self.transport.send({
                    "jsonrpc": "2.0", 
                    "id": msg_id, 
                    "result": {"content": [{"type": "text", "text": "Tool execution initiated."}]}
                })
            except Exception as e:
                self.transport.send({
                    "jsonrpc": "2.0", 
                    "id": msg_id, 
                    "error": {"code": -32000, "message": str(e)}
                })

    def run(self) -> None:
        """Starts listening for MCP messages on stdin."""
        self.transport.listen()
