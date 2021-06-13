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
