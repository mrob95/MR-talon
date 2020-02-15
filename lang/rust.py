from ..imports import *

BINDINGS = utilities.load_toml_relative("config/rust.toml")

ctx = Context("rust", func=actions.context_matches(".rs"))

commands = BINDINGS["commands"]
functions = BINDINGS["functions"]

ctx.keymap({
    **{k: actions.Alternating(v) for k, v in commands.items()},
    **{f"fun {k}": [f"{v}()", Key("left")] for k, v in functions.items()},
    "function [<dgndictation>]": ["fn ", textformat.insert_text(0, 3), "(){}", Key("left left")],
})
