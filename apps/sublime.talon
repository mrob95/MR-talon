app: Sublime Text
-
edit lines: key("ctrl-shift-l")
sort lines: key("f9")
skip next [<user.r20>]:
    key("ctrl-k ctrl-d")
    repeat(r20 or 0)
edit all: key("ctrl-d alt-f3")
reverse selection: key("alt-shift-r")
new (file | tab): key("ctrl-n")
new window: key("ctrl-alt-n")
open file: key("ctrl-o")
open folder: key("ctrl-shift-o")
open recent: key("f10 down:4 right down:9")
save as: key("ctrl-shift-s")
save all: key("f10 f up:8 enter")
revert (file | [unsaved] changes): key("f10 f up:3 enter")
outdent lines: key("ctrl-lbracket")
match bracket: key("ctrl-m")
#
toggle side bar: key("ctrl-k ctrl-b")
show key bindings: key("f10 p right k")
#
find: key("ctrl-f")
next match [<user.n20>]: key("f3:{n10 or 1}")
previous match [<user.n20>]: key("shift-f3{n10 or 1}")
find all: key("alt-enter")
replace: key("ctrl-h")
#
go to file: key("ctrl-p")
go to word: key("ctrl-semicolon")
go to symbol: key("ctrl-r")
go to [symbol in] project: key("ctrl-shift-r")

command pallette: key("ctrl-shift-p")
search in directory: key("ctrl-shift-f")
go to (that | the): key("f12")
fold: key("ctrl-shift-lbracket")
unfold: key("ctrl-shift-rbracket")
unfold all: key("ctrl-k ctrl-j")
fold [level] <user.n20>: key("ctrl-k ctrl-{n20}")
#
full screen: key("f11")
(set | add) bookmark: key("ctrl-f2")
next bookmark: key("f2")
previous bookmark: key("shift-f2")
clear bookmarks: key("ctrl-shift-f2")
#
transform upper: key("ctrl-k ctrl-u")
transform lower: key("ctrl-k ctrl-l")
# {"keys"        : ["ctrl+k" "ctrl+t"] "command": "title_case"},
transform title: key("ctrl-k ctrl-t")
#
build it: key("ctrl-b")
build with: key("ctrl-shift-b")
# cancel build: key("ctrl-break"))
#
record macro: key("ctrl-q")
play macro [<n3>]: key("ctrl-shift-q")
(new | create) snippet: key("alt-n")
#
close tab: key("ctrl-w")
close all tabs: key("f10 f up:2 enter")
next tab: key("ctrl-pgdown")
previous tab: key("ctrl-pgup")
<user.numberth> tab: key("alt-{numberth}")
#
# column <cols>: key("alt-shift-%(cols)s")
# focus <panel>: key("ctrl-%(panel)s")
# move <panel>: key("ctrl-shift-%(panel)s")
duplicate (tab | file): key("ctrl-alt-v")
split right: key("alt-shift-2 ctrl-1 ctrl-shift-2")
#
terminal here: key("ctrl-shift-t")
explorer here: key("ctrl-alt-e")