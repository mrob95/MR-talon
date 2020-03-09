from user.imports import *
from subprocess import Popen
from pathlib import Path
import speakit

BRING = utilities.load_toml_relative("config/bringme.toml")
folders = BRING["folder"]

repeated_action = actions.gen_repeated_action("repeat")
repeat = {str(i): str(i) for i in range(20)}

def current_directory():
    title = ui.active_window().title
    remap = {
        "Downloads": "C:\\Users\\Mike\\Downloads",
        "Documents": "C:\\Users\\Mike\\Documents",
        "Pictures": "C:\\Users\\Mike\\Pictures",
        "Mike": "C:\\Users\\Mike",
    }
    if title in remap.keys():
        title = remap[title]
    return title


ctx = Context("explorer")
ctx.matches = r"""
app: Windows Explorer
"""


path_last_update = None

def update_maps(window):
    if not window.app.exe or not "explorer.exe" in window.app.exe.lower() or window.title != ui.active_window().title:
        return
    remap = {
        "Downloads": "C:\\Users\\Mike\\Downloads",
        "Documents": "C:\\Users\\Mike\\Documents",
        "Pictures": "C:\\Users\\Mike\\Pictures",
        "Mike": "C:\\Users\\Mike",
    }
    title = window.title
    if title in remap.keys():
        title = remap[title]
    global path_last_update
    current_path = Path(title)
    if current_path == path_last_update or not current_path.is_dir():
        return
    path_last_update = current_path
    ctx.lists["directories"] = file_utils.get_directory_map(current_path)
    ctx.lists["files"] = file_utils.get_file_map(current_path)

ui.register("win_title", update_maps)
ui.register("win_focus", update_maps)


ctx.commands = {
    "follow {directories}": [Key("home"), lambda m: Str(m["directories"][0])(m), Key("enter")],
    "open {files}": [Key("home"), lambda m: Str(m["files"][0])(m), Key("enter")],
    "select {directories}": [Key("home"), lambda m: Str(m["directories"][0])(m)],
    "select {files}": [Key("home"), lambda m: Str(m["files"][0])(m)],
    # ---
    "address bar": Key("alt-d"),
    "new folder": Key("ctrl-shift-n"),
    "new file": Key("alt-f, w, t"),
    "[(show | file | folder)] properties": Key("alt-enter"),
    "go up [{repeat}]": repeated_action(Key("alt-up")),
    "page back [{repeat}]": repeated_action(Key("alt-left")),
    "page forward [{repeat}]": repeated_action(Key("alt-right")),

    "go {folders}": [Key("ctrl-l"), lambda m: Str(m["folders"][0])(m), Key("enter")],

    "terminal here": lambda m: utilities.terminal(current_directory().replace("\\", "/")),
    "new window": lambda m: Popen(["explorer", current_directory()]),
}
ctx.lists["repeat"] = repeat
ctx.lists["folders"] = folders