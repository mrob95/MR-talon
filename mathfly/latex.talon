title: /\.tex/
-
document class {tex_document_classes}:
    insert("\\documentclass{{{tex_document_classes}}}")
use package {tex_packages}:
    insert("\\usepackage{{{tex_packages}}}")
use package bib latex:
    insert("\\usepackage[style=authoryear]{{biblatex}}")
begin {tex_environments}:
    insert("\\begin{{{tex_environments}}}")
    key(enter:2)
    insert("\\end{{{tex_environments}}}")
    key(up)
insert {tex_commands}:
    insert("\\{tex_commands}{{}}")
    key(left)
insert {tex_commands_noarg}:
    insert("\\{tex_commands_noarg} ")
greek {tex_greek_letters}:
    insert("\\{tex_greek_letters} ")
symbol {tex_symbols}:
    insert("\\{tex_symbols} ")


template {tex_templates}:
    insert(tex_templates)