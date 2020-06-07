app: Visual Studio Code
app: Code.exe
-
action(edit.line_clone):
    key(shift-alt-down)
#
comment block: key(shift-alt-a)
new (file | tab): key(ctrl-n)
new window: key(ctrl-shift-n)
open file: key(ctrl-o)
open folder: key(ctrl-k ctrl-o)
open recent: key(ctrl-r)
save as: key(ctrl-shift-s)
save all: key(ctrl-k s)
revert (file | changes):
    key(ctrl-shift-p)
    "revert file"
    key(enter)
close all tabs: key(ctrl-k ctrl-w)
close tab <user.n20>: key("ctrl-w:{n20}")
next tab <user.n20>: key("ctrl-pgdown:{n20}")
previous tab <user.n20>: key("ctrl-pgup:{n20}")
<user.numberth> tab: key("alt-{numberth}")
#
terminal here: key(ctrl-shift-c)
explorer here: key(shift-alt-r)
#
# find <dgndictation>: [key(ctrl-f") Text("%(text)s)kKey"escape"],
next match <user.n20>: key("f3:{n20}")
previous match <user.n20>: key("shift-enter:{n20}")
find all: key(alt-enter)
replace: key(ctrl-h)
search in directory: key(ctrl-shift-f)
#
copy relative path: key(ctrl-k ctrl-shift-c)
copy path: key(alt-shift-c)
#
go to word: key(ctrl-;)
go to symbol: key(ctrl-shift-o)
go to [symbol in] project: key(ctrl-t)
go to that: key(f12)
peek (definition | that): key(alt-f12)
command pallette: key(ctrl-shift-p)
rename symbol: key(f2)
#
edit lines: key(shift-alt-i)
sort lines:
    key(ctrl-shift-p)
    "sort ascending"
    key(enter)
edit previous <user.n20>: key("ctrl-alt-d:{n20}")
edit next <user.n20>: key("ctrl-d:{n20}")
skip next <user.n20>: key("ctrl-k ctrl-d:{n20}")
edit all: key(ctrl-shift-l)
#
transform upper:
    key(ctrl-shift-p)
    "uppercase"
    key(enter)
transform lower:
    key(ctrl-shift-p)
    "lowercase"
    key(enter)
transform title:
    key(ctrl-shift-p)
    "titlecase"
    key(enter)
#
fold that: key(ctrl-shift-[)
unfold that: key(ctrl-shift-])
unfold all: key(ctrl-k ctrl-j)
# fold [level] <n2>: key(ctrl-k, ctrl-%(n2)s)
#
full screen: key(f11)
toggle side bar: key(ctrl-b)
(toggle | show) problems: key(ctrl-shift-m)
# flash problems: key(ctrl-shift-m") + Pause("50) +kKey"ctrl-shift-m)
show extensions: key(ctrl-shift-x)
show explorer: key(ctrl-shift-e)
show terminal: key(ctrl-')
new terminal: key(ctrl-shift-')
# show python repel: key(ctrl-shift-p") + Wait() + Txt("pyrepl\n")
open settings: key(ctrl-,)
open keyboard shortcuts: key(ctrl-k ctrl-s)
#
build it: key(ctrl-b)
build with: key(ctrl-shift-b)
format document: key(alt-shift-f)
preview html: key(ctrl-shift-v)
#
column 1: key(alt-shift-1)
column 2: key(alt-shift-2)
column 3: key(alt-shift-3)
column grid: key(alt-shift-5)
focus up: key(ctrl-k ctrl-up)
focus down: key(ctrl-k ctrl-down)
focus left: key(ctrl-k ctrl-left)
focus right: key(ctrl-k ctrl-right)
move up: key(ctrl-k ctrl-shift-up)
move down: key(ctrl-k ctrl-shift-down)
move left: key(ctrl-k ctrl-shift-left)
move right: key(ctrl-k ctrl-shift-right)
split right: key(alt-shift-2 ctrl-k ctrl-shift-right)
split definition: key(ctrl-k f12)
#------------------------------------------------
line <user.digits>:
    key(ctrl-g)
    insert(digits)
    key(enter)
end line <user.digits>:
    key(ctrl-g)
    insert(digits)
    key(enter end)
shunt <user.n20>: key("shift-down:{n20}")
(go to | good) file: key(ctrl-p)
comment line: key(ctrl-/)
indent <user.n20>: key("ctrl-]:{n20}")
[auto] complete: key(ctrl-space)
meta sell: key(shift-alt-;")
meta go: key(ctrl-;")