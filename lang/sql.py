from user.imports import *

ctx = Context("sql")
ctx.matches = r"""
title: /\.sql/
title: /Server Management Studio/
"""

ctx.lists["self.functions"] = {
    "average": "AVG",
    "count": "COUNT",
    "length": "LENGTH",
    "max": "MAX",
    "min": "MIN",
    "sum": "SUM",
}

ctx.lists["self.logicals"] = {
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

