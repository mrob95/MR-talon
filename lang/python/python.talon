title: /.*\.py/
title: /JupyterLab/
title: /IPython:/
title: /PDB:/
-
tag(): user.python
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
    key(left:7)
with open {user.py_fopen_modes}+:
    modes = user.cat(py_fopen_modes_list)
    'with open(, "{modes}") as f:'
    key(home right:10)
with as:
    "with  as :"
    key(left:5)
# Dictation
function [<phrase>]$:
    "def "
    insert(user.snake(phrase or ""))
    "():"
    key(left:2)
method [<phrase>]$:
    "def "
    insert(user.snake(phrase or ""))
    "(self):"
    key(left:2)
selfie [<phrase>]:
    "self."
    insert(user.snake(phrase or ""))
classy [<phrase>]$:
    "class "
    insert(user.title(phrase or ""))
    "():"
    key(left:2)
data classy [<phrase>]$:
    "@dataclass\nclass "
    insert(user.title(phrase or ""))
    "():"
    key(left:2)
commenter <phrase>$:
    "# "
    insert(user.formatted_text(phrase or "", 4, 0))
printer <phrase>$:
    'print("")'
    key(left:2)
    insert(user.formatted_text(phrase or "", 4, 0))
# Types
from typing import {user.py_typing_types}: "from typing import {py_typing_types}"
type {user.py_types}: insert(py_types)
is type {user.py_types}: ": {py_types}"
type {user.py_types}+:
    type_args = user.cat(user.slice(py_types_list, 1), ", ")
    "{py_types_1}[{type_args}]"
produces: key(end left space - > space)
# Imports
import: "import "
from import:
    "from  import "
    key(end left:8)
import {user.py_modules}:
    "import {py_modules}"
import {user.py_imports}:
    insert(py_imports)
# Dunders
magic init:
    "def __init__(self):"
    key(left:2)
magic {user.py_umeths}: "def __{py_umeths}__(self):"
magic {user.py_bmeths}: "def __{py_bmeths}__(self, other):"
magic {user.py_mmeths}: insert(py_mmeths)
# Exceptions
try except:
    "try:"
    key(enter enter)
    "except:"
    key(shift-tab)
try except {user.py_exceptions} [error]:
    "try:"
    key(enter enter)
    "except {py_exceptions}:"
    key(shift-tab)
try except {user.py_exceptions} [error] as:
    "try:"
    key(enter enter)
    "except {py_exceptions} as e:"
    key(shift-tab)
# misc
insert todo: "# TODO: "
insert line break:
    "# ------------------------------------------------"
# Libraries
pandas {user.py_lib_pandas}: user.insert_function(py_lib_pandas)
numb pie {user.py_lib_numpy}: user.insert_function(py_lib_numpy)
regex {user.py_lib_re}: user.insert_function(py_lib_re)
system {user.py_lib_sys}: user.insert_function(py_lib_sys)
OS {user.py_lib_os}: user.insert_function(py_lib_os)
date time now format: user.insert_function('datetime.now().strftime("%Y-%m-%d %H:%M[|]")')
logging get logger: "logger = logging.getLogger(__name__)"
logging basic config:
    """logging.basicConfig(
        level=logging.INFO,
        file=None,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M","""