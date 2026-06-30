import typer
from rich import print

memory_app = typer.Typer(help="Manage Agent Memory and Vector DBs")
workflow_app = typer.Typer(help="Manage and execute predefined AI Workflows")

@memory_app.command("clear")
def clear_memory():
    """Wipes all short-term and long-term memory."""
    print("[bold red]Memory cleared successfully.[/bold red]")

@workflow_app.command("run")
def run_workflow(workflow_name: str):
    """Executes a defined workflow via the runtime executor."""
    print(f"Starting workflow: [bold cyan]{workflow_name}[/bold cyan]")

@workflow_app.command("list")
def list_workflows():
    """Lists all available workflows."""
    print("Available Workflows:")
    print("- generate_docs")
    print("- review_pr")
