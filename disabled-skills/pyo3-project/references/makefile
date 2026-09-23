all:

lint:
	uvx black@24.1.0 --check .
	
format:
	uvx black@24.1.0 .

test:
	uv run python -m pytest

build:
	uv run --with maturin maturin develop

clean:
	rm -rf .pytest_cache __pycache__
