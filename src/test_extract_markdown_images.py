import unittest

from extract_markdown_images import extract_markdown_images


class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) "
            "and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        self.assertListEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
            matches,
        )

    def test_extract_markdown_images_no_matches(self):
        matches = extract_markdown_images("This is text with no images at all")
        self.assertListEqual([], matches)

    def test_extract_markdown_images_empty_alt_text(self):
        matches = extract_markdown_images("An image with no alt text ![](https://example.com/x.png)")
        self.assertListEqual([("", "https://example.com/x.png")], matches)

    def test_extract_markdown_images_ignores_links(self):
        matches = extract_markdown_images(
            "This is a [link](https://www.boot.dev), not an image"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_images_mixed_with_links(self):
        matches = extract_markdown_images(
            "Here is a [link](https://www.boot.dev) and an "
            "![image](https://i.imgur.com/zjjcJKZ.png) in the same text"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_only_image_no_surrounding_text(self):
        matches = extract_markdown_images("![alone](https://example.com/alone.png)")
        self.assertListEqual([("alone", "https://example.com/alone.png")], matches)


if __name__ == "__main__":
    unittest.main()
