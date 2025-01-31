from textnode import *
from htmlnode import *

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"



def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return "heading"
    
    if block.startswith("```") and block.endswith("```"):
        return "code"
    
    block_lines = block.split("\n")
    
    if block_lines[0].startswith(">"):
        for line in block_lines:
            if line.startswith(">"):
                continue
            else:
                return "paragraph"
        return "quote"
    
    if block_lines[0].startswith(("* ", "- ")):
        for line in block_lines:
            if line.startswith(("* ", "- ")):
                continue
            else:
                return "paragraph"
        return "unordered_list"
    
    if block_lines[0].startswith("1. "):
        for i in range(len(block_lines)):
            num_line = i + 1
            if int(block_lines[i][0]) == num_line and block_lines[i].startswith(f"{num_line}. "):
                continue
            else:
                return "paragraph"
        return "ordered_list"


    return "paragraph"

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
