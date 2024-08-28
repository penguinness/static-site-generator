import re

from textnode import TextNode


def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type == "text":
            parts = re.split(r"(?<!!)\[(.*?)\]\((.*?)\)", node.text)
            print(parts)
            for i, part in enumerate(parts):
                if i % 3 == 0 and part:
                    new_nodes.append(TextNode(part, "text"))
                elif i % 3 == 1:
                    new_nodes.append(TextNode(part, "link", parts[i + 1]))
                elif i % 3 == 2:
                    pass
        else:
            new_nodes.append(node)
    return new_nodes
