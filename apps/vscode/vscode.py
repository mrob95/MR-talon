from pathlib import Path
from typing import Optional
from talon import Module, Context, ui, actions, registry, fs
import os
import re
import time
from user.code.speakify import create_voice_mapping

mod = Module()
ctx = Context()

ctx.matches = r"""
app: vscode
"""

@mod.action_class
class Actions:
    def vscode_palette(command: str) -> None:
        """Run a command using the command pallette"""
        actions.key("ctrl-shift-p")
        actions.insert(command)
        actions.key("enter")

    def vscode_select_to(digits: str) -> None:
        """Select from the current cursor position to the specified line"""
        actions.key("ctrl-k ctrl-b ctrl-g")
        actions.insert(digits)
        actions.key("enter end ctrl-k:2")

    def vscode_go_line(digits: str) -> None:
        """Go to the specified line"""
        actions.key("ctrl-g")
        actions.insert(digits)
        actions.key("enter")

    def vscode_mark() -> None:
        """Set mark"""
        actions.key("ctrl-k ctrl-b")

    def vscode_return() -> None:
        """Return to mark"""
        actions.key("ctrl-k ctrl-g escape")

    def vscode_grab_mouse() -> str:
        """Grab the identifier below the mouse cursor and return it"""
        actions.user.vscode_mark()
        actions.mouse_click()
        actions.mouse_click()
        t = actions.edit.selected_text()
        actions.user.vscode_return()
        return t

    def vscode_select_between(start: str, end: str) -> None:
        """Select between two line numbers"""
        if len(end) < len(start):
            # 242, 5  -> "24" + "5" = "245"
            # 242, 55 -> "2" + "55" = "255"
            # 100001, 255 -> "100" + "255" = "100255"
            end = start[:len(start) - len(end)] + end
        actions.user.vscode_go_line(start)
        actions.user.vscode_select_to(end)



@ctx.action_class('user')
class UserAction:
    def get_file_path() -> str:
        title = ui.active_window().title
        first, _, path = title.rpartition(" - ")
        if not first: # e.g. title = "Save As"
            return ""
        if "WSL: Ubuntu" in first:
            if path.startswith("/"):
                path = "\\\\wsl$\\Ubuntu" + path
            else:
                path = path.replace("~/", "\\\\wsl$\\Ubuntu\\home\\mike\\")
        if not os.path.exists(path):
            print(f"get_file_path found non-existent path {path}!")
        return path



@ctx.action_class('edit')
class EditActions:
    def line_clone(): actions.key('shift-alt-down')
    def save():
        actions.key("ctrl-s")
        actions.user.refresh_lists()
