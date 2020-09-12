app: Visual Studio Code
app: Code.exe
-
action(edit.line_clone):
    key(shift-alt-down)
#
new (file | tab): key(ctrl-n)
new window: key(ctrl-shift-n)
open file: key(ctrl-o)
open folder: key(ctrl-k ctrl-o)
open recent: key(ctrl-r)
(go to | good) file: key(ctrl-p)
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
line <user.digits>:
    key(ctrl-g)
    insert(digits)
    key(enter)
end line <user.digits>:
    key(ctrl-g)
    insert(digits)
    key(enter end:2)
shunt <user.n20>: key("shift-down:{n20}")
comment line: key(ctrl-/)
duple comment:
    key(shift-alt-down up ctrl-/ down)
indent <user.n20>: key("ctrl-]:{n20}")
[auto] complete: key(ctrl-space)
#
terminal here: key(ctrl-shift-c)
explorer here: key(shift-alt-r)
#
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
transform upper: user.vscode_palette("uppercase")
transform lower: user.vscode_palette("lowercase")
transform title: user.vscode_palette("titlecase")
rename file: user.vscode_palette("File: Rename")
#
fold that: key(ctrl-shift-[)
unfold that: key(ctrl-shift-])
unfold all: key(ctrl-k ctrl-j)
#
full screen: key(f11)
toggle side bar: key(ctrl-b)
show problems: key(ctrl-shift-m)
show extensions: key(ctrl-shift-x)
show explorer: key(ctrl-shift-e)
show terminal: key(ctrl-')
show git: user.vscode_palette("GitLens: Focus on File History View")
show sequel server: user.vscode_palette("SQL Server: Focus on Connections View")
show settings: key(ctrl-,)
new terminal: key(ctrl-shift-')
show keyboard shortcuts: key(ctrl-k ctrl-s)
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
set anchor: key(ctrl-k ctrl-b)
go to anchor: key(ctrl-k ctrl-g)
insert mouse:
    key(ctrl-k ctrl-b)
    mouse_click()
    mouse_click()
    user.temp_store()
    key(ctrl-k ctrl-g escape)
    user.temp_insert()
insert mouse line:
    key(ctrl-k ctrl-b)
    mouse_click()
    key(home shift-end)
    user.temp_store()
    key(ctrl-k ctrl-g escape)
    user.temp_insert()
print mouse:
    key(ctrl-k ctrl-b)
    mouse_click()
    mouse_click()
    user.temp_store()
    key(ctrl-k ctrl-g escape)
    user.lang_print(user.temp_contents())
remove to <user.digits>:
    key(ctrl-k ctrl-b ctrl-g)
    insert(digits)
    key(enter end ctrl-k ctrl-k backspace)
copy to <user.digits>:
    key(ctrl-k ctrl-b ctrl-g)
    insert(digits)
    key(enter end ctrl-k ctrl-k)
    edit.copy()
