from user.imports import *
from typing import List, Optional

mod = Module()
ctx = Context()

BRING = utilities.load_toml_relative("config/bringme.toml")

@mod.action_class
class Actions:
    def upper(s: str) -> str:
        """Uppercase"""
        return s.upper()

    def cat(l: List[str], sep: str = "") -> str:
        """Concatenate"""
        return sep.join(l)

    def slice(l: List[str], i1: Optional[int] = None, i2: Optional[int] = None) -> List[str]:
        """Slice"""
        if i1 is not None and i2 is None:
            return l[i1:]
        elif i1 is None and i2 is not None:
            return l[:i2]
        elif i1 is not None and i2 is not None:
            return l[i1:i2]
        else:
            return l


mod.list("folders", desc="Commonly accessed folders")
ctx.lists["user.folders"] = BRING["folder"]

mod.list("extensions", desc="Common file extensions")
ctx.lists["user.extensions"] = {
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
ctx.lists["user.alphabet"] = alphabet

mod.list("directions", desc="Directions")
ctx.lists["user.directions"] = {
    "lease": "left",
    "ross": "right",
    "sauce": "up",
    "dunce": "down",
}

mod.list("directions_extreme", desc="Directions extreme")
ctx.lists["user.directions_extreme"] = {
    "sauce": "ctrl-home",
    "lease": "home",
    "dunce": "ctrl-end",
    "ross": "end",
}

mod.list("direction_modifiers", desc="Direction modifiers")
ctx.lists["user.direction_modifiers"] = {
    "queue": "ctrl-shift-",
    "shin": "shift-",
    "fly": "ctrl-",
}

mod.list("capitalisation", desc="Capitalisation")
ctx.lists["user.capitalisation"] = {
    "yell": "1",
    "tie": "2",
    "(Gerrish | camel)": "3",
    "sing": "4",
    "laws": "5",
    "password": "6",
}
mod.list("spacing", desc="Spacings")
ctx.lists["user.spacing"] = {
    "gum": "1",
    "gun": "1",
    "spine": "2",
    "snake": "3",
    "pebble": "4",
}


mod.list("punctuation", desc="Punctuation")
ctx.lists["user.punctuation"] = {
    **CORE["punctuation"],
    **CORE["punctuation2"]
}

mod.list("punctuation2", desc="Punctuation2")
ctx.lists["user.punctuation2"] = CORE["punctuation2"]

mod.list("simple_keys", desc="Simple_keys")
ctx.lists["user.simple_keys"] = CORE["keys"]

mod.list("simple_keys_norepeat", desc="Simple keys norepeat")
ctx.lists["user.simple_keys_norepeat"] = CORE["misc_core_keys"]

# ------------------------------------------------

PERSONAL = utilities.load_toml_relative("config/personal.toml")

mod.list("personal", desc="...")
ctx.lists["user.personal"] = PERSONAL