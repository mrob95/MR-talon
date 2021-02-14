"""
macros are not savable, but they are semantic in that functions are recorded,
not keypresses. This means that macros can interact with your computer state
such as by looking at what is in the clipboard, are referencing nearby text.
"""
from talon import *
from talon import imgui
from dataclasses import dataclass
from typing import Any, List, Optional

@dataclass
class MacroRecorder:
    phrases: Optional[List[Any]] = None
    recording: bool = False
    playing: bool = False
    num_recorded: int = 0
    wait: int = 20 # ms to wait between phrases when executing

    def reset(self):
        self.phrases = []
        self.recording = False
        self.playing = False
        self.num_recorded = 0
        self.wait = 20

    def play(self):
        self.playing = True # Disables "macro start"
        for phrase in self.phrases:
            actions.core.run_phrase(phrase)
            actions.sleep(f"{self.wait}ms")
        self.playing = False

    def add_phrase(self, phrase):
        self.phrases.append(phrase)
        self.num_recorded += 1

    def slow_down(self):
        self.wait += 50

mod = Module()
macro = MacroRecorder()

@imgui.open(x=1100, y=1043, software=False)
def gui(gui: imgui.GUI):
    gui.text(f"Macro recording: {macro.num_recorded}")

@mod.action_class
class Actions:
    def macro_start():
        """record a new macro"""
        # Since we add the last phrase to the macro after it has been executed,
        # macro.phrases will always contain "macro start",
        # so make this a no-op when we are playing the macro.
        if not macro.playing:
            macro.reset()
            macro.recording = True
            gui.show()

    def macro_stop():
        """stop recording"""
        gui.hide()
        macro.recording = False

    def macro_play():
        """play recorded macro"""
        actions.user.macro_stop()
        macro.play()

    def macro_play_slower():
        """play recorded macro, and slow it down for programs which drop keys"""
        actions.user.macro_stop()
        macro.slow_down()
        macro.play()

def macro_cb(recognition_result):
    if macro.recording and "parsed" in recognition_result:
        macro.add_phrase(actions.core.last_phrase())

speech_system.register("post:phrase", macro_cb)
