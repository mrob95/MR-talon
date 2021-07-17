from talon import ui, Module, Context, registry, actions, imgui, cron

@imgui.open(x=550, y=90)
def rss_gui(gui: imgui.GUI):
    if gui.button("SA"):
        actions.user.window_next(0)
        actions.key("ctrl-a")

def show_button(w: ui.Window):
    if w.app.exe.endswith("QuiteRSS.exe"):
        rss_gui.show()
    elif rss_gui.showing:
        rss_gui.hide()

ui.register('win_focus', show_button)