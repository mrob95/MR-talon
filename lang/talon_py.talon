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
    'ctx.lists[""] = '
    key(left:5)
context matches:
    'ctx.matches = r""""""'
    key(left:3 enter:2 up)
