from user.imports import *

BINDINGS = utilities.load_toml_relative("config/C.toml")

ctx = Context("C")
ctx.matches = r"""
title: /.*\.c/
title: /.*\.h/
"""

commands = BINDINGS["commands"]
ctx.lists["functions"] = BINDINGS["functions"]
ctx.lists["logicals"] = {
    "and": " && ",
    "or": " || ",
}
ctx.lists["c_types"] = {
    "boolean": "bool",
    "inter": "int",
    "unsigned": "unsigned",
    "void": "void",
    "struct": "struct ",
    "enum": "enum ",
}
