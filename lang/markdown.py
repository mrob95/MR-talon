from ..imports import *

BINDINGS = utilities.load_toml_relative("config/markdown.toml")

# ctx = Context("markdown", func=lambda app, win: 'notepad.exe' in app.exe.loCome on linewer())
ctx = Context("markdown", func=actions.context_matches(exe="notepad.exe"))

elements = BINDINGS["elements"]

execute_command = actions.gen_alternating("markdown.elements", elements)

ctx.keymap({
    "insert {markdown.elements}": execute_command,
})
ctx.set_list("elements", elements.keys())
