import unittest

from split_nodes_link import split_nodes_link
from textnode import TextNode, TextType


class TestSplitNodesLink(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube",
                    TextType.LINK,
                    "https://www.youtube.com/@bootdotdev",
                ),
            ],
            new_nodes,
        )

    def test_single_link(self):
        node = TextNode("A link [here](https://example.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("A link ", TextType.TEXT),
                TextNode("here", TextType.LINK, "https://example.com"),
            ],
            new_nodes,
        )

    def test_link_at_start(self):
        node = TextNode("[here](https://example.com) at the start", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("here", TextType.LINK, "https://example.com"),
                TextNode(" at the start", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_entire_text_is_link(self):
        node = TextNode("[here](https://example.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [TextNode("here", TextType.LINK, "https://example.com")], new_nodes
        )

    def test_no_link_present(self):
        node = TextNode("just plain text", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([TextNode("just plain text", TextType.TEXT)], new_nodes)

    def test_non_text_node_passed_through_unchanged(self):
        node = TextNode("already bold", TextType.BOLD)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([TextNode("already bold", TextType.BOLD)], new_nodes)

    def test_image_is_not_treated_as_link(self):
        node = TextNode(
            "This is an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode(
                    "This is an ![image](https://i.imgur.com/zjjcJKZ.png)",
                    TextType.TEXT,
                )
            ],
            new_nodes,
        )

    def test_empty_text_node(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([], new_nodes)

    def test_empty_old_nodes_list(self):
        new_nodes = split_nodes_link([])
        self.assertListEqual([], new_nodes)

    def test_multiple_input_nodes_mixed_types(self):
        nodes = [
            TextNode("A [link](https://example.com/a) here", TextType.TEXT),
            TextNode("already italic", TextType.ITALIC),
            TextNode("Another [link](https://example.com/b)", TextType.TEXT),
        ]
        new_nodes = split_nodes_link(nodes)
        self.assertListEqual(
            [
                TextNode("A ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com/a"),
                TextNode(" here", TextType.TEXT),
                TextNode("already italic", TextType.ITALIC),
                TextNode("Another ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com/b"),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
