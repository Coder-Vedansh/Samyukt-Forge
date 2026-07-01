from abc import abstractmethod
from typing import List, Type

from sdk.tools.capability import ToolCapability
from sdk.tools.lifecycle import IToolLifecycle
from sdk.tools.permission import ToolPermission
from sdk.tools.sandbox import ISandbox
from sdk.tools.schema import InputSchema, OutputSchema


class ITool(IToolLifecycle):
    """
    The unified Tool interface.
    A tool is a strict composition of its Capability, Permissions, Schemas, Sandbox, and Lifecycle.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass

    @property
    @abstractmethod
    def capability(self) -> ToolCapability:
        pass

    @property
    @abstractmethod
    def required_permissions(self) -> List[ToolPermission]:
        pass

    @property
    @abstractmethod
    def input_schema(self) -> Type[InputSchema]:
        """Returns the Pydantic model defining expected inputs."""
        pass

    @property
    @abstractmethod
    def output_schema(self) -> Type[OutputSchema]:
        """Returns the Pydantic model defining expected outputs."""
        pass

    @property
    @abstractmethod
    def sandbox(self) -> ISandbox:
        """Returns the isolation boundary instance used to run this tool."""
        pass

    @abstractmethod
    async def execute(self, inputs: InputSchema) -> OutputSchema:
        """
        The core execution logic.
        Note: The orchestrator handles calling pre_execute, sandbox.run_isolated, and post_execute.
        """
        pass
