from talon import ui, Module, Context, actions, imgui
from pyvda import get_apps_by_z_order

mod = Module()
ctx = Context()
current_windows = []
counter = 0

mod.tag("window_switcher_showing", "Set when the window switcher is showing")

@imgui.open()
def window_switcher(gui: imgui.GUI):
    global current_windows
    if not current_windows:
        windows = {w.id: w for w in ui.windows()}
        for a in get_apps_by_z_order():
            w = windows[a.hwnd]
            current_windows.append(w)

    for i, w in enumerate(current_windows, 1):
        gui.text(f"{i: >2}. {w.app.name: <40} {w.title}")


@mod.action_class
class Actions:
    def window_switcher_toggle():
        """Toggle the window switcher UI"""
        if window_switcher.showing:
            window_switcher.hide()
            ctx.tags = []
        else:
            window_switcher.show()
            ctx.tags = ["user.window_switcher_showing"]
        global current_windows, counter
        current_windows = []

    def window_switcher_focus(i: int):
        """Focus one of the windows in the window switcher list"""
        global current_windows
        current_windows[i-1].focus()
        actions.user.window_switcher_toggle()
