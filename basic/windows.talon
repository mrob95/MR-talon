os: windows
-
window {user.directions}: key("win-{directions}")

minimize: user.window_minimise()
maximise: user.window_maximise()
close window: user.window_close()

copy active bundle: user.print_window_info()

take screenshot: key(win-shift-s)
clipboard history: key(win-v)