title: /TIS-100/
-
settings():
    key_hold = 16
    key_wait = 16

fun move: "mov "
fun swap: "swp "
fun save: "sav "
fun add: "add "
fun sub: "sub "
fun negate: "neg "

fun jump {tis100_tags}: "jmp {tis100_tags}"
fun jump: "jmp "
jump negative: "jlz "
jump positive: "jgz "
jump equal zero: "jez "
jump not zero: "jnz "
jump offset: "jro "

move {tis100_registers} {tis100_registers}:
    "mov {tis100_registers_1}, {tis100_registers_2}"

{tis100_registers}: "{tis100_registers}"

tag {tis100_tags}: "{tis100_tags}"


quick reference: key(f1)
program run: key(f5)
program step: key(f6)