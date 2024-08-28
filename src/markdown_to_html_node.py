from htmlnode import HTMLNode
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type
from text_to_html import text_node_to_html_node
from text_to_textnodes import text_to_textnodes
from htmlnode import ParentNode


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == "paragraph":
        return paragraph_to_html_node(block)
    if block_type == "heading":
        return heading_to_html_node(block)
    if block_type == "code":
        return code_to_html_node(block)
    if block_type == "quote":
        return quote_to_html_node(block)
    if block_type == "ordered_list":
        return olist_to_html_node(block)
    if block_type == "unordered_list":
        return ulist_to_html_node(block)
    raise ValueError("Error: Invalid block type")


def paragraph_to_html_node(block):
    lines = block.split("\n")
    lines = [line.strip() for line in lines]
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = block.count("#", 0, block.find(" "))
    heading = block[level + 1 :].strip()
    children = text_to_children(heading)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if line.lstrip().startswith("> "):
            new_lines.append(line.lstrip("> ").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = (item.lstrip())[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = (item.lstrip())[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


markdown = """
        This is **bolded** paragraph
        text in a p
        tag here
        """

node = markdown_to_html_node(markdown)

html = node.to_html()

print(html)
