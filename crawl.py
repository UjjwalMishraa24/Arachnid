
from urllib.parse import urlsplit, urljoin
from bs4 import BeautifulSoup, Tag


def normalize_url(url):
    url_parts = urlsplit(url)
    netloc = url_parts.netloc
    path = url_parts.path
    normalized_url = netloc + path
    return normalized_url

print(normalize_url("https://www.youtube.com/watch?v=QDia3e12czc"))
def get_heading_from_html(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    para = soup.find_all("p")
    h1 = soup.find_all("h1")
    h2 = soup.find_all("h2")
    paragraphs = [p.get_text() for p in para]
    h1s = [h.get_text() for h in h1]
    h2s = [h.get_text() for h in h2]
    return paragraphs, h1s, h2s

