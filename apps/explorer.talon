app: /.*/
and title: /(Save|Open|Browse|Select)/
app: Windows Explorer
-
follow {directories}:
    key("home")
    insert(directories)
    key("enter")
open {files}:
    key("home")
    insert(files)
    key("enter")
select {directories}:
    key("home")
    insert(directories)
select {files}:
    key("home")
    insert(files)
# ---
address bar: key("alt-d")
new folder: key("ctrl-shift-n")
new file: key("alt-f w t")
[(show | file | folder)] properties: key("alt-enter")
rename [that]: key(f2)
go up <user.n20>: key("alt-up:{n20}")
page back <user.n20>: key("alt-left:{n20}")
page forward <user.n20>: key("alt-right:{n20}")
go {folders}:
    key("ctrl-l")
    insert(folders)
    key("enter")
terminal here:
    key("ctrl-l")
    insert("wt.exe")
    key("enter")
dot {extensions}:
    key(".")
    insert(exts)