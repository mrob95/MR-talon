from talon import *

mod = Module()
ctx = Context()
ctx.matches = r"""
title: /shenzhen/
"""

mod.list("tis100_registers")
ctx.lists["user.tis100_registers"] = {
    "acc": "acc",
    "dat": "dat",
    "null": "null",
    "pee zero": "p0",
    "pee one": "p1",
    "ex zero": "x0",
    "ex one": "x1",
    "ex two": "x2",
    "ex three": "x3",
}

mod.list("tis100_tags")
ctx.lists["user.tis100_tags"] = {
    "negative": "negative",
    "positive": "positive",
    "done": "done",
    "start": "start",
}
