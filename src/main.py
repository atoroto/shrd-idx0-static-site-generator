from copystatic import copy_static_to_public

STATIC_DIR = "static"
PUBLIC_DIR = "public"


def main():
    copy_static_to_public(STATIC_DIR, PUBLIC_DIR)


if __name__ == "__main__":
    main()
