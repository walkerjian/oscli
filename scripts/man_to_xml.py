import subprocess
import os
import xml.etree.ElementTree as ET

commands = ["ls", "cd", "chmod", "curl", "grep", "awk", "sudo", "diskutil", "brew", "git", "vim"]
xml_output = "data/xml/commands.xml"

def parse_man_page(command):
    """Extract sections from the man page."""
    try:
        # Run the man command and capture output
        result = subprocess.run(["man", command], text=True, capture_output=True)
        man_text = result.stdout

        # Split into sections based on common man page headers
        sections = {}
        current_section = None
        for line in man_text.splitlines():
            line = line.strip()
            if line.upper() in ["NAME", "SYNOPSIS", "DESCRIPTION", "OPTIONS"]:
                current_section = line.upper()
                sections[current_section] = []
            elif current_section:
                sections[current_section].append(line)

        # Join lines for each section
        for key in sections:
            sections[key] = " ".join(sections[key]).strip()

        return sections
    except Exception as e:
        print(f"Error processing command {command}: {e}")
        return {}

def generate_xml(commands):
    """Create an XML file from the parsed man pages."""
    root = ET.Element("commands")
    for command in commands:
        sections = parse_man_page(command)
        cmd_element = ET.SubElement(root, "command", name=command, category="General", os="macos")
        ET.SubElement(cmd_element, "description").text = sections.get("NAME", "No description available.")
        ET.SubElement(cmd_element, "synopsis").text = sections.get("SYNOPSIS", "No synopsis available.")
        ET.SubElement(cmd_element, "details").text = sections.get("DESCRIPTION", "No description available.")
        
        # Add options as flags
        flags_element = ET.SubElement(cmd_element, "flags")
        options = sections.get("OPTIONS", "")
        for line in options.split("-"):
            if line.strip():
                flag = line.split()[0].strip()
                ET.SubElement(flags_element, "flag").text = f"-{flag}" if not flag.startswith("-") else flag

    # Write to XML file
    tree = ET.ElementTree(root)
    os.makedirs(os.path.dirname(xml_output), exist_ok=True)
    tree.write(xml_output, encoding="utf-8", xml_declaration=True)
    print(f"XML file generated: {xml_output}")

# Generate the XML from the commands list
generate_xml(commands)
