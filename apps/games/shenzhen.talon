title: /SHENZHEN I\/O/
-
settings():
    key_hold = 16
    key_wait = 16

fun move: "mov "
fun mull: "mul "
fun add: "add "
fun sub: "sub "
fun not: "not "
fun sleep: "slp "
fun await: "slx "
fun equal: "teq "
fun greater: "tgt "
fun less: "tlt "
fun compare: "tcp "
fun digit: "dgt "
fun digit set: "dst "
fun no op: "nop "

# fun jump {tis100_tags}: "jmp {tis100_tags}"
fun jump: "jmp "


move {user.tis100_registers} {user.tis100_registers}:
    "mov {tis100_registers_1}, {tis100_registers_2}"

{user.tis100_registers}: "{tis100_registers}"

tag {user.tis100_tags}: "{tis100_tags}"


quick reference: key(f1)
program run: key(f5)
program step: key(f6)

colic:
    key(ctrl:down)
    sleep(16ms)
    user.mouse_drag()
    sleep(16ms)
    user.mouse_release()
    sleep(16ms)
    key(ctrl:up)

kick:
    print("here")
    user.mouse_drag()
    sleep(16ms)
    user.mouse_release()

alt squat:
    key(alt:down)
    sleep(16ms)
    user.mouse_drag()

bench:
    user.mouse_release()
    key(alt:up)

drag right [<user.n20>]:
    user.mouse_drag()
    sleep(50ms)
    user.mouse_move_relative(80*n20, 0)
    sleep(50ms)
    user.mouse_release()

drag left [<user.n20>]:
    user.mouse_drag()
    sleep(50ms)
    user.mouse_move_relative(-80*n20, 0)
    sleep(50ms)
    user.mouse_release()

drag up [<user.n20>]:
    user.mouse_drag()
    sleep(50ms)
    user.mouse_move_relative(0, -80*n20)
    sleep(50ms)
    user.mouse_release()

drag down [<user.n20>]:
    user.mouse_drag()
    sleep(50ms)
    user.mouse_move_relative(0, 80*n20)
    sleep(50ms)
    user.mouse_release()

