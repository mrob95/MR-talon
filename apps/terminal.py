from user.imports import *
from pathlib import Path
import re

BINDINGS = utilities.load_toml_relative("config/terminal.toml")
CORE = utilities.load_toml_relative("config/core.toml")

mingwctx = Context("mingw")
mingwctx.matches = r"""
title: /MINGW64/
title: /MSYS/
"""

path_last_update = None
def update_maps(window):
    global path_last_update
    if "MINGW64" in window.title:
        current_path = Path(re.sub(r"MINGW64:/(\w)?", r"\1:", window.title))
    elif "MSYS:" in window.title:
        current_path = Path(re.sub(r"MSYS:/(\w)?", r"\1:", window.title))
    else:
        return
    if current_path == path_last_update:
        return
    path_last_update = current_path
    mingwctx.lists["directories"] = file_utils.get_directory_map(current_path)
    mingwctx.lists["files"] = file_utils.get_file_map(current_path)
    # mingwctx.lists["git_branches"], mingwctx.lists["git_remotes"], mingwctx.lists["git_files"] = file_utils.get_git_info(current_path)

ui.register("win_title", update_maps)
ui.register("win_focus", update_maps)

mingwctx.defines = r"""
CD {directories}:
    insert('cd "{directories}" && ls')
    key(enter)
file {files}:
    insert('{files} ')
folder {directories}:
    insert('{directories}/')
# git remote rename {git_remotes}:
#     insert("git remote rename {git_remotes} ")
# git check out {git_branches}:
#     insert("git checkout {git_branches} ")
# git add {git_files}:
#     insert("git add ")
"""