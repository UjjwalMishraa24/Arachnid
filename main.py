import sys
import requests
from crawl import normalize_url , get_heading_from_html , get_urls_from_html , get_images_from_html, extract_page_data
from bs4 import BeautifulSoup

# this function takes CLI arguments and mentions the file that ran the the second argument with it.
def main():
    if (len(sys.argv) == 2):
        print("Hello from web-scraper!")
        print(f"Script name: {sys.argv[0]}")
        # print(f"Argument: {sys.argv[1]}")
        print(f"starting crawl at: {sys.argv[1]}")
        html = get_html(sys.argv[1])
        soup = BeautifulSoup(html, 'html.parser')
        print(soup.prettify())
        crwaled_data = crawl_page(sys.argv[1])
        print(crwaled_data)


        
        sys.exit(0)        
    elif (len(sys.argv) < 2):
        print("too few arguments, NO website provided")
        sys.exit(1)
    else:
        print("too many arguments")
        sys.exit(1)
        
# this function takes a url and returns the html content of the page.
def get_html(url):
    try:
        response = requests.get(url , headers={'User-Agent': 'Brave/1.0'})
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        
  # r = requests.get("https://github.com/UjjwalMishraa24")
# print(r.text)




"""
this whole code below is about whether page's other urls are visited ot not
but am thinking that what if i just give it the direct page url that only 
needs to be parsed and not the whole linking  pages through the urls
"""

# below is my hAalfblood prince attempt to apply recusion in the crawl page.

# def crawl_page(base_url, current_url=None, page_data=None):

#         if (current_url == base_url or 
#             current_url == None or 
#             page_data != None or 
#             normalize_url(current_url) in page_data.keys()):
#             return page_data
        
#         else:
#             html = get_html(current_url)
#             print(html)
#             page_data = extract_page_data(normalize_url(current_url), html)



# below its written by cluade code but i ran and reviewed it thoroughly.
def crawl_page(base_url, current_url=None, page_data=None):
    if current_url is None:
        current_url = base_url
    if page_data is None:
        page_data = {}

    current_url_normalized = normalize_url(current_url)

    if current_url_normalized in page_data.keys():
        return page_data  # already crawled, avoid infinite recursion

    html = get_html(current_url)
    if html is None:
        return page_data  # request failed, nothing to add

    page_data[current_url_normalized] = extract_page_data(current_url_normalized, html)

    next_urls = get_urls_from_html(html, base_url)
    for next_url in next_urls:
        page_data = crawl_page(base_url, next_url, page_data)

    return page_data


































































if __name__ == "__main__":
    main()
