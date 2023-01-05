title: /.*\.rs$/
-
type <user.rust_type>: insert(rust_type)
is type <user.rust_type>: insert(": {rust_type}")
turbo <user.rust_type>: insert("::<{rust_type}>")
function main:
	"fn main() {}"
	key(left enter)
create function [<phrase>]$:
    "fn {user.snake(phrase or '')}() -> "
    key(left:5)
create method [<phrase>]$:
    "fn {user.snake(phrase or '')}(self: &Self) -> "
    key(left:5)
create mute method [<phrase>]$:
    "fn {user.snake(phrase or '')}(self: &mut Self) -> "
    key(left:5)
selfie [<phrase>]: "self.{user.snake(phrase or '')}"
semi: key(end:2 ;)
iffae:
	"if  {}"
	key(left enter up end left:2)
shells:
	"else {}"
	key(left enter)
shell iffae:
	"else if  {}"
	key(left enter up end left:2)
use standard:
	"use std::;"
	key(left)
for (loop | each):
	"for  in  {}"
	key(left enter up end left:6)
while loop:
	"while  {}"
	key(left enter up end left:2)
infinite loop:
	"loop {}"
	key(left enter)
letter: "let "
letter mut: "let mut "

produces: " => "
implement [{user.file_variables}]:
	"impl {file_variables or ''} {{}}"
	key(left enter up end left)
matcher [{user.file_variables}]:
	"match {file_variables or ''} {{}}"
	key(left enter up end left)
create structure [<phrase>]$:
	"struct {user.formatted_text(phrase or '', 2, 1)} {{}}"
	key(left)
create enum [<phrase>]$:
	"enum {user.formatted_text(phrase or '', 2, 1)} {{}}"
	key(left)
return: "return "
breaker: "break;"
continuer: "continue;"

derive {user.rust_derives}+:
	items = user.cat(rust_derives_list, ", ")
	"#[derive({items})]"

document {user.functions}: user.browser_open("https://doc.rust-lang.org/std/index.html?search={functions}")
