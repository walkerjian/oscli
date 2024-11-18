import re

def parse_help_text(help_text):
    """
    Parses the help text of a command into options and their descriptions.

    Args:
        help_text (str): The help text of a command.

    Returns:
        dict: A dictionary of options and their descriptions.
    """
    options = {}
    for line in help_text.splitlines():
        match = re.match(r"\s*(-\S|--\S+)\s+(.*)", line)
        if match:
            option, description = match.groups()
            options[option] = description.strip()
    return options
