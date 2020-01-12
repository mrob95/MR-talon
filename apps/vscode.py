from ..imports import *

# ctx = Context("code", bundle="com.microsoft.VSCode")
# ctx = Context("code", func=lambda app, win: 'Code.exe' in app.exe)
ctx = Context("code", func=actions.context_matches(exe="code.exe"))

def Pallette(command):
    return [Key("ctrl-shift-p"), command, Key("enter")]

repeated_action = actions.gen_repeated_action("code.repeat")
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

ctx.keymap({
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
    "close tab [{code.repeat}]": repeated_action(Key("ctrl-w")),
    "next tab [{code.repeat}]": repeated_action(Key("ctrl-pgdown")),
    "previous tab [{code.repeat}]":repeated_action (Key("ctrl-pgup")),
    "{code.numberth} tab": lambda m: press("alt-" + numberth[m["code.numberth"][0]]),
    #
    "terminal here": Key("ctrl-shift-c"),
    "explorer here": Key("shift-alt-r"),
    #
    "find": Key("ctrl-f"),
    # "find <dgndictation>": [Key("ctrl-f"), Text("%(text)s"), Key("escape")],
    "find next [{code.repeat}]": repeated_action(Key("f3")),
    "find previous [{code.repeat}]": repeated_action(Key("s-enter")),
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
    "edit next [{code.repeat}]": repeated_action(Key("ctrl-d")),
    "skip next [{code.repeat}]": repeated_action(Key("ctrl-k ctrl-d")),
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
    "line {code.digits}+": [Key("ctrl-g"), lambda m: Str("".join(m["digits_list"]))(m), Key("enter")],
    "end line {code.digits}+": [Key("ctrl-g"), lambda m: Str("".join(m["digits_list"]))(m), Key("enter end")],
    "shunt [{code.repeat}]": repeated_action(Key("shift-down")),
    "(go to | good) file": Key("ctrl-p"),
    "comment line": Key("ctrl-/"),
    "indent [{code.repeat}]": repeated_action(Key("ctrl-]")),
    "[auto] complete": Key("ctrl-space"),
    # "meta sell": Key("shift-alt-;") + Wait(),
    # "meta go": Key("ctrl-;") + Wait(),
})
ctx.set_list("repeat", repeat.keys())
ctx.set_list("numberth", numberth.keys())
ctx.set_list("digits", digits.keys())