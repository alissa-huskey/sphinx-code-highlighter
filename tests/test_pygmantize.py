"""Syntax highlight testfile.py with custom style/lexer/filter and print"""

from pathlib import Path
import re

from pygments import lex
from pygments.token import Token
from pygments.lexers.python import PythonLexer
from pygments.lexers.html import HtmlLexer
from pygments.lexers.shell import BashLexer
import pytest

from code_highlighter.pygmantize import (
    ArgumentError,
    HighlightedStyle,
    make_lexer
)

@pytest.fixture(scope='session')
def datadir(rootdir):
    return rootdir / "test-code"

def test_lexer(datadir):
    filepath = datadir / "dwarves.py"
    code = filepath.read_text()
    lexer = make_lexer("python", code)

    highlighted, markers = [], []

    for token, text in lex(code, lexer()):
        if str(token).endswith("Highlight"):
            highlighted.append(text)
        elif token is Token.Marker:
            markers.append(text)

    assert not len(markers), "Markers tokens should be removed"
    assert len(highlighted) == 4, "Tokens enclosed by !!! should be highlighted"
    assert "Grumpy" in highlighted
    assert "dwarves" in highlighted
    assert '"' in highlighted

@pytest.mark.parametrize("params, superclass", [
    (dict(language_lexer=PythonLexer()), PythonLexer),
    (dict(lang="python", code='print("oh hai")'), PythonLexer),
    (dict(lang="html"), HtmlLexer),
    (dict(code="$ echo $PATH"), BashLexer),
])
def test_make_lexer(params, superclass):
    lexer = make_lexer(**params)

    assert superclass in lexer.mro(), \
        "Highlighted{Language}Lexer should be subclassed from language lexer"

    assert lexer.__name__ == f"Highlighted{superclass.__name__}", \
        "The lexer class name should be the parents name prefixed by 'Highlighted'"


@pytest.mark.parametrize("params, error", [
    ({}, ArgumentError),
])
def test_make_lexer_exceptions(params, error):
    with pytest.raises(error):
        make_lexer(**params)


def test_highlighted_style():
    styles = HighlightedStyle.styles
    bgc = "#ffffcc"
    token = Token.Name.Namespace

    assert styles[token.Highlight] == f"{styles[token]} bg:{bgc}", \
        "Every token should have a .Highlight subtoken style with the highlight background color"


def test_add_highlight():
    code = """print("!!!well hello!!!")"""
    klass = make_lexer("python", code)
    match = re.search(rf'(!!!)(.+?)(!!!)(.*)$', code)
    lexer = klass()

    # [(10, Token.Name.Highlight, 'well'),
    #  (14, Token.Text.Highlight, ' '),
    #  (15, Token.Name.Highlight, 'hello'),
    #  (23, Token.Literal.String.Double, '"'),
    #  (24, Token.Literal.String.Double, ')')]

    tokens = list(lexer.add_highlight(match, PythonLexer))

    assert "well hello" == "".join(
        [val for _, tok, val in tokens if str(tok).endswith("Highlight")]), \
        "Only tokens enclosed by !!! should be appended with .Highlight"

    assert not any( [token == Token.Marker for pos, token, text in tokens]), \
        "Highlight markers (!!!) should be removed."
