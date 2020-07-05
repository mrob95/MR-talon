{alphabet}: insert(alphabet)
big {alphabet}: insert(user.upper(alphabet))
all caps {alphabet}+: insert(user.upper(user.cat(alphabet_list)))

numb <user.digits>: insert(digits)
{punctuation}: key(punctuation)
{punctuation2}: "{punctuation2}"
long {punctuation2}: " {punctuation2} "
{simple_keys} <user.n20>:
    key("{simple_keys}:{n20}")
{simple_keys_norepeat}: key(simple_keys_norepeat)
{direction_modifiers} <user.n20>:
    key("{direction_modifiers}left:{n20}")
[{direction_modifiers}] {directions} <user.n20>:
    direction_modifiers = direction_modifiers or ""
    key("{direction_modifiers}{directions}:{n20}")
[{direction_modifiers}] {directions_extreme} wally:
    direction_modifiers = direction_modifiers or ""
    key("{direction_modifiers}{directions_extreme}")

[and] save$: key(ctrl-s)
^undo <user.n20>$: key("ctrl-z:{n20}")

action(edit.paste): key(ctrl-v)
spark: edit.paste()
action(edit.copy): key(ctrl-c)
stoosh: edit.copy()
action(edit.line_insert_down): key(ctrl-enter)
check <user.n20>:
    edit.line_insert_down()
    repeat(n20 - 1)
action(edit.line_clone):
    key(home shift-end ctrl-c end enter ctrl-v)
    sleep(50ms)
duple <user.n20>:
    edit.line_clone()
    repeat(n20 - 1)

# Text
say <phrase> [over]:
    insert(user.formatted_text(phrase, 0, 0))
({capitalisation} {spacing} | {capitalisation} | {spacing}) bow <phrase>:
    insert(user.formatted_text(phrase, capitalisation or 0, spacing or 0))
({capitalisation} {spacing} | {capitalisation} | {spacing}) bower <phrase>$:
    insert(user.formatted_text(phrase, capitalisation or 0, spacing or 0))

hug prekris: key(()
hug curly: key({)
hug brax: key([)

repeat last <user.n20>:
    core.repeat_phrase(n20)