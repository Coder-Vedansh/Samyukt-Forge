import typer
from rich import print

from package_manager.installer import InstallationError, PackageInstaller

packages_app = typer.Typer(help="Forge Package Manager commands")
extensions_app = typer.Typer(help="Manage installed Forge extensions")
marketplace_app = typer.Typer(help="Interact with the Forge Marketplace (Legacy)")


def get_installer() -> PackageInstaller:
    # Hardcoded workspace for CLI simulation
    return PackageInstaller("./.forge")


@packages_app.command("install")
def install_package(package_name: str, version: str = "latest", offline: bool = False):
    """Installs a package/plugin via the Forge Package Manager."""
    installer = get_installer()
    try:
        if offline:
            installer.install_offline(package_name)
            print(f"[green]Successfully installed {package_name} offline.[/green]")
        else:
            installer.install(package_name, version)
            print(f"[green]Successfully installed {package_name}@{version}.[/green]")
    except InstallationError as e:
        print(f"[red]Error:[/red] {str(e)}")


@packages_app.command("uninstall")
def uninstall_package(package_name: str):
    """Uninstalls a package/plugin."""
    installer = get_installer()
    try:
        installer.uninstall(package_name)
        print(f"[green]Uninstalling {package_name}...[/green]")
    except Exception as e:
        print(f"[red]Error:[/red] {str(e)}")


@packages_app.command("update")
def update_package(package_name: str = None):
    """Updates one or all packages."""
    installer = get_installer()
    if package_name:
        try:
            installer.update(package_name)
            print(f"[green]Successfully updated {package_name}.[/green]")
        except InstallationError as e:
            print(f"[red]Error updating:[/red] {str(e)}")
    else:
        print("Updating all packages...")


@packages_app.command("list")
def list_packages():
    """Lists all installed packages."""
    print("[bold]Installed Packages:[/bold]")
    print("- forge-openai@1.0.0")


@extensions_app.command("list")
def list_extensions():
    """Alias for package listing, specifically focusing on extensions."""
    print("Listing installed extensions...")
