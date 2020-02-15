from ..imports import *

BINDINGS = utilities.load_toml_relative("config/terminal.toml")
CORE = utilities.load_toml_relative("config/core.toml")

# ctx = Context("terminal", func=lambda app, win: 'MINGW64 in win.title)
ctx = Context("terminal", func=actions.context_matches(exe=["mintty.exe", "windowsterminal.exe"]))

commands = BINDINGS["commands"]
git_commands = BINDINGS["git_commands"]

# def clip_repo():
#     clip = Clipboard.get_system_text()
#     if clip.startswith("https://github.com"):
#         if clip.endswith("/"):
#             clip = clip[:-1]
#         Text(clip).execute()
#         if not clip.endswith(".git"):
#             Text(".git").execute()


ctx.keymap({
    **{k: actions.Alternating(v) for k, v in commands.items()},
    **{f"git {k}": ["git ", actions.Alternating(v)] for k, v in git_commands.items()},
})
