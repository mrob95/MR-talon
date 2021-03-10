from user.utils import utilities
from talon import speech_system
from talon import *
import talon

from win32gui import GetForegroundWindow, GetWindowText
import os
import re
import time
from subprocess import Popen
from pathlib import Path

from ctypes import (c_short, c_long, c_ushort, c_ulong, sizeof,
                    POINTER, pointer, Structure, Union, windll)
import win32con
import win32api
import os
from pathlib import Path

mod = Module()
ctx = Context()

@mod.action_class
class Actions:
    def cd_directory_of(filename: str):
        """"""
        p = Path(filename)
        directory = p.parent.as_posix()
        print(directory)
        actions.insert(f"cd '{directory}'\n")


    def open_pdf(path: str):
        """"""
        Popen(["SumatraPDF", path])

    def view_talon_log():
        """Open the talon log viewer"""
        log_script = os.path.expanduser("~/AppData/Roaming/talon/.venv/Scripts/tail_log.bat")
        Popen([log_script])

    def slow_key(pattern: str, wait: str = "50ms"):
        """Press some keys slowly"""
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

    def print_window_info():
        """Print random window information"""
        print(f"{ui.active_app()=}")
        print(f"{ui.active_app().exe=}")
        print(f"{ui.active_window().title=}")
        # print(f"Shadow app: {ui.active_app()}")
        # print(f"Shadow app exe: {ui.active_app().exe}")
        # print(f"Shadow window title: {ui.active_window().title}")
        # print(f"Actual window title: {GetWindowText(GetForegroundWindow())}")
        # print(f"To check: {talon.windows.winevents.monitor.last_foreground}")
        # print(f"Shadow hwnd: {ui.active_window().id}")
        # print(f"Actual hwnd: {GetForegroundWindow()}")
        # print(talon.windows.winevents._win_info(GetForegroundWindow()))
        # print([w for w in ui.windows() if w.id == GetForegroundWindow()])

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
        pass

    def dragon_mimic(phrase: str):
        """mimic"""
        print(phrase)
        speech_system.engine_mimic(phrase)

    def kill_notepads():
        """"""
        utilities.kill_notepad()

    def record_error(path: str):
        """"""
        actions.key("ctrl-c")
        actions.sleep("200ms")
        s = clip.get().replace("\n", " ")
        actions.app.notify(s)
        with open(path, "a") as f:
            f.write(s + "\n")



# from talon import ctrl
# from talon.experimental.locate import locate
# # ctrl.mouse_move(*locate('example.png')[0].center)

# import time

# st = time.perf_counter()
# pos = locate("user/images/vscode/find-dialogue-cross.png")
# end = time.perf_counter()
# print(end - st)
# print(pos)

# speech_system.register("pre:phrase", lambda j: time.sleep(2t))

# from talon.experimental.textarea import TextArea
# area = TextArea()
# # area.theme = dark_theme
# area.title = 'Talon Buffer'
# area.value = 'hello world\nthis is a test '
# area.show()
# print('value', repr(area.value))
# span = area.word(0)
# print('first word', span, repr(area[span]))
# rect = area.text_to_screen(1)
# print(rect, area.screen_to_text(rect.center))
