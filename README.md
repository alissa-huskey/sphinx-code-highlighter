Sphinx Code Highlighter Directive
=================================

A Sphinx directive that works just like a code-block plus allows you to
highlight partial lines.

Example
-------

`````markdown

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

![demo](docs/img/demo.png)
