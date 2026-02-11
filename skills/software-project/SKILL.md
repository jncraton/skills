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

## Python

- Use `uv` for all tasks. Minimal or no `pyproject.toml`.
- Format with `black`.

## Testing

Prefer minimalistic testing. Test code is still technical debt. Only include meaningful tests.

## Web

If browser testing is needed, prefer pytest and playwright. This command is preferred for installing browsers and running tests:

```sh
pipx run --spec pytest-playwright==1.58.0 playwright install chromium firefox && pipx run --spec pytest-playwright==1.58.0 pytest --browser firefox --browser chromium
```

Use vanilla Javascript and css. Never use a build system. When external dependencies are needed, and them to the makefile to be downloaded with wget before deployment.

For web projects, favor static deployment whenever possible. The default makefile task should build all static 

## Commits

When creating a fresh project, commit changes as they are made, generally one file at a time. Use imperative mood and capitialize commit messages. Commit as jncraton (jncraton@gmail.com).

## Github Actions

Unless otherwise specified, four actions runners should be created to lint, test, deploy, and release the project. See example files for more details.

## References

Templates available in `references/`:

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
