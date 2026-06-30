class ForgeError(Exception):
    """Base exception for all Forge CLI Kernel errors."""
    pass

class PluginLoadError(ForgeError):
    """Raised when a plugin fails to load or resolve dependencies."""
    pass

class CommandNotRegisteredError(ForgeError):
    """Raised when dispatching a command that has no registered handler."""
    pass

class DependencyInjectionError(ForgeError):
    """Raised when a dependency cannot be resolved."""
    pass

class PermissionDeniedError(ForgeError):
    """Raised when a command or plugin attempts an action without proper permissions."""
    pass

class ConfigError(ForgeError):
    """Raised when there is an issue loading or parsing configuration."""
    pass
