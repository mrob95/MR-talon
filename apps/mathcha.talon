title: /.*Mathcha.*/
-
settings():
    key_wait = 15.0

{tex_symbols}:
    key(\)
    insert(tex_symbols)
    key(enter)
    sleep(100ms)
greek {greek_letters}:
    key(\)
    insert(greek_letters)
    key(enter)
<user.digits>:
    insert(digits)
(super script | to the power): key(^)
sub script: key(_)
squared: key(^ 2)
cubed: key(^ 3)
inverse: key(^ - 1)
{fractions}:
    key(shift-left)
    key(\)
    "frac"
    key(enter down)
    insert(fractions)
    key(right)
    sleep(100ms)