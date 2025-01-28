from textnode import *
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("No closing delimiter found")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    images = re.findall(r"\!\[(.*?)\]\((.*?)\)", text)
    return images

def extract_markdown_links(text):
    images = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return images

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = re.split(r"(!.*?\))", old_node.text)
        if len(sections) % 2 == 0:
            raise ValueError("No closing delimiter found")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                image_alt, image_link = extract_markdown_images(sections[i])[0]
                split_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = re.split(r"(\[.*?\))", old_node.text)
        if len(sections) % 2 == 0:
            raise ValueError("No closing delimiter found")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                alt, link = extract_markdown_links(sections[i])[0]
                split_nodes.append(TextNode(alt, TextType.LINK, link))
        new_nodes.extend(split_nodes)
    return new_nodes

def text_to_textnodes(text):
    old_nodes = [TextNode(text, TextType.TEXT)]
    new_nodes = split_nodes_delimiter(old_nodes, "**", "bold")
    new_nodes = split_nodes_delimiter(new_nodes, "*", "italic")
    new_nodes = split_nodes_delimiter(new_nodes, "`", "code")
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes