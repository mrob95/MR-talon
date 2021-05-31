app: Visual Studio Code
and title: /user - .*\.py/
app: Code.exe
and title: /user - .*\.py/
-
standard imports:
    "from talon import ui, Module, Context, registry, actions, imgui, cron\n"
(context and module | module and context):
    """mod = Module()
    ctx = Context()
    """
action class:
    """@mod.action_class
    class Actions:
    """
mod capture:
    '''@mod.capture(rule="")
    def (m):
        ""'''
context lists:
    'ctx.lists["user."] = '
    key(left:5)
context matches:
    'ctx.matches = r""""""'
    key(left:3 enter:2 up)
clip capture:
    """with clip.capture() as s:
        actions.edit.copy()
    text = s.get()
    """
mod list: user.insert_function("mod.list")
mod tag: user.insert_function("mod.tag")
(action | fun) {user.talon_actions}:
    user.insert_function("actions.{talon_actions}")
context list {user.talon_lists}: 'ctx.lists["{talon_lists}"] = '