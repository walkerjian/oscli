from commands.parser import parse_help_text
from ui.menu import display_menu

def main():
    # Simulate fetching help text (can be replaced with subprocess calls)
    docker_help_text = """
    Usage: docker [OPTIONS] COMMAND
      -h, --help    Show help information
      -v, --version Show version
    """

    # Parse the help text
    options = parse_help_text(docker_help_text)

    # Display the menu
    display_menu(options)

if __name__ == "__main__":
    main()
