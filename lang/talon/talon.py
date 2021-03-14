from talon import *
import re

REPLACEMENTS = {
    "str": "string",
    "vscode": "VS code",
    "url": "URL",
    "10": "ten",
    "20": "twenty",
    "r": "are",
    "sys": "sis",
    "py": "pie",
    "cd": "CD",
}

pattern = re.compile(r"[A-Z][a-z]*|[a-z]+|\d+")
def create_spoken_form(symbol):
    words = pattern.findall(symbol)
    result = []
    for i, w in enumerate(words):
        if i == 0 and w == "user": continue
        result.append(REPLACEMENTS[w] if w in REPLACEMENTS else w)
    return " ".join(result)

mod = Module()
ctx = Context()

mod.list("talon_actions")
mod.list("talon_lists")
mod.list("talon_captures")
mod.list("talon_apps")
mod.list("talon_tags")

def update_lists(decls):
    for thing in ["actions", "lists", "captures", "tags", "apps"]:
        names = getattr(decls, thing).keys()
        spoken = [create_spoken_form(s) for s in names]
        ctx.lists[f"user.talon_{thing}"] = dict(zip(spoken, names))
        # print(dict(zip(spoken, names)))

registry.register("update_decls", update_lists)
