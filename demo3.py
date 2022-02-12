from rich.console import Console

console = Console()
console.print("This is some text.")
console.print("This is some text.", style="bold")
console.print("This is some text.", style="bold underline")
console.print("[bold]This [underline]is[/] some text.[/]")

