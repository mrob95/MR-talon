from datetime import time, datetime
from talon import imgui, cron, actions, ui, Module, Context

mod = Module()
ctx = Context()


@imgui.open(x=2150, y=2220)
def google_meet(gui: imgui.GUI):
    if gui.button("Mute"):
        actions.key("ctrl-shift-5")
    #     speech_system.engine_mimic("go to sleep")
    # if gui.button("Code"):
    #     speech_system.engine_mimic("wake up")


@mod.action_class
class Actions:
    def google_meet_toggle():
        """Toggle google meet helper"""
        google_meet.hide() if google_meet.showing else google_meet.show()
