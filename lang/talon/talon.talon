title: /.*\.talon$/
-
OS windows: "os: windows\n"
app is: "app: "
app regex:
    "app: //"
    key(left)
title regex:
    "title: //"
    key(left)
key enter: "key(enter)\n"
#
fun [user] {user.talon_actions}: user.insert_function(talon_actions)
list [user] {user.talon_lists}: "{{{talon_lists}}}"
capture [user] {user.talon_captures}: "<{talon_captures}>"
tag [user] {user.talon_tags}: "tag: {talon_tags}"
set tag [user] {user.talon_tags}: "tag(): {talon_tags}"
#
mod control: "ctrl-"
mod shift: "shift-"
mod (alt | old): "alt-"
mod down: ":down "
mod up: ":up "
#
capture digits: "<user.digits>"
capture ordinals: "<user.numberth>"
capture numbers: "[<user.n20>]"
capture repeat: "<user.r20>"
capture phrase: "<phrase>"
#
lodge and: "and "
lodge or: " or "
assign: " = "
#
command <phrase>$:
    insert(user.formatted_text(phrase or "", 0, 0))
    ":"
commenter <phrase>$:
    "# "
    insert(user.formatted_text(phrase or "", 4, 0))
insert line break:
    "# ------------------------------------------------"
