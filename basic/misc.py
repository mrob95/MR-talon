from user.imports import *
from subprocess import Popen
import os

PERSONAL = utilities.load_toml_relative("config/personal.toml")
CORE = utilities.load_toml_relative("config/core.toml")

searches = CORE["search"]


ctx = Context("misc")

ctx.commands = {
        "{personal}": lambda m: Str(m["personal"][0])(m),
        "close all notepads": lambda m: utilities.kill_notepad(),
        "open scratchpad": lambda m: Popen(["code"]),

        "{searches} search <dgndictation>++": lambda m: utilities.browser_search(m["dgndictation"], m["searches"][0]),

        "take screenshot": Key("win-shift-s"),
    }

ctx.lists["personal"] = PERSONAL
ctx.lists["searches"] = searches