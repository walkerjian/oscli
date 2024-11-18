from rich.console import Console
from rich.prompt import Prompt

console = Console()

def build_menu_tree(commands):
    """Build a tree structure from the available commands."""
    menu_tree = {"commands": {}, "submenus": {}}
    for command in commands:
        menu_tree["commands"][command] = f"Help for {command}"
    return menu_tree

def display_menu(tree):
    """Display a menu and allow traversal."""
    while True:
        console.print("\n[bold blue]OSCLI Menu[/bold blue]")
        options = list(tree["commands"].keys()) + ["Exit"]
        choice = Prompt.ask("Select an option", choices=options)
        if choice == "Exit":
            console.print("Exiting OSCLI. Goodbye!")
            break
        elif choice in tree["commands"]:
            console.print(f"[green]Help for {choice}[/green]")
            console.print(tree["commands"][choice])
        else:
            console.print("[red]Invalid option.[/red]")
