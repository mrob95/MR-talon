from user.imports import *

ctx = Context("code")
ctx.matches = r"""
app: Visual Studio Code
"""

def Pallette(command):
    return [Key("ctrl-shift-p"), command, Key("enter")]

repeated_action = actions.gen_repeated_action("repeat")
repeat = {str(i): str(i) for i in range(20)}
digits = {str(i): str(i) for i in range(10)}
numberth = {
    "first": "1",
    "second": "2",
    "third": "3",
    "fourth": "4",
    "fifth": "5",
    "sixth": "6",
    "seventh": "7",
    "eighth": "8",
    "last": "9",
    "ninth": "9",
}

ctx.commands = {
    "comment block": Key("shift-alt-a"),
    "new (file | tab)": Key("ctrl-n"),
    "new window": Key("ctrl-shift-n"),
    "open file": Key("ctrl-o"),
    "open folder": Key("ctrl-k ctrl-o"),
    "open recent": Key("ctrl-r"),
    "save as": Key("ctrl-shift-s"),
    "save all": Key("ctrl-k s"),
    "revert (file | changes)": Pallette("revert file"),
    "close all tabs": Key("ctrl-k ctrl-w"),
    "close tab [{repeat}]": repeated_action(Key("ctrl-w")),
    "next tab [{repeat}]": repeated_action(Key("ctrl-pgdown")),
    "previous tab [{repeat}]":repeated_action(Key("ctrl-pgup")),
    "{numberth} tab": lambda m: press("alt-" + m["numberth"][0]),
    #
    "terminal here": Key("ctrl-shift-c"),
    "explorer here": Key("shift-alt-r"),
    #
    "find": Key("ctrl-f"),
    # "find <dgndictation>": [Key("ctrl-f"), Text("%(text)s"), Key("escape")],
    "find next [{repeat}]": repeated_action(Key("f3")),
    "find previous [{repeat}]": repeated_action(Key("s-enter")),
    "find all": Key("alt-enter"),
    "replace": Key("ctrl-h"),
    "search in directory": Key("ctrl-shift-f"),
    "search for that": [Key("ctrl-shift-f"), Key("enter")],
    #
    # "go to <dgndictation> [<filetype>]": Key("ctrl-p")
    # + Wait()
    # + Text("%(text)s" + "%(filetype)s")
    # + Wait()
    # + Key("enter"),
    "go to word": Key("ctrl-;"),
    "go to symbol": Key("ctrl-shift-o"),
    "go to [symbol in] project": Key("ctrl-t"),
    "go to that": Key("f12"),
    "peek (definition | that)": Key("alt-f12"),
    "command pallette": Key("ctrl-shift-p"),
    "rename symbol": Key("f2"),
    #
    "edit lines": Key("shift-alt-i"),
    "sort lines": Pallette("sort ascending"),
    "edit next [{repeat}]": repeated_action(Key("ctrl-d")),
    "skip next [{repeat}]": repeated_action(Key("ctrl-k ctrl-d")),
    "edit all": Key("ctrl-shift-l"),
    # "<action> [line] <ln1> [by <ln2>]": Function(navigation.action_lines),
    # "<action> by [line] <ln1>": Key("ctrl-k, ctrl-space, ctrl-g")
    # + Function(lambda ln1: Text(str(ln1 + 1)).execute())
    # + Key("enter, ctrl-k, ctrl-a, %(action)s, ctrl-k, ctrl-g"),
    #
    "transform upper": Pallette("uppercase"),
    "transform lower": Pallette("lowercase"),
    "transform title": Pallette("titlecase"),
    #
    "fold that": Key("ctrl-shift-["),
    "unfold that": Key("ctrl-shift-]"),
    "unfold all": Key("ctrl-k ctrl-j"),
    # "fold [level] <n2>": Key("ctrl-k, ctrl-%(n2)s"),
    #
    "full screen": Key("f11"),
    "toggle side bar": Key("ctrl-b"),
    "(toggle | show) problems": Key("ctrl-shift-m"),
    # "flash problems": Key("ctrl-shift-m") + Pause("50") + Key("ctrl-shift-m"),
    "show extensions": Key("ctrl-shift-x"),
    "show explorer": Key("ctrl-shift-e"),
    "show terminal": Key("ctrl-'"),
    "new terminal": Key("ctrl-shift-'"),
    # "show python repel": Key("ctrl-shift-p") + Wait() + Text("pyrepl\n"),
    "open settings": Key("ctrl-,"),
    "open keyboard shortcuts": Key("ctrl-k ctrl-s"),
    #
    "build it": Key("ctrl-b"),
    "build with": Key("ctrl-shift-b"),
    "format document": Key("alt-shift-f"),
    "preview html": Key("ctrl-shift-v"),
    #
    "column 1": Key("alt-shift-1"),
    "column 2": Key("alt-shift-2"),
    "column 3": Key("alt-shift-3"),
    "column grid": Key("alt-shift-5"),
    "focus up": Key("ctrl-k ctrl-up"),
    "focus down": Key("ctrl-k ctrl-down"),
    "focus left": Key("ctrl-k ctrl-left"),
    "focus right": Key("ctrl-k ctrl-right"),
    "move up": Key("ctrl-k ctrl-shift-up"),
    "move down": Key("ctrl-k ctrl-shift-down"),
    "move left": Key("ctrl-k ctrl-shift-left"),
    "move right": Key("ctrl-k ctrl-shift-right"),
    "split right": Key("alt-shift-2 ctrl-k ctrl-shift-right"),
    "split definition": Key("ctrl-k f12"),
    #------------------------------------------------
    "line {digits}+": [Key("ctrl-g"), lambda m: Str("".join(m["digits_list"]))(m), Key("enter")],
    "end line {digits}+": [Key("ctrl-g"), lambda m: Str("".join(m["digits_list"]))(m), Key("enter end")],
    "shunt [{repeat}]": repeated_action(Key("shift-down")),
    "(go to | good) file": Key("ctrl-p"),
    "comment line": Key("ctrl-/"),
    "indent [{repeat}]": repeated_action(Key("ctrl-]")),
    "[auto] complete": Key("ctrl-space"),
    "meta sell": [Key("shift-alt-;"), actions.wait(25)],
    "meta go": [Key("ctrl-;"), actions.wait(25)],
}
ctx.lists["repeat"] = repeat
ctx.lists["numberth"] = numberth
ctx.lists["digits"] = digits


