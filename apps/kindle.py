from user.imports import *


ctx = Context("kindle")
ctx.matches = r"""
app: Kindle.exe
"""

ctx.defines = r"""
library: key("ctrl-alt-l")
(show | hide) notebook: key("ctrl-b")
(search | find): key("ctrl-f")
(synchronise | refresh): key("f5")
"""