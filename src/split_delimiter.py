from textnode import TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type == "text":
            parts = node.text.split(delimiter)
            for i, part in enumerate(parts):
                if i % 2 != 0:
                    new_nodes.append(TextNode(part, text_type))
                else:
                    new_nodes.append(TextNode(part, "text"))
        else:
            new_nodes.append(node)
    return new_nodes
