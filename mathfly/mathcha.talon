title: /mathcha.io/
-
settings():
    key_wait = 15.0

{user.tex_symbols}:
    key(\)
    insert(tex_symbols)
    key(enter)
    sleep(100ms)
greek {user.greek_letters}:
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
math mode:
    key(\)
    "math-container"
    key(enter)
{user.mathfly_fractions}:
    key(shift-left \)
    "frac"
    key(enter down)
    insert(mathfly_fractions)
    key(right)
    sleep(100ms)