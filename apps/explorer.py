from ..imports import *
from subprocess import Popen 

BRING = utilities.load_toml_relative("config/bringme.toml")
folders = BRING["folder"]

repeated_action = actions.gen_repeated_action("explorer.n")
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

ctx = Context("explorer", func=actions.context_matches(exe="explorer.exe", title=["save", "open", "choose", "select"]))

ctx.keymap({
    "address bar": Key("alt-d"),
    "new folder": Key("ctrl-shift-n"),
    "new file": Key("alt-f, w, t"),
    "[(show | file | folder)] properties": Key("alt-enter"),
    "go up [{explorer.n}]": repeated_action(Key("alt-up")),
    "page back [{explorer.n}]": repeated_action(Key("alt-left")),
    "page forward [{explorer.n}]": repeated_action(Key("alt-right")),

    "go {explorer.folders}": [Key("ctrl-l"), actions.exec_str("explorer.folders", folders), Key("enter")],

    "terminal here": lambda m: utilities.terminal(current_directory().replace("\\", "/")),
    "new window": lambda m: Popen(["explorer", current_directory()]),
})
ctx.set_list("n", repeat.keys())
ctx.set_list("folders", folders.keys())