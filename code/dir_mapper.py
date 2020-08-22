from user.imports import *
from pathlib import Path
import re

mod = Module()
ctx = Context()

mod.list("directories", desc="Currently accessible directories")
mod.list("files", desc="Currently accessible files")

path_last_update = None
def update_maps(window):
    try:
        global path_last_update
        if "MINGW64" in window.title:
            current_path = Path(re.sub(r"MINGW64:/(\w)?", r"\1:", window.title))
        elif "MSYS:" in window.title:
            current_path = Path(re.sub(r"MSYS:/(\w)?", r"\1:", window.title))
        elif window.app.exe and "explorer.exe" in window.app.exe.lower():
            remap = {
                "Downloads": "C:/Users/Mike/Downloads",
                "Documents": "C:/Users/Mike/Documents",
                "Pictures": "C:/Users/Mike/Pictures",
                "Mike": "C:/Users/Mike",
            }
            title = window.title
            if title in remap:
                title = remap[title]
            current_path = Path(title)
        else:
            return
        if not current_path.exists() or current_path == path_last_update:
            return
        path_last_update = current_path
        ctx.lists["user.directories"] = file_utils.get_directory_map(current_path)
        ctx.lists["user.files"] = file_utils.get_file_map(current_path)
        # mingwctx.lists["user.git_branches"], mingwctx.lists["user.git_remotes"], mingwctx.lists["user.git_files"] = file_utils.get_git_info(current_path)
    except:
        return

ui.register("win_title", update_maps)
ui.register("win_focus", update_maps)