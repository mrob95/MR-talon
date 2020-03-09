from user.imports import *
from pathlib import Path
import speakit
import re
# print(dir(talon))
BINDINGS = utilities.load_toml_relative("config/terminal.toml")
CORE = utilities.load_toml_relative("config/core.toml")

ctx = Context("terminal")
ctx.matches = r"""
app: mintty.exe
app: WindowsTerminal.exe
"""

# ctx = Context("terminal", func=lambda app, win: 'MINGW64 in win.title)
# ctx = Context("terminal", func=actions.context_matches(exe=["mintty.exe", "windowsterminal.exe"]))

commands = BINDINGS["commands"]
git_commands = BINDINGS["git_commands"]
ctx.lists["terminal_commands"] = commands.keys()
ctx.lists["git_commands"] = git_commands.keys()
# def clip_repo():
#     clip = Clipboard.get_system_text()
#     if clip.startswith("https://github.com"):
#         if clip.endswith("/"):
#             clip = clip[:-1]
#         Text(clip).execute()
#         if not clip.endswith(".git"):
#             Text(".git").execute()

ctx.commands = {
    "{terminal_commands}": lambda m: actions.exec_alternating(commands[m["terminal_commands"][0]]),

    "git {git_commands}": [Str("git "), lambda m: actions.exec_alternating(git_commands[m["git_commands"][0]])],
}

mingwctx = Context("mingw")
mingwctx.matches = r"""
title: /MINGW64/
"""

path_last_update = None
def update_maps(window):
    if not "MINGW64" in window.title:
        return
    global path_last_update
    current_path = Path(re.sub(r"MINGW64:/(\w)?", r"\1:", window.title))
    if current_path == path_last_update:
        return
    path_last_update = current_path
    mingwctx.lists["directories"] = file_utils.get_directory_map(current_path)
    mingwctx.lists["files"] = file_utils.get_file_map(current_path)
    mingwctx.lists["git_branches"], mingwctx.lists["git_remotes"], mingwctx.lists["git_files"] = file_utils.get_git_info(current_path)

ui.register("win_title", update_maps)
ui.register("win_focus", update_maps)

mingwctx.commands = {
    "CD {directories}": ['cd "', lambda m: Str(m["directories"][0])(m), '" && ls', Key("enter")],
    "file {files}": [lambda m: Str(m["files"][0])(m), " "],
    "git remote rename {git_remotes}": ["git remote rename ", lambda m: Str(m["git_remotes"][0])(m), " "],
    "git check out {git_branches}": ["git checkout ", lambda m: Str(m["git_branches"][0])(m), " "],
    "git add {git_files}": ["git add ", lambda m: Str(m["git_files"][0])(m), " "],
}

# mod.list('name', help='...')
# ctx.lists['self.name'] = {}

# @mingwctx.capture('directories', rule='{directories}')
# def directories(m):
#     return m["directories"][0]

# mingwctx.defines = r"""
# CD {directories}:
#     insert(directories)
#     insert(directories_1)
#     insert(directories_0)
#     insert('cd "{directories_1}" && ls')
#     Key(enter)

# git remote rename {git_remotes}:
#     insert("git remote {git_remotes} ")
# git check out {git_branches}:
#     insert("git checkout {git_branches} ")
# git add {git_files}:
#     insert("git add ")
#     insert(git_files_0)
# """