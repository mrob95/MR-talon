from talon import *

mod = Module()
ctx = Context()
ctx.matches = r"""
title: /TIS-100/
"""

ctx.lists["tis100_registers"] = {
    "up": "up",
    "left": "left",
    "down": "down",
    "right": "right",
    "nil": "nil",
    "last": "last",
    "any": "any",
    "ack": "acc",
}

ctx.lists["tis100_tags"] = {
    "negative": "negative",
    "positive": "positive",
    "done": "done",
    "start": "start",
}