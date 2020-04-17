from talon import Context, Module

mod = Module()
ctx = Context()

symbols = {
    # operators
    "fraction": "frac",
    "summation": "sum",
    "product": "prod",
    "product": "lim",
    "[square] root": "sqrt",
    "generic root": "root",
    "integral": "int",
    "double integral": "iint",
    "triple integral": "iiint",
    "times": "times",
    "divide": "div",
    "C dot": "cdot",
    "plus or minus": "pm",
    "partial": "partial",
    "infinity": "infty",
    "(nice frack | nice fraction)": "nicefrac",
    "binomial": "binom",
    "vector nabla": "nabla",
    # accents
    "accent hat": "hat",
    "accent tilde": "tilde",
    "accent dot": "dot",
    "accent double dot": "ddot",
    "accent bar": "bar",
    "accent vector": "vec",
    # trig
    "sine": "sin",
    "cosine": "cos",
    "tangent": "tan",
    "secant": "sec",
    "cosecant": "csc",
    "cotangent": "cot",
    "arc sine": "arcsin",
    "arc cosine": "arccos",
    "arc tan": "arctan",
    "hyperbolic sine": "sinh",
    "hyperbolic cosine": "cosh",
    "hyperbolic cotangent": "coth",
    "hyperbolic tangent": "tanh",
    # functions
    "argument": "arg",
    "degree": "deg",
    "determinant": "det",
    "dimension": "dim",
    "(natural (log | logarithm) | log natural)": "ln",
    "logarithm": "log",
    "maximum": "max",
    "minimum": "min",
    "modulus": "bmod",
    "infimum": "inf",
    "supremum": "sup",
    "probability": "Pr",
    # relations
    "there exists": "exists",
    "member [of]": "in",
    "for all": "forall",
    "[is] not equal [to]": "neq",
    "[is] greater [than] [or] equal [to]": "geq",
    "[is] less [than] [or] equal [to]": "leq",
    "[is] approximately [equal] [to]": "approx",
    "proportional [to]": "propto",
    "preference less [than]": "prec",
    "preference less equals": "preceq",
    "preference greater [than]": "succ",
    "preference greater equal": "succeq",
    # logic
    "logic and": "land",
    "logic or": "lor",
    "logic not": "lnot",
    #
    "left arrow": "leftarrow",
    "right arrow": "rightarrow",
    "up arrow": "uparrow",
    "down arrow": "downarrow",
    "left right arrow": "leftrightarrow",
    "maps to": "mapsto",
    "oh plus": "oplus",
    "oh times": "otimes",
    "big oh plus": "bigoplus",
    "big oh times": "bigotimes",
    #
    "dot dot dot": "dots",
    "diagonal dots": "ddots",
    "horizontal dots": "cdots",
    "vertical dots": "vdots",
    # sets
    "empty set": "emptyset",
    "subset": "subset",
    "superset": "supset",
    "strict subset": "subsetneq",
    "strict superset": "supsetneq",
    "intersection": "cap",
    "union": "cup",
    "GCD": "gcd",
    "cat hom": "hom",
    "kernel": "ker",
    "unit": "unitone",
    "unit two": "unittwo",
    "unit fraction": "unitfrac",
    "text fraction": "tfrac",
    "display fraction": "dfrac",
    "continued fraction": "cfrac",
    "continued fraction (left)": "cfracleft",
    "continued fraction (right)": "cfracright",
    "text binomial": "tbinom",
    "display binomial": "dbinom",
}

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

mod.list("tex_symbols", desc="TeX mathematical symbols")
ctx.lists['tex_symbols'] = symbols

mod.list("tex_greek_letters", desc="TeX greek letters")
ctx.lists["tex_greek_letters"] = {
    **greek_letters,
    **{f"big {k}": v.title() for k, v in greek_letters.items()}
}
