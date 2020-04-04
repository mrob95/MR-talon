from talon import Context, Module
from user.utils import utilities

DATA = utilities.load_toml_relative("config/tex_data.toml")


mod = Module()
ctx = Context()

symbols = DATA["tex_symbols1"]
symbols.update(DATA["tex_symbols2"])
symbols.update({
    "fraction": "frac",
    "summation": "sum",
    "product": "prod",
    "product": "lim",
    "square root": "sqrt",
    "math mode": "math-container",
    "accent hat": "hat",
    "accent tilde": "tilde",
    "accent dot": "dot",
    "accent double dot": "ddot",
    "accent bar": "bar",
    "accent vector": "vec",
})

mod.list("tex_symbols", desc="TeX")
ctx.lists['tex_symbols'] = symbols

mod.list("greek_letters", desc="Greek letters")
ctx.lists["greek_letters"] = {
    **DATA["greek_letters"],
    **{f"big {k}": v.title() for k, v in DATA["greek_letters"].items()}
}

