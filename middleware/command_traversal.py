import os
import subprocess

def get_available_commands():
    """Get a list of all available commands from the PATH environment variable."""
    commands = set()
    for path in os.getenv("PATH", "").split(":"):
        if os.path.isdir(path):
            for command in os.listdir(path):
                commands.add(command)
    return sorted(commands)

def get_command_help(command):
    """Fetch the help text for a given command."""
    try:
        result = subprocess.run(
            [command, "--help"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return result.stdout or result.stderr
    except Exception as e:
        return f"Failed to fetch help for {command}: {e}"

def parse_help_text(help_text):
    """Parse help text into a structured format."""
    parsed_data = {}
    lines = help_text.splitlines()
    for line in lines:
        # Simplified parsing: match lines with options and descriptions
        if line.startswith("-"):
            parts = line.split(maxsplit=1)
            if len(parts) == 2:
                flag, description = parts
                parsed_data[flag] = description
    return parsed_data
