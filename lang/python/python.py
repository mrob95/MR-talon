from typing import Mapping
from user.imports import *

mod = Module()
ctx = Context("python")
mod.tag("python")

ctx.matches = r"""
tag: user.python
"""

ctx.lists["user.functions"] = {
    "integer": "int",
    "int": "int",
    "hitter items": "iteritems",
    "iter items": "iteritems",
    "append": "append",
    "apply": "apply",
    "bites": "bytes",
    "breakpoint": "breakpoint",
    "capitalise": "capitalize",
    "clear": "clear",
    "callable": "callable",
    "character": "chr",
    "copy": "copy",
    "count": "count",
    "ends with": "endswith",
    "enumerate": "enumerate",
    "extend": "extend",
    "find all": "find_all",
    "find": "find",
    "float": "float",
    "hex": "hex",
    "head": "head",
    "get attribute": "getattr",
    "has attribute": "hasattr",
    "join": "join",
    "index": "index",
    "insert": "insert",
    "items": "items",
    "is instance": "isinstance",
    "init": "__init__",
    "keys": "keys",
    "length": "len",
    "list": "list",
    "logger debug": "logger.debug",
    "logger info": "logger.info",
    "logger error": "logger.error([|], exc_info=True)",
    "lower": "lower",
    "min": "min",
    "minimum": "min",
    "max": "max",
    "maximum": "max",
    "pop": "pop",
    "print": "print",
    "quit": "quit",
    "range": "range",
    "read lines": "readlines",
    "read": "read",
    "remove": "remove",
    "replace": "replace",
    "reverse": "reverse",
    "set default": "setdefault",
    "sort": "sort",
    "string": "str",
    "strip": "strip",
    "split": "split",
    "starts with": "startswith",
    "sum": "sum",
    "title": "title",
    "tuple": "tuple",
    "type": "type",
    "update": "update",
    "upper": "upper",
    "values": "values",
    "write": "write",
}

ctx.lists["user.logicals"] = {
    "and": " and ",
    "as": " as ",
    "else": " else ",
    "if": " if ",
    "in": " in ",
    "is": " is ",
    "is not": " is not ",
    "not": " not ",
    "not in": " not in ",
    "or": " or ",
    "for": " for ",
}

# mod.list("py_umeths", desc="Unary methods")
mod.list("py_umeths")
ctx.lists["user.py_umeths"] = {
    "integer": "int",
    "iter": "iter",
    "length": "len",
    "negation": "neg",
    "boolean": "nonzero",
    "non zero": "nonzero",
    "reper": "repr",
    "representation": "repr",
    "absolute": "abs",
    "ceiling": "ceil",
    "call": "call",
    "dir": "dir",
    "enter": "enter",
    "floor": "floor",
    "invert": "invert",
    "name": "name",
    "new": "new",
    "positive": "pos",
    "size of": "sizeof",
    "string": "str",
    "truncate": "trunc",
    "unicode": "unicode",
}

# mod.list("py_bmeths", desc="Binary methods")
mod.list("py_bmeths")
ctx.lists["user.py_bmeths"] = {
    "add": "add",
    "subtract": "sub",
    "multiply": "mul",
    "divide": "div",
    "floor divide": "floordiv",
    "equal": "eq",
    "not equal": "ne",
    "less than": "lt",
    "greater than": "gt",
    "less equal": "le",
    "greater equal": "ge",
    "modulo": "mod",
    "power": "pow",
    "and": "and",
    "or": "or",
    "ex or": "xor",
    "left shift": "lshift",
    "right shift": "rshift",
}

# mod.list("py_mmeths", desc="Misc methods")
mmeths = {
    "new"             : ["new", "cls"],
    "delete"          : ["del", "self"],
    "get attribute"   : ["getattr", "self, name"],
    "delete attribute": ["delattr", "self, name"],
    "set attribute"   : ["setattr", "self, name, value"],
    "get item"        : ["getitem", "self, key"],
    "set item"        : ["setitem", "self, key, value"],
    "delete item"     : ["delitem", "self, key"],
    "contains"        : ["contains", "self, item"],
    "missing"         : ["missing", "self, key"],
    "round"           : ["round", "self, n"],
    "exit"            : ["exit", "type, value, traceback"],
}
mod.list("py_mmeths")
ctx.lists["user.py_mmeths"] = {
    f"{k}": f"def __{v[0]}__({v[1]}):" for k, v in mmeths.items()
}

