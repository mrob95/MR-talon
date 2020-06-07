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
alphabet = {
    "anti": "a",
    "bat": "b",
    "cap": "c",
    "die": "d",
    "each": "e",
    "fail": "f",
    "gone": "g",
    "harp": "h",
    "sit": "i",
    "jury": "j",
    "crunch": "k",
    "look": "l",
    "made": "m",
    "near": "n",
    "odd": "o",
    "pet": "p",
    "queer": "q",
    "red": "r",
    "sun": "s",
    "trap": "t",
    "urge": "u",
    "vest": "v",
    "whale": "w",
    "box": "x",
    "yes": "y",
    "zulu": "z",
}
mod.list("alphabet", desc="Alphabet")
ctx.lists["alphabet"] = {
    **alphabet,
    **{f"big {k}": v.upper() for k, v in alphabet.items()}
}

mod.list("directions", desc="Directions")
ctx.lists["directions"] = {
    "lease": "left",
    "ross": "right",
    "sauce": "up",
    "dunce": "down",
}
mod.list("directions_extreme", desc="Directions extreme")
ctx.lists["directions_extreme"] = {
    "sauce": "ctrl-home",
    "lease": "home",
    "dunce": "ctrl-end",
    "ross": "end",
}

mod.list("direction_modifiers", desc="Direction modifiers")
ctx.lists["direction_modifiers"] = {
    "queue": "ctrl-shift-",
    "shin": "shift-",
    "fly": "ctrl-",
}

mod.list("capitalisation", desc="Capitalisation")
ctx.lists["capitalisation"] = {
    "yell": "1",
    "tie": "2",
    "(Gerrish | camel)": "3",
    "sing": "4",
    "laws": "5",
    "password": "6",
}
mod.list("spacing", desc="Spacings")
ctx.lists["spacing"] = {
    "gum": "1",
    "gun": "1",
    "spine": "2",
    "snake": "3",
    "pebble": "4",
}


mod.list("punctuation", desc="Punctuation")
ctx.lists["punctuation"] = {
    **CORE["punctuation"],
    **CORE["punctuation2"]
}

mod.list("punctuation2", desc="Punctuation2")
ctx.lists["punctuation2"] = CORE["punctuation2"]

mod.list("simple_keys", desc="Simple_keys")
ctx.lists["simple_keys"] = CORE["keys"]

mod.list("simple_keys_norepeat", desc="Simple keys norepeat")
ctx.lists["simple_keys_norepeat"] = CORE["misc_core_keys"]
