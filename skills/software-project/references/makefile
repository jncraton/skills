all: deploy

lint:
	npx prettier@3.6.2 --check .
	npx jshint@2.13.6
	
format:
	npx prettier@3.6.2 --write .

%.min.js: %.js
	npx uglify-js@3.19.3 --compress --mangle -- $< > $@

dep.css:
	wget https://example.com/dep.css

test: index.html
	pipx run --spec pytest-playwright==0.7.2 playwright install chromium firefox && pipx run --spec pytest-playwright==0.7.2 pytest --browser firefox --browser chromium

deploy:
	# Build static files to project root

clean:
	rm -rf .pytest_cache __pycache__ dep.css
