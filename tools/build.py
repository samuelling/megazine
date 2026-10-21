"""Build the GitHub Pages index.html from tools/page.html (the same file is published as the preview)."""
from pathlib import Path
root = Path(__file__).resolve().parent.parent
frag = (root / "tools" / "page.html").read_text()
html = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        + frag.replace('<header', '</head>\n<body>\n<header', 1) + '\n</body>\n</html>\n')
(root / "index.html").write_text(html)
print("wrote index.html")
