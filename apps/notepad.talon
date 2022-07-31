app.exe: notepad.exe
-
insert all:
    key(ctrl-a ctrl-c)
    sleep(100ms)
    user.workspace_send(9)
    key(alt-tab)
    sleep(100ms)
    key(ctrl-v)
