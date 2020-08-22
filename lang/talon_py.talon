app: Visual Studio Code
and title: /^user - .*\.py/
app: Code.exe
and title: /^user - .*\.py/
-
standard imports:
    "from talon import *\n"
(context and module | module and context):
    """mod = Module()
    ctx = Context()
    """
action class:
    """@mod.action_class
    class Actions:
    """
context lists:
    'ctx.lists["user."] = '
    key(left:5)
context matches:
    'ctx.matches = r""""""'
    key(left:3 enter:2 up)
mod list: user.insert_function("mod.list")
    # 'mod.list(, desc="...")'
    # key(left:13)
mod tag: user.insert_function("mod.tag")
    # 'mod.tag(, desc="...")'
    # key(left:13)
fun key: user.insert_function("actions.key")
fun sleep: user.insert_function("actions.sleep")
fun insert: user.insert_function("actions.insert")
