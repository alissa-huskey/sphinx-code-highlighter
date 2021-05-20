"""Pygments lexer and style"""

from dataclasses import dataclass

from pygments.lexer import inherit, using, bygroups
from pygments.token import *
from sphinx.pygments_styles import SphinxStyle
from sphinx.highlighting import PygmentsBridge


__all__ = ["make_lexer", "HighlightedStyle", "Cfg", "CFG"]


@dataclass
class Cfg:
    """Config options"""
    marker: str = "!!!"
    bg: str = "#ffffcc"

CFG = Cfg()

class HighlightedStyle(SphinxStyle):
    """A pygments style adding a an Highlight subtype to all existing tokens,
       mapped to styles the same style with a background color appended.
    """
    styles = SphinxStyle.styles

    styles.update({
        t.Highlight: f"{s} bg:{CFG.bg}"
        for t, s in SphinxStyle.styles.items()
        if Generic is not t
    })

def make_lexer(lang: str=None, code: str=None, language_lexer=None):
    """Return a HighlightedCodeLexer class subclassed from the language lexer class,
       either deduced from lang (str) and code (str) or the class of language_lexer
       (pygments.lexer) instance.

    Params
    ------
    * language_lexer (pygments.Lexer) -- an instance of the lexer class to subclass
    * lang (str)                      -- name of the language
    * code (str)                      -- code to be lexed
    """

    # let sphinx figure out the language based on the content and language name
    if not language_lexer:
        language_lexer = PygmentsBridge().get_lexer(code, lang)

    # get the class type to subclass
    parent = language_lexer.__class__

    class HighlightedCodeLexer(parent):
        """A pygments lexer to that adds a Highlight subtype to all tokens found between
          the marker text (!!!) and let the parent class lex everything else."""

        language_lexer = parent

        def add_highlight(lexer, match, ctx=None):
            """Add a Highlight subtype to tokens between markers while stripping the
               markers themselves.

               Expects 4 match groups: marker, highlighted content, marker, rest of line
            """

            # make a callback function that assigns Token.Marker to the markers and
            # run everything else through the parent lexer
            lex = bygroups(Token.Marker, using(parent), Token.Marker, using(parent))

            # call it on the matches then iterate through the resulting tokens
            markers = 0
            for index, token, value in lex(lexer, match, ctx):

                # keep track of where we are in the line
                # but don't yield markers in the output stream
                if token is Token.Marker:
                    markers += 1
                    continue

                # add a Highlight subtype to tokens before the last marker
                if markers < 2:
                    token = token.Highlight

                # yield the modified stream
                yield index, token, value

        tokens = {
            'root': [
                # find lines where part is enclosed in highlight markers
                # delgate to add_highlight callback in four match groups:
                # marker, highlighted content, marker, the rest of the line
                (rf'({CFG.marker})(.+?)({CFG.marker})(.*)$', add_highlight),

                # all other tokens are inherited from parent class
                inherit
            ],
        }

    lang = lang or language_lexer.name
    HighlightedCodeLexer.__name__ = f"Highlighted{lang}Lexer"

    return HighlightedCodeLexer
