from talon import Module, Context, actions, clip
import re

mod = Module()
ctx = Context()

@mod.action_class
class Actions:
    def insert_function(pattern: str):
        """Insert a string, followed by parentheses, wrapping selected text."""
        # try:
        #     with clip.capture() as s:
        #         actions.edit.copy()
        #     actions.insert(f"{pattern}({s.get()})")
        # except clip.NoChange:
        #     actions.insert(f"{pattern}()")
        #     actions.key("left")
        old_clip = clip.get()
        clip.set_text("")
        actions.edit.copy()
        new_clip = clip.get()
        actions.insert(f"{pattern}({new_clip})")
        if not new_clip:
            actions.key("left")
        clip.set(old_clip)


mod.list("functions", desc="like_this()")
mod.list("logicals", desc="logical operators")
