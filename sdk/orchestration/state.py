from typing import Any

from sdk.orchestration.core import Node, NodeContext


class Checkpoint(Node):
    """
    Wraps a node, explicitly forcing the orchestrator to serialize and save the state mid-execution.
    """

    def __init__(self, name: str, node: Node):
        super().__init__(name)
        self.node = node

    async def execute(self, context: NodeContext, **kwargs: Any) -> Any:
        pass


class Streaming(Node):
    """
    Wraps a node to indicate its output should be yielded partially to the user dynamically.
    """

    def __init__(self, name: str, node: Node):
        super().__init__(name)
        self.node = node

    async def execute(self, context: NodeContext, **kwargs: Any) -> Any:
        pass
