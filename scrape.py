import urllib.request
import re
import sys

html = urllib.request.urlopen(sys.argv[1]).read().decode('utf8')
main = re.search(r"<main.*?</main>", html, flags=re.I|re.M|re.DOTALL)[0]

main = re.sub("<style.*?</style>", "", main, flags=re.I|re.M|re.DOTALL)
main = re.sub("<script.*?</script>", "", main, flags=re.I|re.M|re.DOTALL)
main = re.sub("[\n\r]", "", main)
main = re.sub("<tr.*?>", "\n\n", main)
main = re.sub("<li.*?>", "\n\n", main)
main = re.sub("<h\d.*?>", "\n\n", main)
main = re.sub("<p>", "\n\n", main)
main = re.sub("<p .*?>", "\n\n", main)
main = re.sub("<.*?>", "", main)
main = re.sub("\n[ \t]+", "\n", main)
main = re.sub("[ \t]+", " ", main)
main = re.sub("\n\n+", "\n\n", main)
main = main.strip()

with open(sys.argv[2], 'w') as f:
    f.write(main)
