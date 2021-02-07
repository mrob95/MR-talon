from talon import *

mod = Module()

@imgui.open(x=0, y=30, software=False)
def window_info(gui: imgui.GUI):
    gui.text(f"{ui.active_app()}")
    gui.text(f"{ui.active_app().exe}")
    gui.text(f"{ui.active_window().title}")

@mod.action_class
class Actions:
    def window_info_toggle():
        """"""
        window_info.hide() if window_info.showing else window_info.show()
