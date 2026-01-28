import urllib.request
import re
import html
import sys
from concurrent.futures import ThreadPoolExecutor


def fetch_url(url):
    with urllib.request.urlopen(url) as response:
        return response.read().decode("utf-8")


def clean_html(text):
    text = re.sub(r"<h1>(.*?)</h1>", r"# \1\n\n", text, flags=re.S)
    text = re.sub(r"<p[^>]*>(.*?)</p>", r"\1\n\n", text, flags=re.S)
    text = re.sub(r"<br\s*/?>", r"\n", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text).strip()
    lines = [line.strip() for line in text.splitlines()]
    lines = [l for l in lines if not l.lower().startswith("related story")]
    return re.sub("\n\n+", "\n\n", "\n".join(lines))


def fetch_story(story_url):
    try:
        story_html = fetch_url(story_url)

        title_match = re.search(r'<h1 class="story-title">(.*?)</h1>', story_html, re.S)
        content_match = re.search(
            r'<div class="paragraphs-container">(.*?)</div>', story_html, re.S
        )

        if title_match and content_match:
            title = html.unescape(title_match.group(1).strip())
            content = clean_html(content_match.group(1))
            return f"# {title}\n\n{story_url}\n\n{content}\n\n"
    except Exception as e:
        return f"Error fetching {story_url}: {e}"
    return None


def main():
    base_url = "https://text.npr.org"
    index_url = base_url + "/1001"
    index_html = fetch_url(index_url)

    links = re.findall(r'class="topic-title" href="(/[^"]+)"', index_html)
    story_urls = [base_url + link for link in links]

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(fetch_story, story_urls))

    for result in results:
        if result:
            if result.startswith("Error fetching"):
                print(result, file=sys.stderr)
            else:
                print(result)


if __name__ == "__main__":
    main()
