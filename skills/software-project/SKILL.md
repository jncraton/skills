---
name: software-project
description: Create, refine, or review a software project
---

Use a simple makefile for automation (lint, format, test, clean)

Minimize dependencies. Pin all versions

## Web

- Vanilla JS and CSS. No JS build systems.
- Favor static deployment. Makefile `all` should build assets.
- Use `npx` for tools. Download external deps with `wget` in makefile.
- Quality: Semantic HTML, responsive design, system fonts, accessibility.

Test with pytest and playwright:

```sh
uvx --with pytest-playwright==0.7.2 playwright install chromium firefox && uvx --with pytest-playwright==0.7.2 pytest --browser chromium --browser firefox
```

## Python

- Use `uv` for all tasks. Minimal or no `pyproject.toml`.
- Format with `black`.

## Testing

Prefer minimalistic testing. Test code is still technical debt. Only include meaningful tests.

## Commits

When creating a fresh project, commit changes as they are made, generally one file at a time. Use imperative mood and capitialize commit messages. Commit as jncraton (jncraton@gmail.com).

## Github Actions

Unless otherwise specified, four actions runners should be created to lint, test, deploy, and release the project. See example files for more details.

## References

Templates available in `references/`:

```
> find references -type f -printf '%P\n'
.prettierrc.json
readme.md
.jshintrc
makefile
test_index.py
.gitignore
.github/workflows/release.yml
.github/workflows/lint.yml
.github/workflows/deploy.yml
.github/workflows/test.yml
index.html
```

Use these files as templates and match these filenames, including casing.
