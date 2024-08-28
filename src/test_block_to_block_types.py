import unittest
from block_to_block_type import block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph_block(self):
        paragraph_block = """
        First item
        Second item
        Third item
        Fourth item
        """
        block_type = block_to_block_type(paragraph_block)
        self.assertEqual(block_type, "paragraph")

    def test_code_block(self):
        code_block = """
        ```
        {
        "firstName": "John",
        "lastName": "Smith",
        "age": 25
        }
        ```
        """
        block_type = block_to_block_type(code_block)
        self.assertEqual(block_type, "code")

    def test_heading_block1(self):
        heading_block1 = """
        # Heading 1
        """
        block_type = block_to_block_type(heading_block1)
        self.assertEqual(block_type, "heading")

    def test_heading_block6(self):
        heading_block6 = """
        ###### Heading 6
        """
        block_type = block_to_block_type(heading_block6)
        self.assertEqual(block_type, "heading")

    def test_quote_block(self):
        quote_block = """
        > This is a block quote. This
        > paragraph has two lines.
        >
        > 1. This is a list inside a block quote.
        > 2. Second item.
        """
        block_type = block_to_block_type(quote_block)
        self.assertEqual(block_type, "quote")

    def test_ordered_list_block(self):
        ordered_list_block = """
        1. First item
        2. Second item
        3. Third item
        4. Fourth item
        """
        block_type = block_to_block_type(ordered_list_block)
        self.assertEqual(block_type, "ordered_list")

    def test_unordered_list_block1(self):
        unordered_list_block1 = """
        - First item
        - Second item
        - Third item
        - Fourth item
        """
        block_type = block_to_block_type(unordered_list_block1)
        self.assertEqual(block_type, "unordered_list")

    def test_unordered_list_block2(self):
        unordered_list_block2 = """
        * First item
        * Second item
        * Third item
        * Fourth item
        """
        block_type = block_to_block_type(unordered_list_block2)
        self.assertEqual(block_type, "unordered_list")
