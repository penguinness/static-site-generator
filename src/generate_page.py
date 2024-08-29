import os

from markdown_to_html_node import markdown_to_html_node

from extract_title import extract_title


def generate_page(from_path, template_path, dest_path):
    # 1. Print message for page generation
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # 2. Read the markdown file at from_path and store the contents in markdown_content.
    with open(from_path, "r") as f:
        markdown_content = f.read()

    # 3. Read the template file at template_path and store the contents in template_content
    with open(template_path, "r") as f:
        template_content = f.read()

    # 4. Convert the markdown file to an HTML string
    html_content = markdown_to_html_node(markdown_content).to_html()

    # 5. Extract the title of markdown_content
    title = extract_title(markdown_content)

    # 6. Replace title and content in template with the new title and content
    html_output = template_content.replace("{{ Title }}", title).replace(
        "{{ Content }}", html_content
    )

    # 7. Write html_output to a file at dest_path
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(html_output)
