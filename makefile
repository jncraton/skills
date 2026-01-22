all: readme.md

.PHONY: readme.md

format:
	uvx black@26.1.0 generate.py
	npx prettier@3.8.1 --write .

readme.md:
	python3 generate.py

clean:
	rm -f index.md *.html **/*.html uv.lock .python-version