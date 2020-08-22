app: scinoteb.exe
-
{user.tex_symbols}:
    key(ctrl:down)
    insert(tex_symbols)
    key(ctrl:up)

matrix {user.digits10} by {user.digits10}:
    key(f10)
    sleep(50ms)
    key(i down:8 enter)
    insert(digits10_1)
    key(tab)
    insert(digits10_2)
    key(enter)

greek {user.sn55_greek_letters}:
    key("ctrl-g {sn55_greek_letters}")

fraction: key(ctrl-f)
over: key(ctrl-shift-left ctrl-f)
(super script | to the power): key(ctrl-h)
sub script: key(ctrl-l)
squared: key(ctrl-h 2 right)
cubed: key(ctrl-h 3 right)
inverse: key(ctrl-h - 1 right)
inverse half: key(ctrl-h - ctrl-f 1 down 2) right right)
(parens | parentheses | prens): key(ctrl-0)
(squares | square brackets): key(ctrl-6)
absolute: key(ctrl-\\)
norma: key(ctrl-shift-\\)
chi squared: key(ctrl-g q ctrl-h 2 right)
(radical | square root): key(ctrl-r)
summation: key(ctrl-7)
accent hat: key(ctrl-^)
accent tilde: key(ctrl-~)
accent dot: key(ctrl-.)
accent double dot: key(ctrl-\")
accent bar: key(ctrl-_)
accent arrow: key(ctrl--)
#
# Program control
#
new file: key(f10 f enter)
open file: key(ctrl-o)
save file: key(f10 f s)
save as: key(f10 f down:5 enter)
print file: key(ctrl-p)
export document: key(f10 f down:7 enter)
page preview: key(f10 f down:17 enter)
body math: key(alt-2 down enter)
body text: key(alt-2 down:2 enter)
(begin | insert) [bulleted] list: key(alt-1 down:2 enter)
(begin | insert) numbered list: key(alt-1 down:4 enter)
end [(bulleted | numbered)] list: key(alt-1 up enter)
insert normal text: key(alt-3 down enter)
insert big text: key(alt-3 down:2 enter)
insert small text: key(alt-3 down:9 enter)
insert bold text: key(alt-3 down:3 enter)
insert italic text: key(alt-3 down:6 enter)
insert bold symbols: key(alt-3 down:4 enter)
insert centred text: key(alt-2 down:3 enter)
insert left text: key(alt-2 down:4 enter)
insert right text: key(alt-2 down:5 enter)
insert quotation: key(alt-2 down:11 enter)
insert (heading | title) [one]: key(alt-2 down:6 enter)
insert (heading | title) two: key(alt-2 down:7 enter)
insert (heading | title) three: key(alt-2 down:8 enter)
insert (heading | title) four: key(alt-2 down:9 enter)
insert (heading | title) five: key(alt-2 down:10 enter)
evaluate: key(ctrl-e)
evaluate numerically: key(f10 c down enter)
toggle math: key(ctrl-m)
toggle text: key(ctrl-t)
label above: key(f10 i down:11 enter a enter)
label below: key(f10 i down:11 enter b enter)
add matrix row: key(f10 e up up enter enter)
add matrix column: key(f10 e up enter enter)