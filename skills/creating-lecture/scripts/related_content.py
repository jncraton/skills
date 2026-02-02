import sys
import json
import urllib.request
import urllib.parse
import re


def clean_html(text):
    return re.sub(r"<[^>]*>", "", text).replace("\n", " ")


def search_images(query):
    params = {
        "action": "query",
        "format": "json",
        "prop": "imageinfo",
        "iiprop": "url|extmetadata",
        "iiurlwidth": 500,
        "generator": "search",
        "gsrsearch": f"{query} incategory:Quality_images",
        "gsrnamespace": 6,
    }
    url = f"https://commons.wikimedia.org/w/api.php?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "ImageSearchScript/1.0"})
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
                print(f"{thumb_url} {description[:300]}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        search_images(sys.argv[1])
