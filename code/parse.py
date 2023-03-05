from talon import ui, Module, Context, registry, actions, imgui, cron
from user.code.speakify import create_voice_mapping
import os
import re

mod = Module()
ctx = Context()

mod.list("file_variables")
mod.list("file_types")


@imgui.open(x=0, y=30)
def list_info(gui: imgui.GUI):
    gui.text("-- file_variables --")
    variables = registry.lists["user.file_variables"][0].items()
    variables = sorted(variables, key=lambda v: v[0])
    for spoken, actual in variables:
        gui.text(f"{spoken}: {actual}")

@mod.action_class
class Actions:
    def get_var_regex() -> str:
        """Return a regex to parse the contents of the current file for variables"""
        raise NotImplementedError

    def get_type_regex() -> str:
        """Return a regex to parse the contents of the current file for types"""
        raise NotImplementedError

    def get_file_path() -> str:
        """Return the path of the current file"""
        raise NotImplementedError

    def update_lists(file_contents: str):
        """Parse the passed string"""
        if not file_contents:
            return
        try:
            var_regex = re.compile(actions.user.get_var_regex())
            variable_idents = set()
            for c in var_regex.findall(file_contents):
                if len(c[1]) > 2:
                    variable_idents.add(c[1])

            var_mapping = create_voice_mapping(variable_idents, acronyms=False)
            ctx.lists["user.file_variables"] = var_mapping
        except NotImplementedError:
            pass

        try:
            type_regex = re.compile(actions.user.get_type_regex())
            type_idents = set(type_regex.findall(file_contents))
            type_mapping = create_voice_mapping(type_idents, acronyms=False)
            ctx.lists["user.file_types"] = type_mapping
        except NotImplementedError:
            pass

    def refresh_lists():
        """refresh user.file_variables"""
        refresh(None)

    def list_info_toggle():
        """toggle window info imgui"""
        list_info.hide() if list_info.showing else list_info.show()


previous_file = (None, None) # path, mtime

def refresh(_):
    try:
        global previous_file
        path = actions.user.get_file_path()
        if not path:
            return
        if os.path.getsize(path) > 1_000_000:
            return
        mtime = os.path.getmtime(path)
        if path == previous_file[0]:
            if previous_file[1] and mtime <= previous_file[1]:
                return
        with open(path, "r") as f:
            contents = f.read()
        actions.user.update_lists(contents)
        previous_file = path, mtime
    except NotImplementedError:
        return

ui.register("win_title", refresh)
