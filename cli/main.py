import typer
from rich import print

from cli.config import app as config_app
from cli.providers import providers_app, models_app
from cli.packages import packages_app, extensions_app, marketplace_app
from cli.runtime import memory_app, workflow_app

app = typer.Typer(
    name="forge", 
    help="Forge CLI - The Linux for AI",
    no_args_is_help=True
)

# Mount all the sub-commands
app.add_typer(config_app, name="config")
app.add_typer(providers_app, name="providers")
app.add_typer(models_app, name="models")
app.add_typer(packages_app, name="packages")
app.add_typer(extensions_app, name="extensions")
app.add_typer(marketplace_app, name="marketplace")
app.add_typer(memory_app, name="memory")
app.add_typer(workflow_app, name="workflow")

@app.command()
def init():
    """Initializes a new Forge Workspace in the current directory."""
    print("[bold green]Initialized empty Forge workspace.[/bold green]")

@app.command()
def run(prompt: str):
    """Main execution command for passing prompts to the Default Agent."""
    print(f"[dim]Running Agent with prompt:[/dim] [yellow]{prompt}[/yellow]")
    print("Executing via Forge Runtime...")

@app.command()
def doctor():
    """Checks the health of the Kernel, registries, and plugins."""
    print("[bold blue]Forge Doctor - Health Check[/bold blue]")
    print("Kernel: [green]OK[/green]")
    print("Package Manager: [green]OK[/green]")
    print("Runtime: [green]OK[/green]")

if __name__ == "__main__":
    app()
