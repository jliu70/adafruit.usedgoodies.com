from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({
    "good" : "green",
    "bad": "bold red"
})

console = Console(theme=custom_theme)
console.print("File downloaded!", style="good")
console.print("File corrupted!", style="bad")
console.print("The internet is [bad]down![/bad]")

# wip 1
# wip 2
# wip 3 
