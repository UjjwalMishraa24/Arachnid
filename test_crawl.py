import unittest
from crawl import normalize_url , get_heading_from_html , get_urls_from_html , get_images_from_html, extract_page_data
class TestCrawl(unittest.TestCase):


# test for normalising similar urls  
    def test_normalize_url(self):
        input_url = "https://www.youtube.com/watch?v=QDia3e12czc"
        actual = normalize_url(input_url)
        expected = "www.youtube.com/watch"
        self.assertEqual(actual, expected)


# written to get the content of the html tags like h1, h2, and p.
    def test_html_parsing(self):
        html = '''<!DOCTYPE html>
        <html>
        <head>
        <title>Page Title</title>
        </head>
        <body>

        <h1>This is a Heading</h1>
        <p>This is a paragraph.</p>

        </body>
        </html>'''
        actual = get_heading_from_html(html)
        expected = (['This is a paragraph.'], ['This is a Heading'], [])
        self.assertEqual(actual, expected)
        
# 2 below tests are below for absolute and relative url parse.
    def test_get_urls_from_html_absolute(self):
        input_url = "https://crawler-test.com"
        input_body = '<html><body><a href="https://crawler-test.com"><span>Boot.dev</span></a></body></html>'
        actual = get_urls_from_html(input_body, input_url)
        expected = ["https://crawler-test.com"]
        self.assertEqual(actual, expected)

    def test_get_urls_from_html_relative(self):
        input_url = "https://crawler-test.com"
        input_body = '<html><body><a href="/"><span>Boot.dev</span></a></body></html>'
        actual = get_urls_from_html(input_body, input_url)
        expected = ["https://crawler-test.com/"]
        self.assertEqual(actual, expected)

# 2 below tests are for absolute and relative image url parse.
    def test_get_images_from_html_relative(self):
        input_url = "https://crawler-test.com"
        input_body = '<html><body><img src="/logo.png" alt="Logo"></body></html>'
        actual = get_images_from_html(input_body, input_url)
        expected = ["https://crawler-test.com/logo.png"]
        self.assertEqual(actual, expected)

    def test_get_images_from_html_absolute(self):
        input_url = "https://crawler-test.com"
        input_body = '<html><body><img src="https://crawler-test.com/logo.png" alt="Logo"></body></html>'
        actual = get_images_from_html(input_body, input_url)
        expected = ["https://crawler-test.com/logo.png"]
        self.assertEqual(actual, expected)



    # def test_extract_page_data_basic(self):
    #     input_url = "https://crawler-test.com"
    #     input_body = '''<html><body>
    #         <h1>Test Title</h1>
    #         <p>This is the first paragraph.</p>
    #         <a href="/link1">Link 1</a>
    #         <img src="/image1.jpg" alt="Image 1">
    #     </body></html>'''
    #     actual = extract_page_data(input_body, input_url)
    #     expected = {
    #         "url": "https://crawler-test.com",
    #         "heading": "Test Title",
    #         "content of page": ("This is the first paragraph.", ["Test Title"], []),
    #         "outgoing urls": ["https://crawler-test.com/link1"],
    #         "image urls": ["https://crawler-test.com/image1.jpg"]
    #     }
    #     self.assertEqual(actual, expected)

























if __name__ == "__main__":
    unittest.main()