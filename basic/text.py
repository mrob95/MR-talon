from user.imports import *

CORE = utilities.load_toml_relative("config/core.toml")

capitalisations = CORE["capitalisation"]
spacings = CORE["spacing"]


def get_formatting(m):
    try:
        capitalisation = capitalisations[m["text.capitalisation"][0]]
    except KeyError:
        capitalisation = 0
    try:
        spacing = spacings[m["text.spacing"][0]]
    except KeyError:
        spacing = 0
    t = m["dgndictation"]
    textformat.format_text(t, capitalisation, spacing)


ctx = Context("text")

ctx.keymap(
    {
        "say <dgndictation> [over]": textformat.insert_text(0,0),
        "({text.capitalisation} {text.spacing} | {text.capitalisation} | {text.spacing}) (bow|bowel) <dgndictation>":
            get_formatting,
    }
)
ctx.set_list("capitalisation", capitalisations.keys())
ctx.set_list("spacing", spacings.keys())