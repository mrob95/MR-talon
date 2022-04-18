from talon import ui, Module, Context, registry, actions, imgui, cron

mod = Module()
ctx = Context()

ctx.matches = r"""
tag: user.terminal
"""


@ctx.action_class('edit')
class EditActions:
    def line_clone():
        # "duple" misrecognition
        actions.mimic('git pull')

    def delete_word():
        actions.key("ctrl-w")

@ctx.action_class('user')
class EditActions:
    def delete_word_right():
        actions.key("alt-d")
