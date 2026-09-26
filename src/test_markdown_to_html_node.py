import unittest

from markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading(self):
        md = "## This is a **heading**"

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>This is a <b>heading</b></h2></div>",
        )

    def test_quote(self):
        md = """
> This is a quote
> that spans _two_ lines
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote that spans <i>two</i> lines</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- This is a list
- with items
- and _more_ items
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. This is an ordered list
2. with items
3. and _more_ items
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is an ordered list</li><li>with items</li><li>and <i>more</i> items</li></ol></div>",
        )

    def test_multiple_blocks(self):
        md = """
# Header

Paragraph with **bold** text

> A quote block

- item one
- item two
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Header</h1><p>Paragraph with <b>bold</b> text</p><blockquote>A quote block</blockquote><ul><li>item one</li><li>item two</li></ul></div>",
        )


if __name__ == "__main__":
    unittest.main()
