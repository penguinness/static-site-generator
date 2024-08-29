import os
import shutil

from copystatic import copy_files_recursive

from generate_page import generate_page

from generate_pages_recursive import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    # 1. Delete public directory if exists
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    # 2. Copy files from static to public
    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    # 3. Generate a page by copying from markdown_path using template_path and writing it to dest_path
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)


main()
