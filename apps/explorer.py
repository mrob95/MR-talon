from ..imports import *

BRING = utilities.load_toml_relative("config/bringme.toml")

folders = BRING["folder"]

repeated_action = actions.gen_repeated_action("explorer.n")

repeat = {str(i): str(i) for i in range(20)}

ctx = Context("explorer", func=lambda app, win: 'explorer.exe' in app.exe.lower() or "save" in win.title.lower())

ctx.keymap({
    "address bar": Key("alt-d"),
    "new folder": Key("ctrl-shift-n"),
    "new file": Key("alt-f, w, t"),
    "[(show | file | folder)] properties": Key("alt-enter"),
    "go up [{explorer.n}]": repeated_action(Key("alt-up")),
    "page back [{explorer.n}]": repeated_action(Key("alt-left")),
    "page forward [{explorer.n}]": repeated_action(Key("alt-right")),

    "go {explorer.folders}": [Key("ctrl-l"), actions.exec_str("explorer.folders", folders), Key("enter")],
})
ctx.set_list("n", repeat.keys())
ctx.set_list("folders", folders.keys())