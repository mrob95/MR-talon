from user.imports import *
from subprocess import Popen

BINDINGS = utilities.load_toml_relative("config/r.toml")

ctx = Context("R", func=actions.context_matches([
    # ".r",
    "rstudio"]))

commands = BINDINGS["commands"]
functions = BINDINGS["r_functions"]
graphs = BINDINGS["r_graph"]
cheatsheets = BINDINGS["cheatsheets"]

def r_func(data):
    if isinstance(data, str):
        return [f"{data}()", Key("left")]
    else:
        return [f"{data[0]}({data[1]})", Key(("left "*int(data[2])).strip())]

ctx.keymap({
    **{k: actions.Alternating(v) for k, v in commands.items()},
    **{f"fun {k}": r_func(v) for k, v in functions.items()},
    **{f"graph {k}": r_func(v) for k, v in graphs.items()},
    **{f"library {k}": f"library({v})" for k, v in graphs.items()},
    **{f"cheatsheet {k}": lambda m: Popen(["SumatraPDF", f"%USERPROFILE%/Documents/cheatsheets/R/{v}.pdf"]) for k, v in cheatsheets.items()},
})