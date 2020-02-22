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
file_map = {}
path_last_update = None

mingwctx = Context("mingw", func=lambda app, win: 'MINGW64' in win.title)

def update_directory_map(current_path):
    global directory_map
    directories = [p.name for p in current_path.iterdir() if p.is_dir()]
    spoken_forms = speakit.split_symbols(directories, max_len=3)
    directory_map = dict(zip(spoken_forms, directories))
    mingwctx.lists["directories"] = directory_map
    # print(directory_map)

def update_file_map(current_path):
    global file_map
    files = [p for p in current_path.iterdir() if p.is_file()]
    spoken_forms = speakit.split_symbols([p.stem for p in files], max_len=3)
    file_map = dict(zip(spoken_forms, [f.name for f in files]))
    mingwctx.lists["files"] = file_map
    print(file_map)


def update_maps(window):
    if not "MINGW64" in window.title:
        return
    global path_last_update
    current_path = Path(window.title.replace("MINGW64:/c", "C:"))
    if current_path == path_last_update:
        return
    path_last_update = current_path
    mingwctx.lists["directories"] = file_utils.get_directory_map(current_path)
    mingwctx.lists["files"] = file_utils.get_file_map(current_path)

ui.register("win_title", update_maps)
ui.register("win_focus", update_maps)

mingwctx.keymap({
    "CD {directories}": ['cd "', lambda m: Str(m["directories"][0])(m), '" && ls', Key("enter")],
    "file {files}": [lambda m: Str(m["files"][0])(m), " "],
})