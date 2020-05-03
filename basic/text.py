from user.imports import *

CORE = utilities.load_toml_relative("config/core.toml")

capitalisations = CORE["capitalisation"]
spacings = CORE["spacing"]


def get_formatting(m):
    try:
        capitalisation = int(m["capitalisation"])
    except KeyError:
        capitalisation = 0
    try:
        spacing = int(m["spacing"])
    except KeyError:
        spacing = 0
    t = m["dgndictation"]
    textformat.format_text(t, capitalisation, spacing)


ctx = Context("text")

ctx.commands = {
        "say <dgndictation> [over]": textformat.insert_text(0,0),
        "({capitalisation} {spacing} | {capitalisation} | {spacing}) bow <dgndictation>":
            get_formatting,
        "({capitalisation} {spacing} | {capitalisation} | {spacing}) bower <dgndictation>++":
            get_formatting,
    }


ctx.lists["capitalisation"] = capitalisations
ctx.lists["spacing"] = spacings