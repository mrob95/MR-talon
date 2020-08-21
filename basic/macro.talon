macro (start | record):
    user.macro_start()
macro stop:
    user.macro_stop()
macro play <user.n20>:
    user.macro_play()
    repeat(n20 - 1)
