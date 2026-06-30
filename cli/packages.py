import typer
from rich import print

packages_app = typer.Typer(help="Forge Package Manager commands")
extensions_app = typer.Typer(help="Manage installed Forge extensions")
marketplace_app = typer.Typer(help="Interact with the Forge Marketplace")

@packages_app.command("install")
def install_package(package_name: str, version: str = "latest"):
    """Installs a package/plugin via the Forge Package Manager."""
    print(f"Installing [green]{package_name}@{version}[/green]...")

@packages_app.command("uninstall")
def uninstall_package(package_name: str):
    """Uninstalls a package/plugin."""
    print(f"Uninstalling [red]{package_name}[/red]...")

@packages_app.command("update")
def update_package(package_name: str = None):
    """Updates one or all packages."""
    if package_name:
        print(f"Updating [green]{package_name}[/green]...")
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

@marketplace_app.command("search")
def search_marketplace(query: str):
    """Searches the remote Forge Marketplace for extensions."""
    print(f"Searching Marketplace for: [yellow]{query}[/yellow]...")
