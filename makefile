SKILLS := $(patsubst skills/%,%.skill,$(wildcard skills/*))

all: skills.zip $(SKILLS)

.PHONY: readme.md

skills.zip:
	zip -9 -r $@ skills

%.skill:
	cd skills/$* && zip -9 -r ../../$@ *

format:
	uvx black@26.1.0 generate.py skills/*/scripts/*.py
	npx --yes prettier@3.8.1 --write .

readme.md:
	python3 generate.py

clean:
	rm -rf skills.zip *.skill index.md *.html **/*.html uv.lock .python-version .venv venv .ruff_cache
