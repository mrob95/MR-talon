from user.imports import *

mod = Module()
ctx = Context()

BRING = utilities.load_toml_relative("config/bringme.toml")

mod.list("folders", desc="Commonly accessed folders")
ctx.lists["folders"] = BRING["folder"]

mod.list("extensions", desc="Common file extensions")
ctx.lists["extensions"] = {
    "markdown": "md",
    "PDF": "pdf",
    "jay peg": "jpg",
    "PNG": "png",
    "pie": "py",
    "rust": "rs",
    "sequel": "sql",
    "talon": "talon",
    "tech": "tex",
    "text": "txt",
}

#------------------------------------------------------

CORE = utilities.load_toml_relative("config/core.toml")

mod.list("alphabet", desc="Alphabet")
ctx.lists["alphabet"] = {
    **CORE["letters_alt"],
    **{f"big {k}": v.upper() for k, v in CORE["letters_alt"].items()}
}

mod.list("directions", desc="Directions")
ctx.lists["directions"] = CORE["directions"]
mod.list("directions_extreme", desc="Directions extreme")
ctx.lists["directions_extreme"] = {
    "sauce": "ctrl-home",
    "lease": "home",
    "dunce": "ctrl-end",
    "ross": "end",
}

mod.list("direction_modifiers", desc="Direction modifiers")
ctx.lists["direction_modifiers"] = CORE["modifiers"]

mod.list("punctuation", desc="Punctuation")
ctx.lists["punctuation"] = {**CORE["punctuation"], **CORE["punctuation2"]}

mod.list("punctuation2", desc="Punctuation2")
ctx.lists["punctuation2"] = CORE["punctuation2"]

mod.list("simple_keys", desc="Simple_keys")
ctx.lists["simple_keys"] = CORE["keys"]

mod.list("simple_keys_norepeat", desc="Simple keys norepeat")
ctx.lists["simple_keys_norepeat"] = CORE["misc_core_keys"]
