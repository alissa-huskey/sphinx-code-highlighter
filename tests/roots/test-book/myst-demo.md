MyST Markdown Demo
==================

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
