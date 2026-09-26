import unittest

from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()
