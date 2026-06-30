# Examples

Common patterns and code snippets for Forge CLI developers.

## Emitting an Event
```python
from kernel.bus.events import EventBus

bus = EventBus()
await bus.publish("user.login", {"user_id": 123})
```

## Creating an MCP Client
```python
from mcp.client import MCPClient

client = MCPClient("node server.js")
client.connect()
tools = client.discover_tools()
```
