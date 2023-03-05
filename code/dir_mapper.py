from talon import ui, Module, Context, registry
from typing import Dict, Optional
from pathlib import Path
from itertools import islice
import re
import time
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


def get_makefile_map(current_path: Path) -> Dict[str, str]:
    makefile_path = current_path / "Makefile"
    if not makefile_path.exists():
        return {}

    result = {}
    contents = makefile_path.read_text()
    for line in contents.split("\n"):
        m = re.match(r"^([^\.\t]+):", line)
        if not m:
            continue
        target = m.group(1)
        for spoken_form in create_spoken_forms(target):
            result[spoken_form] = target
    return result


def get_current_path(window: ui.Window) -> Optional[Path]:
    if "MINGW64" in window.title:
        return Path(re.sub(r"MINGW64:/(\w)?", r"\1:/", window.title))
    elif "MSYS:" in window.title:
        return Path(re.sub(r"MSYS:/(\w)?", r"\1:/", window.title))
    elif "mike@DESKTOP-74I5GN5: /mnt" in window.title:
        return Path(re.sub(r"^mike@DESKTOP.+: /mnt/(\w)?", r"\1:/", window.title))
    elif "mike@DESKTOP-74I5GN5: ~" in window.title:
        # debian wsl
        return Path(window.title.replace("mike@DESKTOP-74I5GN5: ~", "\\\\wsl$\\Ubuntu\\home\\mike"))
    elif "WindowsTerminal.exe" in window.app.exe:
        raw, _, _ = window.title.partition(" - ")
        if window.title.startswith("/c/"):
            return Path("C:/" + raw[3:])
        elif window.title.startswith("/"):
            return Path("\\\\wsl$\\Ubuntu\\" + raw.lstrip("/"))
        else:
            return Path(raw.replace("~", "\\\\wsl$\\Ubuntu\\home\\mike"))
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
        return Path(title)
    else:
        return None


mod = Module()
ctx = Context()

mod.list("directories", desc="Currently accessible directories")
mod.list("files", desc="Currently accessible files")
mod.list("makefile_targets", desc="Makefile targets in the current directory")

path_last_update = None
def update_maps(window: ui.Window):
    try:
        global path_last_update
        current_path = get_current_path(window)
        # print(f'current_path = {current_path}')
        if current_path is None or not current_path.exists() or current_path == path_last_update:
            # print("update_maps: done")
            return
        path_last_update = current_path
        # start = time.perf_counter()
        ctx.lists["user.directories"] = get_directory_map(current_path)
        # print(f"update_maps: Directories done at {time.perf_counter()-start}s")
        ctx.lists["user.files"] = get_file_map(current_path)
        # print(f"update_maps: Files done at {time.perf_counter()-start}s")
        ctx.lists["user.makefile_targets"] = get_makefile_map(current_path)
        # print(f"update_maps: Makefile done at {time.perf_counter()-start}s")
    except:
        return

ui.register("win_title", update_maps)
# ui.register("win_focus", update_maps)
