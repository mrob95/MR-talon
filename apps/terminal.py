from ..imports import *
from pathlib import Path
import speakit

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



directory_map = {}
path_last_update = None

mingwctx = Context("mingw", func=lambda app, win: 'MINGW64' in win.title)

def update_directory_map(current_path):
    global directory_map
    directories = [p.name for p in current_path.iterdir() if p.is_dir()]
    spoken_forms = speakit.split_symbols(directories)
    directory_map = dict(zip(spoken_forms, directories))
    mingwctx.set_list("directories", directory_map.keys())

def update_maps(window):
    if not "MINGW64" in window.title:
        return
    global path_last_update
    current_path = Path(window.title.replace("MINGW64:/c", "C:"))
    if current_path == path_last_update:
        return
    path_last_update = current_path
    update_directory_map(current_path)

def change_directory(m):
    dire = directory_map[m["directories"][0]]
    Str(f'cd "{dire}" && ls')(m)
    Key("enter")(m)

ui.register("win_title", update_maps)
ui.register("win_focus", update_maps)

mingwctx.keymap({
    "CD {mingw.directories}": change_directory,
})