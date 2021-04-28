from talon import ui, Module, Context, registry, actions, imgui, cron
from typing import Optional

mod = Module()
ctx = Context()

@mod.capture(rule="<user.letters> <user.line_numbers>")
def xl_cell(m) -> str:
    "An excel cell"
    return f"{m.letters}{m.line_numbers}".upper()

@mod.action_class
class Actions:
    def xl_select_cells(first: str, second: Optional[str] = None):
        """Select a cell, or range of cells"""
        target = f"{first}:{second}" if second else first
        actions.key("ctrl-g")
        actions.insert(target)
        actions.key("enter")