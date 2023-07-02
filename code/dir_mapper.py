from talon import ui, Module, Context, registry, actions
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


mod = Module()
ctx = Context()

mod.list("directories", desc="Currently accessible directories")
mod.list("files", desc="Currently accessible files")
mod.list("makefile_targets", desc="Makefile targets in the current directory")

path_last_update = None
def update_maps(window: ui.Window):
    global path_last_update
    try:
        current_path = actions.user.get_current_path(window)
    except NotImplementedError:
        return
    if current_path is None or current_path == path_last_update:
        return
    current_path = Path(current_path)
    path_last_update = current_path
    ctx.lists["user.directories"] = get_directory_map(current_path)
    ctx.lists["user.files"] = get_file_map(current_path)
    ctx.lists["user.makefile_targets"] = get_makefile_map(current_path)

@mod.action_class
class Actions:
    def get_current_path(window: ui.Window) -> Optional[str]:
        """Returns the current path"""

def crash(w):
    raise Exception("crash")

# ui.register("win_title", crash)
# ui.register("win_focus", crash)
ui.register("win_title", update_maps)
ui.register("win_focus", update_maps)
