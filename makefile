all: index.md

format:
	uvx black@26.1.0 generate.py

index.md:
	python3 gen_index.py

clean:
	rm -f index.md *.html **/*.html