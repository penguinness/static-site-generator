import unittest

from textnode import TextNode

from split_delimiter import split_nodes_delimiter


class TestSplitDelimiter(unittest.TestCase):
    def test_split_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        test_nodes = [
            TextNode("This is text with a ", "text"),
            TextNode("code block", "code"),
            TextNode(" word", "text"),
        ]
        self.assertEqual(new_nodes, test_nodes)

    def test_split_delimiter_bold(self):
        node = TextNode("This is text with a **bold block** word", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        test_nodes = [
            TextNode("This is text with a ", "text"),
            TextNode("bold block", "bold"),
            TextNode(" word", "text"),
        ]
        self.assertEqual(new_nodes, test_nodes)

    def test_split_delimiter_italic(self):
        node = TextNode("This is text with a *italic block* word", "text")
        new_nodes = split_nodes_delimiter([node], "*", "italic")
        test_nodes = [
            TextNode("This is text with a ", "text"),
            TextNode("italic block", "italic"),
            TextNode(" word", "text"),
        ]
        self.assertEqual(new_nodes, test_nodes)
