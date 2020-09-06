app: RStudio
-
new (file | tab): key(ctrl-shift-n)
open file: key(ctrl-o)
go to file: key(ctrl-.)
# "open recent": Mouse("[20, 34], left") + Key("down:5, right"),
# "open project": Mouse("[20, 34], left") + Key("down:6, enter"),
# "open recent project": Mouse("[20, 34], left") + Key("down:8, right"),
save all: key(ctrl-alt-s)
select all: key(ctrl-a)
find: key(ctrl-f)
find that: key(ctrl-f3)
align that: key(ctrl-i)
# [go to] line <ln1>: key("as-g/10") + Text("%(ln1)s") + Key("enter")
line <user.digits>:
    key(shift-alt-g)
    insert(digits)
    key(enter)
end line <user.digits>:
    key(shift-alt-g)
    insert(digits)
    key(enter end)
shunt <user.n20>: key("shift-down:{n20}")
# ------------------------------------------------
focus (main | editor): key(ctrl-1)
focus console: key(ctrl-2)
focus terminal: key(alt-shift-t)
focus help: key(ctrl-3)
focus history: key(ctrl-4)
focus files: key(ctrl-5)
focus plots: key(ctrl-6)
focus packages: key(ctrl-7)
focus environment: key(ctrl-8)
focus viewer: key(ctrl-9)
focus git: key(ctrl-f1)
focus connections: key(ctrl-f5)
# ------------------------------------------------
next tab <user.n20>: key("ctrl-f12:{n20}")
previous tab <user.n20>: key("ctrl-f11:{n20}")
first tab: key(ctrl-shift-f11)
last tab: key(ctrl-shift-f12)
close tab: key(ctrl-w)
# ------------------------------------------------
run (line | that): key(ctrl-enter)
(run document | build it): key(ctrl-alt-r)
comment (line | selected | block): key(ctrl-shift-c)
knit (document | file): key(ctrl-shift-k)
next plot: key(ctrl-alt-f12)
previous plot: key(ctrl-alt-f11)
create function: key(ctrl-alt-x)
create variable: key(ctrl-alt-v)
rename that: key(ctrl-alt-shift-m)
# ------------------------------------------------
help that: user.r_paste_into_console("?{{text}}")
glimpse that: user.r_paste_into_console("glimpse({{text}})")
head that: user.r_paste_into_console("head({{text}})")
vee table that: user.r_paste_into_console("library(vtable)\nvtable({{text}})")
