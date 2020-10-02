from user.utils import utilities
from talon import Module, Context, actions, ctrl, ui
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
        ctrl.mouse_click(up=True)
        current_exe = ui.active_app().exe.lower()
        if "shellexperiencehost.exe" in current_exe:
            actions.sleep("100ms")
            utilities.save_clipboard_image()

    def mouse_move_relative(x: int, y: int):
        """"""
        x_cur, y_cur = ctrl.mouse_pos()
        actions.mouse_move(x_cur+x, y_cur+y)