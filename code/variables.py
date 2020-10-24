from talon import *
from talon.grammar import Phrase
from typing import Union

mod = Module()
ctx = Context()

mod.list("variables")
ctx.lists["user.variables"] = {}

@mod.action_class
class Actions:
    def store_variable(phrase: Union[Phrase, str]):
        """"""
        old_clip = clip.get()
        clip.set_text("")
        actions.edit.copy()
        actions.sleep("150ms")
        text = clip.get()
        words = " ".join(actions.dictate.parse_words(phrase))
        ctx.lists["user.variables"] = {
            **ctx.lists["user.variables"],
            words: text,
        }
        app.notify(f"{words}: {text}")

        clip.set(old_clip)

    def clear_variables():
        """"""
        ctx.lists["user.variables"] = {}