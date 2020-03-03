from user.imports import *

BINDINGS = utilities.load_toml_relative("config/C.toml")

ctx = Context("c", func=actions.context_matches(".c"))

commands = BINDINGS["commands"]
functions = BINDINGS["functions"]

execute_command = actions.gen_alternating("c.commands", commands)

ctx.keymap({
    "{c.commands}": execute_command,
    "fun {c.functions}": [actions.exec_str("c.functions", functions), "()", Key("left")],
    "function [<dgndictation>]": ["def ", textformat.insert_text(0, 3), "() {}", Key("left "*4)],
})
ctx.set_list("functions", functions.keys())
ctx.set_list("commands", commands.keys())
