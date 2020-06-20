os: windows
app: WindowsTerminal.exe
-
action(edit.paste): key(ctrl-shift-v)
action(edit.copy):
    print("Local")
    key(ctrl-shift-c)
# ---
<user.numberth> tab: key("ctrl-alt-{numberth}")
close tab <user.n20>: user.slow_key("ctrl-shift-w:{n20}")
next tab <user.n20>: key("ctrl-tab:{n20}")
previous tab <user.n20>: key("ctrl-shift-tab:{n20}")
duplicate tab: key(ctrl-shift-d)
new tab: key(ctrl-shift-t)
open settings: key(ctrl-,)
focus left: key(ctrl-alt-shift-left)
focus right: key(ctrl-alt-shift-right)
focus up: key(ctrl-alt-shift-up)
focus down: key(ctrl-alt-shift-down)
size left <user.n20>: key("alt-shift-left:{n20}")
size right <user.n20>: key("alt-shift-right:{n20}")
size up <user.n20>: key("alt-shift-up:{n20}")
size down <user.n20>: key("alt-shift-down:{n20}")
split right: key(ctrl-shift-h)
split down: key(ctrl-h)
drop down: key(ctrl-shift-f1)
clear screen: key(ctrl-l)