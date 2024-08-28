import unittest

from htmlnode import ParentNode

from htmlnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_to_html2(self):
        node = ParentNode(
            None,
            [
                LeafNode("b", "Bold text"),
            ],
        )
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html3(self):
        node = ParentNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
