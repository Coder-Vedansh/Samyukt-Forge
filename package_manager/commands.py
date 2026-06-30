from package_manager.manifest import ManifestManager
from package_manager.installer import Installer
from package_manager.client import RegistryClient
from package_manager.resolver import DependencyResolver

class PackageManagerCLI:
    """
    Entry points for the `forge <command>` package manager CLI commands.
    """
    def __init__(self, workspace_dir: str = "."):
        self.manifest = ManifestManager(workspace_dir)
        self.installer = Installer()
        self.client = RegistryClient()
        self.resolver = DependencyResolver()

    async def install(self, package_name: str, version: str = "latest"):
        print(f"Resolving {package_name}@{version}...")
        info = await self.client.get_package_info(package_name)
        target_version = info["latest"] if version == "latest" else version
        
        success = self.installer.install(package_name, target_version)
        if success:
            self.manifest.add_dependency(package_name, f"^{target_version}")
            print(f"Successfully installed {package_name}@{target_version}")

    def uninstall(self, package_name: str):
        success = self.installer.uninstall(package_name)
        if success:
            self.manifest.remove_dependency(package_name)
            print(f"Successfully uninstalled {package_name}")

    async def update(self, package_name: str = None):
        """Updates a specific package, or all packages if None is provided."""
        packages_to_update = [package_name] if package_name else list(self.manifest.load().dependencies.keys())
        for pkg in packages_to_update:
            info = await self.client.get_package_info(pkg)
            self.installer.install(pkg, info["latest"])
            self.manifest.add_dependency(pkg, f"^{info['latest']}")
            print(f"Updated {pkg} to {info['latest']}")

    async def publish(self, package_path: str, token: str):
        success = await self.client.publish(package_path, token)
        if success:
            print("Successfully published package to Forge Registry.")
        else:
            print("Failed to publish package.")

    async def search(self, query: str):
        results = await self.client.search(query)
        for res in results:
            print(f"{res['name']} ({res['version']}) - {res['description']}")

    def list_installed(self):
        manifest = self.manifest.load()
        for pkg, ver in manifest.dependencies.items():
            print(f"{pkg}: {ver}")
