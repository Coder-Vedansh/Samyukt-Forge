from pydantic import BaseModel


class ToolPermission(BaseModel):
    """
    Defines a strict security grant required to run a tool.
    Matches the schema utilized in Phase 14's PackageManifest.
    """

    resource: str  # e.g., 'fs', 'network', 'process'
    action: str  # e.g., 'read', 'write', 'exec'
    target: str  # e.g., '/tmp', 'github.com', '*'

    def to_string(self) -> str:
        """Returns the canonical string representation (e.g., 'fs:read:/tmp')"""
        return f"{self.resource}:{self.action}:{self.target}"
