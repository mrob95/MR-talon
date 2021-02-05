"""
macros are not savable, but they are semantic in that functions are recorded,
not keypresses. This means that macros can interact with your computer state
such as by looking at what is in the clipboard, are referencing nearby text.
"""
from talon import *

macro = []
recording = False
num_recorded = 0

ctx = Context("macro")
mod = Module()


@imgui.open(x=1300, y=1045, software=False)
def gui_macro_recording(gui: imgui.GUI):
    global num_recorded
    gui.text(f"Macro recording: {num_recorded}")


@mod.action_class
class Actions:
    def macro_start():
        """record a new macro"""
        global macro
        global recording
        gui_macro_recording.show()
        macro = []
        recording = True

    def macro_stop():
        """stop recording"""
        global recording
        gui_macro_recording.hide()
        recording = False

    def macro_play():
        """play recorded macro"""
        actions.user.macro_stop()
        # :-1 because we don't want to replay `macro play`
        for words in macro[:-1]:
            print(words)
            actions.mimic(words)

def fn(d):
    global num_recorded
    if recording and "parsed" in d:
        macro.append(d["parsed"]._unmapped)
        num_recorded += 1

speech_system.register("pre:phrase", fn)
