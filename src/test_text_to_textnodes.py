import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode


class TestTextToTextnodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![penguin image](https://www.penguin.com/wp-content/uploads/2021/05/logo-sm-view.gif) and a [link](https://khanacademy.org)"
        new_nodes = text_to_textnodes(text)
        test_nodes = [
            TextNode("This is ", "text"),
            TextNode("text", "bold"),
            TextNode(" with an ", "text"),
            TextNode("italic", "italic"),
            TextNode(" word and a ", "text"),
            TextNode("code block", "code"),
            TextNode(" and an ", "text"),
            TextNode(
                "penguin image",
                "image",
                "https://www.penguin.com/wp-content/uploads/2021/05/logo-sm-view.gif",
            ),
            TextNode(" and a ", "text"),
            TextNode("link", "link", "https://khanacademy.org"),
        ]
        self.assertEqual(new_nodes, test_nodes)
