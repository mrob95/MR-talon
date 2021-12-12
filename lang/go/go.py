from talon import ui, Module, Context, registry, actions, imgui, cron

mod = Module()
ctx = Context()

ctx.matches = r"""
title: /\.go/
"""

@ctx.action_class("user")
class Actions:
    def lang_print(s: str):
        actions.insert(f'fmt.Println(f"{s}: ", {s})')

ctx.lists["user.functions"] = {
    "make": "make",
    "make map": "make(map[[|]])",
    "print": "fmt.Println",
    "print F": 'fmt.Printf("[|]\n")',
    "length": "len",
    "int": "int",
    "to integer": "strconv.Atoi",
    "to string": "strconv.Itoa",
}

ctx.lists["user.logicals"] = {
    "and": " && ",
    "or": " || ",
}

mod.list("go_types")
ctx.lists["user.go_types"] = {
    "integer": "int",
    "boolean": "bool",
    "string": "string",
    "empty interface": "interface{}",
    "rune": "rune",
    "byte": "byte",
    "float thirty two": "float32",
    "float sixty four": "float64",
}

@mod.capture(rule="{user.go_types} | <user.go_map> | <user.go_slice>")
def go_type(m) -> str:
    """A Go type"""
    return str(m)

@mod.capture(rule="map {user.go_types}*")
def go_map(m) -> str:
    """A Go map map, e.g. map int string"""
    d = {1: "map[[|]]", 2: "map[{m.go_types_1}][|]", 3: "map[{m.go_types_1}]{m.go_types_2}"}
    return d[len(m)].format(m=m)

@mod.capture(rule="slice [<number>] [{user.go_types}]")
def go_slice(m) -> str:
    """A Go map slice, e.g. slice string"""
    number = getattr(m, "number", "")
    type = getattr(m, "go_types", "")
    return f"[{number}]{type}"
