title: /.*\.py/
title: /JupyterLab/
title: /IPython:/
title: /PDB:/
-
args and kwargs: "*args, **kwargs"
assign: " = "
assert: "assert "
breaker: "break"
double under:
	"____"
	key(left:2)
for each:
	"for  in :"
	key(left:5)
for loop:
	"for i in range():"
	key(left:2)
if name is main:
    "if __name__ == '__main__':"
    key(enter)
(iffae | iffy):
	"if :"
	key(left)
iffae not:
	"if not :"
	key(left)
insert long comment:
	"''''''"
	key(left:3, enter:2, up)
insert doc string:
    '""""""'
    key(left:3, enter:2, up)
lambda:
	"lambda :"
	key(left)
return: "return "
shell iffae:
	"elif :"
	key(left)
shells: "else:"
set trace: "import pdb; pdb.set_trace()"
value false: "False"
value none: "None"
value true: "True"
while loop:
	"while :"
	key(left)
with open:
    "with open() as f:"
    key(left:8)
with as:
    "with  as :"
    key(left:5)
    # Dictation
function [<phrase>]$:
    "def "
    insert(user.snake(phrase or ""))
    "():"
    key(left left)
method [<phrase>]$:
    "def "
    insert(user.snake(phrase or ""))
    "(self):"
    key(left left)
selfie [<phrase>]:
    "self."
    insert(user.snake(phrase or ""))
classy [<phrase>]$:
    "class "
    insert(user.title(phrase or ""))
    "():"
    key(left left)
commenter <phrase>$:
    "# "
    insert(user.formatted_text(phrase or "", 4, 0))
printer <phrase>$:
    'print("")'
    key(left:2)
    insert(user.formatted_text(phrase or "", 4, 0))
# Types
from typing import {py_types}: "from typing import {py_types}"
type {py_types}: insert(py_types)
is type {py_types}: ": {py_types}"
produces: key(end left space - > space)
# Imports
import: "import "
from import:
    "from  import "
    key(home right:5)
import {py_modules}:
    "import {py_modules}"
import {py_imports}:
    insert(py_imports)
# Dunders
magic init:
    "def __init__(self):"
    key(left left)
magic {py_umeths}: "def __{py_umeths}__(self):"
magic {py_bmeths}: "def __{py_bmeths}__(self, other):"
magic {py_mmeths}: insert(py_mmeths)
# Exceptions
try except:
    "try:"
    key(enter enter)
    "except:"
    key(shift-tab)
try except {py_exceptions} [error]:
    "try:"
    key(enter enter)
    "except {py_exceptions}:"
    key(shift-tab)
try except {py_exceptions} [error] as:
    "try:"
    key(enter enter)
    "except {py_exceptions} as e:"
    key(shift-tab)
# misc
insert line break:
    "# ------------------------------------------------"