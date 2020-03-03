from user.imports import *

repeated_action = actions.gen_repeated_action("brave.repeat")
BRING = utilities.load_toml_relative("config/bringme.toml")

sites = BRING["website"]

# ctx = Context("brave", func=lambda app, win: 'Google brave' in win.title)
ctx = Context("brave", func=actions.context_matches(exe="brave.exe"))

repeat = {str(i): str(i) for i in range(20)}
numberth = {
    "first": "1",
    "second": "2",
    "third": "3",
    "fourth": "4",
    "fifth": "5",
    "sixth": "6",
    "seventh": "7",
    "eighth": "8",
    "ninth": "9",
    "last": "9",
}

ctx.keymap({
    "new incognito window": Key("ctrl-shift-n"),
    "new tab [{brave.repeat}]": repeated_action(Key("ctrl-t")),
    "next tab [{brave.repeat}]": repeated_action(Key("ctrl-tab")),
    "previous tab [{brave.repeat}]": repeated_action(Key("ctrl-shift-tab")),
    "close tab [{brave.repeat}]": repeated_action([Key("ctrl-w"), actions.wait(50)]),
    "reopen tab [{brave.repeat}]": repeated_action(Key("ctrl-shift-t")),
    "{brave.numberth} tab": lambda m: press("ctrl-" + numberth[m["brave.numberth"][0]]),
    "page back [{brave.repeat}]": repeated_action(Key("alt-left")),
    "page forward [{brave.repeat}]": repeated_action(Key("alt-right")),
    "zoom reset": Key("ctrl-0"),
    "refresh": Key("ctrl-f5"),
    "switch focus [{brave.repeat}]": repeated_action(Key("f6")),
    # "find <text>": [Key("ctrl-f/20"), "%(text)s"],
    "[find] next match [{brave.repeat}]": repeated_action(Key("ctrl-g")),
    "[find] prior match [{brave.repeat}]": repeated_action(Key("ctrl-shift-g")),
    "[toggle] caret browsing": Key("f7"),
    "home page": Key("alt-home"),
    # "show history"            : Key("ctrl-h"),
    "show history": [Key("ctrl-t"), "brave://history/\n"],
    "google search": Key("ctrl-l"),
    "image search": [Key("ctrl-l left"), Str("https://www.google.com/searchbyimage?&image_url="), Key("enter")],
    "show downloads": Key("ctrl-j"),
    "add bookmark": Key("ctrl-d"),
    "bookmark all tabs": Key("ctrl-shift-d"),
    "[toggle] bookmark bar": Key("ctrl-shift-b"),
    "show bookmarks": Key("ctrl-shift-o"),
    "switch user": Key("ctrl-shift-m"),
    "brave task manager": Key("shift-escape"),
    "[toggle] full screen": Key("f11"),
    "focus notification": Key("alt-n"),
    "allow notification": Key("alt-shift-a"),
    "deny notification": Key("alt-shift-a"),
    "developer tools": Key("f12"),
    "view [page] source": Key("ctrl-u"),
    "resume": Key("f8"),
    "step over": Key("f10"),
    "step into": Key("f11"),
    "step out": Key("shift-f11"),
    "copy all": Key("ctrl-a ctrl-c"),
    "go {brave.sites}": [actions.wait(50), Key("ctrl-l"), actions.wait(50), actions.exec_str("brave.sites", sites), Key("enter")],
    # "search <text>": [Key("ctrl-l/10"), "%(text)s", Key("enter"),]
    # "science hub": [Key("ctrl-l/10, left/10"), "https://sci-hub.tw/", Key("enter")],
    # Key("alt-d") + Store() + Key("delete"), "https://sci-hub.tw/") + Retrieve() + Key("enter"),

    # "save image": Function(utilities.brave_save_image),
    # Surfing
    "(toggle) surfing keys": Key("alt-s"),
    "split right": Key("w-left/50, W/50, w-right"),
    # "duplicate tab": Key("y, t"),
    # "go to root": Key("g, U"),
    # "scroll left [{brave.repeat}]": repeated_action(lambda m: press("h")),
    # "scroll right [{brave.repeat}]": repeated_action(lambda m: press("l")),
})
ctx.set_list("repeat", repeat.keys())
ctx.set_list("numberth", numberth.keys())
ctx.set_list("sites", sites.keys())