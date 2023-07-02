app: windows_explorer
-
follow {user.directories}:
    key(home)
    insert(directories)
    key(enter)
open {user.files}:
    key(home)
    insert(files)
    key(enter)
select {user.directories}:
    key(home)
    insert(directories)
select {user.files}:
    key(home)
    insert(files)
# ---
address bar: key(alt-d)
copy path:
    key(alt-d)
    key(ctrl-c)
    user.clip_replace("\\\\", "/")
    key(escape)
new folder: key(ctrl-shift-n)
new file: key(alt-f w t)
new window:
    key(ctrl-l)
    insert("explorer .")
    key(enter)
[(show | file | folder)] properties: key(alt-enter)
rename [that]: key(f2)
go up [<user.n20>]: key("alt-up:{n20 or 1}")
page back [<user.n20>]: key("alt-left:{n20 or 1}")
page forward [<user.n20>]: key("alt-right:{n20 or 1}")
go {user.folders}:
    key(ctrl-l)
    insert(folders)
    key(enter)
terminal here:
    key(ctrl-l)
    insert("wt.exe")
    key(enter)
dot {user.extensions}:
    key(".")
    insert(exts)
