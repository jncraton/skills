import sys
import json
import urllib.request
import urllib.parse
import re
from pathlib import Path

def clean_html(text):
    return re.sub(r"<[^>]*>", "", text).replace("\n", " ")


def search_images(query):
    keywords = ' '.join(query.split())
    params = {
        "action": "query",
        "format": "json",
        "prop": "imageinfo",
        "iiprop": "url|extmetadata",
        "iiurlwidth": 500,
        "generator": "search",
        "gsrsearch": f"{keywords} incategory:Quality_images",
        "gsrlimit": 50,
        "gsrnamespace": 6,
    }
    url = f"https://commons.wikimedia.org/w/api.php?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "ImageSearchScript/1.0"})
    print("## Images\n")
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        pages = data.get("query", {}).get("pages", {})
        for page in pages.values():
            title = page.get("title", "")
            imageinfo = page.get("imageinfo", [{}])[0]
            thumb_url = imageinfo.get("thumburl")
            if thumb_url:
                metadata = imageinfo.get("extmetadata", {})
                description = metadata.get("ImageDescription", {}).get("value", title)
                description = clean_html(description)
                if len(description) > 100:
                    print(f"{thumb_url} {description[:500]}")


def search_quotes(query):
    quote_path = Path(__file__).parent.parent / "references/quotes.txt"
    keywords = query.split()

    matcher = re.compile("|".join(keywords), flags=re.I)


    quotes = []
    for quote in open(quote_path):
        matches = len(re.findall(matcher, quote))
        quality = matches / len(quote.split("\t")[1])
        if quality > 0:
            quotes.append((quality, quote))

    print("## Quotes\n")
    for quote in sorted(quotes, reverse=True)[:5]:
        print(quote[1])

if __name__ == "__main__":
    if len(sys.argv) > 1:
        search_images(' '.join(sys.argv[1:]))
        print()
        search_quotes(' '.join(sys.argv[1:]))

