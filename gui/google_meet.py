from datetime import time, datetime
from talon import imgui, cron, actions, ui, Module, speech_system

@imgui.open(x=1450, y=1042)
def google_meet(gui: imgui.GUI):
    if gui.button("Talk"):
        speech_system.engine_mimic("go to sleep")
        # actions.key("F17")
    if gui.button("Code"):
        speech_system.engine_mimic("wake up")
        # actions.key("F17")

def activate_if_google_meet(w: ui.Window):
    if "google meet" in w.title:
        google_meet.show()


ui.register("win_title", activate_if_google_meet)

mod = Module()

@mod.action_class
class Actions:
    def google_meet_toggle():
        """Toggle google meet helper"""
        google_meet.hide() if google_meet.showing else google_meet.show()
