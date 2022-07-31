from talon import ui, Module, Context, registry, actions, imgui, cron
from typing import Optional

mod = Module()
ctx = Context()

mod.list("file_variables")
mod.list("file_functions")


@imgui.open(x=0, y=30)
def list_info(gui: imgui.GUI):
    # print(registry.lists["user.file_variables"])
    for spoken, actual in registry.lists["user.file_variables"][0].items():
        gui.text(f"{spoken}: {actual}")

@mod.action_class
class Actions:
    def get_file_contents() -> str:
        """Return the full contents of the current file"""
        raise NotImplementedError

    def refresh_lists(file_contents: str):
        """Parse the passed string"""
        raise NotImplementedError

    def list_info_toggle():
        """toggle window info imgui"""
        list_info.hide() if list_info.showing else list_info.show()


def refresh(_):
    try:
        contents = actions.user.get_file_contents()
        actions.user.refresh_lists(contents)
    except NotImplementedError:
        return

ui.register("win_title", refresh)
