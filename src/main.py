from textnode import TextNode
from htmlnode import *

def main():
    dummy_textnode = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(dummy_textnode)

    children_list = [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
        ParentNode("p", [
            LeafNode("a", "Click me!", {"href": "https://www.boot.dev"})
        ])
    ]

    to_html_children_str = "".join(map(lambda node: node.to_html(), children_list))
    print(to_html_children_str)
    print(children_list[-1])


if __name__ == "__main__":
    main()
