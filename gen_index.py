import os
import re
from pathlib import Path

def extract_metadata(file_path):
    """Extracts name and description from YAML frontmatter in a Markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not match:
            return None
        
        yaml_text = match.group(1)
        metadata = {}
        
        for line in yaml_text.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                metadata[key.strip().lower()] = value.strip()
                
        return metadata
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def generate_index():
    skills = []
    for path in Path('.').iterdir():
        if path.is_dir():
            skill_file = path / 'SKILL.md'
            if not skill_file.exists():
                skill_file = path / 'SKILLS.md'
            
            if skill_file.exists():
                meta = extract_metadata(skill_file)
                if meta and 'name' in meta and 'description' in meta:
                    skills.append(meta)

    if not skills:
        print("No valid skill files found in subdirectories.")
        return

    skills.sort(key=lambda x: x['name'].lower())

    with open('index.md', 'w', encoding='utf-8') as f:
        f.write('# Skills\n\n')
        for skill in skills:
            f.write(f"- {skill['name']}: {skill['description']}\n")
    
    print(f"Successfully generated index.md with {len(skills)} skills.")

if __name__ == "__main__":
    generate_index()