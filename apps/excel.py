from talon import *
from typing import Optional

mod = Module()
ctx = Context()

<<<<<<< HEAD
@mod.capture(rule="<user.letters> <user.line_numbers>")
def xl_cell(m) -> str:
    "An excel cell"
    return f"{m.letters}{m.line_numbers}".upper()
=======
@mod.capture(rule="<user.letters> <user.digits>")
def xl_cell(m) -> str:
    "An excel cell"
    return f"{m.letters}{m.digits}".upper()
>>>>>>> 2fe6539... Excel

@mod.action_class
class Actions:
    def xl_select_cells(first: str, second: Optional[str] = None):
        """Select a cell, or range of cells"""
<<<<<<< HEAD
        print(first, second)
=======
>>>>>>> 2fe6539... Excel
        target = f"{first}:{second}" if second else first
        actions.key("ctrl-g")
        actions.insert(target)
        actions.key("enter")