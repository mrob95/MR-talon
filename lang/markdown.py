from user.imports import *

BINDINGS = utilities.load_toml_relative("config/markdown.toml")


ctx = Context("markdown")
ctx.matches = r"""
app: /.*/
and title: /.*\.md$/
app: Notepad
"""

ctx.commands = {
    "insert {elements}": lambda m: actions.exec_alternating(elements[m["elements"][0]]),
}
elements = BINDINGS["elements"]
ctx.lists["elements"] = elements.keys()