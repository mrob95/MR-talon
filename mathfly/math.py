from talon import Context, Module

fractions = {
    "half": "2",
    "halves": "2",
    "quarter": "4",
    "fourth": "4",
    "fifth": "5",
    "sixth": "6",
    "seventh": "7",
    "eighth": "8",
    "ninth": "9",
    "tenth": "10",
}

mod = Module()
ctx = Context()

mod.list("mathfly_fractions", "Fractions")
ctx.lists["user.mathfly_fractions"] = {
    **fractions,
    **{f"{k}s": v for k, v in fractions.items()},
}