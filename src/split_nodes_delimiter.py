from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    res: list[TextNode] = []
    for n in old_nodes:
        if n.text_type != TextType.TEXT:
            res.append(n)
            continue

        parts = n.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError(
                f"invalid markdown: no closing delimiter found for '{delimiter}'"
            )

        for i, part in enumerate(parts):
            if part == "":
                continue
            if i % 2 == 0:
                res.append(TextNode(part, TextType.TEXT))
            else:
                res.append(TextNode(part, text_type))

    return res
