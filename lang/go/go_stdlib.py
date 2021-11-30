from talon import ui, Module, Context, registry, actions, imgui, cron
import json
from pathlib import Path


mod = Module()
ctx = Context()

ctx.matches = r"""
title: /\.go/
"""

go_packages = {
    "archive": "archive",
    "buff IO": "bufio",
    "builtin": "builtin",
    "bytes": "bytes",
    "compress": "compress",
    "container": "container",
    "context": "context",
    "crypto": "crypto",
    "database": "database",
    "debug": "debug",
    "embed": "embed",
    "encoding": "encoding",
    "errors": "errors",
    "expvar": "expvar",
    "flag": "flag",
    "format": "fmt",
    "go": "go",
    "hash": "hash",
    "html": "html",
    "image": "image",
    "index": "index",
    "IO": "io",
    "log": "log",
    "math": "math",
    "mime": "mime",
    "net": "net",
    "os": "os",
    "path": "path",
    "plugin": "plugin",
    "reflect": "reflect",
    "regex": "regexp",
    "syntax": "syntax",
    "runtime": "runtime",
    "sort": "sort",
    "string convert": "strconv",
    "stir conv": "strconv",
    "strings": "strings",
    "sync": "sync",
    "sis call": "syscall",
    "testing": "testing",
    "text": "text",
    "time": "time",
    "unicode": "unicode",
    "unsafe": "unsafe",
    "internal": "internal",
}

ctx.lists["user.doclinks"] = {
    **{k: f"https://pkg.go.dev/{v}" for k, v in go_packages.items()},
}


package_spoken_look_up = {v: k for k, v in go_packages.items()}

with open(Path(__file__).parent / "std_libs_2.json", "r") as f:
    libs_map = json.load(f)

go_stdlib_identifiers = {}
for package, identifier_map in libs_map.items():
    package_spoken = package_spoken_look_up[package]
    for spoken, ident in identifier_map.items():
        go_stdlib_identifiers[f"{package_spoken} {spoken}"] = ident

mod.list("go_stdlib")
ctx.lists["user.go_stdlib"] = go_stdlib_identifiers
mod.list("go_packages")
ctx.lists["user.go_packages"] = go_packages
