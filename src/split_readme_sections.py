import os
import re


input_file = "../README.md"
output_dir = "../docs"
toc_file = os.path.join(output_dir, "00_TableofContents.md")

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()



section_lines = []
section_name = None
section_counter = 1
toc_entries = []

def sanitize_filename(name):
    # Remove special characters and extra spaces
    return re.sub(r'[^A-Za-z0-9_ -]', '', name).replace(" ", "")


for line in lines:
    if line.startswith("### "):
        if section_name and section_lines:
            # Skip creating a file for Table of Contents section
            if section_name.strip().lower() != "table of contents":
                filename = f"{section_counter:02d}_" + sanitize_filename(section_name) + ".md"
                with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as out:
                    out.writelines(section_lines)
                toc_entries.append((section_name, filename))
                section_counter += 1
        section_name = line.strip().replace("### ", "")
        section_lines = [line]
    else:
        if section_name:
            section_lines.append(line)



# Write the last section
if section_name and section_lines:
    if section_name.strip().lower() != "table of contents":
        filename = f"{section_counter:02d}_" + sanitize_filename(section_name) + ".md"
        with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as out:
            out.writelines(section_lines)
        toc_entries.append((section_name, filename))

# Generate Table of Contents file
with open(toc_file, "w", encoding="utf-8") as toc:
    toc.write("### Table of Contents\n\n")
    for name, filename in toc_entries:
        toc.write(f"* [{name}]({filename})\n")
    toc.write("\n")

print("Archivos generados en la carpeta 'docs/'")
