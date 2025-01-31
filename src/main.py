from textnode import TextNode
from htmlnode import *
from inline_markdown import *
from block_markdown import *
import re

def main():
    #dummy_textnode = TextNode("This is a text node", "bold", "https://www.boot.dev")
    #print(dummy_textnode)

    #children_list = [
    #    LeafNode("b", "Bold text"),
    #    LeafNode(None, "Normal text"),
    #    LeafNode("i", "italic text"),
    #    LeafNode(None, "Normal text"),
    #    ParentNode("p", [
    #        LeafNode("a", "Click me!", {"href": "https://www.boot.dev"})
    #    ])
    #]

    #to_html_children_str = "".join(map(lambda node: node.to_html(), children_list))
    #print(to_html_children_str)
    #print(children_list[-1])

    #text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    #images = extract_markdown_images(text)
    #print(images)

    #text2 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    #links = extract_markdown_links(text2)
    #print(links)

    #print("===TEST SPLIT LINK/IMAGE NODES===")
    #for image in images:
     #   image_alt, image_link = image[0], image[1]
      #  print(f"alt: {image_alt} image link: {image_link}")
       # sections = text.split(f"![{image_alt}]({image_link})", 1)
        #print(sections)
    #split_link_node = re.split(r"(\[.*?\))", text)
    #print(split_link_node)

    #test_alt, test_link = extract_markdown_links(split_link_node[1])[0]
    #print(test_alt, test_link)

    #print("__________________________________________")
    #test_split_link_node = TextNode(
    #"This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
    #TextType.TEXT,
    #)
    #new_nodes = split_nodes_link([test_split_link_node])
    #print(new_nodes)

    #print("___________++++++++++_________________")
    #final_text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    #split_textnodes = text_to_textnodes(final_text)
    #print(split_textnodes)
    #print("++++++++++++++++BLOCK MARKDOWN TEST++++++++++++++++++++++++")
    #block_text = """
#This is **bolded** paragraph
#
#This is another paragraph with *italic* text and `code` here
#This is the same paragraph on a new line
#
#* This is a list
#* with items
#"""
#    print(block_text)
#    block_text_split = markdown_to_blocks(block_text)
#    print(block_text_split)

    print(block_to_block_type("###### Heading Check"))
    print(block_to_block_type("Testy"))
    print(block_to_block_type("``` Test ```"))
    print(block_to_block_type("``` Test ``"))
    print(block_to_block_type(">Test\n>Test2"))
    print(block_to_block_type(">Test\n>Test2\n-Test3"))
    print(block_to_block_type("* Test\n- Test2"))
    print(block_to_block_type("* Test\n- Test2\n*Test3"))
    print(block_to_block_type("1. Test\n2. Test2"))
    print(block_to_block_type("1. Test\n2. Test2\n4. Test3"))






if __name__ == "__main__":
    main()
