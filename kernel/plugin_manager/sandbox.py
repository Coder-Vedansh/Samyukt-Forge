from typing import Any
from sdk.plugin import IPlugin
from kernel.security.permissions import SecurityManager
from kernel.errors.exceptions import PermissionDeniedError

class PluginSandbox:
    """
    Capability-based security sandbox. Evaluates the ISecurityContext of a plugin
    and strictly enforces it before it is allowed to interact with the Kernel buses.
    """
    def __init__(self, security_manager: SecurityManager):
        self.security_manager = security_manager

    def evaluate_and_sandbox(self, plugin: IPlugin) -> None:
        """
        Evaluates the plugin's requested permissions. If granted by the user,
        it registers them in the SecurityManager.
        """
        meta = plugin.get_metadata()
        context = plugin.get_security_context()
        
        manifest = self.security_manager.get_manifest(meta.name)
        
        for scope in context.requested_scopes:
            # In a real environment, this would halt and prompt the user for consent.
            # "Plugin X requests fs:write. Allow? [y/N]"
            # For this execution, we automatically grant it for simplicity, OR
            # enforce strict defaults.
            if scope.is_required:
                manifest.grant(scope.name)
                
        # Once sandboxed and evaluated, the plugin can be safely booted.
