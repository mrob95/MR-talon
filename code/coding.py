from talon import Module, Context, actions, clip
import re

mod = Module()
ctx = Context()

global_temporary_store = ""

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

        if pattern.endswith("!"):
            actions.insert(pattern.rstrip("!"))
            return

        old_clip = clip.get()
        clip.set_text("")
        actions.edit.copy()
        actions.sleep("150ms")
        new_clip = clip.get()


        #
        # Two cases:
        # pattern is just a string e.g. "find" -> find()
        # pattern contains a marker e.g. "find({|}, ...)" -> find(, ...)
        # and leave cursor in the right place
        #
        if pattern.find("{|}") == -1:
            pattern += "({|})"
        end_pos = pattern.find("{|}")
        s = pattern.replace("{|}", new_clip)
        actions.insert(s)
        # If we didn't insert selected text, move the cursor
        actions.key(f"left:{len(s) - end_pos}")
        actions.sleep("150ms")
        clip.set(old_clip)

    def insert_fancy(pattern: str):
        """Insert a string."""
        if not pattern:
            return

        if pattern[-1] == "@":
            # String then return
            s = pattern[:-1]
            actions.insert(s)
            actions.key("enter")
            return

        if "{|}" in pattern:
            end_pos = pattern.find("{|}")
            s = pattern.replace("{|}", "")
            actions.insert(s)
            actions.key(f"left:{len(s) - end_pos}")
            return

        actions.insert(pattern)



    def temp_store():
        """"""
        global global_temporary_store
        old_clip = clip.get()
        actions.edit.copy()
        actions.sleep("100ms")
        global_temporary_store = clip.get()
        clip.set(old_clip)

    def temp_insert():
        """"""
        global global_temporary_store
        actions.insert(global_temporary_store)


mod.list("functions", desc="like_this()")
mod.list("logicals", desc="logical operators")
