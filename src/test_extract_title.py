import unittest

from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
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
        title = extract_title(markdown)
        self.assertEqual(title, "Heading 1")
