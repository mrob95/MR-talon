from talon import ui, Module, Context, registry, actions, imgui, cron, app
from typing import Dict
import os
import json
import re

mod = Module()

if app.platform == "windows":
    snippet_path = os.path.expandvars(r"%AppData%\Code\User\snippets")
elif app.platform == "mac":
    snippet_path = os.path.expanduser(
        "~/Library/Application Support/Code/User/snippets"
    )


def get_user_snippets(lang: str) -> Dict[str, str]:
    p = f"{snippet_path}/{lang}.json"
    if not os.path.exists(p):
        return {}
    with open(p, "r") as f:
        raw = f.read()
        clean = re.sub("//.*", "", raw)
        js = json.loads(clean)
    return {k: v["prefix"] for k, v in js.items()}


@mod.action_class
class Actions:
    def snippet(s: str) -> None:
        """Insert a snippet"""
        actions.key("alt-\\")
        actions.insert(s)
        actions.key("enter")

mod.list("snippets")

py_ctx = Context()
py_ctx.matches = r"""
tag: user.python
"""
py_ctx.lists["user.snippets"] = {
    **get_user_snippets("python"), **{
        "class funky": "def(class method)",
        "class static funky": "def(class static method)",
        "class": "class",
        "else if": "elif",
        "for": "for",
        "funky": "def",
        "if else": "if/else",
        "if": "if",
        "lambda": "lambda",
        "try except": "try/except",
        "while": "while",
        "with": "with",
    }
}

tf_ctx = Context()
tf_ctx.matches = r"""
title: /.*\.tf/
"""
tf_ctx.lists["user.snippets"] = {
    **get_user_snippets("terraform"), **{
        "module": "module",
        "provisioner": "provisioner",
        "output": "output",
        "variable": "vare",
        }
}

go_ctx = Context()
go_ctx.matches = r"""
title: /\.go/
"""
go_ctx.lists["user.snippets"] = {
    **get_user_snippets("go"), **{
        "single import": "im",
        "multiple imports": "ims",
        "single constant": "co",
        "multiple constants": "cos",
        "type function": "tyf",
        "type interface": "tyi",
        "type struct": "tys",
        "package main and main function": "pkgm",
        "function": "func",
        "method": "meth",
        "variable": "var",
        "switch": "switch",
        "select": "sel",
        "case clause": "cs",
        "for": "for",
        "for range": "forr",
        "channel": "ch",
        "map": "map",
        "empty interface": "in",
        # "append": "append",
        "if": "if",
        "else": "el",
        "if else": "ie",
        "if error": "iferr",
        "fmt Print line": "fp",
        "fmt Print F": "ff",
        "log Print line": "lp",
        "log Print F": "lf",
        "log variable content": "lv",
        "make": "make",
        "new": "new",
        "panic": "pn",
        # "http ResponseWriter *Request": "wr",
        # "http.HandleFunc": "hf",
        # "http handler declaration": "hand",
        # "http.Redirect": "rd",
        # "http.Error": "herr",
        # "http.ListenAndServe": "las",
        # "http.Serve": "sv",
        "go routine anonymous function": "go",
        "go routine function": "gf",
        "defer": "df",
        "test function": "tf",
        "test main": "tm",
        "benchmark function": "bf",
        "example function": "ef",
        "table driven test": "tdt",
        "init function": "finit",
        "main function": "fmain",
        "method": "meth",
        "hello world web app": "helloweb",
        "sort implementation": "sort",
    }
}
