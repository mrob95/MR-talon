from talon import *

mod = Module()
ctx = Context()

ctx.matches = r"""
app: scinoteb.exe
"""

sn55_greek_letters = {
    "alpha": "a",
    "beater": "b",
    "gamma": "g",
    "delta": "d",
    "epsilon": "e",
    "zita": "z",
    "eater": "h",
    "theta": "y",
    "iota": "i",
    "kappa": "k",
    "lambda": "l",
    "mu": "m",
    "new": "n",
    "zee": "x",
    "pie": "p",
    "row": "r",
    "sigma": "s",
    "tau": "t",
    "upsilon": "u",
    "phi": "f",
    "chi": "q",
    "sigh": "c",
    "omega": "w",
}

ctx.lists["user.greek_letters"] = {
    **sn55_greek_letters,
    **{f"big {k}": v.title() for k, v in sn55_greek_letters.items()}
}