import unittest
from textnode import TextNode
from htmlnode import LeafNode
from text_to_html import text_node_to_html_node


class TestTextToHTML(unittest.TestCase):
    def test_text_to_html_text(self):
        text_node = TextNode("Pingu", "text")
        html_node = text_node_to_html_node(text_node)
        test_node = LeafNode(None, "Pingu")
        self.assertEqual(html_node, test_node)

    def test_text_to_html_bold(self):
        text_node = TextNode("Pingu", "bold")
        html_node = text_node_to_html_node(text_node)
        test_node = LeafNode("b", "Pingu")
        self.assertEqual(html_node, test_node)

    def test_text_to_html_italic(self):
        text_node = TextNode("Pingu", "italic")
        html_node = text_node_to_html_node(text_node)
        test_node = LeafNode("i", "Pingu")
        self.assertEqual(html_node, test_node)

    def test_text_to_html_code(self):
        text_node = TextNode("Pingu", "code")
        html_node = text_node_to_html_node(text_node)
        test_node = LeafNode("code", "Pingu")
        self.assertEqual(html_node, test_node)

    def test_text_to_html_link(self):
        text_node = TextNode("Pingu", "link", "https://www.penguin.com/")
        html_node = text_node_to_html_node(text_node)
        test_node = LeafNode("a", "Pingu", {"href": "https://www.penguin.com/"})
        self.assertEqual(html_node, test_node)

    def test_text_to_html_image(self):
        text_node = TextNode(
            "Pingu",
            "image",
            "https://www.penguin.com/wp-content/uploads/2021/05/logo-sm-view.gif",
        )
        html_node = text_node_to_html_node(text_node)
        test_node = LeafNode(
            "img",
            "",
            {
                "src": "https://www.penguin.com/wp-content/uploads/2021/05/logo-sm-view.gif",
                "alt": "Pingu",
            },
        )
        self.assertEqual(html_node, test_node)

    def test_text_to_html_error(self):
        text_node = TextNode("err", "error")
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node)
