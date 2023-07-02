from talon import ui, Module, Context, registry, actions, imgui, cron
import re
import os
from typing import Iterator, NamedTuple, List, Optional, Callable, Dict

from user.code.speakify import create_spoken_forms, map_numbers_to_spoken

mod = Module()
ctx = Context()

ctx.matches = r"""
app: windows_terminal
"""


@ctx.action_class('edit')
class EditActions:
    # https://github.com/mrob95/WindowsTerminal-config/blob/master/settings.json
    def paste(): actions.key('ctrl-shift-v')
    def copy():  actions.key('ctrl-shift-c')


@ctx.action_class("user")
class Actions:
    def get_current_path(window: ui.Window) -> Optional[str]:
        raw, _, _ = window.title.partition(" - ")
        if window.title.startswith("/c/"):
            result = "C:/" + raw[3:]
        elif window.title.startswith("/"):
            result = "\\\\wsl$\\Ubuntu\\" + raw.lstrip("/")
        else:
            result = raw.replace("~", "\\\\wsl$\\Ubuntu\\home\\mike")
        if not os.path.exists(result):
            return None
        return result
