
from urllib.parse import urlsplit, urljoin
from bs4 import BeautifulSoup, Tag


# for getting url in a normal form.
def normalize_url(url):
    url_parts = urlsplit(url)
    netloc = url_parts.netloc
    path = url_parts.path
    normalized_url = netloc + path
    return normalized_url

# print(normalize_url("https://www.youtube.com/watch?v=QDia3e12czc"))


# for getting the content of the html tags like h1, h2, and p.
def get_heading_from_html(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    para = soup.find_all("p")
    h1 = soup.find_all("h1")
    h2 = soup.find_all("h2")
    paragraphs = [p.get_text() for p in para]
    h1s = [h.get_text() for h in h1]
    h2s = [h.get_text() for h in h2]
    return paragraphs, h1s, h2s


# for getting the urls from the html body and normalise them to absolute urls
def get_urls_from_html(html: str, base_url: str) -> list:
        soup = BeautifulSoup(html, "html.parser")
        link =  soup.find_all("a")
        urls = []
        for l in link:
            href = l.get("href")
            if href:
                urls.append(urljoin(base_url, href))
        return urls


# for getting the image urls from the html body and normalise them to absolute urls
def get_images_from_html(html :str, base_url : str) -> list:
    soup = BeautifulSoup(html, "html.parser")
    image =soup.find_all("img")
    images = []
    for i in image:
        src = i.get("src")
        if src:
            images.append(urljoin(base_url, src))
    return images

# all data combined to see as a result till now.
def extract_page_data(html: str, page_url: str) -> dict:
    page_data = {
        "url": normalize_url(page_url),
        "content of page": get_heading_from_html(html),
        "outgoing urls": get_urls_from_html(html, page_url),
        "image urls": get_images_from_html(html, page_url)
    }
    return page_data

# input_url = "https://crawler-test.com"
# input_body = '''<html><body>
#         <h1>Test Title</h1>
#         <p>This is the first paragraph.</p>
#         <a href="/link1">Link 1</a>
#         <img src="/image1.jpg" alt="Image 1">
#     </body></html>'''

# print(extract_page_data(input_body, input_url))

