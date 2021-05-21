sphinx-code-highlighter
=======================

![pypi][badge-pypi]
![python][badge-python]
![license][badge-license]


A simple [Sphinx](https://www.sphinx-doc.org/) extension that adds a
`code-block-hl` directive -- it's `code-block`, but with partial line highlighting.


``````{div} full-width

`````{panels}
:card: shadow-none border-0 p1
:header: +h4 card-title bg-white text-info border-bottom-0 mb-0 pb-0 -card-header

Turns this
^^^

```rst

.. code-block-hl:: toml

   # pyproject.toml

   [tool.poetry.dependencies]
   python = "^3.8"
   !!!sphinx-code-highlighter!!! = "^0.0.1"

```

---

Into this
^^^

```{code-block-hl} toml
# pyproject.toml

[tool.poetry.dependencies]
python = "^3.8"
!!!sphinx-code-highlighter!!! = "^0.0.1"

```

---

And this
^^^

```rst

.. code-block-hl:: python

   # conf.py
   extensions = [
       !!!"code_highlighter"!!!,
       # ...
   ]

```

---

Into that
^^^

```{code-block-hl} python
 # conf.py
 extensions = [
     !!!"code_highlighter"!!!,
     # ...
 ]

```

`````

``````

[badge-pypi]: https://img.shields.io/pypi/v/sphinx-code-highlighter.svg
[badge-python]: https://img.shields.io/pypi/pyversions/sphinx-code-highlighter.svg
[badge-license]: https://img.shields.io/github/license/alissa-huskey/sphinx-code-highlighter.svg
