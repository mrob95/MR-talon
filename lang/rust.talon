title: /.*\.rs$/
-
type <user.rust_type>: insert(rust_type)
is type <user.rust_type>: insert(": {rust_type}")
turbo fish <user.rust_type>: insert("::<{rust_type}>")
function main:
	"fn main() {}"
	key(left enter)
create function [<phrase>]$:
    "fn {user.snake(phrase or '')}() -> "
    key(left:5)
semi: key(end:2 ;)
iffae: "if "
shells:
	"else {}"
	key(left enter)
shell iffae:
	"else if "
	key(left enter)
use standard:
	"use std::;"
	key(left)
for (loop | each):
	"for  in  {}"
	key(left enter up end left:6)
while loop:
	"while  {}"
	key(left enter up end left:2)
letter: "let "
letter mute: "let mut "

right arrow: " => "
produces: " -> "
implement [{user.file_variables}]:
	"impl {file_variables or ''} {{}}"
	key(left enter up home right:6)
matcher [{user.file_variables}]:
	"match {file_variables or ''} {{}}"
	key(left enter up home right:6)
create structure [<phrase>]$:
	"struct {user.formatted_text(phrase or '', 2, 1)} {{}}"
	key(left)
create enum [<phrase>]$:
	"enum {user.formatted_text(phrase or '', 2, 1)} {{}}"
	key(left)
return: "return "

derive {user.rust_derives}+:
	items = user.cat(rust_derives_list, ", ")
	"#[derive({items})]"
