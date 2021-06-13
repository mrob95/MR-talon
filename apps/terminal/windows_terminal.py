from talon import ui, Module, Context, registry, actions, imgui, cron
import re
from typing import Iterator, NamedTuple, List, Optional, Callable, Dict

from user.code.speakify import create_spoken_forms, map_numbers_to_spoken
from user.accessibility.terminal.wt import WindowsTerminalAccess, first_where

mod = Module()
ctx = Context()

ctx.matches = r"""
tag: user.terminal
and title: /MSYS:.*/
"""

def parse_git_status_to_speakable(lines: List[str]) -> Dict[str, str]:
    file_map = {}
    current = 1

    for line in lines:
        contains_file = re.match(r"^\s+[^(\s]", line)
        if contains_file:
            # first group is e.g. 'modified:' or 'deleted:'
            file_name_match = re.match(r"^\s+(?P<action>[a-z\s]+:\s+)?(?P<filename>.+?)(?P<info> \(.+?\))?$", line)
            if file_name_match:
                file_name = file_name_match.group("filename")
                file_map[map_numbers_to_spoken(current)] = file_name
                current += 1
                # for spoken in create_spoken_forms(file_name):
                #     file_map[spoken] = file_name
            else:
                # Shouldn't ever hit this, means the regexes are missing something
                print(line)

    return file_map


PS1 = r"^Mike@DESKTOP-74I5GN5 MSYS (?P<dir>.+?)(?: \((?P<branch>.+?)\))?$"
PROMPT = r"^\$(?: (?P<cmd>.+?))?$"

last_end = -1

# def update(window: Optional[ui.Window] = None):
#     global last_end

#     if window is None or window.app.exe.endswith("WindowsTerminal.exe"):
#         w = WindowsTerminalAccess(PS1, PROMPT)
#         res = w.get_command_results(w.get_document_text())
#         # git_status = first_where(lambda c: "git status" in c.command, res, 3)
#         # print(f'git_status = {git_status}')
#         # if git_status and git_status.end != last_end:
#         #     ctx.lists["user.git_status_items"] = parse_git_status_to_speakable(git_status.lines)
#         #     last_end = git_status.end
#         last_command = next(res)
#         if "git add -p" in last_command.command:
#             ctx.tags = ["user.git_patching"]
#         else:
#             ctx.tags = []

# @ctx.action_class("main")
# class CoreActions:
#     def key(key: str):
#         actions.next(key)
#         if "enter" in key:
#             actions.sleep("500ms")
#             update(None)

# ui.register("win_title", update)
# ui.register("win_focus", update)

@imgui.open(x=0, y=600)
def numbers_gui(gui: imgui.GUI):
    filenames = registry.lists["user.git_status_items"][0].values()
    for i, filename in enumerate(filenames, 1):
        gui.text(f"{i}. {filename}")

@mod.action_class
class Actions:
    def numbers_gui_flash():
        """flash the numbers gui"""
        numbers_gui.show()
        cron.after("2s", lambda: numbers_gui.hide())