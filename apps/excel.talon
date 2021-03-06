app: Excel
-
settings():
    key_wait = 10

zoom in <user.n20>: key("ctrl-alt-+:{n20}")
zoom out <user.n20>: key("ctrl-alt-+:{n20}")

new tab: key(shift-f11)
previous tab <user.n20>: key("ctrl-pgup:{n20}")
next tab <user.n20>: key("ctrl-pgdown:{n20}")

close window: key(ctrl-w)
new file: key(ctrl-n)
open file: key(ctrl-o)
save as: key(f12)

rename tab:
    key(alt-h)
    sleep(200ms)
    key(o r)

duplicate tab:
    key(alt-h)
    sleep(200ms)
    key(o m)
    sleep(200ms)
    key(end tab space enter)

paste special: key(ctrl-alt-v)
paste values:
    key(alt-h)
    sleep(200ms)
    key(v e)

insert cells:
    key(ctrl-shift-+)
insert row:
    key(ctrl-shift-+)
    sleep(200ms)
    key(down enter)
insert column:
    key(ctrl-shift-+)
    sleep(200ms)
    key(down:2 enter)
destroy row:
    key(ctrl--)
    sleep(200ms)
    key(down:2 enter)
destroy column:
    key(ctrl--)
    sleep(200ms)
    key(down:3 enter)

select row: key(shift-space)
select column: key(ctrl-space)

go to file: key(alt-f)
go to home: key(alt-h)
go to page layout: key(alt-p)
go to insert: key(alt-n)
go to data: key(alt-a)
go to view: key(alt-w)
go to formula: key(alt-m)

fill down <user.n20>: key("ctrl-d:{n20}")
absolute reference <user.n20>: key("f4:{n20}")


edit cell: key(f2)
cell fill: key(alt-h h)
cell bold: key(ctrl-b)
cell border: key(alt-h b)
cell align left: key(alt-h a l)
cell align centre: key(alt-h a c)
cell align right: key(alt-h a r)

cell format general: key(ctrl-shift-~)
cell format currency: key(ctrl-shift-$)
cell format (percentage|percent): key(ctrl-shift-%)
cell format scientific: key(ctrl-shift-^)
cell format date: key(ctrl-shift-#)
cell format time: key(ctrl-shift-@)
cell format number: key(ctrl-shift-!)

cell border right: key(alt-r)
cell border left: key(alt-l)
cell border top: key(alt-t)
cell border bottom: key(alt-b)
cell border upward diagonal: key(alt-d)
cell border horizontal interior: key(alt-h)
cell border vertical interior: key(alt-v)
cell border remove: key(ctrl-shift-_)
cell border outline: key(ctrl-shift-&)

disable dragon add-in:
    key(alt-f t)
    sleep(200ms)
    key(down:10)
    sleep(200ms)
    key(tab:3 down:2 tab space)
    sleep(200ms)
    key(space enter)
    sleep(200ms)
    key(enter)

replace: key(ctrl-h)

select <user.xl_cell>: user.xl_select_cells(xl_cell)
select <user.xl_cell> by <user.xl_cell>: user.xl_select_cells(xl_cell_1, xl_cell_2)