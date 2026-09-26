import unittest

from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_empty_string(self):
        blocks = markdown_to_blocks("")
        self.assertEqual(blocks, [])

    def test_excessive_newlines_between_blocks(self):
        md = """
This is the first block



This is the second block
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is the first block",
                "This is the second block",
            ],
        )

    def test_strips_leading_and_trailing_whitespace(self):
        md = "   \nThis is a block with leading whitespace   \n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is a block with leading whitespace"])

    def test_single_block(self):
        md = "Just one block of text"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Just one block of text"])


if __name__ == "__main__":
    unittest.main()
