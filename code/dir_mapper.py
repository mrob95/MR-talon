from talon import ui, Module, Context, registry
from typing import Dict
from pathlib import Path
from itertools import islice
import re
from user.code.speakify import create_spoken_forms


MAX = 100

def get_directory_map(current_path: Path) -> Dict[str, str]:
    directories = [p.name for p in islice(current_path.iterdir(), MAX) if p.is_dir()]
    result = {}
    for directory in directories:
        for spoken_form in create_spoken_forms(directory):
            result[spoken_form] = directory
    return result


def get_file_map(current_path: Path) -> Dict[str, str]:
    files = [p for p in islice(current_path.iterdir(), MAX) if p.is_file()]
    result = {}
    for path in files:
        for spoken_form in create_spoken_forms(path.stem):
            result[spoken_form] = path.name
    return result


mod = Module()
ctx = Context()

mod.list("directories", desc="Currently accessible directories")
mod.list("files", desc="Currently accessible files")

path_last_update = None
def update_maps(window: ui.Window):
    try:
        global path_last_update
        if "MINGW64" in window.title:
            current_path = Path(re.sub(r"MINGW64:/(\w)?", r"\1:/", window.title))
        elif "MSYS:" in window.title:
            current_path = Path(re.sub(r"MSYS:/(\w)?", r"\1:/", window.title))
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
        ctx.lists["user.directories"] = get_directory_map(current_path)
        ctx.lists["user.files"] = get_file_map(current_path)
    except:
        return

ui.register("win_title", update_maps)
ui.register("win_focus", update_maps)
