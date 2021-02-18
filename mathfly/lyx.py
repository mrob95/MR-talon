from talon import *

mod = Module()
ctx = Context()

ctx.matches = r"""
app: LyX.exe
"""

greek_letters = {
    "alpha": "alpha",
    "beater": "beta",
    "gamma": "gamma",
    "delta": "delta",
    "epsilon": "varepsilon",
    "zita": "zeta",
    "eater": "eta",
    "theta": "theta",
    "iota": "iota",
    "kappa": "kappa",
    "lambda": "lambda",
    "mu": "mu",
    "new": "nu",
    "zee": "xi",
    "pie": "pi",
    "row": "rho",
    "sigma": "sigma",
    "tau": "tau",
    "upsilon": "upsilon",
    "phi": "phi",
    "chi": "chi",
    "sigh": "psi",
    "omega": "omega",
}

ctx.lists["user.greek_letters"] = {
    **greek_letters,
    **{f"big {k}": v.title() for k, v in greek_letters.items()}
}