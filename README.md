Sphinx Code Highlighter Directive
=================================

Goal
----

A Sphinx directive works just like a code-block, plus allows you to highlight
partial lines.

Example
-------

`````markdown

```{code-block}
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
  name = dwarves[i]
  print(f"{name}s Room")
  i += 1

`````
