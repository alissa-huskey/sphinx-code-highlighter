from os import environ
from pathlib import Path
import re
from subprocess import run

import pytest

from . import show_path

@pytest.mark.sphinx('html', testroot="docs")
def test_sphinx(app, status, warning):
    """Test building via sphinx"""

    app.builder.build(['rst-demo'])

    html = (app.outdir / 'rst-demo.html').read_text()
    css = (app.outdir / "_static" / "pygments.css").read_text()
    style = app.builder.highlighter.formatter_args.get('style')

    assert style.__name__ == "HighlightedStyle"

    highlighted = re.findall('<span class=".+?-Highlight">(.+?)</span>', html)

    assert ["dwarves", "name"] == highlighted, \
        "Tokens enclosed in !!! should be marked with a *-Highlight class"

    styles = re.search('\..+?-Highlight { .*background-color: .+? }', css)

    assert styles, ".*-Highlight styles should be written to the stylesheet"

@pytest.mark.slow
def test_jupyter_book(rootdir, tmpdir):
    """Test building via jupyter-book"""

    tmpdir = Path(tmpdir)
    bookdir = rootdir / "test-book"

    cmd = [ "jb", "build", str(bookdir),
            "--path-output", str(tmpdir),
            "--warningiserror" ]

    result = run(cmd, capture_output=True)

    line = lambda: print("-" * 100)


    if result.returncode != 0:
        line()
        print(result.stdout.decode())
        line()

    cmd[2] = show_path("bookdir", bookdir)
    cmd[4] = show_path("testdir", tmpdir, environ.get("TMPDIR"), "$TMPDIR/")
    print("To rerun:")
    print(f"touch {cmd[2]}/*.md && \\")
    print(" ".join(cmd))
    line()

    assert result.returncode == 0

    html = (tmpdir/"_build"/"html"/"myst-demo.html").read_text()
    css = (tmpdir/"_build"/"html"/"_static"/"pygments.css").read_text()

    highlighted = re.findall('<span class=".+?-Highlight">(.+?)</span>', html)

    assert ["dwarves", "name"] == highlighted, \
        "Tokens enclosed in !!! should be marked with a *-Highlight class"

    styles = re.search('\..+?-Highlight { .*background-color: .+? }', css)

    assert styles, ".*-Highlight styles should be written to the stylesheet"
