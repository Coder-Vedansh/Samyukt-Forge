from typing import Any, Callable, List

from sdk.orchestration.core import Node, NodeContext


class Sequential(Node):
    """Executes a list of nodes one after another."""

    def __init__(self, name: str, nodes: List[Node]):
        super().__init__(name)
        self.nodes = nodes

    async def execute(self, context: NodeContext, **kwargs: Any) -> Any:
        pass


class Parallel(Node):
    """Executes multiple nodes concurrently."""

    def __init__(self, name: str, nodes: List[Node]):
        super().__init__(name)
        self.nodes = nodes

    async def execute(self, context: NodeContext, **kwargs: Any) -> Any:
        pass


class Conditional(Node):
    """Branches execution based on a callable condition."""

    def __init__(
        self,
        name: str,
        condition_fn: Callable[[NodeContext], bool],
        true_node: Node,
        false_node: Node,
    ):
        super().__init__(name)
        self.condition_fn = condition_fn
        self.true_node = true_node
        self.false_node = false_node

    async def execute(self, context: NodeContext, **kwargs: Any) -> Any:
        pass


class Loop(Node):
    """Repeats a sub-node until a condition is met."""

    def __init__(self, name: str, node: Node, condition_fn: Callable[[NodeContext], bool]):
        super().__init__(name)
        self.node = node
        self.condition_fn = condition_fn

    async def execute(self, context: NodeContext, **kwargs: Any) -> Any:
        pass


class Retry(Node):
    """Wraps a node with transient failure retry logic."""

    def __init__(self, name: str, node: Node, max_retries: int = 3):
        super().__init__(name)
        self.node = node
        self.max_retries = max_retries

    async def execute(self, context: NodeContext, **kwargs: Any) -> Any:
        pass
