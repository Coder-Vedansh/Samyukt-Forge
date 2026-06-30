from kernel.config.manager import ConfigManager


def test_config_manager_initialization():
    """Ensure the ConfigManager initializes correctly."""
    manager = ConfigManager()
    config = manager.get_config()
    assert config.debug is False
    assert config.log_level == "INFO"
    assert config.workspace_dir == "./.forge"


def test_config_manager_get_default():
    """Ensure get() returns default value if key is not found."""
    manager = ConfigManager()
    assert manager.get("missing_key", "default_val") == "default_val"
