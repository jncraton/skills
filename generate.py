import os
import re
from pathlib import Path
import markdown


def convert_md_to_html(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                md_path = os.path.join(root, file)
                html_path = os.path.splitext(md_path)[0] + ".html"

                with open(md_path, "r", encoding="utf-8") as f:
                    text = f.read()
                    html = markdown.markdown(text)

                with open(html_path, "w", encoding="utf-8") as f:
                    f.write(html)
                print(f"Converted: {md_path}")

                if file == "SKILL.md":
                    with open(
                        os.path.join(root, "index.html"), "w", encoding="utf-8"
                    ) as f:
                        f.write(html)
                    print(f"Wrote index for {root}")


def extract_metadata(file_path):
    """Extracts name and description from YAML frontmatter in a Markdown file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        match = re.search(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
        if not match:
            return None

        yaml_text = match.group(1)
        metadata = {}

        for line in yaml_text.split("\n"):
            if ":" in line:
                key, value = line.split(":", 1)
                metadata[key.strip().lower()] = value.strip()

        return metadata
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None


def generate_index():
    skills = []
    for path in Path(".").iterdir():
        if path.is_dir():
            skill_file = path / "SKILL.md"
            if not skill_file.exists():
                skill_file = path / "SKILLS.md"

            if skill_file.exists():
                meta = extract_metadata(skill_file)
                if meta and "name" in meta and "description" in meta:
                    skills.append(meta)

    if not skills:
        print("No valid skill files found in subdirectories.")
        return

    skills.sort(key=lambda x: x["name"].lower())

    with open("readme.md", "w", encoding="utf-8") as f:
        f.write("# Skills\n\n")
        for skill in skills:
            f.write(f"- [{skill['name']}]({skill['name']}/): {skill['description']}\n")

    print(f"Successfully generated index.md with {len(skills)} skills.")


if __name__ == "__main__":
    generate_index()
    convert_md_to_html(".")
