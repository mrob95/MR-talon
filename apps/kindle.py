from ..imports import *

ctx = Context("kindle", func=actions.context_matches(exe="kindle.exe"))

ctx.keymap({
    "library": Key("ctrl-alt-l"),
    "(show | hide) notebook": Key("ctrl-b"),
    "(search | find)": Key("ctrl-f"),
    "(synchronise | refresh)": Key("f5"),
})
