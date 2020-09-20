from user.utils import utilities
from talon import *

BINDINGS = utilities.load_toml_relative("config/rust.toml")



ctx = Context("rust")
ctx.matches = r"""
title: /.*\.rs$/
"""
commands = BINDINGS["commands"]
functions = BINDINGS["functions"]

ctx.commands = {
    # **{k: actions.Alternating(v) for k, v in commands.items()},
    # **{f"fun {k}": [f"{v}()", Key("left")] for k, v in functions.items()},
    # "function [<dgndictation>]": ["fn ", textformat.insert_text(0, 3), "(){}", Key("left left")],
}