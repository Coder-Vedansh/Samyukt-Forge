from typing import List

from sdk.tools.core import ITool


class AgentToolRegistry:
    """
    Registry of tools explicitly available to this agent.
    """

    def __init__(self, tools: List[ITool]):
        self.tools = {tool.name: tool for tool in tools}

    def get_all(self) -> List[ITool]:
        return list(self.tools.values())
