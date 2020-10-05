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
fun key: user.insert_function("key")
fun sleep: user.insert_function("sleep")
fun insert: user.insert_function("insert")
fun action: user.insert_function("action")
fun print: user.insert_function("print")
fun function: user.insert_function("user.insert_function")
fun formatted [text]: user.insert_function("user.formatted_text")
fun snake [text]: user.insert_function("user.snake")
#
mod control: "ctrl-"
mod shift: "shift-"
mod (alt | old): "alt-"
mod down: ":down "
mod up: ":up "
#
capture digits: "<user.digits>"
capture ordinals: "<user.numberth>"
capture numbers: "<user.n20>"
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