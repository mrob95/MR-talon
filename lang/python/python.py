from typing import Mapping, Union, Optional, Dict
from talon import ui, Module, Context, registry, actions, imgui, cron
from user.code.speakify import create_voice_mapping
import re
import time

mod = Module()
ctx = Context("python")
mod.tag("python")

ctx.matches = r"""
tag: user.python
"""

def print_string(s):
    return f"print(f'{s} = {{{s}}}')"


def set_list(name: str, values: Dict):
    ctx.lists[name] = values

@ctx.action_class("user")
class Actions:
    def lang_print(s: str):
        actions.insert(print_string(s))
    def get_var_regex() -> str:
        return r"(import\s+|\s|,|\()([A-Za-z_]+?)(,|:|\)|\s*=|\(|\.|\n)"


@mod.action_class
class Actions:
    def print_all_assignments():
        """Adds a print statement below each assignment in a selected block of python code."""
        text = actions.edit.selected_text()
        new_lines = []
        for line in text.split("\n"):
            # Special case for e.g. 'if test: a = 1'
            one_line_if_match = re.match(r"(\s*)(.+?):\s*((.+)=(.+))$", line)
            if one_line_if_match:
                ws, if_statement, assignment, *_ = one_line_if_match.groups()
                new_lines.append(f"{ws}{if_statement}")
                new_lines.append(f"{ws}    {assignment}")
                line = f"{ws}    {assignment}"
            else:
                new_lines.append(line)

            for pattern, extra_whitespace in [
                (r"^(\s*)([^\(\#]+?) = .+?$", ""),
                (r"^(\s*)for (.+?) in .+?:$", "    "),
            ]:
                assignment_match = re.match(pattern, line)
                if assignment_match:
                    whitespace, assigned = assignment_match.groups()
                    for sub_assigned in assigned.split(","):
                        sub_assigned = sub_assigned.strip()
                        new_lines.append(f"{whitespace}{extra_whitespace}{print_string(sub_assigned)}")
        actions.user.paste("\n".join(new_lines))

    def print_arguments():
        """Adds a print statement below a selected function declaration containing its arguments."""
        text = actions.edit.selected_text()
        text_no_newlines = text.replace("\n", "")

        match = re.search(r"def (.+?)\((.+?)\):", text_no_newlines)
        if not match: return
        name, args_str = match.groups()

        # Get rid of e.g. Union[str, int]
        args_str = re.sub(r"\[.+?\]", "", args_str)
        args = args_str.split(",")
        args_to_print = []
        for arg in args:
            if arg in {"self", "cls"}: continue
            arg_name = arg.strip().split(" ")[0].split("=")[0].strip(": ")
            args_to_print.append(f"{arg_name}={{{arg_name}}}")

        print_str = f'print(f"{name}: {", ".join(args_to_print)}")'
        result = "\n    ".join((text, print_str))
        actions.user.paste(result)

    def refactor_assignment():
        """Refactor a simple if-else assignment into an inline assignmenth"""
        text = actions.edit.selected_text()
        match = re.search(r"(\s*)if (.+?):\s+(?P<ident>.+?)\s?=\s?(.+?)\n\s*else:\s+(?P=ident)\s?=\s?(.+?)", text, re.MULTILINE)

        if match:
            ws, test, ident, value_if, value_else = match.groups()
            actions.user.paste(f"{ws}{ident} = {value_if} if {test} else {value_else}")

mod.list("py_modules")
ctx.lists["user.py_modules"] = {
    "jason": "json",
    "logging": "logging",
    "numb pie": "numpy as np",
    "O S": "os",
    "pandas": "pandas as pd",
    "pie test": "pytest",
    "regex": "re",
    "requests": "requests",
    "random": "random",
    "sis": "sys",
    "subprocess": "subprocess",
    "time": "time",
    "tommel": "toml",
}

mod.list("py_imports")
ctx.lists["user.py_imports"] = {
    "argument parser": "from argparse import ArgumentParser",
    "beautiful soup": "from bs4 import BeautifulSoup",
    "create engine": "from sqlalchemy import create_engine",
    "counter": "from collections import Counter",
    "default dictionary": "from collections import defaultdict",
    "default dict": "from collections import defaultdict",
    "date time": "from datetime import datetime",
    "data class": "from dataclasses import dataclass",
    "Enum": "from enum import Enum, auto",
    "mock": "from mock import Mock, patch",
    "path": "from pathlib import Path",
    "thread pool executor": "from concurrent.futures import ThreadPoolExecutor",
    "progress bar": "from tqdm import tqdm",
    "pretty print": "from pprint import pprint",
    "wraps": "from functools import wraps",
}

