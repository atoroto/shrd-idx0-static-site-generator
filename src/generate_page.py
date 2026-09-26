import os

from extract_title import extract_title
from markdown_to_html_node import markdown_to_html_node


def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f:
        markdown_content = f.read()

    with open(template_path) as f:
        template_content = f.read()

    title = extract_title(markdown_content)
    html_content = markdown_to_html_node(markdown_content).to_html()

    full_html = template_content.replace("{{ Title }}", title).replace(
        "{{ Content }}", html_content
    )

    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(full_html)
