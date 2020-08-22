from talon import Module, Context, ui
import struct
from ctypes import cdll, windll
from win32gui import GetForegroundWindow
import win32gui
import win32con
from user.utils import utilities
try:
    import pyvda
except ImportError:
    pass

ASFW_ANY = -1


def go_to_n(n):
    windll.user32.AllowSetForegroundWindow(ASFW_ANY)
    pyvda.GoToDesktopNumber(n)

mod = Module()

@mod.action_class
class Actions:
    def window_maximise():
        """Maximise the current window"""
        wndh = GetForegroundWindow()
        win32gui.ShowWindow(wndh, win32con.SW_MAXIMIZE)

    def window_minimise():
        """Minimise the current window"""
        wndh = GetForegroundWindow()
        win32gui.ShowWindow(wndh, win32con.SW_MINIMIZE)

    def window_close():
        """Close the current window"""
        wndh = GetForegroundWindow()
        win32gui.PostMessage(wndh, win32con.WM_CLOSE, 0, 0)

    def workspace_send(n: int):
        """Send the current window to a given workspace"""
        wndh = ui.active_window().id
        pyvda.MoveWindowToDesktopNumber(wndh, n)

    def workspace_move(n: int):
        """Send the current window to a given workspace, and follow it"""
        wndh = ui.active_window().id
        pyvda.MoveWindowToDesktopNumber(wndh, n)
        pyvda.GoToDesktopNumber(n)

    def workspace_go(n: int):
        """Go to a given workspace"""
        windll.user32.AllowSetForegroundWindow(ASFW_ANY)
        pyvda.GoToDesktopNumber(n)

    def workspace_next(n: int):
        """Go to the next workspace (without animation)"""
        current = pyvda.GetCurrentDesktopNumber()
        go_to_n(current+n)

    def workspace_previous(n: int):
        """Go to the previous workspace (without animation)"""
        current = pyvda.GetCurrentDesktopNumber()
        go_to_n(current-n)