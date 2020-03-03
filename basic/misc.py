from user.imports import *
from subprocess import Popen
import os

PERSONAL = utilities.load_toml_relative("config/personal.toml")
CORE = utilities.load_toml_relative("config/core.toml")

searches = CORE["search"]

ctx = Context("misc")

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

print(BASE_PATH)

ctx.keymap(
    {
        "{misc.personal}": actions.exec_str("misc.personal", PERSONAL),
        "close all notepads": lambda m: utilities.kill_notepad(),
        "open scratchpad": lambda m: Popen(["code"]),

        "{misc.searches} search <dgndictation>++": lambda m: utilities.browser_search(m["dgndictation"], searches[m["misc.searches"][0]]),

        "take screenshot": Key("win-shift-s"),
    }
)
ctx.set_list("personal", PERSONAL.keys())
ctx.set_list("searches", searches.keys())