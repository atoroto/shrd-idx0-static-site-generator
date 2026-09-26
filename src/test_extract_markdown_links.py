import unittest

from extract_markdown_links import extract_markdown_links


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)

    def test_extract_markdown_links_multiple(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and "
            "[to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
            matches,
        )

    def test_extract_markdown_links_no_matches(self):
        matches = extract_markdown_links("This is text with no links at all")
        self.assertListEqual([], matches)

    def test_extract_markdown_links_empty_anchor_text(self):
        matches = extract_markdown_links("A link with no anchor text [](https://example.com)")
        self.assertListEqual([("", "https://example.com")], matches)

    def test_extract_markdown_links_ignores_images(self):
        matches = extract_markdown_links(
            "This is an ![image](https://i.imgur.com/zjjcJKZ.png), not a link"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_links_mixed_with_images(self):
        matches = extract_markdown_links(
            "Here is an ![image](https://i.imgur.com/zjjcJKZ.png) and a "
            "[link](https://www.boot.dev) in the same text"
        )
        self.assertListEqual([("link", "https://www.boot.dev")], matches)

    def test_extract_markdown_links_only_link_no_surrounding_text(self):
        matches = extract_markdown_links("[alone](https://example.com/alone)")
        self.assertListEqual([("alone", "https://example.com/alone")], matches)


if __name__ == "__main__":
    unittest.main()
