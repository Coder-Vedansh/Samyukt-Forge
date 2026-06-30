from typing import Dict, List, Set
from kernel.errors.exceptions import PermissionDeniedError

class PermissionManifest:
    """
    Defines the capabilities a specific plugin or agent is allowed to access.
    """
    def __init__(self, owner_id: str):
        self.owner_id = owner_id
        self.allowed_scopes: Set[str] = set()

    def grant(self, scope: str) -> None:
        self.allowed_scopes.add(scope)

    def revoke(self, scope: str) -> None:
        self.allowed_scopes.discard(scope)

    def has_permission(self, scope: str) -> bool:
        return scope in self.allowed_scopes or "*" in self.allowed_scopes

class SecurityManager:
    """
    Centralized Security Manager that intercepts commands to enforce permissions.
    """
    def __init__(self):
        self._manifests: Dict[str, PermissionManifest] = {}

    def get_manifest(self, owner_id: str) -> PermissionManifest:
        if owner_id not in self._manifests:
            self._manifests[owner_id] = PermissionManifest(owner_id)
        return self._manifests[owner_id]

    def verify_permission(self, owner_id: str, required_scope: str) -> None:
        manifest = self.get_manifest(owner_id)
        if not manifest.has_permission(required_scope):
            raise PermissionDeniedError(
                f"Owner '{owner_id}' lacks required permission scope: {required_scope}"
            )
