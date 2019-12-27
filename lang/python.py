from ..imports import *

BINDINGS = utilities.load_toml_relative("config/python.toml")

ctx = Context("python", func=lambda app, win: '.py' in win.title)

commands = BINDINGS["commands"]
functions = BINDINGS["functions"]
umeths = BINDINGS["unary_methods"]
bmeths = BINDINGS["binary_methods"]
mmeths = BINDINGS["misc_methods"]

execute_command = actions.gen_alternating("python.commands", commands)

ctx.keymap({
    "{python.commands}": execute_command,
    "fun {python.functions}": [actions.exec_str("python.functions", functions), "()", Key("left")],
    "function [<dgndictation>]": ["def ", textformat.insert_text(0, 3), "():", Key("left left")],
    "method [<dgndictation>]": ["def ", textformat.insert_text(0, 3), "(self):", Key("left left")],
    "selfie [<dgndictation>]": ["self.", textformat.insert_text(0, 3)],
    "classy [<dgndictation>]": ["class ", textformat.insert_text(2, 1), "():"],
    "magic init": ["def __init__(self):", Key("left "*2)],
    "magic {python.umeths}": ["def __", actions.exec_str("python.umeths", umeths), "__(self):"],
    "magic {python.bmeths}": ["def __", actions.exec_str("python.bmeths", bmeths), "__(self, other):"],
    "magic {python.mmeths}": lambda m: Str("def __%s__(%s):" % tuple(mmeths[m["python.mmeths"]])),
})
ctx.set_list("functions", functions.keys())
ctx.set_list("commands", commands.keys())
ctx.set_list("umeths", umeths.keys())
ctx.set_list("bmeths", bmeths.keys())
ctx.set_list("mmeths", mmeths.keys())
