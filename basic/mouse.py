from user.utils import utilities
from talon import *
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

    def copy_mouse_position():
        """Copy the current mouse position coordinates"""
        position = ctrl.mouse_pos()
        clip.set_text((repr(position)))

    def copy_mouse_position_relative_window():
        """Copy the current mouse position coordinates"""
        x, y = ctrl.mouse_pos()
        rect = ui.active_window().rect
        clip.set_text((x - rect.left, y - rect.top))

    def mouse_move_relative_window(x: int, y: int):
        """"""
        rect = ui.active_window().rect
        actions.mouse_move(x+rect.left, y+rect.top)

    def mouse_move_center_active_window():
        """move the mouse cursor to the center of the currently active window"""
        rect = ui.active_window().rect
        ctrl.mouse_move(rect.left + (rect.width / 2), rect.top + (rect.height / 2))