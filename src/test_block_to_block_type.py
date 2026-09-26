import unittest

from block_to_block_type import BlockType, block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    def test_heading_level_1(self):
        self.assertEqual(block_to_block_type("# heading"), BlockType.HEADING)

    def test_heading_level_6(self):
        self.assertEqual(block_to_block_type("###### heading"), BlockType.HEADING)

    def test_heading_without_space_is_paragraph(self):
        self.assertEqual(block_to_block_type("#heading"), BlockType.PARAGRAPH)

    def test_heading_with_seven_hashes_is_paragraph(self):
        self.assertEqual(block_to_block_type("####### heading"), BlockType.PARAGRAPH)

    def test_code_block(self):
        block = "```\ncode here\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_code_block_missing_closing_backticks_is_paragraph(self):
        block = "```\ncode here"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_code_block_missing_opening_newline_is_paragraph(self):
        block = "```code here\n```"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_quote_single_line(self):
        self.assertEqual(block_to_block_type("> a quote"), BlockType.QUOTE)

    def test_quote_multiline(self):
        block = "> line one\n> line two\n>line three"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_quote_with_non_quote_line_is_paragraph(self):
        block = "> line one\nnot a quote line"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_unordered_list_single_item(self):
        self.assertEqual(block_to_block_type("- item one"), BlockType.UNORDERED_LIST)

    def test_unordered_list_multiline(self):
        block = "- item one\n- item two\n- item three"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_unordered_list_missing_space_is_paragraph(self):
        block = "-item one\n- item two"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_single_item(self):
        self.assertEqual(block_to_block_type("1. item one"), BlockType.ORDERED_LIST)

    def test_ordered_list_multiline(self):
        block = "1. item one\n2. item two\n3. item three"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_ordered_list_not_starting_at_one_is_paragraph(self):
        block = "2. item one\n3. item two"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_skipped_number_is_paragraph(self):
        block = "1. item one\n3. item two"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_missing_space_is_paragraph(self):
        block = "1.item one"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_plain_paragraph(self):
        block = "This is just a regular paragraph of text."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_paragraph_with_multiple_lines(self):
        block = "This is line one\nThis is line two"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
