---
name: pyo3-project
description: Create, refine, or review a pyo3 Python/Rust package
---

Use a simple makefile for automation (lint, format, test, clean)

Minimize dependencies. Pin all versions

## Python

- Use `uv` for all tasks. Minimal or no `pyproject.toml`
- Format with `black`

## Testing

Prefer minimalistic testing. Test code is still technical debt. Only include meaningful tests.

## Commits

When creating a fresh project, commit changes as they are made, generally one file at a time. Use imperative mood and capitialize commit messages. Commit as jncraton (jncraton@gmail.com).

## Github Actions

Unless otherwise specified, five actions runners should be created to lint, test, deploy, release, and publis the project to pypi. See example files for more details.

## References

Templates available in `references/`:

```
> find references -type f -printf '%P\n'
makefile
.gitignore
.github/workflows/release.yml
.github/workflows/lint.yml
.github/workflows/deploy.yml
.github/workflows/test.yml
.github/workflows/pypi.yml
```

Use these files as templates and match these filenames, including casing.
