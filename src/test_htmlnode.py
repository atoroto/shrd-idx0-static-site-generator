import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_great_grandchildren(self):
        great_grandchild_node = LeafNode("i", "great-grandchild")
        grandchild_node = ParentNode("b", [great_grandchild_node])
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b><i>great-grandchild</i></b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        parent_node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            parent_node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_to_html_with_multiple_parent_children(self):
        parent_node = ParentNode(
            "div",
            [
                ParentNode("span", [LeafNode("b", "first")]),
                ParentNode("span", [LeafNode("i", "second")]),
            ],
        )
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>first</b></span><span><i>second</i></span></div>",
        )

    def test_to_html_with_props(self):
        parent_node = ParentNode(
            "div",
            [LeafNode("span", "child")],
            props={"class": "container"},
        )
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container"><span>child</span></div>',
        )

    def test_to_html_no_children_raises(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_children_none_raises(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_no_tag_raises(self):
        parent_node = ParentNode(None, [LeafNode("span", "child")])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_child_missing_value_raises(self):
        parent_node = ParentNode("div", [LeafNode("span", "")])
        with self.assertRaises(ValueError):
            parent_node.to_html()


if __name__ == "__main__":
    unittest.main()
