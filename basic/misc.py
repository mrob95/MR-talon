from user.imports import *
from subprocess import Popen
from talon import speech_system, actions
import os
import time
import dragonfly

def test_music(m):
    dragonfly.Key("playpause").execute()

PERSONAL = utilities.load_toml_relative("config/personal.toml")
CORE = utilities.load_toml_relative("config/core.toml")

searches = CORE["search"]


ctx = Context("misc")


# def ginfo(w):
#     print(hash(str(speech_system.engine.engine.grammar_blobs['talon_main'][2])))

# ui.register('post:app_activate', ginfo)

ctx.commands = {
        # "music play": test_music,
        "{personal}": lambda m: Str(m["personal"])(m),
        "close all notepads": lambda m: utilities.kill_notepad(),
        "open scratchpad": lambda m: Popen(["code"]),
        # "print grammar blob": ginfo,

        "{searches} search <dgndictation>++": lambda m: utilities.browser_search(m["dgndictation"], m["searches"]),

        "take screenshot": Key("win-shift-s"),
    }

ctx.lists["personal"] = PERSONAL
ctx.lists["searches"] = searches