import typer
from rich.console import Console
from rich.table import Table

from package_manager.marketplace import MarketplaceClient

app = typer.Typer(help="Interact with the Forge Plugin Marketplace")
console = Console()
client = MarketplaceClient()


@app.command()
def search(query: str):
    """Search for plugins in the marketplace."""
    results = client.search(query)

    if not results:
        console.print(f"[yellow]No packages found for '{query}'.[/yellow]")
        return

    table = Table(title=f"Search Results for '{query}'")
    table.add_column("Package", style="cyan")
    table.add_column("Version", style="magenta")
    table.add_column("Rating", justify="right")
    table.add_column("Description")

    for pkg in results:
        table.add_row(pkg["name"], pkg["version"], f"{pkg['rating']} \u2b50", pkg["description"])

    console.print(table)


@app.command()
def publish(package_path: str, token: str = typer.Option(..., prompt=True, hide_input=True)):
    """Publish a local .forgepkg to the marketplace."""
    try:
        console.print(f"Publishing {package_path}...")
        client.publish(package_path, token)
        console.print("[green]Successfully published package![/green]")
    except Exception as e:
        console.print(f"[red]Error publishing:[/red] {str(e)}")


@app.command()
def info(package_name: str):
    """View metadata and ratings for a specific package."""
    metadata = client.get_metadata(package_name)
    if not metadata:
        console.print(f"[red]Package '{package_name}' not found.[/red]")
        return

    ratings = client.get_ratings(package_name)

    console.print(f"\n[bold cyan]{metadata['name']}[/bold cyan] v{metadata['version']}")
    console.print(f"Permissions: {', '.join(metadata.get('permissions', []))}")
    console.print(
        f"Rating: {ratings['average_rating']} \u2b50 ({ratings['total_reviews']} reviews)"
    )
    for review in ratings["reviews"]:
        console.print(
            f"  - [italic]{review['user']}[/italic]: {review['comment']} ({review['rating']} \u2b50)"
        )
    console.print()
