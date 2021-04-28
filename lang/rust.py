from talon import ui, Module, Context, registry, actions, imgui, cron

mod = Module()
ctx = Context()
ctx.matches = r"""
title: /.*\.rs$/
"""

@ctx.action_class("user")
class Actions:
    def lang_print(s: str):
        actions.insert(f'println!("{s}: {{}}", {s});')


ctx.lists["user.functions"] = {
    "unwrap": "unwrap",
    "parse": "parse",
    "lines": "lines",
    "to string": "to_string",
    "iter": "iter",
    "clone": "clone",
    "next": "next",
    "push": "push",
    "get": "get",
    "print": 'println("{}", [|]);',
}

ctx.lists["user.logicals"] = {
    "and": " && ",
    "or": " || ",
    "else": " else ",
    "if": "if ",
}

mod.list("rust_types")
ctx.lists["user.rust_types"] = {
    "eye 3 2": "i32",
    "you 3 2": "u32",
    "string": "str",
}
