import os

# --------------------------
# CONFIGURATION
# --------------------------
IGNORE_FOLDERS = {
    "__pycache__",
    ".git",
    ".github",
    ".ruff_cache",
    ".venv",
    ".vscode",
}

# File extensions you WANT to show (Python scripts)
ALLOWED_EXTENSIONS = {".py", ".yml", ".md"}

project_name = os.path.basename(os.getcwd())

# --------------------------
# TREE FUNCTION
# --------------------------
def tree(path=".", prefix=""):
    items = []
    for name in os.listdir(path):
        full_path = os.path.join(path, name)

        # Ignore folders you don't want
        if os.path.isdir(full_path) and name in IGNORE_FOLDERS:
            continue

        # Only show folders + allowed file types
        if os.path.isfile(full_path):
            ext = os.path.splitext(name)[1]
            if ext not in ALLOWED_EXTENSIONS:
                continue  # Skip data files, images, etc.

        items.append(name)

    # Sort so folders appear before files
    items.sort(key=lambda x: (not os.path.isdir(os.path.join(path, x)), x))

    # Tree drawing
    pointers = ["├── "] * (len(items) - 1) + ["└── "] if items else []
    for pointer, name in zip(pointers, items):
        full_path = os.path.join(path, name)
        print(prefix + pointer + name)

        # Recurse into directories
        if os.path.isdir(full_path):
            extension = "│   " if pointer == "├── " else "    "
            tree(full_path, prefix + extension)


# Art by Joan Stark (Spunk): https://asciiart.website/artist.php?artist_id=4&page=1
def ascii_header():
    project = os.path.basename(os.getcwd())

    ascii_lines = [
        "  .-'- -.",
        " (  ó    )",
        "(  ,    ó )",
        " ( \'./  .'",
        "  '-| |-'",
        "    | |",
        "    |.|"
    ]


    max_width = max(len(line) for line in ascii_lines)
    project_center = len(project) // 2
    art_center = max_width // 2
    shift = project_center - art_center
    padded_ascii = [(" " * shift) + line for line in ascii_lines]
    separator = "-" * len(project)

    return "\n".join(padded_ascii) + "\n" + project + "\n" + separator




# --------------------------
# RUN
# --------------------------
if __name__ == "__main__":
    print(ascii_header())
    tree(".")
