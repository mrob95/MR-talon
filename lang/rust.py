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
    def get_var_regex() -> str:
        return r"(\s|,\s*|\()([A-Za-z!_]+?)(,|:|\)|\s*=|\(|\.|\n)"


ctx.lists["user.functions"] = {
    "as string": "as_str",
    "collect": "collect",
    "collect into": "collect::<[|]>()",
    "clone": "clone",
    "cloned": "cloned",
    "count": "count",
    "get": "get",
    "into": "into",
    "iter": "iter",
    "iter mute": "iter_mut",
    "lines": "lines",
    "length": "len",
    "map": "map(|[|]| )",
    "max": "max",
    "min": "min",
    "next": "next",
    "Okay": "Ok",
    "parse": "parse",
    "parse into": "parse::<[|]>()",
    "push": "push",
    "print": 'println!("{}", [|]);',
    "print debug": 'println!("{:?}", [|]);',
    "panic": "panic!",
    "Some": "Some",
    "sort": "sort",
    "split": "split",
    "split once": "split_once",
    "to string": "to_string",
    "to owned": "to_owned",
    "trim": "trim",
    "take": "take",
    "unwrap": "unwrap",
    "vector": "vec!"
}

ctx.lists["user.logicals"] = {
    "and": " && ",
    "as": " as ",
    "or": " || ",
    "else": " else ",
    "if": "if ",
    "in": " in ",
}

mod.list("rust_types")
ctx.lists["user.rust_types"] = {
    "eye 3 2": "i32",
    "you 3 2": "u32",
    "stir": "str",
    "string": "String",
}

ctx.lists["user.values"] = {
    "false": "false",
    "none": "None",
    "true": "true",
}

mod.list("rust_type_modifiers")
ctx.lists["user.rust_type_modifiers"] = {
    "mute": "mute",
    "ref": "ref",
}

mod.list("rust_collections")
ctx.lists["user.rust_collections"] = {
    "vector": "Vec",
    "Option": "Option",
    "Result": "Result",
}

@mod.capture(rule="[{user.rust_type_modifiers}+] {user.rust_types}")
def rust_basic_type(m) -> str:
    """A Rust type, e.g. ref stir -> &str"""
    result = m["rust_types"]
    modifiers = ""
    if hasattr(m, "rust_type_modifiers_list"):
        mods = m["rust_type_modifiers_list"]
        if "mute" in mods:
            modifiers += "mut "
        if "ref" in mods:
            modifiers += "&"
    return f"{modifiers}{result}"

@mod.capture(rule="[{user.rust_type_modifiers}+] [{user.rust_collections}] <user.rust_basic_type>+")
def rust_type(m) -> str:
    """A Rust type, e.g. ref stir -> &str"""
    types = m["rust_basic_type_list"]
    if len(types) > 1:
        typ = "(" + ", ".join(types) + ")"
    else:
        typ = types[0]
    modifiers = ""
    if hasattr(m, "rust_type_modifiers_list"):
        mods = m["rust_type_modifiers_list"]
        if "mute" in mods:
            modifiers += "mut "
        if "ref" in mods:
            modifiers += "&"
    if hasattr(m, "rust_collections"):
        coll = m["rust_collections"]
        return f"{modifiers}{coll}<{typ}>"
    f"{modifiers}{typ}"
