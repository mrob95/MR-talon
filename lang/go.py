from talon import *

mod = Module()
ctx = Context()

ctx.matches = r"""
title: /\.go/
"""

@ctx.action_class("user")
class Actions:
    def lang_print(s: str):
        actions.insert(f'print(f"{s}: {{{s}}}")')

ctx.lists["user.functions"] = {
    "make": "make",
    "make map": "make(map[[|]])",
    "print": "fmt.Println",
    "to integer": "strconv.Atoi",
    "to string": "strconv.Itoa",
}

ctx.lists["user.logicals"] = {
    "and": " && ",
    "or": " || ",
}
