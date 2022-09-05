from talon import Module, actions, imgui

mod = Module()

@imgui.open(x=1200, y=800)
def workspace_switcher(gui: imgui.GUI):
    if gui.button("|     <     |"):
        actions.user.workspace_previous(1)
    if gui.button("|     >     |"):
        actions.user.workspace_next(1)

@mod.action_class
class Actions:
    def workspace_switcher_toggle():
        """toggle workspace switcher imgui"""
        workspace_switcher.hide() if workspace_switcher.showing else workspace_switcher.show()
