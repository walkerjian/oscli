from bs4 import BeautifulSoup
import os
import xml.etree.ElementTree as ET


def extract_section(soup, section_name):
    """Extract text under a specific section heading."""
    section = soup.find("h1", string=section_name) or soup.find("h2", string=section_name)
    if section:
        content = section.find_next("p")
        if content:
            return content.get_text(strip=True)
    return None


def parse_html_to_xml():
    """Convert HTML man pages to structured XML."""
    output_dir = "data/xml"
    os.makedirs(output_dir, exist_ok=True)

    root = ET.Element("commands")
    input_dir = "data/man_html"

    for file_name in os.listdir(input_dir):
        if file_name.endswith(".html"):
            command_name = file_name.replace(".html", "")
            file_path = os.path.join(input_dir, file_name)

            print(f"Processing: {file_name}")
            with open(file_path, "r") as file:
                soup = BeautifulSoup(file, "html.parser")
                command = ET.SubElement(root, "command", name=command_name, category="General", os="macos")

                # Extract NAME section
                name_section = extract_section(soup, "NAME")
                if name_section:
                    description = name_section.split("–", 1)[-1].strip() if "–" in name_section else name_section
                else:
                    description = "No description available."
                ET.SubElement(command, "description").text = description

                # Extract SYNOPSIS
                synopsis_section = extract_section(soup, "SYNOPSIS")
                if synopsis_section:
                    synopsis_element = ET.SubElement(command, "synopsis")
                    ET.SubElement(synopsis_element, "line").text = synopsis_section

                # Extract DESCRIPTION
                description_section = extract_section(soup, "DESCRIPTION")
                if description_section:
                    ET.SubElement(command, "details").text = description_section

    # Write XML to file
    tree = ET.ElementTree(root)
    output_path = os.path.join(output_dir, "commands.xml")
    tree.write(output_path, encoding="utf-8", xml_declaration=True)
    print(f"XML file generated: {output_path}")


if __name__ == "__main__":
    parse_html_to_xml()


html_dir = "data/man_html"
xml_output = "data/xml/commands.xml"

commands = ET.Element("commands")

for html_file in os.listdir(html_dir):
    if html_file.endswith(".html"):
        with open(os.path.join(html_dir, html_file), "r") as file:
            soup = BeautifulSoup(file, "html.parser")
            
            # Extract the command name from the filename
            command_name = html_file.replace(".html", "")
            
            # Try to parse the NAME section for the description
            name_section = soup.find("pre") or soup.find("div")  # Adjust based on your HTML structure
            description = "No description available."
            if name_section:
                for line in name_section.text.splitlines():
                    if line.strip().startswith("NAME"):
                        description = line.split("–", 1)[-1].strip()  # Adjust the delimiter based on your data
            
            # Try to parse the OPTIONS section for flags
            options_section = soup.find_all("b")  # Look for bolded options
            flags = []
            for option in options_section:
                text = option.text.strip()
                if text.startswith("-") or text.startswith("--"):
                    flags.append(text)
            
            # Create XML elements
            command = ET.SubElement(commands, "command", name=command_name, category="General", os="macos")
            ET.SubElement(command, "description").text = description
            flags_element = ET.SubElement(command, "flags")
            for flag in flags:
                ET.SubElement(flags_element, "flag").text = flag

# Write to XML file
tree = ET.ElementTree(commands)
os.makedirs(os.path.dirname(xml_output), exist_ok=True)
tree.write(xml_output, encoding="utf-8", xml_declaration=True)

print(f"XML file generated: {xml_output}")