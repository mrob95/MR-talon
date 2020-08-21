title: /\.tex/
-
document class {user.tex_document_classes}:
    insert("\\documentclass{{{tex_document_classes}}}")
use package {user.tex_packages}:
    insert("\\usepackage{{{tex_packages}}}")
use package bib latex:
    insert("\\usepackage[style=authoryear]{{biblatex}}")
begin {user.tex_environments}:
    insert("\\begin{{{tex_environments}}}")
    key(enter:2)
    insert("\\end{{{tex_environments}}}")
    key(up)
insert {user.tex_commands}:
    insert("\\{tex_commands}{{}}")
    key(left)
insert {user.tex_commands_noarg}:
    insert("\\{tex_commands_noarg} ")
greek {user.tex_greek_letters}:
    insert("\\{tex_greek_letters} ")
symbol {user.tex_symbols}:
    insert("\\{tex_symbols} ")


template {user.tex_templates}:
    insert(tex_templates)