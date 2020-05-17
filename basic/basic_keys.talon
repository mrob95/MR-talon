{alphabet}: insert(alphabet)
numb <user.digits>: insert(digits)
{punctuation}: key(punctuation)
long {punctuation2}: " {punctuation2} "
{simple_keys} <user.n20>: key("{simple_keys}:{n20}")
{simple_keys_norepeat}: key(simple_keys_norepeat)
{direction_modifiers} <user.n20>:
    key("{direction_modifiers}-left:{n20}")
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
