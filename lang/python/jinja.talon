title: /.html/
title: /.xml/
-
gin variable:
    "{{{{  }}}}"
    key(left:3)

gin if:
    "{{% if  %}}"
    key(enter)
    "{{% endif %}}"
    key(up end left:3)
gin else if:
    "{{% elif  %}}"
    key(left:3)
gin else:
    "{{% else %}}"
    key(left:3)

gin for:
    "{{% for  in  %}}"
    key(enter)
    "{{% endfor %}}"
    key(up end left:7)

gin extends:
    '{{% extends "" %}}'
    key(left:4)
gin block:
    "{{% block  %}}"
    key(enter)
    "{{% endblock %}}"
    key(up end left:3)

gin macro:
    "{{% macro  -%}}"
    key(enter)
    "{{%- endmacro %}}"
    key(up end left:3)

lodge and: " and "
lodge as: " as "
lodge else: " else "
lodge if: " if "
lodge in: " in "
lodge is: " is "
lodge is defined: " is defined "
lodge is not: " is not "
lodge not: " not "
lodge not in: " not in "
lodge or: " or "
lodge for: " for "

value true: "true"
value false: "false"
value none: "none"

loop index: "loop.index"
loop index zero: "loop.index0"
loop first: "loop.first"
loop last: "loop.last"
loop length: "loop.length"
loop cycle: "loop.cycle()"
loop depth: "loop.depth"
loop depth zero: "loop.depth0"
loop previous item: "loop.previtem"
loop next item: "loop.nextitem"
