import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode(None, "Hi! I am penguinness.")
        self.assertEqual(node.to_html(), "Hi! I am penguinness.")

    def test_to_html2(self):
        node = LeafNode("p", "Hi! I am penguinness.")
        self.assertEqual(node.to_html(), "<p>Hi! I am penguinness.</p>")

    def test_to_html3(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )


if __name__ == "__main__":
    unittest.main()
