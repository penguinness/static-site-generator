import unittest
from htmlnode import ParentNode, LeafNode

from markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHTMLNode(unittest.TestCase):
    maxDiff = None

    def test_markdown_to_html_node(self):
        markdown = """
        # Heading 1

        ## Heading 2

        This is the first paragraph.

        This is the second paragraph.

        > This is a blockquote.
        > This is another blockquote.
        > This is another blockquote.

        1. First item in ordered list
        2. Second item in ordered list
        3. Third item in ordered list

        - First item in unordered list
        - Second item in unordered list
        - Third item in ordered list
        """
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><h2>Heading 2</h2><p>This is the first paragraph.</p><p>This is the second paragraph.</p><blockquote>This is a blockquote. This is another blockquote. This is another blockquote.</blockquote><ol><li>First item in ordered list</li><li>Second item in ordered list</li><li>Third item in ordered list</li></ol><ul><li>First item in unordered list</li><li>Second item in unordered list</li><li>Third item in ordered list</li></ul></div>",
        )

    def test_markdown_to_html_node2(self):
        markdown = """
        This is a code block

        ```
        {
            "firstName": "John",
            "lastName": "Smith",
            "age": 25
        }
        ```        
        """
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(
            html,
            """<div><p>This is a code block</p><pre><code>        {
            "firstName": "John",
            "lastName": "Smith",
            "age": 25
        }
        </code></pre></div>""",
        )

    def test_markdown_to_html_node3(self):
        markdown = """
        This is **bolded** paragraph
        text in a p
        tag here
        """
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_lists(self):
        md = """
        - This is a list
        - with items
        - and *more* items

        1. This is an `ordered` list
        2. with items
        3. and more items
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )
