from talon import ui, Module, Context, registry, actions, imgui, cron


mod = Module()
ctx = Context()
ctx.matches = r"""
title: /.sh$/
"""

ctx.lists["user.logicals"] = {
    "and": " && ",
    "or": " || ",
}
