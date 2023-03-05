from talon import ui, Module, Context, registry, actions, imgui, cron

mod = Module()
ctx = Context()

ctx.matches = r"""
title: /\.go/
"""

@ctx.action_class("user")
class Actions:
    def lang_print(s: str):
        actions.insert(f'fmt.Println("{s}: ", {s})')
    def get_type_regex() -> str:
        return r"type ([A-Za-z]+)"
    def get_var_regex() -> str:
        return r"(\s|,|\()([A-Za-z_]+?)(,|:|\)|\s*=|\(|\.|\n)"

ctx.lists["user.functions"] = {
    "close": "close",
    "error": "fmt.Errorf",
    "int": "int",
    "length": "len",
    "make": "make",
    "print F": 'fmt.Printf("[|]")',
    "print": "fmt.Println",
    "sprint F": 'fmt.Sprintf("[|]")',
    "string": "string",
    "to integer": "strconv.Atoi",
    "to string": "strconv.Itoa",
}

ctx.lists["user.logicals"] = {
    "and": " && ",
    "or": " || ",
}

ctx.lists["user.values"] = {
    "false": "false",
    "nil": "nil",
    "null": "nil",
    "true": "true",
}

mod.list("go_types")
ctx.lists["user.go_types"] = {
    "integer": "int",
    "inter eight": "int8",
    "inter sixteen": "int16",
    "inter thirty two": "int32",
    "inter sixty four": "int64",
    "you inter eight": "uint8",
    "you inter sixteen": "uint16",
    "you inter thirty two": "uint32",
    "you inter sixty four": "uint64",
    "boolean": "bool",
    "string": "string",
    "empty interface": "interface{}",
    "error": "error",
    "rune": "rune",
    "byte": "byte",
    "float thirty two": "float32",
    "float sixty four": "float64",
}

@mod.capture(rule="[ref] ({user.go_types} | <user.go_map> | <user.go_slice> | <user.go_chan> | {user.file_types})")
def go_type(m) -> str:
    """A Go type"""
    if m[0] == "ref":
        return "*" + m[1]
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

@mod.capture(rule="channel {user.go_types}")
def go_chan(m) -> str:
    """A Go map slice, e.g. slice string"""
    type = getattr(m, "go_types", "")
    return f"chan {type}"
