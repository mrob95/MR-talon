from talon import *

mod = Module()
ctx = Context()

mod.tag("vscode")

ctx.matches = r"""
tag: vscode
"""

mark_window_title = None

@mod.action_class
class Actions:
    def vscode_palette(command: str) -> None:
        """"""
        actions.key("ctrl-shift-p")
        actions.insert(command)
        actions.key("enter")

    def vscode_select_to(digits: str) -> None:
        """"""
        actions.key("ctrl-k ctrl-b ctrl-g")
        actions.insert(digits)
        actions.key("enter end ctrl-k:2")

    def vscode_go_line(digits: str) -> None:
        """"""
        actions.key("ctrl-g")
        actions.insert(digits)
        actions.key("enter")

    def vscode_mark() -> None:
        """"""
        global mark_window_title
        mark_window_title = ui.active_window().title
        actions.key("ctrl-k ctrl-b")

    def vscode_return() -> None:
        """"""
        global mark_window_title
        current_window_title = ui.active_window().title
        if current_window_title == mark_window_title:
            actions.key("ctrl-k ctrl-g escape")
        else:
            actions.key("ctrl-k ctrl-right")
            actions.key("ctrl-k ctrl-g escape")

    def vscode_grab_mouse() -> str:
        """Grab the identifier below the mouse cursor and return it"""
        actions.user.vscode_mark()
        actions.mouse_click()
        actions.mouse_click()
        t = actions.edit.selected_text()
        actions.user.vscode_return()
        return t