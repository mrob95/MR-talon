from talon import *

mod = Module()

phrase = "==="

@imgui.open(x=1200, y=1043)
def recognitions(gui: imgui.GUI):
    gui.text(phrase)

@mod.action_class
class Actions:
    def recognitions_toggle():
        """Toggle the recognition monitor"""
        recognitions.hide() if recognitions.showing else recognitions.show()


def f(o):
    global phrase
    if o["phrase"]:
        phrase = " ".join(o["phrase"])

speech_system.register("post:phrase", f)
recognitions.show()