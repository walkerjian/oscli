import re

def parse_help_text(help_text):
    """
    Parses a command's help text and extracts options with their descriptions.
    
    Args:
        help_text (str): The help text string.
    
    Returns:
        dict: A dictionary of options and their corresponding descriptions.
    """
    options = {}
    lines = help_text.splitlines()
    for line in lines:
        match = re.match(r"^\s*(-\w,?\s*--\w+)\s+(.*)", line.strip())
        if match:
            flags, description = match.groups()
            for flag in flags.split(","):
                options[flag.strip()] = description.strip()
    return options
