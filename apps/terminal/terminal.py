from talon import *

mod = Module()
ctx = Context()

ctx.matches = r"""
tag: user.terminal
"""

lengths = []

@ctx.action_class("main")
class Actions:
    def auto_format(text: str) -> str:
        """"""
        global lengths
        lengths.append(len(text))
        return text


@ctx.action_class("edit")
class Actions:
    def undo():
        """"""
        global lengths
        print(lengths)
        if lengths:
            actions.key(f"backspace:{lengths.pop()}")

