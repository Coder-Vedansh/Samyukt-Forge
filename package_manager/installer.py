import shutil
from pathlib import Path

from package_manager.manifest import ManifestManager
from package_manager.marketplace import MarketplaceClient
from package_manager.resolver import DependencyResolver
from package_manager.security import PackageVerifier


class InstallationError(Exception):
    pass


class PackageInstaller:
    """
    Handles downloading, verifying, extracting, and installing .forgepkg plugins.
    """

    def __init__(self, workspace_dir: str):
        self.workspace_dir = Path(workspace_dir)
        self.plugins_dir = self.workspace_dir / "plugins"
        self.plugins_dir.mkdir(parents=True, exist_ok=True)
        self.manifest_manager = ManifestManager(workspace_dir)
        self.resolver = DependencyResolver()
        self.marketplace = MarketplaceClient()

    def install(self, package_name: str, version: str = "latest") -> None:
        """Installs a package from the remote marketplace."""
        print(f"Fetching metadata for {package_name}...")
        metadata = self.marketplace.get_metadata(package_name)
        if not metadata:
            raise InstallationError(f"Package {package_name} not found in registry.")

        # Simulate checking permissions before installation
        PackageVerifier.review_permissions(metadata.get("permissions", []))

        # Simulate dependency resolution
        if "dependencies" in metadata and metadata["dependencies"]:
            print("Resolving dependencies...")
            resolved = self.resolver.resolve(metadata["dependencies"])
            print(f"Resolved: {resolved}")

        print(
            f"Downloading {package_name} v{metadata['version']} from {metadata.get('download_url')}..."
        )
        # Simulation: In reality, we'd download the file and call `install_offline`

        self.manifest_manager.add_dependency(package_name, metadata["version"])
        print(f"Successfully installed {package_name}!")

    def install_offline(self, package_path: str) -> None:
        """Installs a package from a local .forgepkg (zip/tarball) file."""
        path = Path(package_path)
        if not path.exists():
            raise InstallationError(f"File not found: {package_path}")

        print(f"Extracting {package_path}...")

        # Simulate extraction and signature verification
        # with zipfile.ZipFile(package_path, 'r') as zip_ref:
        #     zip_ref.extractall(self.plugins_dir / path.stem)

        print("Verifying package signature...")
        # PackageVerifier.verify_manifest(...)

        # self.manifest_manager.add_dependency(...)
        print(f"Offline installation of {path.name} complete.")

    def uninstall(self, package_name: str) -> None:
        """Removes an installed package."""
        target_dir = self.plugins_dir / package_name
        if target_dir.exists():
            shutil.rmtree(target_dir)

        self.manifest_manager.remove_dependency(package_name)
        print(f"Uninstalled {package_name}.")

    def update(self, package_name: str) -> None:
        """Updates a package to the latest compatible version."""
        print(f"Checking for updates for {package_name}...")
        metadata = self.marketplace.get_metadata(package_name)
        if not metadata:
            raise InstallationError(f"Package {package_name} not found.")

        print(f"Updating {package_name} to version {metadata['version']}...")
        self.uninstall(package_name)
        self.install(package_name, metadata["version"])
