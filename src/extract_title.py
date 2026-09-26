class MissingTitleError(Exception):
    pass


def extract_title(markdown: str) -> str:
    h1_lines = [line for line in markdown.split("\n") if line.startswith("# ")]
    if not h1_lines:
        raise MissingTitleError("no h1 header found")
    return h1_lines[0][2:].strip()
