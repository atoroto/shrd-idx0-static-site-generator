import unittest

from extract_title import MissingTitleError, extract_title


class TestExtractTitle(unittest.TestCase):
    def test_simple_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_strips_extra_whitespace(self):
        self.assertEqual(extract_title("#   Hello World   "), "Hello World")

    def test_title_among_other_lines(self):
        md = """
Some intro text

# The Real Title

More content below
"""
        self.assertEqual(extract_title(md), "The Real Title")

    def test_ignores_h2_and_deeper_headers(self):
        md = """
## Not this one
### Also not this one
# This one
"""
        self.assertEqual(extract_title(md), "This one")

    def test_uses_first_h1_when_multiple_present(self):
        md = "# First Title\n# Second Title"
        self.assertEqual(extract_title(md), "First Title")

    def test_raises_when_no_h1_present(self):
        with self.assertRaises(MissingTitleError):
            extract_title("## Only an h2\nSome text")

    def test_raises_on_empty_string(self):
        with self.assertRaises(MissingTitleError):
            extract_title("")


if __name__ == "__main__":
    unittest.main()
