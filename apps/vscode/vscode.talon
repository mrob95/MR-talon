app: vscode
-
tag(): user.command_mode
new (file | tab): key(ctrl-n)
new window: key(ctrl-shift-n)
open file: key(ctrl-o)
open folder: key(ctrl-k ctrl-o)
open recent: key(ctrl-r)
save as: key(ctrl-shift-s)
save all: key(ctrl-k s)
revert (file | changes): user.vscode_palette("revert file")
close all tabs: key(ctrl-k ctrl-w)
close tab [<user.n20>]: user.slow_key("ctrl-w:{n20 or 1}", "100ms")
next tab [<user.n20>]: key("ctrl-pgdown:{n20 or 1}")
previous tab [<user.n20>]: key("ctrl-pgup:{n20 or 1}")
<user.numberth> tab: key("alt-{numberth}")
#
line <user.line_numbers>: user.vscode_go_line(line_numbers)
end line <user.line_numbers>:
    user.vscode_go_line(line_numbers)
    key(end:2)
select by <user.line_numbers>: user.vscode_select_to(line_numbers)
select <user.line_numbers> by <user.line_numbers>:
    user.vscode_go_line(line_numbers_1)
    user.vscode_select_to(line_numbers_2)
    #
shunt [<user.n20>]: key("shift-down:{n20 or 1}")
comment line: key(ctrl-/)
duple comment: key(shift-alt-down up ctrl-/ down)
insert to do: key(ctrl-/ T O D O : space)
insert line break:
    key(ctrl-/)
    " ------------------------------------------------"
indent [<user.n20>]: key("ctrl-]:{n20 or 1}")
[auto] complete: key(ctrl-space)
#
terminal here: key(ctrl-shift-c)
explorer here: key(shift-alt-r)
#
next match [<user.n20>]: key("f3:{n20 or 1}")
previous match [<user.n20>]: key("shift-enter:{n20 or 1}")
find all: key(alt-enter)
replace: key(ctrl-h)
search in directory: key(ctrl-shift-f)
#
copy relative path: key(ctrl-k ctrl-shift-c)
copy path: key(alt-shift-c)
#
go last [<user.r20>]:
    key(ctrl-k ctrl-pgdown)
    repeat(r20 or 0)
go next [<user.r20>]:
    key(ctrl-k ctrl-pgup)
    repeat(r20 or 0)
(go to | good) file: key(ctrl-p)
cutter fail: key(ctrl-p)
go to <phrase> [{user.filetype}]$:
    key(ctrl-p)
    sleep(100ms)
    insert(user.phrase_to_str(phrase))
    insert(filetype or "")
    # key(enter)
go to word: key(ctrl-;)
go to symbol: key(ctrl-shift-o)
go to [symbol in] project: key(ctrl-t)
go to definition: key(f12)
peek definition: key(alt-f12)
peek references: key(shift-f12)
command pallette: key(ctrl-shift-p)
rename (symbol | that): key(f2)
#
edit lines: key(shift-alt-i)
sort lines: user.vscode_palette("sort ascending")
edit previous [<user.n20>]: key("ctrl-alt-d:{n20 or 1}")
edit next [<user.n20>]: key("ctrl-d:{n20 or 1}")
skip next [<user.n20>]: key("ctrl-k ctrl-d:{n20 or 1}")
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
fold level [<user.n20>]: key("ctrl-k ctrl-{n20}")
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
#
set (anchor | mark): key(ctrl-k ctrl-b)
go to (anchor | mark): key(ctrl-k ctrl-g)
insert mouse: user.paste(user.vscode_grab_mouse())
print mouse: user.lang_print(user.vscode_grab_mouse())
#
git revert: key(ctrl-k ctrl-r)
git stage: key(ctrl-k ctrl-alt-s)
git unstage: key(ctrl-k ctrl-n)
git diff: key(ctrl-shift-g ,)


#
refresh file: print(user.vscode_get_file_contents())
very {user.vscode_variables}: "{vscode_variables}"
fun {user.vscode_functions}: user.insert_function(vscode_functions)


#
command server write: key(ctrl-shift-alt-p)
test lineup:
    out = user.vscode("workbench.view.explorer")
    print(out)
