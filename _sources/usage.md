---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
Usage
=====

The `code-block-hl` directive works just like the [code-block directive][]
but with the added feature of partially highlighted lines. 

Syntax
------

While the builtin version only allows you to highlight full lines via the
`:emphasize-lines:` option, with this extension you can surround the parts of
lines you want to highlight with `!!!`.

`````{tabbed} reST

You can use the directive in [reStructuredText][] documents...

```rst

.. code-block-hl:: python
  :linenos:
  :caption: The text surrounded by "!!!" gets highlighted.

  dwarves = [
    "Bashful",
    "Dopey",
    "Happy",
    "Grumpy",
    "Sleepy",
    "Sneezy",
    "Doc",
  ]

  i = 0
  while i < len(!!!dwarves!!!):
    !!!name!!! = dwarves[i]
    print(f"{name}s Room")
    i += 1

```

`````


```````{tabbed} MyST

Or [MyST Markdown] documents.

`````md

```{code-block-hl} python
:linenos:
:caption: "The text surrounded by `!!!` gets highlighted."
dwarves = [
  "Bashful",
  "Dopey",
  "Happy",
  "Grumpy",
  "Sleepy",
  "Sneezy",
  "Doc",
]

i = 0
while i < len(!!!dwarves!!!):
  !!!name!!! = dwarves[i]
  print(f"{name}s Room")
  i += 1
```

`````

```````

Screenshots
-----------

```{tabbed} Sphinx Book Theme

Rendered via the [Sphinx Book Theme][]:

![sphinx-book-demo][]

```

```{tabbed} Alabaster Theme

The [Alabaster Theme][]:

![alabaster-demo][]

```

```{tabbed} Read the Docs Theme

And the [Read the Docs Theme][]:

![rtd-demo][]

```


[sphinx-book-demo]: img/sphinx-book-demo.png
[alabaster-demo]: img/alabaster-demo.png
[rtd-demo]: img/rtd-demo.png
[code-block directive]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-code-block
[reStructuredText]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/
[MyST Markdown]: https://myst-parser.readthedocs.io/en/latest/using/syntax.html

[Sphinx Book Theme]: https://sphinx-book-theme.readthedocs.io/en/latest/index.html
[Alabaster Theme]: https://alabaster.readthedocs.io/en/latest/
[Read the Docs Theme]: https://sphinx-rtd-theme.readthedocs.io/en/stable/
