import unittest
from crawl import normalize_url , get_heading_from_html

class TestCrawl(unittest.TestCase):
    def test_normalize_url(self):
        input_url = "https://www.youtube.com/watch?v=QDia3e12czc"
        actual = normalize_url(input_url)
        expected = "www.youtube.com/watch"
        self.assertEqual(actual, expected)


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

if __name__ == "__main__":
    unittest.main()