# ctx.defines = r"""
# next tab [{repeat}]:
#     key(ctrl-pgdown)
#     core.repeat_action(repeat)
# # "previous tab [{repeat}]": repeated_action (Key("ctrl-pgup")),
# # "{numberth} tab": lambda m: press("alt-" + m["numberth"][0]),
# comment line: key(ctrl-/)
# comment block: key(shift-alt-a)
# new (file | tab): key(ctrl-n)
# new window: key(ctrl-shift-n)
# open file: key(ctrl-o)
# open folder: key(ctrl-k ctrl-o)
# open recent: key(ctrl-r)
# save as: key(ctrl-shift-s)
# save all: key(ctrl-k s)
# close all tabs: key(ctrl-k ctrl-w)
# #
# terminal here: key(ctrl-shift-c)
# explorer here: key(shift-alt-r)
# #
# find: key(ctrl-f)
# find all: key(alt-enter)
# replace: key(ctrl-h)
# search in directory: key(ctrl-shift-f)
# go to word: key(ctrl-;)
# go to symbol: key(ctrl-shift-o)
# go to [symbol in] project: key(ctrl-t)
# go to that: key(f12)
# peek (definition | that): key(alt-f12)
# command pallette: key(ctrl-shift-p)
# rename symbol: key(f2)
# #
# edit lines: key(shift-alt-i)
# edit all: key(ctrl-shift-l)
# #
# fold that: key(ctrl-shift-[)
# unfold that: key(ctrl-shift-])
# unfold all: key(ctrl-k ctrl-j)
# #
# full screen: key(f11)
# toggle side bar: key(ctrl-b)
# (toggle | show) problems: key(ctrl-shift-m)
# show extensions: key(ctrl-shift-x)
# show explorer: key(ctrl-shift-e)
# show terminal: key(ctrl-')
# new terminal: key(ctrl-shift-')
# open settings: key(ctrl-,)
# open keyboard shortcuts: key(ctrl-k ctrl-s)
# #
# build it: key(ctrl-b)
# build with: key(ctrl-shift-b)
# format document: key(alt-shift-f)
# preview html: key(ctrl-shift-v)
# #
# column 1: key(alt-shift-1)
# column 2: key(alt-shift-2)
# column 3: key(alt-shift-3)
# column grid: key(alt-shift-5)
# focus up: key(ctrl-k ctrl-up)
# focus down: key(ctrl-k ctrl-down)
# focus left: key(ctrl-k ctrl-left)
# focus right: key(ctrl-k ctrl-right)
# move up: key(ctrl-k ctrl-shift-up)
# move down: key(ctrl-k ctrl-shift-down)
# move left: key(ctrl-k ctrl-shift-left)
# move right: key(ctrl-k ctrl-shift-right)
# split right: key(alt-shift-2 ctrl-k ctrl-shift-right)
# split definition: key(ctrl-k f12)
# """