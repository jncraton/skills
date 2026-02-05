""" Get related content for topics

Example:

> python3 scripts/related_content.py "Guido van Rossum" "Triangle Area" "Variable"
"""

import sys
import json
import urllib.request
import urllib.parse
import re
from pathlib import Path

def clean_html(text):
    return re.sub(r"<[^>]*>", "", text).replace("\n", " ")


def search_images(queries):
    print("## Images\n")
    for query in queries:
        print(f"### {query}\n")
        params = {
            "action": "query",
            "format": "json",
            "prop": "imageinfo",
            "iiprop": "url|extmetadata",
            "iiurlwidth": 960,
            "generator": "search",
            "gsrsearch": query,
            "gsrsort": "relevance",
            "gsrlimit": 50,
            "gsrnamespace": 6,
        }
        url = f"https://commons.wikimedia.org/w/api.php?{urllib.parse.urlencode(params)}"
        req = urllib.request.Request(url, headers={"User-Agent": "ImageSearchScript/1.0"})
        count = 0
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            pages = data.get("query", {}).get("pages", {})
            results = []
            for page in pages.values():
                title = page.get("title", "")
                imageinfo = page.get("imageinfo", [{}])[0]
                thumb_url = imageinfo.get("thumburl")
                if thumb_url:
                    metadata = imageinfo.get("extmetadata", {})
                    description = metadata.get("ImageDescription", {}).get("value", title)
                    description = clean_html(description)
                    quality = min(0.5, len(description) / 30)
                    categories = metadata.get("Categories", {}).get("value", "")
                    if "Featured pictures" in categories:
                        quality += 3
                    if "Quality images" in categories:
                        quality += 2
                    if "Valued images" in categories:
                        quality += 1
                    
                    results.append({
                        "index": page.get("index", 0),
                        "quality": quality,
                        "url": thumb_url,
                        "description": description,
                        "categories": categories
                    })
            
            # Sort by quality (descending) then by search index (ascending)
            results.sort(key=lambda x: (-x["quality"], x["index"]))
            
            for res in results[:3]:
                marker = ""
                if "Featured pictures" in res["categories"]:
                    marker = "[FEATURED] "
                elif "Quality images" in res["categories"]:
                    marker = "[QUALITY] "
                elif "Valued images" in res["categories"]:
                    marker = "[VALUED] "
                
                print(f"{res['url']}\tq:{res['quality']:.01f}\t{marker}{res['description'][:500]}")
                count += 1
            print()

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
        search_images(sys.argv[1:])
        print()
        search_quotes(' '.join(sys.argv[1:]))

