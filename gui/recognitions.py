from talon import *

mod = Module()

phrase = "==="

@imgui.open(x=0, y=0, software=False)
def recognitions(gui: imgui.GUI):
    gui.text(phrase)

@mod.action_class
class Actions:
    def recognitions_toggle():
        """"""
        recognitions.hide() if recognitions.showing else recognitions.show()


def f(o):
    global phrase
    phrase = " ".join(o["phrase"]) or "==="

speech_system.register("post:phrase", f)
