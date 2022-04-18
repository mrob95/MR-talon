{user.alphabet}: insert(alphabet)
big {user.alphabet}: insert(user.upper(alphabet))
all caps {user.alphabet}+: insert(user.upper(user.cat(alphabet_list)))

(numb | number) <user.digits>: insert(digits)
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

[and] save$: edit.save()
^undo [<user.r20>]$:
    edit.undo()
    repeat(r20 or 0)

spark: edit.paste()
stoosh: edit.copy()
check [<user.r20>]:
    edit.line_insert_down()
    repeat(r20 or 0)
duple [<user.r20>]:
    edit.line_clone()
    repeat(r20 or 0)

splat [<user.r20>]:
    edit.delete_word()
    repeat(r20 or 0)
splat ross [<user.r20>]:
    user.delete_word_right()
    repeat(r20 or 0)


# Text
say <phrase> [over]:
    insert(user.formatted_text(phrase, 0, 0))
({user.capitalisation} {user.spacing} | {user.capitalisation} | {user.spacing}) bow <phrase>:
    insert(user.formatted_text(phrase, capitalisation or 0, spacing or 0))
({user.capitalisation} {user.spacing} | {user.capitalisation} | {user.spacing}) burner <phrase>$:
    insert(user.formatted_text(phrase, capitalisation or 0, spacing or 0))

hug prekris: key(()
hug curly: key({)
hug brax: key([)
repeat last [<user.n20>]:
    core.repeat_phrase(n20)
