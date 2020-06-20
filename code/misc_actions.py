from user.imports import *
from talon import Module, Context, actions, clip
from win32gui import GetForegroundWindow, GetWindowText
import os
import re
import time
import dragonfly

from ctypes import (c_short, c_long, c_ushort, c_ulong, sizeof,
                    POINTER, pointer, Structure, Union, windll)
import win32con
import win32api


mod = Module()
ctx = Context()

@mod.action_class
class Actions:
    def slow_key(pattern: str, wait: str = "50ms"):
        """Press some keys slowly"""
        print(pattern)
        keys = pattern.split(" ")
        keys2 = []
        for k in keys:
            chord_rep = k.split(":")
            if len(chord_rep) == 1:
                keys2.append(chord_rep[0])
            elif len(chord_rep) == 2:
                keys2.extend([chord_rep[0]]*int(chord_rep[1]))
        for k in keys2:
            actions.key(k)
            actions.sleep(wait)

    def clip_replace(pattern: str, replacement: str):
        """Replace pattern in clipboard"""
        actions.sleep("150ms")
        cb = clip.text()
        actions.sleep("150ms")
        replaced = re.sub(pattern, replacement, cb)
        clip.set(replaced)

    def insert_git_url():
        """Insert git url from clipboard"""
        cb = clip.text()
        # actions.sleep("150ms")
        if cb.startswith("https://github.com"):
            if not cb.endswith(".git"):
                giturl = cb + ".git"
            else:
                giturl = cb
            actions.insert(giturl)

    def print_window_info():
        """Print random window information"""
        print(f"Shadow app: {ui.active_app()}")
        print(f"Shadow app exe: {ui.active_app().exe}")
        print(f"Shadow window title: {ui.active_window().title}")
        print(f"Actual window title: {GetWindowText(GetForegroundWindow())}")
        print(f"To check: {talon.windows.winevents.monitor.last_foreground}")
        print(f"Shadow hwnd: {ui.active_window().id}")
        print(f"Actual hwnd: {GetForegroundWindow()}")
        print(talon.windows.winevents._win_info(GetForegroundWindow()))
        print([w for w in ui.windows() if w.id == GetForegroundWindow()])

    def print_copy_info():
        """"""
        print("registry.actions['edit.copy']")
        print(registry.actions['edit.copy'])
        print([a.ctx for a in registry.actions['edit.copy']])
        # print(registry.contexts)
        # print(registry.contexts["user.basic.basic_keys.talon"])
        # print(registry.contexts["user.apps.windows_terminal.talon"])
        print('registry.contexts["user.basic.basic_keys.talon"] > registry.contexts["user.apps.windows_terminal.talon"]')
        print(registry.contexts["user.basic.basic_keys.talon"] > registry.contexts["user.apps.windows_terminal.talon"])

    def test_action(thing: str):
        """testing"""
        print(thing)
        # VOLUME_UP = win32con.VK_VOLUME_UP
        # VOLUME_DOWN = win32con.VK_VOLUME_DOWN
        # VOLUME_MUTE = win32con.VK_VOLUME_MUTE
        # MEDIA_NEXT_TRACK = win32con.VK_MEDIA_NEXT_TRACK
        # MEDIA_PREV_TRACK = win32con.VK_MEDIA_PREV_TRACK
        # MEDIA_PLAY_PAUSE = win32con.VK_MEDIA_PLAY_PAUSE
        # BROWSER_BACK = win32con.VK_BROWSER_BACK
        # BROWSER_FORWARD = win32con.VK_BROWSER_FORWARD
        # dragonfly.Key("playpause").execute()
        # print(MEDIA_PLAY_PAUSE)
        # scancode = windll.user32.MapVirtualKeyW(MEDIA_PLAY_PAUSE, 0)
        # print(scancode)
