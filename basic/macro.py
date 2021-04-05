from talon import imgui, ctrl, actions, Module, speech_system
from dataclasses import dataclass
from typing import Any, List, Optional, Tuple

MousePosition = Tuple[int, int]
@dataclass
class MacroRecorder:
    phrases: Optional[List[Any]] = None
    recording: bool = False
    playing: bool = False
    num_recorded: int = 0
    wait: int = 20 # ms to wait between phrases when executing
    mouse_marks: Optional[List[MousePosition]] = None
    mark_cursor: int = 0

    def reset(self):
        self.phrases = []
        self.recording = False
        self.playing = False
        self.num_recorded = 0
        self.wait = 20
        self.mouse_marks = []

    def play(self):
        self.mark_cursor = 0
        self.playing = True # Disables "macro start"
        for phrase in self.phrases:
            actions.mimic(phrase)
            actions.sleep(f"{self.wait}ms")
        self.playing = False

    def add_phrase(self, phrase):
        self.phrases.append(phrase)
        self.num_recorded += 1

    def slow_down(self):
        self.wait += 50

    def create_mouse_mark(self):
        x, y = ctrl.mouse_pos()
        self.mouse_marks.append((x, y))

    def move_to_mark(self):
        assert self.playing
        actions.sleep(f"{self.wait + 50}ms")
        pos = self.mouse_marks[self.mark_cursor]
        actions.mouse_move(*pos)
        self.mark_cursor += 1
        actions.sleep(f"{self.wait + 50}ms")

mod = Module()
macro = MacroRecorder()

@imgui.open(x=1050, y=1043)
def gui(gui: imgui.GUI):
    gui.text(f"Macro recording: {macro.num_recorded}")

@mod.action_class
class Actions:
    def macro_start():
        """record a new macro"""
        # Since we add the last phrase to the macro after it has been executed,
        # macro.phrases will always contain "macro start",
        # so make this a no-op when we are playing the macro.
        if macro.playing: return
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

    def macro_mouse_mark():
        """mark the current mouse position, or return to it if the macro is playing"""
        if macro.playing:
            macro.move_to_mark()
        else:
            macro.create_mouse_mark()


def macro_cb(recognition_result):
    if macro.recording and "parsed" in recognition_result:
        macro.add_phrase(recognition_result["parsed"]._unmapped)

speech_system.register("post:phrase", macro_cb)
