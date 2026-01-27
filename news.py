import urllib.request
import re
import html

import sys

def fetch_url(url):
    with urllib.request.urlopen(url) as response:
        return response.read().decode('utf-8')

def clean_html(text):
    text = re.sub(r'<h1>(.*?)</h1>', r'# \1\n\n', text, flags=re.S)
    text = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', text, flags=re.S)
    text = re.sub(r'<br\s*/?>', r'\n', text)
    text = re.sub(r'<[^>]+>', '', text)
    return html.unescape(text).strip()

def main():
    base_url = "https://text.npr.org"
    index_url = base_url + "/1001"
    index_html = fetch_url(index_url)
    
    links = re.findall(r'class="topic-title" href="(/[^"]+)"', index_html)
    
    for link in links:
        story_url = base_url + link
        try:
            story_html = fetch_url(story_url)
            
            title_match = re.search(r'<h1 class="story-title">(.*?)</h1>', story_html, re.S)
            content_match = re.search(r'<div class="paragraphs-container">(.*?)</div>', story_html, re.S)
            
            if title_match and content_match:
                title = html.unescape(title_match.group(1).strip())
                content = clean_html(content_match.group(1))
                print(f"# {title}\n\n{story_url}\n\n{content}\n\n---\n")
        except Exception as e:
            print(f"Error fetching {story_url}: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
