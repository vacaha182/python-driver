import os
import re

input_file = "README.md"
output_dir = "docs"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()


section_lines = []
section_name = None
section_counter = 1

def sanitize_filename(name):
    # Remove special characters and extra spaces
    return re.sub(r'[^A-Za-z0-9_ -]', '', name).replace(" ", "")


for line in lines:
    if line.startswith("### "):
        if section_name and section_lines:
            filename = f"{section_counter:02d}_" + sanitize_filename(section_name) + ".md"
            with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as out:
                out.writelines(section_lines)
            section_counter += 1
        section_name = line.strip().replace("### ", "")
        section_lines = [line]
    else:
        if section_name:
            section_lines.append(line)


# Write the last section
if section_name and section_lines:
    filename = f"{section_counter:02d}_" + sanitize_filename(section_name) + ".md"
    with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as out:
        out.writelines(section_lines)

print("Archivos generados en la carpeta 'docs/'")
