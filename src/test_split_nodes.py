import unittest
from textnode import TextNode
from split_nodes_image import split_nodes_image
from split_nodes_link import split_nodes_link


class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            "text",
        )
        new_nodes = split_nodes_image([node])
        test_nodes = [
            TextNode("This is text with a ", "text", None),
            TextNode("rick roll", "image", "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", "text", None),
            TextNode("obi wan", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertEqual(new_nodes, test_nodes)

    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to khan academy](https://www.khanacademy.org/) and [to youtube](https://www.youtube.com/@khanacademy)",
            "text",
        )
        new_nodes = split_nodes_link([node])
        test_nodes = [
            TextNode("This is text with a link ", "text", None),
            TextNode("to khan academy", "link", "https://www.khanacademy.org/"),
            TextNode(" and ", "text", None),
            TextNode("to youtube", "link", "https://www.youtube.com/@khanacademy"),
        ]
        self.assertEqual(new_nodes, test_nodes)
