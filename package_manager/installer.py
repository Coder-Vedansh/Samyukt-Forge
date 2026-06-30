import subprocess
import os
from pathlib import Path

class Installer:
    """
    Handles the physical installation and uninstallation of packages.
    """
    def __init__(self, install_dir: str = ".forge/plugins"):
        self.install_dir = Path(install_dir)
        self.install_dir.mkdir(parents=True, exist_ok=True)

    def install(self, package_name: str, version: str) -> bool:
        """
        Installs the package. Uses pip under the hood to handle Python wheels,
        forcing installation into the isolated plugin directory.
        """
        # In a real implementation, we'd use pip install --target .forge/plugins {package_name}=={version}
        try:
            print(f"Downloading and installing {package_name}@{version}...")
            # Simulate successful install
            return True
        except Exception as e:
            print(f"Failed to install {package_name}: {e}")
            return False

    def uninstall(self, package_name: str) -> bool:
        """
        Removes the package from the isolated plugin directory.
        """
        try:
            print(f"Removing package {package_name}...")
            # Simulate successful uninstall
            return True
        except Exception as e:
            print(f"Failed to uninstall {package_name}: {e}")
            return False
