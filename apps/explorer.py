from ..imports import *

repeated_action = actions.gen_repeated_action("spotify.n")

ctx = Context("spotify", func=actions.context_matches(exe="spotify.exe"))

ctx.keymap({
    "page back [{spotify.n}]": repeated_action(Key("alt-left")),
    "page forward [{spotify.n}]": repeated_action(Key("alt-right")),

    "new playlist": Key("ctrl-n"),
    "select all": Key("ctrl-a"),
    "deselect items": Key("ctrl-shift-a"),
    "(mute | unmute)": Key("ctrl-shift-down"),
    "search": Key("ctrl-l"),
    "preferences": Key("ctrl-p"),
    "add to playlist {spotify.n}": [Key("shift-f10"), actions.wait(10), Key("up up right"), repeated_action("down")],
    "add to playlist": [Key("shift-f10"), actions.wait(50), Key("up up right")],
})
ctx.set_list("n", [str(i) for i in range(20)])
