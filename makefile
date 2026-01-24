all: skills.zip

.PHONY: readme.md

skills.zip:
	rm -rf skills skills.zip
	mkdir skills
	cp -R *ing* skills
	zip -9 -r $@ skills
	rm -rf skills

creating-lecture/references/py4e.md:
	wget -O py4e.epub http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.epub
	# The following is a nasty hack to truncate several chapter from the epub
	unzip py4e.epub -d py4e
	truncate --size 0 py4e/EPUB/text/ch001.xhtml # intro
	truncate --size 0 py4e/EPUB/text/ch012.xhtml # web services
	truncate --size 0 py4e/EPUB/text/ch013.xhtml # networking
	truncate --size 0 py4e/EPUB/text/ch015.xhtml # databases
	truncate --size 0 py4e/EPUB/text/ch016.xhtml # data vis
	truncate --size 0 py4e/EPUB/text/ch017.xhtml
	truncate --size 0 py4e/EPUB/text/ch018.xhtml
	truncate --size 0 py4e/EPUB/text/ch019.xhtml
	rm -f py4e.epub
	cd py4e && zip -r ../py4e.epub *
	rm -rf py4e
	# Convert epub to markdown stripping images and html attrs and wrappers
	pandoc py4e.epub -o $@ --lua-filter=filters.lua
	rm -f py4e.epub

format:
	uvx black@26.1.0 generate.py
	npx prettier@3.8.1 --write .

readme.md:
	python3 generate.py

clean:
	rm -rf skills.zip index.md *.html **/*.html uv.lock .python-version .venv
