import os

from extract_title import extract_title
from markdown_to_html_node import markdown_to_html_node


def generate_page(
    from_path: str, template_path: str, dest_path: str, basepath: str = "/"
) -> None:
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
    full_html = full_html.replace('href="/', f'href="{basepath}').replace(
        'src="/', f'src="{basepath}'
    )

    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(full_html)


def generate_pages_recursive(
    content_dir_path: str,
    template_path: str,
    dest_dir_path: str,
    basepath: str = "/",
) -> None:
    for entry in os.listdir(content_dir_path):
        from_path = os.path.join(content_dir_path, entry)
        dest_path = os.path.join(dest_dir_path, entry)

        if os.path.isdir(from_path):
            generate_pages_recursive(from_path, template_path, dest_path, basepath)
        elif entry.endswith(".md"):
            dest_path = os.path.join(
                dest_dir_path, entry.removesuffix(".md") + ".html"
            )
            generate_page(from_path, template_path, dest_path, basepath)
