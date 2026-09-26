from extract_markdown_images import extract_markdown_images
from textnode import TextNode, TextType


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    res: list[TextNode] = []
    for n in old_nodes:
        if n.text_type != TextType.TEXT:
            res.append(n)
            continue

        images = extract_markdown_images(n.text)
        if not images:
            if n.text != "":
                res.append(n)
            continue

        remaining_text = n.text
        for alt, url in images:
            before, remaining_text = remaining_text.split(f"![{alt}]({url})", 1)
            if before != "":
                res.append(TextNode(before, TextType.TEXT))
            res.append(TextNode(alt, TextType.IMAGE, url))

        if remaining_text != "":
            res.append(TextNode(remaining_text, TextType.TEXT))

    return res
