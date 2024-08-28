import unittest
from extract_markdown_images import extract_markdown_images
from extract_markdown_links import extract_markdown_links


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(
            extract_markdown_images(text),
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
        )

    def test_extract_markdown_links(self):
        text = text = (
            "This is text with a link [to khan academy](https://www.khanacademy.org/) and [to youtube](https://www.youtube.com/@khanacademy)"
        )
        self.assertEqual(
            extract_markdown_links(text),
            [
                ("to khan academy", "https://www.khanacademy.org/"),
                ("to youtube", "https://www.youtube.com/@khanacademy"),
            ],
        )
