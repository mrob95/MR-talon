title: /.*\.rs$/
-
type <user.rust_type>: insert(rust_type)
is type <user.rust_type>: insert(": {rust_type}")
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
	key(left enter up home right:4)
while loop:
	"while  {}"
	key(left enter up home right:6)
letter: "let "
letter mute: "let mut "

right arrow: " => "
produces: " -> "
pattern match:
	"match  {}"
	key(left enter up home right:6)
create structure [<phrase>]$:
	"struct {user.formatted_text(phrase or '', 2, 1)} {}"
	key(left:5)
create enum [<phrase>]$:
	"enum {user.formatted_text(phrase or '', 2, 1)} {}"
	key(left:5)
return: "return "

derive debug: "#[derive(Debug)]"
