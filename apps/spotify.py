from user.imports import *

repeated_action = actions.gen_repeated_action("repeat")


ctx = Context("spotify")
ctx.matches = r"""
app: Spotify.exe
"""

ctx.commands = {
    "page back [{repeat}]": repeated_action(Key("alt-left")),
    "page forward [{repeat}]": repeated_action(Key("alt-right")),

    "new playlist": Key("ctrl-n"),
    "select all": Key("ctrl-a"),
    "deselect items": Key("ctrl-shift-a"),
    "(mute | unmute)": Key("ctrl-shift-down"),
    "search": Key("ctrl-l"),
    "preferences": Key("ctrl-p"),
    "add to playlist {repeat}": [Key("shift-f10"), actions.wait(10), Key("up up right"), repeated_action("down")],
    "add to playlist": [Key("shift-f10"), actions.wait(50), Key("up up right")],
}
ctx.lists["repeat"] = [str(i) for i in range(20)]
