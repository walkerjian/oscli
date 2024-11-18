from middleware.command_traversal import get_available_commands, get_command_help, parse_help_text
from ui.menu_builder import build_menu_tree, display_menu

def main():
    # Step 1: Fetch available commands
    console.print("[blue]Fetching available commands...[/blue]")
    commands = get_available_commands()

    # Step 2: Parse help text for a subset of commands
    command_help = {cmd: parse_help_text(get_command_help(cmd)) for cmd in commands[:10]}  # Limit to 10 for demo

    # Step 3: Build the menu tree
    menu_tree = build_menu_tree(command_help)

    # Step 4: Display the menu
    display_menu(menu_tree)

if __name__ == "__main__":
    from rich.console import Console
    console = Console()
    main()
