"""
macros are not savable, but they are semantic in that functions are recorded,
not keypresses. This means that macros can interact with your computer state
such as by looking at what is in the clipboard, are referencing nearby text.
"""

from talon import *
from talon import actions

macro = []
macro_recording = False

def macro_record(p, j):
    global macro_recording
    if macro_recording:
        if j["cmd"] == "p.end" and j["grammar"] == "talon":
            m = actions.core.last_phrase()
            print(m)
            macro.append(m)

speech_system.engine.register("post:phrase", macro_record)

ctx = Context("macro")
mod = Module()

@mod.action_class
class Actions:
    def macro_start():
        """..."""
        global macro_recording
        global macro
        macro_recording = True
        macro = []


    def macro_stop():
        """..."""
        global macro
        global macro_recording
        if macro_recording:
            macro = macro[1:]
            macro_recording = False

    def macro_play():
        """..."""
        global macro
        actions.user.macro_stop()
        for item in macro:
            actions.core.run_phrase(item)