import logging
logging.getLogger("comtypes").setLevel(logging.WARNING)
import os

from talon.voice import Key, ui
import struct
from ctypes import cdll, windll
from . import utilities
from win32gui import GetForegroundWindow
import win32gui
import win32con

import pyvda

ASFW_ANY = -1

def maximise(m):
    wndh = GetForegroundWindow()
    win32gui.ShowWindow(wndh, win32con.SW_MAXIMIZE)

def minimise(m):
    wndh = GetForegroundWindow()
    win32gui.ShowWindow(wndh, win32con.SW_MINIMIZE)

def close_window(m):
    wndh = GetForegroundWindow()
    win32gui.PostMessage(wndh, win32con.WM_CLOSE, 0, 0)


def move_current_to_n(n=0, follow=False):
    wndh = ui.active_window().id
    pyvda.MoveWindowToDesktopNumber(wndh, n)
    if follow:
        pyvda.GoToDesktopNumber(n)

def go_to_n(n):
    # Helps make sure that the target desktop gets focus
    windll.user32.AllowSetForegroundWindow(ASFW_ANY)
    pyvda.GoToDesktopNumber(n)

def go_next(n=1):
    current = pyvda.GetCurrentDesktopNumber()
    go_to_n(current+n)

def go_previous(n=1):
    current = pyvda.GetCurrentDesktopNumber()
    go_to_n(current-n)