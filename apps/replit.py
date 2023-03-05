from talon import ui, Module, Context, registry, actions, imgui, cron


mod = Module()
ctx = Context()

ctx.matches = r"""
title: /.* - Replit - .*/
"""

@ctx.action_class('edit')
class EditActions:
    def line_insert_down():
        actions.key('end enter')
