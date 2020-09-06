from talon import *

mod = Module()
ctx = Context()
ctx.matches = r"""
app: RStudio
"""

@mod.action_class
class Actions:
    def r_paste_into_console(pattern: str):
        """"""
        with clip.capture() as s:
            actions.edit.copy()
        text = s.get()
        actions.key("ctrl-2")
        actions.insert(pattern.replace("{text}", text))
        actions.key("enter ctrl-1")

