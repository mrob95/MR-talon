title: /.*\.rs$/
-
type {user.rust_types}: insert(rust_types)
is type {user.rust_types}: insert(": {rust_types}")
function main:
	"fn main() {}"
	key(left enter)
semi: key(end:2 ;)
iffae:
	"if  {}"
	key(left enter up home right:3)
shells:
	"else {}"
	key(left enter)
use standard:
	"use std::;"
	key(left)
for loop:
	"for  in  {}"
	key(left enter up home right:4)
while loop:
	"while  {}"
	key(left enter up home right:6)
letter: "let "
letter mute: "let mut "
value true: "true"
value false: "false"
right arrow: " => "
produces: " -> "
pattern match:
	"match  {}"
	key(left enter up home right:6)
structure:
	"struct  {}"
	key(left enter up home right:7)
enumerate:
	"enum  {}"
	key(left enter up home right:5)
return: "return "
