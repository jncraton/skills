all: test

lint:
	uvx black@24.1.0 --check .

format:
	uvx black@24.1.0 .

test:
	PYTHONPATH=. uvx --with pytest==9.0.2 pytest --doctest-modules

upload:
	uv build
	uv publish

clean:
	rm -rf .pytest_cache __pycache__ build dist *.egg-info */__pycache__ uv.lock
