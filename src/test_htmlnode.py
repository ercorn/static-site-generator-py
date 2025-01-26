import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode()
        self.assertRaises(NotImplementedError, lambda: node.to_html())

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(' href="https://www.google.com" target="_blank"', node.props_to_html())

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        leaf_node = LeafNode("p", "What a strange world", {"class": "primary"},)
        parent_node = ParentNode("p", [
            LeafNode("a", "Click me!", {"href": "https://www.boot.dev"})
        ])

        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )
        self.assertEqual(
            leaf_node.__repr__(),
            "LeafNode(p, What a strange world, {'class': 'primary'})",
        )
        self.assertEqual(
            parent_node.__repr__(),
            "ParentNode(p, children: [LeafNode(a, Click me!, {'href': 'https://www.boot.dev'})], None)",
        )

    def test_values(self):
        node = HTMLNode("div", "I wish I could read")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "I wish I could read")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_to_html_no_children(self):
        node = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual("<p>This is a paragraph of text.</p>", node.to_html())
        self.assertEqual('<a href="https://www.google.com">Click me!</a>', node2.to_html())

    def test_values_no_children(self):
        node = LeafNode("div", "I wish I could read")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "I wish I could read")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_parent_to_html_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_parent_no_children(self):
        node = ParentNode("p", None)
        node2 = ParentNode("a", [], {"href": "https://www.boot.dev"})
        self.assertRaises(ValueError, lambda: node.to_html())
        self.assertRaises(ValueError, lambda: node2.to_html())

    def test_parent_nested_parent(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ParentNode("p", [
                    LeafNode("a", "Click me!", {"href": "https://www.boot.dev"})
                ])
            ],
        )
        self.assertEqual(node.to_html(),
            '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<p><a href="https://www.boot.dev">Click me!</a></p></p>'
            )
        
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()
