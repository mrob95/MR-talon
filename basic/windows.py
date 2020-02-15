from ..imports import *
from win32gui import GetForegroundWindow, GetWindowText
import os

CORE = utilities.load_toml_relative("config/core.toml")

ctx = Context("windows")

directions = CORE["directions"]
repeat = {str(i): str(i) for i in range(20)}

repeated_action = actions.gen_repeated_action("windows.repeat")

def copy_bundle(m):
    # bundle = ui.active_app().bundle
    # clip.set(ui.active_app().exe)
    # clip.set(dir(ui.active_app()))Previous tab
    # app.notify('Copied app bundle', body='{}'.format(bundle))
    # print(dir(ui.active_app()))
    # print(dir(ui.active_window()))
    print(ui.active_app())
    print(ui.active_app().exe)
    print(f"Shadow window title: {ui.active_window().title}")
    print(f"Actual window title: {GetWindowText(GetForegroundWindow())}")
    print(talon.registry.last_active_contexts)
    # print(ui.windows())
    print(f"To check: {talon.windows.winevents.monitor.last_foreground}")
    print(f"Shadow: {ui.active_window().id}")
    print(f"Actual: {GetForegroundWindow()}")
    print(talon.windows.winevents._win_info(GetForegroundWindow()))
    print([w for w in ui.windows() if w.id == GetForegroundWindow()])
    # print(os.path.abspath(__file__))

last_window = ""

def print_non_natlink(i, o):
    if "natspeak" not in str(o):
        print(i, o)
    shadow_title = ui.active_window().title
    actual_title = GetWindowText(GetForegroundWindow())
    global last_window
    if shadow_title != actual_title:
        if last_window != shadow_title:
            print("Window state mismatch detected")
            print(f"Shadow window title: {shadow_title}")
            print(f"Actual window title: {actual_title}")
            last_window = shadow_title
        else:
            pass
    else:
        last_window = ""


from talon import ui
ui.register('win_focus', print)

def next_work(m):
    try:
        rep = int(m["windows.repeat"][0])
    except KeyError:
        rep = 1
    workspace.go_next(rep)

def previous_work(m):
    try:
        rep = int(m["windows.repeat"][0])
    except KeyError:
        rep = 1
    workspace.go_previous(rep)

ctx.keymap({
        "copy active bundle": copy_bundle,

        "window {windows.direction}": lambda m: press("win-" + directions[m["windows.direction"][0]]),
        "minimize": workspace.minimise,
        "maximise": workspace.maximise,
        "close window": workspace.close_window,
        "show work [spaces]": Key("win-tab"),
        "(create | new) work [space]": Key("win-ctrl-d"),
        "close work space": Key("win-ctrl-f4"),
        "next work [space] [{windows.repeat}]": next_work,
        "(previous | prior) work [space] [{windows.repeat}]": previous_work,

        "[go] work [space] {windows.repeat}": lambda m: workspace.go_to_n(int(m["windows.repeat"][0])),

        "send work [space] {windows.repeat}": lambda m: workspace.move_current_to_n(int(m["windows.repeat"][0])),
        "move work [space] {windows.repeat}": lambda m: workspace.move_current_to_n(int(m["windows.repeat"][0]), True),
        # "close all work [spaces]": workspace.close_all,
        "show window information": utilities.windowinfo,
    }
)
ctx.set_list("repeat", repeat.keys())
ctx.set_list("direction", directions.keys())