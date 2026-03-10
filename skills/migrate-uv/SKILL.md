---
name: migrate-uv
description: Migrate Python Package to Modern uv Tooling
---

## Purpose
This skill converts legacy Python packages (using `setup.py`, `setup.cfg`, `requirements.txt`, `twine`, `pip`, etc.) to a modern stack based on uv, hatchling, and GitHub Actions.

---

## Target Stack

| Concern | Old tooling | New tooling |
|---|---|---|
| Build backend | setuptools / setup.py | hatchling (via pyproject.toml) |
| Package manager | pip + requirements.txt | uv |
| Linting/formatting | flake8, isort, etc. | `uvx black@24.1.0` |
| Testing | pytest (installed) | `uvx --with pytest==9.0.2 pytest` |
| Publishing | twine | `uv publish` |
| CI – publish | ad-hoc | `.github/workflows/pypi.yml` |
| CI – release | ad-hoc | `.github/workflows/release.yml` |

---

## Step-by-Step Migration Process

### 1. Analyse the existing package
Collect the following from the old files before writing anything:

- Package name — from `setup.py` (`name=`), `setup.cfg` (`[metadata] name =`), or directory name
- Version — same sources, or from `__version__` in source
- Description — `description=` field
- Author name + email
- Dependencies — `install_requires` in setup.py / `[options] install_requires` in setup.cfg / `requirements.txt`
- Python version floor — `python_requires` or lowest version tested
- Entry points / scripts — `entry_points` or `scripts` keys
- Any extra classifiers the user wants to keep

If any of these are ambiguous, ask the user before proceeding.

### 2. Create `pyproject.toml`
Use the template at `templates/pyproject.toml`.

Substitution map:

| Placeholder | Value |
|---|---|
| `{{PACKAGE_NAME}}` | package name (also used as the CLI entry-point module path — adjust if the package layout differs) |
| `{{VERSION}}` | current version string, e.g. `1.2.1` |
| `{{DESCRIPTION}}` | one-line description |
| `{{AUTHOR_NAME}}` | author full name |
| `{{AUTHOR_EMAIL}}` | author email |
| `{{DEPENDENCIES}}` | comma-separated quoted strings, one per line, e.g. `"requests>=2.28",` — leave empty string `""` if none |

If there is no CLI entry point, remove the `[project.scripts]` section entirely.

If the package layout is not `packagename/cli.py:main`, adjust the entry point accordingly.

### 3. Create `makefile`
Copy `templates/makefile` verbatim. It requires no substitution.

Only modify it if:
- The project uses a test runner other than pytest → update the `test` target
- There are project-specific clean artifacts (e.g. `*.epub`) → append them to the `clean` target

### 4. Create GitHub Actions workflows

Create these two files (creating `.github/workflows/` if needed):

`.github/workflows/pypi.yml` — copy from `templates/.github/workflows/pypi.yml` verbatim.
- Triggers on version tags (`v*.*.*`)
- Uses OIDC trusted publishing (no API token needed — user must configure this in PyPI project settings)

`.github/workflows/release.yml` — copy from `templates/.github/workflows/release.yml` verbatim.
- Triggers on version tags (`v*.*.*`)  
- Runs tests then creates a GitHub Release with auto-generated notes

### 5. Remove legacy files
Tell the user to delete these if they exist:
- `setup.py`
- `setup.cfg`
- `requirements.txt` (dependencies now live in `pyproject.toml`)
- `MANIFEST.in` (hatchling handles this)
- Any old `.github/workflows` files that duplicated the above

### 6. PyPI Trusted Publishing setup (one-time, manual)
Remind the user to configure OIDC trusted publishing on PyPI so `uv publish` works without a token:

1. Go to `https://pypi.org/manage/project/<package-name>/settings/`
2. Under Trusted Publishers, add a new publisher:
   - Publisher: GitHub Actions
   - Owner: their GitHub org/username
   - Repository: repo name
   - Workflow name: `pypi.yml`
   - Environment: *(leave blank)*

---

## Output Checklist

After completing the migration, confirm each item:

- [ ] `pyproject.toml` created with all placeholders filled
- [ ] `makefile` created / updated
- [ ] `.github/workflows/pypi.yml` created
- [ ] `.github/workflows/release.yml` created
- [ ] User informed which legacy files to delete
- [ ] User reminded to configure PyPI Trusted Publishing

---

## Common Edge Cases

No CLI entry point (library-only package):  
Remove `[project.scripts]` from `pyproject.toml`. The `Makefile` and workflows are unchanged.

Multiple entry points:  
Add additional lines under `[project.scripts]`, e.g.:
```toml
[project.scripts]
tool-a = "mypkg.a:main"
tool-b = "mypkg.b:main"
```

Extras / optional dependencies:  
Add an `[project.optional-dependencies]` section:
```toml
[project.optional-dependencies]
dev = ["pytest", "black"]
```

src layout (`src/mypkg/` instead of `mypkg/`):  
Change the wheel target:
```toml
[tool.hatch.build.targets.wheel]
packages = ["src/{{PACKAGE_NAME}}"]
```

Non-MIT license:  
Update the classifier in `pyproject.toml` and add a `license = {text = "..."}` field.

Private / internal packages (no PyPI publish):  
Omit `pypi.yml` entirely. Keep `release.yml` for GitHub Releases only.