mod.list("py_decorators", "Python decorators e.g. @property")
ctx.lists["user.py_decorators"] = {
    "class method": "classmethod",
    "context manager": "context_manager",
    "LRU cache": "lru_cache",
    "property": "property",
    "static method": "staticmethod",
    "total ordering": "total_ordering",
    "wraps": "wraps",
}

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
    "exists": "exists",
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
    "logger warning": "logger.info",
    "logger error": "logger.error([|], exc_info=True)",
    "lower": "lower",
    "min": "min",
    "minimum": "min",
    "max": "max",
    "maximum": "max",
    "pop": "pop",
    "path": "Path",
    "print": "print",
    "quit": "quit",
    "range": "range",
    "read lines": "readlines",
    "read": "read",
    "read text": "read_text",
    "remove": "remove",
    "replace": "replace",
    "reverse": "reverse",
    "set": "set",
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
    "write text": "write_text",
}

ctx.lists["user.logicals"] = {
    "and": " and ",
    "and not": " and not ",
    "as": " as ",
    "else": " else ",
    "if": " if ",
    "if not": " if not ",
    "in": " in ",
    "is": " is ",
    "is not": " is not ",
    "not": " not ",
    "not in": " not in ",
    "or": " or ",
    "or not": " or not ",
    "for": " for ",
}

ctx.lists["user.values"] = {
    "false": "False",
    "none": "None",
    "true": "True",
}

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

mod.list("py_mmeths")
ctx.lists["user.py_mmeths"] = {
    "new"             : "def __new__(cls):",
    "delete"          : "def __del__(self):",
    "get attribute"   : "def __getattr__(self, name):",
    "delete attribute": "def __delattr__(self, name):",
    "set attribute"   : "def __setattr__(self, name, value):",
    "get item"        : "def __getitem__(self, key):",
    "set item"        : "def __setitem__(self, key, value):",
    "delete item"     : "def __delitem__(self, key):",
    "contains"        : "def __contains__(self, item):",
    "missing"         : "def __missing__(self, key):",
    "round"           : "def __round__(self, n):",
    "exit"            : "def __exit__(type, value, traceback):",
}

mod.list("py_exceptions")
ctx.lists["user.py_exceptions"] = {
    "arithmetic error"        : "ArithmeticError",
    "assertion error"         : "AssertionError",
    "attribute error"         : "AttributeError",
    "environment error"       : "EnvironmentError",
    "EOF error"               : "EOFError",
    "exception error"         : "Exception",
    "floating-point error"    : "FloatingPointError",
    "import error"            : "ImportError",
    "index error"             : "IndexError",
    "IO error"                : "IOError",
    "key error"               : "KeyError",
    "keyboard interrupt error": "KeyboardInterrupt",
    "lookup error"            : "LookupError",
    "name error"              : "NameError",
    "not implemented error"   : "NotImplementedError",
    "OS error"                : "OSError",
    "overflow error"          : "OverflowError",
    "runtime error"           : "RuntimeError",
    "standard error"          : "StandardError",
    "stop iteration error"    : "StopIteration",
    "syntax error"            : "SyntaxError",
    "system exit error"       : "SystemExit",
    "type error"              : "TypeError",
    "unbound local error"     : "UnboundLocalError",
    "value error"             : "ValueError",
    "zero division error"     : "ZeroDivisionError",
}

mod.list("py_typing_types")
py_typing_types = {
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
    "cast": "cast",
    "Callable": "Callable",
    "Chain Map": "ChainMap",
    "Class Var": "ClassVar",
    "Collection": "Collection",
    "Container": "Container",
    "Context Manager": "ContextManager",
    "Coroutine": "Coroutine",
    "Counter": "Counter",
    "Default Dictionary": "DefaultDict",
    "Deque": "Deque",
    "Dictionary": "Dict",
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
    "type checking": "TYPE_CHECKING",
    "Union": "Union",
    "Values View": "ValuesView",
    "Wrapper Descriptor Type": "WrapperDescriptorType",
}
ctx.lists["user.py_typing_types"] = py_typing_types

mod.list("py_types")
ctx.lists["user.py_types"] = {
    **py_typing_types, **{
    "data frame": "pd.DataFrame",
    "path": "Path",
    "string": "str",
    "float": "float",
    "int": "int",
    "integer": "int",
    "boolean": "bool",
    "bool": "bool",
    }
}

mod.list("py_fopen_modes")
ctx.lists["user.py_fopen_modes"] = {
    "append": "a",
    "binary": "b",
    "plus": "+",
    "read": "r",
    "write": "w",
}