mod.list("py_exceptions")
ctx.lists["user.py_exceptions"] = {
    "arithmetic"        : "ArithmeticError",
    "assertion"         : "AssertionError",
    "attribute"         : "AttributeError",
    "environment"       : "EnvironmentError",
    "EOF"               : "EOFError",
    "exception"         : "Exception",
    "floating-point"    : "FloatingPointError",
    "import"            : "ImportError",
    "index"             : "IndexError",
    "IO"                : "IOError",
    "key"               : "KeyError",
    "keyboard interrupt": "KeyboardInterrupt",
    "lookup"            : "LookupError",
    "name"              : "NameError",
    "not implemented"   : "NotImplementedError",
    "OS"                : "OSError",
    "overflow"          : "OverflowError",
    "runtime"           : "RuntimeError",
    "standard"          : "StandardError",
    "stop iteration"    : "StopIteration",
    "syntax"            : "SyntaxError",
    "system exit"       : "SystemExit",
    "type"              : "TypeError",
    "unbound local"     : "UnboundLocalError",
    "value"             : "ValueError",
    "zero division"     : "ZeroDivisionError",
}

mod.list("py_types")
ctx.lists["user.py_types"] = {
    "string": "str",
    "float": "float",
    "int": "int",
    "integer": "int",
    "boolean": "bool",
    "bool": "bool",
    "Abstract Set": "AbstractSet",
    "Any": "Any",
    "Any Str": "AnyStr",
    "Async Context Manager": "AsyncContextManager",
    "Async Generator": "AsyncGenerator",
    "Async Iterable": "AsyncIterable",
    "Async Iterator": "AsyncIterator",
    "Awaitable": "Awaitable",
    "Binary I O": "BinaryIO",
    "Byte String": "ByteString",
    "Callable": "Callable",
    "Chain Map": "ChainMap",
    "Class Var": "ClassVar",
    "Collection": "Collection",
    "Container": "Container",
    "Context Manager": "ContextManager",
    "Coroutine": "Coroutine",
    "Counter": "Counter",
    "Default Dict": "DefaultDict",
    "Deque": "Deque",
    "Dict": "Dict",
    "Forward Ref": "ForwardRef",
    "Frozen Set": "FrozenSet",
    "Generator": "Generator",
    "Generic": "Generic",
    "Hashable": "Hashable",
    "I O": "IO",
    "Items View": "ItemsView",
    "Iterable": "Iterable",
    "Iterator": "Iterator",
    "K T": "KT",
    "Keys View": "KeysView",
    "List": "List",
    "Mapping": "Mapping",
    "Mapping View": "MappingView",
    "Match": "Match",
    "Method Descriptor Type": "MethodDescriptorType",
    "Method Wrapper Type": "MethodWrapperType",
    "Mutable Mapping": "MutableMapping",
    "Mutable Sequence": "MutableSequence",
    "Mutable Set": "MutableSet",
    "Named Tuple": "NamedTuple",
    "Named Tuple Meta": "NamedTupleMeta",
    "New Type": "NewType",
    "No Return": "NoReturn",
    "Optional": "Optional",
    "Ordered Dict": "OrderedDict",
    "Pattern": "Pattern",
    "Reversible": "Reversible",
    "Sequence": "Sequence",
    "Set": "Set",
    "Sized": "Sized",
    "Supports Abs": "SupportsAbs",
    "Supports Bytes": "SupportsBytes",
    "Supports Complex": "SupportsComplex",
    "Supports Float": "SupportsFloat",
    "Supports Int": "SupportsInt",
    "Supports Round": "SupportsRound",
    "Text": "Text",
    "Text IO": "TextIO",
    "Tuple": "Tuple",
    "Type": "Type",
    "Type Var": "TypeVar",
    "Union": "Union",
    "Values View": "ValuesView",
    "Wrapper Descriptor Type": "WrapperDescriptorType",
}

mod.list("py_modules")
ctx.lists["user.py_modules"] = {
    "jason": "json",
    "logging": "logging",
    "tommel": "toml",
    "O S": "os",
    "pandas": "pandas as pd",
    "numb pie": "numpy as np",
    "pie test": "pytest",
    "regex": "re",
    "requests": "requests",
    "sis": "sys",
}

mod.list("py_imports")
ctx.lists["user.py_imports"] = {
    "argument parser": "from argparse import ArgumentParser",
    "beautiful soup": "from bs4 import BeautifulSoup",
    "create engine": "from sqlalchemy import create_engine",
    "counter": "from collections import Counter",
    "date time": "from datetime import datetime",
    "data class": "from dataclasses import dataclass",
    "Enum": "from enum import Enum, auto",
    "path": "from pathlib import Path",
    "thread pool executor": "from concurrent.futures import ThreadPoolExecutor",
    "progress bar": "from tqdm import tqdm",
    "wraps": "from functools import wraps",
}
