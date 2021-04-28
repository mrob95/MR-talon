from talon import ui, Module, Context, registry, actions, imgui, cron

mod = Module()
ctx = Context()
ctx.matches = r"""
title: /TIS-100/
"""

mod.list("tis100_registers")
ctx.lists["user.tis100_registers"] = {
    "up": "up",
    "left": "left",
    "down": "down",
    "right": "right",
    "nil": "nil",
    "last": "last",
    "any": "any",
    "ack": "acc",
}

mod.list("tis100_tags")
ctx.lists["user.tis100_tags"] = {
    "negative": "negative",
    "positive": "positive",
    "done": "done",
    "start": "start",
}