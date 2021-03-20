from talon import *
from pathlib import Path
from itertools import islice
import re

pattern = re.compile(r"[A-Z][a-z]*|[a-z]+|\d")
def create_spoken_forms(symbols, max_len=3):
    return [" ".join(list(islice(pattern.findall(s), max_len))) for s in symbols]
MAX = 100

def get_directory_map(current_path):
    directories = [p.name for p in islice(current_path.iterdir(), MAX) if p.is_dir()]
    spoken_forms = create_spoken_forms(directories)
    return dict(zip(spoken_forms, directories))

def get_file_map(current_path):
    files = [p for p in islice(current_path.iterdir(), MAX) if p.is_file()]
    spoken_forms = create_spoken_forms([p.stem for p in files])
    return dict(zip(spoken_forms, [f.name for f in files]))


mod = Module()
ctx = Context()

mod.list("directories", desc="Currently accessible directories")
mod.list("files", desc="Currently accessible files")

path_last_update = None
def update_maps(window):
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
