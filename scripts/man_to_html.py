import os
import subprocess

# Directories
MAN_HTML_DIR = "data/man_html"

# List of commands to process
commands = [
    "ls", "cd", "pwd", "mkdir", "rm", "cat", "grep", "awk", "sed", "curl", "ping",
    "diskutil", "sudo", "chmod", "brew", "git", "vim"
]

def convert_man_to_html(command):
    """
    Converts the man page of a command to HTML using man2html.
    """
    output_path = os.path.join(MAN_HTML_DIR, f"{command}.html")
    try:
        # Execute man2html
        result = subprocess.run(
            ["man", command],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode != 0:
            print(f"Error retrieving man page for {command}: {result.stderr}")
            return False
        
        # Write output to HTML file
        with open(output_path, "w") as file:
            file.write(result.stdout)
        print(f"Converted {command} man page to HTML: {output_path}")
        return True
    except Exception as e:
        print(f"Error processing {command}: {e}")
        return False

def main():
    """
    Main function to process commands and convert their man pages to HTML.
    """
    # Create directory if it doesn't exist
    os.makedirs(MAN_HTML_DIR, exist_ok=True)

    for command in commands:
        convert_man_to_html(command)

if __name__ == "__main__":
    main()
