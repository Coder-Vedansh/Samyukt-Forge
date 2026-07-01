from enum import Enum


class ToolCapability(str, Enum):
    """
    Categorizes the intrinsic nature of a Tool.
    Used by the Kernel to apply global policies and group contextually.
    """

    COMPUTE = "compute"  # Pure data manipulation, no IO
    FILE_SYSTEM = "file_system"  # Reads or writes to the local disk
    NETWORK = "network"  # Makes external HTTP/RPC requests
    BROWSER = "browser"  # Controls headless browsers
    DATABASE = "database"  # Executes queries against DBs
    SYSTEM = "system"  # Executes shell commands or process management
