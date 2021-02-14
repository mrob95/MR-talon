# Macro must be at the start of a phrase, as the entire
# phrase containing "macro start" will be included in the macro
^macro (start | record): user.macro_start()
macro stop: user.macro_stop()
macro play [<user.r20>]:
    user.macro_play()
    repeat(r20 or 0)
macro play slower: user.macro_play_slower()