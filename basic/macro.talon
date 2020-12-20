macro (start | record):
    user.macro_start()
macro stop:
    user.macro_stop()
macro play [<user.r20>]:
    user.macro_play()
    repeat(r20 or 0)
