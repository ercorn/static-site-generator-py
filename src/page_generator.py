from block_markdown import markdown_to_html_node
import os

def extract_title(markdown):
    for line in markdown.split("\n"):
        if line[:2] == "# ":
            return line[2:].strip()
    raise ValueError("No h1 header found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating path from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as markdown_file:
        markdown = markdown_file.read()
    with open(template_path) as template_file:
        template = template_file.read()
    
    html_string = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    print(f"Title: {title}")
    final_html = template.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html_string)
    
    print(f"Dest Dirname: {os.path.dirname(dest_path)}")

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    
    
    with open(dest_path, "w") as index_file:
        index_file.write(final_html)

