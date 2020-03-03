from user.imports import *

ctx = Context("latex", func=actions.context_matches(title=".tex"))

BINDINGS = utilities.load_toml_relative("config/latex.toml")


def begin_end(item):
    env, arg = (item[0], item[1]) if isinstance(item, list) else (item, "")
    return [f"\\begin{{{env}}}{arg}", Key("enter enter"), f"\\end{{{env}}}", Key("up")]

def package(item):
    opts, pack = (item[0], item[1]) if isinstance(item, list) else ("", item)
    return f"\\usepackage{opts}{{{pack}}}"

def symbol(item):
    if isinstance(item, list):
        num_args = int(item[1])
        return [f"\\{item[0]}", "{}"*num_args, Key("left "*(2*num_args-1))]
    else:
        return f"\\{item} "

ctx.keymap({
    # e.g. \documentclass{article}
    **{f"document class {k}": f"\\documentclass{{{v}}}" for k, v in BINDINGS["document_classes"].items()},
    # \begin{document}
    **{f"begin {k}": begin_end(v) for k, v in BINDINGS["environments"].items()},
    # \usepackage{geometry}
    **{f"use package {k}": package(v) for k, v in BINDINGS["packages"].items()},
    # \section{}
    **{f"insert {k}": [f"\\{v}{{}}", Key("left")] for k, v in BINDINGS["command"].items()},
    # \item
    **{f"insert {k}": f"\\{v} " for k, v in BINDINGS["commandnoarg"].items()},
    # \alpha
    **{f"greek {k}": f"\\{v} " for k, v in BINDINGS["greek_letters"].items()},
    # \Alpha
    **{f"greek big {k}": f"\\{v.title()} " for k, v in BINDINGS["greek_letters"].items()},
    # \sqrt{} | \int
    **{f"symbol {k}": symbol(v) for k, v in BINDINGS["symbols"].items()},
    **{f"symbol {k}": actions.Alternating(v) for k, v in BINDINGS["misc_symbols"].items()},
})