import typer
from rich import print

app = typer.Typer(help="Manage Forge CLI configuration")


@app.command("view")
def view_config():
    """Displays the current Forge CLI configuration."""
    print("[bold blue]Configuration:[/bold blue]")
    print("Debug: False")
    print("Workspace: .forge")


@app.command("set")
def set_config(key: str, value: str):
    """Sets a specific configuration value."""
    print(f"Set [green]{key}[/green] to [yellow]{value}[/yellow]")
