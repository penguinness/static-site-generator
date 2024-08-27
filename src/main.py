from textnode import TextNode


def main():
    node = TextNode(
        "This is a text node",
        "bold",
        "https://github.com/penguinness/static-site-generator",
    )
    print(repr(node))


main()
