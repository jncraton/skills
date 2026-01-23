all: skills.zip

.PHONY: readme.md

skills.zip:
	rm -rf skills skills.zip
	mkdir skills
	cp -R *ing* skills
	zip -9 -r $@ skills
	rm -rf skills

format:
	uvx black@26.1.0 generate.py
	npx prettier@3.8.1 --write .

readme.md:
	python3 generate.py

clean:
	rm -rf skills.zip index.md *.html **/*.html uv.lock .python-version .venv
