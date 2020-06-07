from user.imports import *
from talon import Module, Context, actions, ctrl
import time

mod = Module()
ctx = Context()

@mod.action_class
class Actions:
    def mouse_drag():
        """Drag"""
        ctrl.mouse_click(down=True)

    def mouse_release():
        """Drag"""
        current_exe = ui.active_app().exe.lower()
        if "shellexperiencehost.exe" in current_exe:
            ctrl.mouse_click(up=True)
            actions.sleep("100ms")
            utilities.save_clipboard_image()
        ctrl.mouse_click(up=True)

# ctx.commands = {
#     # 'shifty': lambda m: press_key_and_click(m, 'shift'),
#     # 'colic': lambda m: press_key_and_click(m, 'ctrl'),
#     # 'mouse alt click': lambda m: press_key_and_click(m, 'alt'),
#     # "millick": lambda m: click(m, 2),
#     # 'kick': click,
#     # 'kick double': dubclick,
#     # 'squat': mouse_drag,
#     'bench': actions.ContextAction(
#         mouse_release, {
#             "shellexperiencehost.exe": [lambda m: print("Saving screenshot"), mouse_release, actions.wait(100), utilities.save_clipboard_image]
#         }
#     ),
# }


# import uiautomation as auto
# # notepadWindow = auto.WindowControl(searchDepth=1, ClassName='Visual Studio Code')
# print(auto.GetRootControl())
# ctrl = auto.GetFocusedControl()
# print(ctrl)
# print(ctrl.GetWindowText())
# children = ctrl.GetChildren()
# print(children)
# print([c.IsEnabled for c in children])
# print(dir(ctrl))

# def pprint_ui(ui, indent=0):
#     print(f"{'-'*indent} {ui.ControlTypeName} {ui.IsEnabled}")
#     children = ui.GetChildren()
#     for c in children:
#         pprint_ui(c, indent+1)

# pprint_ui(ctrl)