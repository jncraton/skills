import urllib.request
import re
import sys

from markdownify import markdownify

html = urllib.request.urlopen(sys.argv[1]).read().decode('utf8')
main = re.search(r"<main.*?</main>", html, flags=re.I|re.M|re.DOTALL)[0]
md = markdownify(main, strip=['a'])

with open(sys.argv[2], 'w') as f:
    f.write(md)
