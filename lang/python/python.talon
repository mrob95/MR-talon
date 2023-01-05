title: /.*\.py/
title: /JupyterLab/
title: /IPython:/
title: /PDB:/
title: /.* - python\s*$/
title: /.* - pytest\s*$/
-
tag(): user.python
args and kwargs: "*args, **kwargs"
assign: " = "
assert: "assert "
breaker: "break"
double under: user.insert_fancy("__[|]__")
for each: user.insert_fancy("for [|] in :")
for loop: user.insert_fancy("for i in range([|]):")
if name (is | equals) main: "if __name__ == '__main__':\n"
(iffae | iffy): user.insert_fancy("if [|]:")
iffae not: user.insert_fancy("if not [|]:")
shell iffae: user.insert_fancy("elif [|]:")
shells: "else:"
insert (doc | long) string:
    '""""""'
    key(left:3 enter:2 up)
lambda: user.insert_fancy("lambda [|]:")
return: "return "
while loop: user.insert_fancy("while [|]:")
with open: user.insert_fancy("with open([|]) as f:")
with open {user.py_fopen_modes}+:
    modes = user.cat(py_fopen_modes_list)
    'with open(, "{modes}") as f:'
    key(home right:10)
with as: user.insert_fancy("with [|] as :")
# Dictation
create function [<phrase>]$:
    "def {user.snake(phrase or '')}():"
    key(left:2)
create method [<phrase>]$:
    "def {user.snake(phrase or '')}(self):"
    key(left:2)
selfie [<phrase>]: "self.{user.snake(phrase or '')}"
classy [<phrase>]$:
    "class {user.formatted_text(phrase or '', 2, 1)}:"
    key(left)
data classy [<phrase>]$:
    "@dataclass\nclass {user.formatted_text(phrase or '', 2, 1)}:"
    key(left)
commenter <phrase>$:
    "# "
    insert(user.formatted_text(phrase or "", 4, 0))
printer <phrase>$:
    'print("{user.formatted_text(phrase or \'\', 4, 0)}")'
atty {user.py_decorators}: "@{py_decorators}"
print [all] assignments: user.print_all_assignments()
print arguments: user.print_arguments()
refactor assignment: user.refactor_assignment()
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
from import: user.insert_fancy("from [|] import ")
import {user.py_modules}: "import {py_modules}"
import {user.py_imports}: insert(py_imports)
# Dunders
magic init: user.insert_fancy("def __init__(self[|]):")
magic {user.py_umeths}: "def __{py_umeths}__(self):"
magic {user.py_bmeths}: "def __{py_bmeths}__(self, other):"
magic {user.py_mmeths}: insert(py_mmeths)
# Exceptions
raise {user.py_exceptions} [error]:
    "raise {py_exceptions}()"
    key(left)
try except:
    "try:"
    key(enter:2)
    "except:"
    key(shift-tab)
try except {user.py_exceptions} [error]:
    "try:"
    key(enter:2)
    "except {py_exceptions}:"
    key(shift-tab)
try except {user.py_exceptions} [error] as:
    "try:"
    key(enter:2)
    "except {py_exceptions} as e:"
    key(shift-tab)
# Libraries
pandas {user.py_lib_pandas}: user.insert_function(py_lib_pandas)
document pandas {user.py_lib_pandas}:
    clean = user.replace("pd.", "", py_lib_pandas)
    user.browser_open("https://pandas.pydata.org/pandas-docs/stable/search.html?q={clean}")
numb pie {user.py_lib_numpy}: user.insert_function(py_lib_numpy)
regex {user.py_lib_re}: user.insert_function(py_lib_re)
system {user.py_lib_sys}: user.insert_function(py_lib_sys)
OS {user.py_lib_os}: user.insert_function(py_lib_os)
sunny {user.py_lib_spark}: user.insert_function(py_lib_spark)
date time {user.py_lib_datetime}: user.insert_function(py_lib_datetime)
jason {user.py_lib_json}: user.insert_function(py_lib_json)
subprocess {user.py_lib_subprocess}: user.insert_function(py_lib_subprocess)
pie test {user.py_lib_pytest}: user.insert_function(py_lib_pytest)

logging get logger: "logger = logging.getLogger(__name__)"
logging basic config:
    """logging.basicConfig(
        level=logging.INFO,
        file=None,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M","""
