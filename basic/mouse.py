from user.imports import *
from talon import Module, Context, actions, ctrl
import time

mod = Module()
ctx = Context()

@mod.action_class
class Actions:
    def mouse_drag():
        """Drag"""
        ctrl.mouse_click(down=True)

    def mouse_release():
        """Drag"""
        current_exe = ui.active_app().exe.lower()
        if "shellexperiencehost.exe" in current_exe:
            ctrl.mouse_click(up=True)
            actions.sleep("100ms")
            utilities.save_clipboard_image()
        ctrl.mouse_click(up=True)
