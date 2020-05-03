from user.imports import *
from win32gui import GetForegroundWindow, GetWindowText
import os

CORE = utilities.load_toml_relative("config/core.toml")

ctx = Context("windows")

directions = CORE["directions"]
repeat = {str(i): str(i) for i in range(20)}

repeated_action = actions.gen_repeated_action("repeat")

def copy_bundle(m):
    # bundle = ui.active_app().bundle
    # clip.set(ui.active_app().exe)
    # clip.set(dir(ui.active_app()))Previous tab
    # app.notify('Copied app bundle', body='{}'.format(bundle))
    # print(dir(ui.active_app()))
    # print(dir(ui.active_window()))
    print(f"Shadow app: {ui.active_app()}")
    print(f"Shadow app exe: {ui.active_app().exe}")
    print(f"Shadow window title: {ui.active_window().title}")
    print(f"Actual window title: {GetWindowText(GetForegroundWindow())}")
    # print(ui.windows())
    print(f"To check: {talon.windows.winevents.monitor.last_foreground}")
    print(f"Shadow hwnd: {ui.active_window().id}")
    print(f"Actual hwnd: {GetForegroundWindow()}")
    print(talon.windows.winevents._win_info(GetForegroundWindow()))
    print([w for w in ui.windows() if w.id == GetForegroundWindow()])
    # print(os.path.abspath(__file__))


ctx.commands = {
    "copy active bundle": copy_bundle,

    # "window {direction}": lambda m: press("win-" + m["direction"]),
    "show window information": utilities.windowinfo,
}
