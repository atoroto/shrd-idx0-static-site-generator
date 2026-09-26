from block_to_block_type import BlockType, block_to_block_type
from htmlnode import ParentNode
from markdown_to_blocks import markdown_to_blocks
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


def markdown_to_html_node(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    children = [block_to_html_node(block) for block in blocks]
    return ParentNode("div", children)


def block_to_html_node(block: str) -> ParentNode:
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    if block_type == BlockType.UNORDERED_LIST:
        return unordered_list_to_html_node(block)
    if block_type == BlockType.ORDERED_LIST:
        return ordered_list_to_html_node(block)
    raise ValueError(f"invalid block type: {block_type}")


def text_to_children(text: str) -> list:
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(text_node) for text_node in text_nodes]


def paragraph_to_html_node(block: str) -> ParentNode:
    text = " ".join(block.split("\n"))
    return ParentNode("p", text_to_children(text))


def heading_to_html_node(block: str) -> ParentNode:
    level = len(block) - len(block.lstrip("#"))
    text = block[level + 1 :]
    return ParentNode(f"h{level}", text_to_children(text))


def code_to_html_node(block: str) -> ParentNode:
    text = block[4:-3]
    code_leaf = text_node_to_html_node(TextNode(text, TextType.TEXT))
    return ParentNode("pre", [ParentNode("code", [code_leaf])])


def quote_to_html_node(block: str) -> ParentNode:
    lines = [line.lstrip(">").strip() for line in block.split("\n")]
    text = " ".join(lines)
    return ParentNode("blockquote", text_to_children(text))


def unordered_list_to_html_node(block: str) -> ParentNode:
    items = []
    for line in block.split("\n"):
        text = line[2:]
        items.append(ParentNode("li", text_to_children(text)))
    return ParentNode("ul", items)


def ordered_list_to_html_node(block: str) -> ParentNode:
    items = []
    for i, line in enumerate(block.split("\n"), start=1):
        text = line[len(f"{i}. ") :]
        items.append(ParentNode("li", text_to_children(text)))
    return ParentNode("ol", items)
