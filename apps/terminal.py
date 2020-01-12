from ..imports import *

BINDINGS = utilities.load_toml_relative("config/terminal.toml")
CORE = utilities.load_toml_relative("config/core.toml")

# ctx = Context("terminal", func=lambda app, win: 'MINGW64 in win.title)
ctx = Context("terminal", func=actions.context_matches("mingw64"))

commands = BINDINGS["commands"]
git_commands = BINDINGS["git_commands"]

def execute_command(list_name, lookup):
    def f(m):
        c = lookup[m[list_name][0]]
        if isinstance(c, str):
            Str(c)(None)
        else:
            for i, key_or_text in enumerate(c):
                if i%2 == 0:
                    Str(key_or_text)(None)
                else:
                    Key(key_or_text)(None)
    return f

ctx.keymap({
    "{terminal.commands}": execute_command("terminal.commands", commands),
    "git {terminal.git_commands}": ["git ", execute_command("terminal.git_commands", git_commands)],
})
ctx.set_list("commands", commands.keys())
ctx.set_list("git_commands", git_commands.keys())