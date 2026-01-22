all: index.md

format:
	uvx black@26.1.0 generate.py
	npx prettier@3.8.1 --write .

index.md:
	python3 generate.py

clean:
	rm -f index.md *.html **/*.html