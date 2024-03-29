from typing import Any
from talon import speech_system
from talon import ui, Module, Context, registry, actions, imgui, cron, clip, debug

import os
import webbrowser
import re
import time
from subprocess import Popen, run
from pathlib import Path

mod = Module()
ctx = Context()

@mod.action_class
class Actions:
    def browser_open(url: str):
        """Open the passed url in a web browser"""
        webbrowser.open_new_tab(url)

    def cd_directory_of(filename: str):
        """CD to the directory of the path passed."""
        p = Path(filename)
        directory = p.as_posix() if filename.endswith("/") else p.parent.as_posix()
        actions.insert(f"cd '{directory}'\n")

    def open_pdf(path: str):
        """Open a file using SumatraPDF"""
        Popen(["SumatraPDF", path])

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

    def dragon_mimic(phrase: str):
        """Mimic a phrase using the speech engine"""
        speech_system.engine_mimic(phrase)

    def kill_notepads():
        """Close all notepad windows"""
        run(["taskkill", "/IM", "notepad.exe", "/f", "/s", "localhost"], capture_output=True)
