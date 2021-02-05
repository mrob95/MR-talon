os: windows
-
window {user.directions}: key("win-{directions}")
window pin: user.window_pin()
window unpin: user.window_unpin()

minimize: user.window_minimise()
maximise: user.window_maximise()
close window: user.window_close()
show work [spaces]: key(win-tab)
(create | new) work [space]: key(win-ctrl-d)
close work space: key(win-ctrl-f4)
next work [space] [<user.n20>]: user.workspace_next(n20 or 1)
(previous | prior) work [space] [<user.n20>]: user.workspace_previous(n20 or 1)

[go] work [space] <user.n20>: user.workspace_go(n20)

send work [space] <user.n20>: user.workspace_send(n20)
move work [space] <user.n20>: user.workspace_move(n20)

copy active bundle: user.print_window_info()

take screenshot: key(win-shift-s)
clipboard history: key(win-v)