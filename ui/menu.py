from rich.console import Console
from rich.table import Table

def display_menu(options):
    """
    Displays a menu for the parsed options.

    Args:
        options (dict): Command options and descriptions.
    """
    console = Console()
    table = Table(title="OSCLI Menu")
    table.add_column("Option", justify="left")
    table.add_column("Description", justify="left")

    for option, description in options.items():
        table.add_row(option, description)

    console.print(table)
