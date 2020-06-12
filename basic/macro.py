"""
macros are not savable, but they are semantic in that functions are recorded,
not keypresses. This means that macros can interact with your computer state
such as by looking at what is in the clipboard, are referencing nearby text.
"""

from talon.voice import Context, talon, Key, Str, press
from talon.engine import engine
from talon import actions
# actions.core.recent_commands()

macro = []
macro_recording = False

def macro_record(j):
    global macro_recording
    if macro_recording:
        if j["cmd"] == "p.end" and j["grammar"] == "talon":
            m = actions.core.last_phrase()
            print(m)
            macro.append(m)

def macro_start(m):
    global macro_recording
    global macro
    macro_recording = True
    macro = []


def macro_stop(m):
    global macro
    global macro_recording
    if macro_recording:
        macro = macro[1:]
        macro_recording = False


def macro_play(m):
    macro_stop(None)
    try:
        repeat = int(m["repeat"])
    except KeyError:
        repeat = 1
    for _ in range(repeat):
        for item in macro:
            actions.core.run_phrase(item)

engine.register("post:phrase", macro_record)


ctx = Context("macro")
ctx.commands = {
    "macro (start | record)": macro_start,
    "macro stop": macro_stop,
    "macro play [{repeat}]": macro_play,
    # "macro print": macro_print,
}
ctx.lists["repeat"] = [str(i) for i in range(20)]