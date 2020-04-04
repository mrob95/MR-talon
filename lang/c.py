from user.imports import *

BINDINGS = utilities.load_toml_relative("config/C.toml")


ctx = Context("C")
ctx.matches = r"title: /.*\.c/\ntitle: /.*\.h/\n"

commands = BINDINGS["commands"]
functions = BINDINGS["functions"]

ctx.commands = {
    "{commands}": lambda m: actions.exec_alternating(commands[m["commands"]]),
    "fun {functions}": [lambda m: Str(m["functions"])(m), "()", Key("left")],

    "function [<dgndictation>]": ["def ", textformat.insert_text(0, 3), "() {}", Key("left "*4)],
}
ctx.lists["functions"] = functions
ctx.lists["commands"] = commands.keys()
