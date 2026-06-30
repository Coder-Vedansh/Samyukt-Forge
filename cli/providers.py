import typer
from rich import print
from rich.table import Table

providers_app = typer.Typer(help="Manage AI Providers (OpenAI, Anthropic, Ollama)")
models_app = typer.Typer(help="Manage installed Models")


@providers_app.command("list")
def list_providers():
    """Lists all available AI providers installed via plugins."""
    table = Table(title="Installed AI Providers")
    table.add_column("Provider Name", style="cyan")
    table.add_column("Status", style="green")
    table.add_row("OpenAI", "Active")
    table.add_row("Anthropic", "Active")
    print(table)


@models_app.command("list")
def list_models():
    """Lists all available models provided by installed plugins."""
    table = Table(title="Available Models")
    table.add_column("Model Name", style="cyan")
    table.add_column("Provider", style="magenta")
    table.add_row("gpt-4o", "OpenAI")
    table.add_row("claude-3-5-sonnet", "Anthropic")
    print(table)
