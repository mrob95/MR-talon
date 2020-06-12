from user.imports import *

BINDINGS = utilities.load_toml_relative("config/C.toml")

ctx = Context("C")
ctx.matches = r"""
title: /.*\.c/
title: /.*\.h/
"""

commands = BINDINGS["commands"]
ctx.lists["functions"] = {
    "file open": "fopen",
    "file seek": "fseek",
    "file close": "fclose",
    "file read": "fread",
    "rewind": "rewind",
    "free": "free",
    "mallock": "malloc",
    "mem copy": "memcpy",
    "print": "printf",
    "size of": "sizeof",
    "stir length": "strlen",
    "stir copy": "strcpy",
    "string length": "strlen",
    "string copy": "strcpy",
}
ctx.lists["logicals"] = {
    "and": " && ",
    "or": " || ",
}
ctx.lists["c_types"] = {
    "boolean": "bool ",
    "inter": "int ",
    "file": "FILE *",
    "unsigned": "unsigned ",
    "void": "void ",
    "struct": "struct ",
    "enum": "enum ",
    "char star": "char *",
}
