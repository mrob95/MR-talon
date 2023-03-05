app: Notepad
-
insert all:
    key(ctrl-a ctrl-c)
    sleep(100ms)
    user.workspace_send(9)
    key(alt-tab)
    sleep(200ms)
    key(ctrl-v)
