from ..imports import *

CORE = utilities.load_toml_relative("config/core.toml")

ctx = Context("windows")

directions = CORE["directions"]
repeat = {str(i): str(i) for i in range(20)}

repeated_action = actions.gen_repeated_action("windows.repeat")

def copy_bundle(m):
    bundle = ui.active_app().bundle
    clip.set(ui.active_app().exe)
    # clip.set(dir(ui.active_app()))
    # app.notify('Copied app bundle', body='{}'.format(bundle))

ctx.keymap(
    {
        "copy active bundle": copy_bundle,

        "window {windows.direction}": lambda m: press("win-" + directions[m["windows.direction"]]),
        "minimize": workspace.minimise,
        "maximise": workspace.maximise,
        "close window": Key("alt-f4"),
        "show work [spaces]": Key("win-tab"),
        "(create | new) work [space]": Key("win-ctrl-d"),
        "close work space": Key("win-ctrl-f4"),
        "next work [space] [{windows.repeat}]": repeated_action(Key("win-ctrl-right")),
        "(previous | prior) work [space] [{windows.repeat}]": repeated_action(Key("win-ctrl-left")),

        "[go] work [space] {windows.repeat}": lambda m: workspace.go_to_n(int(m["windows.repeat"])),

        "send work [space] {windows.repeat}": lambda m: workspace.move_current_to_n(int(m["windows.repeat"])),
        "move work [space] {windows.repeat}": lambda m: workspace.move_current_to_n(int(m["windows.repeat"]), True),
        # "close all work [spaces]": workspace.close_all,
        "show window information": utilities.windowinfo,
    }
)
ctx.set_list("repeat", repeat.keys())
ctx.set_list("direction", directions.keys())