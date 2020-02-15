from ..imports import *

BINDINGS = utilities.load_toml_relative("config/python.toml")

ctx = Context("python", func=actions.context_matches(".py"))

commands = BINDINGS["commands"]
functions = BINDINGS["functions"]
exceptions = BINDINGS["exceptions"]
umeths = BINDINGS["unary_methods"]
bmeths = BINDINGS["binary_methods"]
mmeths = BINDINGS["misc_methods"]

ctx.keymap({
    **{k: actions.Alternating(v) for k, v in commands.items()},
    **{f"fun {k}": [f"{v}()", Key("left")] for k, v in functions.items()},
    "function [<dgndictation>]": ["def ", textformat.insert_text(0, 3), "():", Key("left left")],
    "method [<dgndictation>]": ["def ", textformat.insert_text(0, 3), "(self):", Key("left left")],
    "selfie [<dgndictation>]": ["self.", textformat.insert_text(0, 3)],
    "classy [<dgndictation>]": ["class ", textformat.insert_text(2, 1), "():"],
    "commenter [<dgndictation>++]": ["# ", textformat.insert_text(4, 0)],
    "magic init": ["def __init__(self):", Key("left "*2)],
    **{f"magic {k}": f"def __{v}__(self):" for k, v in umeths.items()},
    **{f"magic {k}": f"def __{v}__(self, other):" for k, v in bmeths.items()},
    **{f"magic {k}": f"def __{v[0]}__({v[1]}):" for k, v in mmeths.items()},
    "try except": ["try:", Key("enter enter"), "except:", Key("shift-tab")],
    **{f"try except {k} [error]": ["try:", Key("enter enter"), f"except {v}:", Key("shift-tab")] for k, v in exceptions.items()},
})
