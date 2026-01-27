import os
import re
from pathlib import Path
import markdown
from tokenizers import Tokenizer


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

                if file.lower() in ["skill.md", "readme.md"]:
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


def load_tokenizer():
    """Load the Gemma 3 tokenizer from Hugging Face."""
    try:
        tokenizer = Tokenizer.from_pretrained("Qwen/Qwen3-0.6B")
        return tokenizer
    except Exception as e:
        print(f"Warning: Could not load tokenizer: {e}")
        return None


def count_tokens(text, tokenizer):
    """Count tokens in the given text using the provided tokenizer."""
    if tokenizer is None:
        return 0
    try:
        encoding = tokenizer.encode(text)
        return len(encoding.ids)
    except Exception as e:
        print(f"Warning: Could not count tokens: {e}")
        return 0


def generate_index():
    tokenizer = load_tokenizer()

    skills = []
    for path in Path("skills").iterdir():
        if path.is_dir():
            print(f"Found {path} for index")
            skill_file = path / "SKILL.md"
            if not skill_file.exists():
                skill_file = path / "SKILLS.md"

            if skill_file.exists():
                meta = extract_metadata(skill_file)
                if meta["name"] != str(path)[7:]:
                    raise ValueError(f"Skill name does not match path: {path}")
                if meta and "name" in meta and "description" in meta:
                    # Read the full content of the skill file
                    with open(skill_file, "r", encoding="utf-8") as f:
                        content = f.read()

                    # Count tokens in the skill content
                    token_count = count_tokens(content, tokenizer)
                    meta["token_count"] = token_count
                    skills.append(meta)

    if not skills:
        print("No valid skill files found in subdirectories.")
        return

    skills.sort(key=lambda x: x["name"].lower())

    with open("readme.md", "w", encoding="utf-8") as f:
        f.write(
            "# Skills\n\n"
            "[skills.zip](https://jncraton.github.io/skills/skills.zip) | "
            "[spec](https://agentskills.io/)"
            "\n\n"
        )
        for skill in skills:
            token_info = (
                f" ({skill['token_count']} tokens)"
                if skill.get("token_count", 0) > 0
                else ""
            )
            f.write(
                f"- [{skill['name']}](skills/{skill['name']}/SKILL.md){token_info}: {skill['description']}\n"
            )

        f.write("\n\n" + """
## Setup

opencode:

```sh
ln -s AGENTS.md ~/.config/opencode/AGENTS.md
ln -s skills ~/.config/opencode/skills
```
""".strip())

    print(f"Successfully generated readme.md with {len(skills)} skills.")


if __name__ == "__main__":
    generate_index()
