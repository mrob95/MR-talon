from talon import *

mod = Module()
ctx = Context()

ctx.matches = r"""
app: Visual Studio Code
"""

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

