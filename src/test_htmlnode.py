import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_no_props(self):
        node = HTMLNode("p", "This is a paragraph")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_one_prop(self):
        node = HTMLNode("a", "Click me", props={"href": "https://www.boot.dev"})
        self.assertEqual(node.props_to_html(), ' href="https://www.boot.dev"')

    def test_props_to_html_multiple_props(self):
        node = HTMLNode(
            "a",
            "Click me",
            props={"href": "https://www.boot.dev", "target": "_blank"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.boot.dev" target="_blank"',
        )

    def test_values(self):
        node = HTMLNode(
            "p",
            "This is a paragraph",
            children=None,
            props={"class": "primary"},
        )
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is a paragraph")
        self.assertIsNone(node.children)
        self.assertEqual(node.props, {"class": "primary"})

    def test_repr(self):
        node = HTMLNode("p", "This is a paragraph", None, {"class": "primary"})
        node_repr = repr(node)
        self.assertIn("HTMLNode", node_repr)
        self.assertIn("p", node_repr)
        self.assertIn("This is a paragraph", node_repr)
        self.assertIn("primary", node_repr)

    def test_to_html_not_implemented(self):
        node = HTMLNode("p", "This is a paragraph")
        with self.assertRaises(NotImplementedError):
            node.to_html()


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me", props={"href": "https://www.boot.dev"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.boot.dev">Click me</a>'
        )

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "This is a heading")
        self.assertEqual(node.to_html(), "<h1>This is a heading</h1>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just raw text")
        self.assertEqual(node.to_html(), "Just raw text")

    def test_leaf_to_html_no_value_raises(self):
        node = LeafNode("p", "")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_repr(self):
        node = LeafNode("a", "Click me", props={"href": "https://www.boot.dev"})
        node_repr = repr(node)
        self.assertIn("LeafNode", node_repr)
        self.assertIn("a", node_repr)
        self.assertIn("Click me", node_repr)
        self.assertIn("boot.dev", node_repr)
        self.assertNotIn("children", node_repr)


if __name__ == "__main__":
    unittest.main()
