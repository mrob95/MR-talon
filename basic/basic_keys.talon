{user.alphabet}: insert(alphabet)
big {user.alphabet}: insert(user.upper(alphabet))
all caps {user.alphabet}+: insert(user.upper(user.cat(alphabet_list)))

numb <user.digits>: insert(digits)
{user.punctuation}: key(punctuation)
{user.punctuation2}: "{punctuation2}"
long {user.punctuation2}: " {punctuation2} "
{user.simple_keys} [<user.n20>]: key("{simple_keys}:{n20 or 1}")
{user.simple_keys_norepeat}: key(simple_keys_norepeat)


{user.direction_modifiers} [<user.n20>]: key("{direction_modifiers}left:{n20 or 1}")
[{user.direction_modifiers}] {user.directions} [<user.n20>]:
    key("{direction_modifiers or ''}{directions}:{n20 or 1}")
[{user.direction_modifiers}] {user.directions_extreme} wally:
    key("{direction_modifiers or ''}{directions_extreme}")
{user.personal}: insert(personal)

[and] save$: key(ctrl-s)

action(edit.undo): key(ctrl-z)
^undo [<user.r20>]$:
    edit.undo()
    repeat(r20 or 0)

action(edit.paste): key(ctrl-v)
spark: edit.paste()
action(edit.copy): key(ctrl-c)
stoosh: edit.copy()
action(edit.line_insert_down): key(ctrl-enter)
check [<user.r20>]:
    edit.line_insert_down()
    repeat(r20 or 0)
action(edit.line_clone):
    key(home shift-end ctrl-c end enter ctrl-v)
    sleep(50ms)
duple [<user.r20>]:
    edit.line_clone()
    repeat(r20 or 0)

# Text
say <phrase> [over]:
    insert(user.formatted_text(phrase, 0, 0))
({user.capitalisation} {user.spacing} | {user.capitalisation} | {user.spacing}) bow <phrase>:
    insert(user.formatted_text(phrase, capitalisation or 0, spacing or 0))
({user.capitalisation} {user.spacing} | {user.capitalisation} | {user.spacing}) stern <phrase>$:
    insert(user.formatted_text(phrase, capitalisation or 0, spacing or 0))

hug prekris: key(()
hug curly: key({)
hug brax: key([)

repeat last [<user.n20>]:
    core.repeat_phrase(n20)