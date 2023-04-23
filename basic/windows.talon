os: windows
-
window {user.directions}: key("win-{directions}")
window {user.directions} {user.directions}: key("win-{directions_1} win-{directions_2}")

minimize: user.window_minimise()
maximise: user.window_maximise()
close window: user.window_close()

copy active bundle: user.print_window_info()

take screenshot: key(win-shift-s)
clipboard history: key(win-v)