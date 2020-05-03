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
app: /.*/
and title: /Save/
app: /.*/
and title: /Open/
app: /.*/
and title: /Browse/
app: /.*/
and title: /Select/
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


# ctx.commands = {
#     "follow {directories}": [Key("home"), lambda m: Str(m["directories"])(m), Key("enter")],
#     "open {files}": [Key("home"), lambda m: Str(m["files"])(m), Key("enter")],
#     "select {directories}": [Key("home"), lambda m: Str(m["directories"])(m)],
#     "select {files}": [Key("home"), lambda m: Str(m["files"])(m)],
#     # ---
#     "address bar": Key("alt-d"),
#     "new folder": Key("ctrl-shift-n"),
#     "new file": Key("alt-f, w, t"),
#     "[(show | file | folder)] properties": Key("alt-enter"),
#     "go up [{repeat}]": repeated_action(Key("alt-up")),
#     "page back [{repeat}]": repeated_action(Key("alt-left")),
#     "page forward [{repeat}]": repeated_action(Key("alt-right")),

#     "go {folders}": [Key("ctrl-l"), lambda m: Str(m["folders"])(m), Key("enter")],

#     # "terminal here": lambda m: utilities.terminal(current_directory().replace("\\", "/")),
#     "terminal here": [Key("ctrl-l"), Str("wt.exe"), Key("enter")],
#     "new window": lambda m: Popen(["explorer", current_directory()]),

#     "dot {exts}": [Key("."), lambda m: Str(m["exts"])(m)],
# }
ctx.lists["repeat"] = repeat
ctx.lists["folders"] = folders
ctx.lists["exts"] = {
    "pie": "py",
    "talon": "talon",
    "sequel": "sql",
    "rust": "rs",
    "tech": "tex",
}

ctx.defines = r"""
follow {directories}:
    key("home")
    insert(directories)
    key("enter")
open {files}:
    key("home")
    insert(files)
    key("enter")
select {directories}:
    key("home")
    insert(directories)
select {files}:
    key("home")
    insert(files)
# ---
address bar: key("alt-d")
new folder: key("ctrl-shift-n")
new file: key("alt-f w t")
[(show | file | folder)] properties: key("alt-enter")
go up <user.n20>: key("alt-up:{n20}")
page back <user.n20>: key("alt-left:{n20}")
page forward <user.n20>: key("alt-right:{n20}")
go {folders}:
    key("ctrl-l")
    insert(folders)
    key("enter")

# "terminal here: lambda m: utilities.terminal(current_directory().replace("\\", "/")),
terminal here:
    key("ctrl-l")
    insert("wt.exe")
    key("enter")
dot {exts}:
    key(".")
    insert(exts)
"""