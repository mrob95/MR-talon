import time
from datetime import time, datetime
from talon import *

mod = Module()

@imgui.open(x=1450, y=1043)
def pomodoro(gui: imgui.GUI):
    cur_time = datetime.now().time()
    min_scaled = cur_time.minute % 30
    if min_scaled < 25:
        gui.text(f"Work: {24-min_scaled:02d} : {59-cur_time.second:02d}")
    else:
        gui.text(f"Rest: {29-min_scaled:02d} : {59-cur_time.second:02d}")


@mod.action_class
class Actions:
    def pomodoro_toggle():
        """Toggle pomodoro"""
        pomodoro.hide() if pomodoro.showing else pomodoro.show()
