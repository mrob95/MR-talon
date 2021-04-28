from talon import ui, Module, Context, registry, actions, imgui, cron

ctx = Context("sql")
ctx.matches = r"""
title: /\.sql/
title: /Server Management Studio/
"""

ctx.lists["user.functions"] = {
    "average": "avg",
    "count": "count",
    "length": "length",
    "max": "max",
    "min": "min",
    "sum": "sum",
}

ctx.lists["user.logicals"] = {
    "and": " and ",
    "as": " as ",
    "between": " between ",
    "in": " in ",
    "is": " is ",
    "is not": " is not ",
    "like": " like ",
    "or": " or ",
    "on": " on ",
    "then": " then ",
    "not": " not ",
}

