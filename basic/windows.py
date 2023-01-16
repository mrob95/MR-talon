from talon import Module, ui
import win32gui
import win32con

mod = Module()

@mod.action_class
class Actions:
    def window_maximise():
        """Maximise the current window"""
        wndh = ui.active_window().id
        win32gui.ShowWindow(wndh, win32con.SW_MAXIMIZE)

    def window_minimise():
        """Minimise the current window"""
        wndh = ui.active_window().id
        win32gui.ShowWindow(wndh, win32con.SW_MINIMIZE)

    def window_close():
        """Close the current window"""
        wndh = ui.active_window().id
        win32gui.PostMessage(wndh, win32con.WM_CLOSE, 0, 0)
