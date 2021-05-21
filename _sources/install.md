Install
=======

1. Install the `sphinx-code-highlighter` module via pip
   ```shell
   pip install sphinx-code-highlighter
   ```
   Or poetry
   ```shell
   poetry add sphinx-code-highlighter
   ```
2. Add `code_highlighter` to the [extensions][sphinx-extensions] array of your {file}`config.py`:
   ```{code-block} python
   # conf.py
   extensions = [
       "code_highlighter",
       # ...
   ]
   ```
   Or your [Jupyter Book][jupyter-config] {file}`_config.yml`:
   ```{code-block} yaml
   # _config.yml
   sphinx:
     extra_extensions:
       - code_highlighter
       # ...
   ```
3. Add `sphinx-code-highlighter` to your {file}`requirements.txt` for publishing (for example to [Google Pages][google-pages].)

   ```{code-block} text
   # requirements.txt
   jupyter-book
   sphinx-code-highlighter
   ```

[sphinx-extensions]: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-extensions
[jupyter-config]: https://jupyterbook.org/customize/config.html
[google-pages]: https://jupyterbook.org/publish/gh-pages.html
