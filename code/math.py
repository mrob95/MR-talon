from talon import Context, Module

fractions = {
    "half": "2",
    "halves": "2",
    "thirds": "3",
    "fourths": "4",
    "quarters": "4",
    "quarter": "4",
    "fifth": "5",
    "fifths": "5",
    "sixth": "6",
    "sixths": "6",
    "seventh": "7",
    "sevenths": "7",
    "eighth": "8",
    "eighths": "8",
    "ninth": "9",
    "ninths": "9",
    "tenth": "10",
    "tenths": "10",
}

mod = Module()
ctx = Context()

mod.list("fractions", "Fractions")
ctx.lists["fractions"] = fractions