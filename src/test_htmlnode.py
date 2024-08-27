import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "h1",
            None,
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        result = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), result)

    def test_values(self):
        node = HTMLNode("div", "I believe in backend supremacy")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "I believe in backend supremacy")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_init(self):
        node = HTMLNode(
            "div", "I believe in backend supremacy", None, {"class": "opinion"}
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(div, I believe in backend supremacy, None, {'class': 'opinion'})",
        )


if __name__ == "__main__":
    unittest.main()
