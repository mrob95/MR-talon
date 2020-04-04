window {directions_alt}: key("win-{directions_alt}")

minimize: user.window_minimise()
maximise: user.window_maximise()
close window: user.window_close()
show work [spaces]: key(win-tab)
(create | new) work [space]: key(win-ctrl-d)
close work space: key(win-ctrl-f4)
next work [space] <user.n20>: user.workspace_next(n20)
(previous | prior) work [space] <user.n20>: user.workspace_previous(n20)

[go] work [space] <user.n20>:
    user.workspace_go(n20)

send work [space] <user.n20>:
    user.workspace_send(n20)
move work [space] <user.n20>:
    user.workspace_move(n20)
