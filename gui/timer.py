from datetime import time, datetime
from talon import imgui, cron

@imgui.open(x=1450, y=1042)
def timer(gui: imgui.GUI):
    if gui.button("Bag done"):
        timer.hide()

def check_time():
    for t in [13, 18]:
        if time(hour=t) <= datetime.now().time() <= time(hour=t, minute=1):
            timer.show()

cron.interval("59s", check_time)
