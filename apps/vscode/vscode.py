from typing import Optional
from talon import Module, Context, ui, actions, registry, fs
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


@ctx.action_class('user')
class UserAction:
    def get_file_contents() -> str:
        actions.user.vscode_mark()
        actions.key("ctrl-a")
        t = actions.edit.selected_text()
        actions.user.vscode_return()
        return t


@ctx.action_class('edit')
class EditActions:
    # def save():
    #     actions.key("ctrl-s")
    #     try:
    #         actions.user.refresh_lists(None)
    #     except NotImplementedError:
    #         return
    #     try:
    #         contents = actions.user.get_file_contents()
    #     except NotImplementedError:
    #         return

    #     actions.user.refresh_lists(contents)

    def line_clone(): actions.key('shift-alt-down')
