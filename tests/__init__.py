"""Test package global helpers"""

from pathlib import Path

__all__ = ["show_path"]

def show_path(title, path, relative_to=Path.cwd(), prefix=""):
    """Prints "title: pretty_path", and returns pretty_path
       pretty_path is path relative to relative_to (default: working directory),
       with optional prefix"""

    path = Path(path).resolve()

    if relative_to:
        path = path.relative_to(Path(relative_to).resolve())

    path_text = f"{prefix}{path}"

    print(f"{title}: {path_text}")

    return path_text

