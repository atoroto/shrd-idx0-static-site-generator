from extract_markdown_links import extract_markdown_links
from textnode import TextNode, TextType


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    res: list[TextNode] = []
    for n in old_nodes:
        if n.text_type != TextType.TEXT:
            res.append(n)
            continue

        links = extract_markdown_links(n.text)
        if not links:
            if n.text != "":
                res.append(n)
            continue

        remaining_text = n.text
        for anchor, url in links:
            before, remaining_text = remaining_text.split(f"[{anchor}]({url})", 1)
            if before != "":
                res.append(TextNode(before, TextType.TEXT))
            res.append(TextNode(anchor, TextType.LINK, url))

        if remaining_text != "":
            res.append(TextNode(remaining_text, TextType.TEXT))

    return res
