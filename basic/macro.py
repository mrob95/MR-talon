"""
macros are not savable, but they are semantic in that functions are recorded,
not keypresses. This means that macros can interact with your computer state
such as by looking at what is in the clipboard, are referencing nearby text.
"""
from talon import *
from talon import imgui

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
        # First will be "macro start"
        for item in macro[1:]:
            actions.core.run_phrase(item)
            actions.sleep("20ms")

def f(o):
    global num_recorded
    if recording and "parsed" in o:
        macro.append(actions.core.last_phrase())
        num_recorded += 1

speech_system.register("post:phrase", f)
