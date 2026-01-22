all: index.md

index.md:
	python3 gen_index.py

clean:
	rm -f index.md *.html **/*.html