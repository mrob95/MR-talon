import time
from talon import Context, Module, actions, clip, ui

ctx = Context()
mod = Module()

@ctx.action_class("edit")
class edit_actions:
    def selected_text() -> str:
        with clip.capture() as s:
            actions.edit.copy()
        try:
            return s.get()
        except clip.NoChange:
            return ""
    def undo(): actions.key('ctrl-z')
    def paste(): actions.key('ctrl-v')
    def copy(): actions.key('ctrl-c')
    def save(): actions.key('ctrl-s')
    def line_insert_down(): actions.key('ctrl-enter')
    def line_clone():
        actions.key('home shift-end ctrl-c end enter ctrl-v')
        actions.sleep('50ms')
    def delete_word(): actions.key("ctrl-backspace")

@mod.action_class
class Actions:
    def paste(text: str):
        """Pastes text and preserves clipboard"""

        with clip.revert():
            clip.set_text(text)
            actions.edit.paste()
            # sleep here so that clip.revert doesn't revert the clipboard too soon
            actions.sleep("150ms")

    def delete_word_right():
        """Delete a word to the right"""
        actions.key("ctrl-delete")
