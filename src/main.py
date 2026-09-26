import os

from copystatic import copy_static_to_public
from generate_page import generate_page

STATIC_DIR = "static"
PUBLIC_DIR = "public"
CONTENT_DIR = "content"
TEMPLATE_PATH = "template.html"


def main():
    copy_static_to_public(STATIC_DIR, PUBLIC_DIR)
    generate_page(
        os.path.join(CONTENT_DIR, "index.md"),
        TEMPLATE_PATH,
        os.path.join(PUBLIC_DIR, "index.html"),
    )


if __name__ == "__main__":
    main()
