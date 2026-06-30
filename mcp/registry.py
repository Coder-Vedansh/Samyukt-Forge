from typing import Dict, Any, List
from sdk.tool import ITool

class MCPToolRegistry:
    """
    Maps Forge's internal ITool interfaces to the JSON-RPC MCP format.
    """
    def __init__(self):
        self._tools: Dict[str, ITool] = {}

    def register_tool(self, tool: ITool) -> None:
        self._tools[tool.name] = tool

    def get_tool(self, name: str) -> ITool:
        return self._tools.get(name)

    def list_tools_mcp_format(self) -> List[Dict[str, Any]]:
        """
        Converts internal tools to MCP `tools/list` schema.
        """
        mcp_tools = []
        for name, tool in self._tools.items():
            parameters = tool.get_parameters()
            
            # Convert internal ToolParameter to JSON schema properties
            properties = {}
            required = []
            for param_name, param_def in parameters.items():
                properties[param_name] = {
                    "type": param_def.type,
                    "description": param_def.description
                }
                if param_def.required:
                    required.append(param_name)

            mcp_tools.append({
                "name": name,
                "description": tool.description,
                "inputSchema": {
                    "type": "object",
                    "properties": properties,
                    "required": required
                }
            })
        return mcp_tools
