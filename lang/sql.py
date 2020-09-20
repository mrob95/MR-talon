from talon import *

ctx = Context("sql")
ctx.matches = r"""
title: /\.sql/
title: /Server Management Studio/
"""

ctx.lists["user.functions"] = {
    "average": "AVG",
    "count": "COUNT",
    "length": "LENGTH",
    "max": "MAX",
    "min": "MIN",
    "sum": "SUM",
}

ctx.lists["user.logicals"] = {
    "and": " AND ",
    "as": " AS ",
    "between": " BETWEEN ",
    "in": " IN ",
    "is": " IS ",
    "is not": " IS NOT ",
    "like": " LIKE ",
    "or": " OR ",
    "on": " ON ",
    "then": " THEN ",
    "not": " NOT ",
}

