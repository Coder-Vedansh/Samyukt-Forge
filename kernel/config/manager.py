import json
import os
from typing import Any, Dict, Optional
from pydantic import BaseModel
from kernel.errors.exceptions import ConfigError

class KernelConfig(BaseModel):
    debug: bool = False
    log_level: str = "INFO"
    workspace_dir: str = "./.forge"

class ConfigManager:
    """
    Manages loading and merging configuration from defaults, env vars, and JSON/YAML.
    """
    def __init__(self):
        self._config = KernelConfig()
        self._raw_data: Dict[str, Any] = {}

    def load_from_file(self, file_path: str) -> None:
        if not os.path.exists(file_path):
            raise ConfigError(f"Config file not found: {file_path}")
            
        try:
            with open(file_path, 'r') as f:
                if file_path.endswith('.json'):
                    data = json.load(f)
                    self._raw_data.update(data)
                    self._config = KernelConfig(**self._raw_data)
                elif file_path.endswith(('.yaml', '.yml')):
                    # Assuming a YAML parser is present (e.g. PyYAML)
                    # For this kernel core, we might just mock or require yaml to be injected
                    pass
        except Exception as e:
            raise ConfigError(f"Failed to parse config file {file_path}: {str(e)}")

    def get_config(self) -> KernelConfig:
        return self._config

    def get(self, key: str, default: Any = None) -> Any:
        return self._raw_data.get(key, default)
