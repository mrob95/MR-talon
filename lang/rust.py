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
    "as string": "as_str",
    "collect": "collect",
    "collect into": "collect::<[|]>()",
    "clone": "clone",
    "count": "count",
    "get": "get",
    "into": "into",
    "iter": "iter",
    "iter mute": "iter_mut",
    "lines": "lines",
    "length": "len",
    "map": "map",
    "next": "next",
    "parse": "parse",
    "push": "push",
    "print": 'println!("{}", [|]);',
    "to string": "to_string",
    "to owned": "to_owned",
    "unwrap": "unwrap",
}

ctx.lists["user.logicals"] = {
    "and": " && ",
    "as": " as ",
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

ctx.lists["user.values"] = {
    "false": "false",
    "none": "None",
    "true": "true",
}
