from talon import Module, Context, actions, clip
import re
mod = Module()
ctx = Context()

mod.list("filetype")
ctx.lists["user.filetype"] = {
    "pie": ".py",
    "python": ".py",
    "talon": ".talon",
    "see": ".c",
    "header": ".h",
    "H": ".h",
    "rust": ".rs",
    "tommel": ".toml",
    "text": ".txt",
    "mark": ".md",
    "markdown": ".md",
}

@mod.action_class
class Actions:
    def lang_print(s: str):
        """print"""

    def insert_function(pattern: str):
        """Insert a string, followed by parentheses, wrapping selected text."""
        if pattern.endswith("!"):
            actions.insert(pattern.rstrip("!"))
            return

        # text = actions.edit.selected_text()

        #
        # Two cases:
        # pattern is just a string e.g. "find" -> find()
        # pattern contains a marker e.g. "find([|], ...)" -> find(, ...)
        # and leave cursor in the right place
        #
        if pattern.find("[|]") == -1:
            pattern += "([|])"
        end_pos = pattern.find("[|]")
        s = pattern.replace("[|]", "")
        actions.insert(s)
        # If we didn't insert selected text, move the cursor
        actions.key(f"left:{len(s) - end_pos}")

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

        if "[|]" in pattern:
            end_pos = pattern.find("[|]")
            s = pattern.replace("[|]", "")
            actions.insert(s)
            actions.key(f"left:{len(s) - end_pos}")
            return

        actions.insert(pattern)


mod.list("functions", desc="like_this()")
mod.list("logicals", desc="logical operators")