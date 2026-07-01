from typing import Any

from sdk.orchestration.core import Node, NodeContext


class HumanApproval(Node):
    """
    A specialized Node that pauses execution and yields to the CLI/UI for user sign-off.
    """

    def __init__(self, name: str, prompt: str):
        super().__init__(name)
        self.prompt = prompt

    async def execute(self, context: NodeContext, **kwargs: Any) -> Any:
        pass
