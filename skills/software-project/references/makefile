all: deploy

lint:
	npx --yes prettier@3.6.2 --check .
	uvx black@24.1.0 --check .
	
format:
	npx --yes prettier@3.6.2 --write .
	uvx black@24.1.0 .

%.min.js: %.js
	npx --yes uglify-js@3.19.3 --compress --mangle -- $< > $@

dep.css:
	wget -O dep.css https://example.com/dep.css

test:
	uv run --with pytest-playwright==0.7.2 python -m playwright install chromium firefox
	uv run --with pytest-playwright==0.7.2 python -m pytest --browser chromium --browser firefox

deploy: dep.css

clean:
	rm -rf .pytest_cache __pycache__ dep.css
