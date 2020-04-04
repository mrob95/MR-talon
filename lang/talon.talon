title: /.*\.talon$/
-
key enter: "key(enter)\n"
fun key:
    "key()"
    key(left)
fun insert:
    "insert()"
    key(left)
mod control: "ctrl-"
mod shift: "shift-"
mod alt: "alt-"
mod down: ":down "
mod up: ":up "
capture digits: "<user.digits>"
capture ordinals: "<user.numberth>"
capture numbers: "<user.n20>"
capture repeat: "<user.r20>"
lodge and: "and "
lodge or: "or "
assign: " = "