from typing import Optional
from talon import Module, Context, ui, actions, registry, fs
import re
import time
from user.code.speakify import create_voice_mapping

mod = Module()
ctx = Context()

ctx.matches = r"""
app: vscode
"""

mark_window_title = None

@mod.action_class
class Actions:
    def vscode_palette(command: str) -> None:
        """Run a command using the command pallette"""
        actions.key("ctrl-shift-p")
        actions.insert(command)
        actions.key("enter")

    def vscode_select_to(digits: str) -> None:
        """Select from the current cursor position to the specified line"""
        actions.key("ctrl-k ctrl-b ctrl-g")
        actions.insert(digits)
        actions.key("enter end ctrl-k:2")

    def vscode_go_line(digits: str) -> None:
        """Go to the specified line"""
        actions.key("ctrl-g")
        actions.insert(digits)
        actions.key("enter")

    def vscode_mark() -> None:
        """Set mark"""
        global mark_window_title
        mark_window_title = ui.active_window().title
        actions.key("ctrl-k ctrl-b")

    def vscode_return() -> None:
        """Return to mark"""
        global mark_window_title
        current_window_title = ui.active_window().title
        if current_window_title == mark_window_title:
            actions.key("ctrl-k ctrl-g escape")
        else:
            actions.key("ctrl-k ctrl-right")
            actions.key("ctrl-k ctrl-g escape")

    def vscode_grab_mouse() -> str:
        """Grab the identifier below the mouse cursor and return it"""
        actions.user.vscode_mark()
        actions.mouse_click()
        actions.mouse_click()
        t = actions.edit.selected_text()
        actions.user.vscode_return()
        return t

    def vscode_get_file_contents() -> str:
        """Return the full contents of the current file"""
        # actions.key("escape [ | ]")
        actions.user.vscode_mark()
        actions.key("ctrl-a")
        t = actions.edit.selected_text()
        actions.user.vscode_return()
        # actions.key("backspace:3")
        return t

    def vscode_parse_file_contents(file_contents: Optional[str]):
        """Parse the passed string"""


mod.list("vscode_variables")
mod.list("vscode_functions")

last_title: str = ""

def refresh_current_file_info(active_window: ui.Window):
    """If vscode_parse_file_contents is implemented and the file contents have changed,
    call it with the new contents."""
    try:
        actions.user.vscode_parse_file_contents(None)
    except NotImplementedError:
        return

    global last_title
    if "vscode" not in registry.apps: return

    title = active_window.title
    if title == last_title:
        return
    if not title.endswith(".py"): return
    last_title = title
    if title.startswith("●"):
        # File is dirty
        return

    # TODO: Exclude remotes
    # project, _, filename = title.partition(" - ")
    # with open(filename, encoding="utf-8") as f:
    #     file_contents = f.read()

    # file_contents = Actions.vscode_get_file_contents()
    # actions.user.vscode_parse_file_contents(file_contents)

# ui.register("win_title", refresh_current_file_info)
# ui.register("win_focus", refresh_current_file_info)


#  ------------------------------------------------
#  PYTHON
#  ------------------------------------------------

py_ctx = Context()
py_ctx.matches = r"""
app: vscode
and title: /\.py$/
"""

mod.list("vscode_members")
mod.list("vscode_methods")

CLASS_REGEX = re.compile(r"class (?P<name>[A-Za-z_]+?)(?:\((?P<super>[A-Za-z_]+?)\))?:")
VAR_REGEX = re.compile(r"([A-Za-z_]+?) = .+?")
FUNC_USE_REGEX = re.compile(r"([A-Za-z_]+?)\(")
FUNC_DEF_REGEX = re.compile(r"def ([A-Za-z_]+?)\(")
METHOD_DEF_REGEX = re.compile(r"\s+def ([A-Za-z_]+?)\(")
SELF_REGEX = re.compile(r"\s+self\.([A-Za-z_]+?)\(")
IMPORT_REGEX = re.compile(r"import ([A-Za-z_,\ ]+)")


@ctx.action_class("user")
class PyActions():
    def vscode_parse_file_contents(file_contents: Optional[str]):
        if file_contents is None:
            return
        t_start = time.perf_counter()

        classes = [c[0] for c in CLASS_REGEX.findall(file_contents)]
        class_mapping = create_voice_mapping(classes)

        vars = VAR_REGEX.findall(file_contents)
        var_mapping = create_voice_mapping(vars)

        funcs = FUNC_USE_REGEX.findall(file_contents) + FUNC_DEF_REGEX.findall(file_contents)
        func_mapping = create_voice_mapping(funcs)

        imports = []
        for import_list in IMPORT_REGEX.findall(file_contents):
            imports.extend([i.strip() for i in import_list.split(",")])
        import_mapping = create_voice_mapping(imports)

        ctx.lists["user.vscode_functions"] = func_mapping | class_mapping
        ctx.lists["user.vscode_variables"] = var_mapping | func_mapping | class_mapping | import_mapping
        # print(ctx.lists["user.vscode_functions"])

        members = SELF_REGEX.findall(file_contents)
        methods = METHOD_DEF_REGEX.findall(file_contents)
        ctx.lists["user.vscode_members"] = create_voice_mapping(members)
        ctx.lists["user.vscode_methods"] = create_voice_mapping(methods)

        t_end = time.perf_counter()

        print(f"Time taken: {t_end - t_start}")
