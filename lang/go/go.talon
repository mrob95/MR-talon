title: /\.go/
-
iffae:
    "if  {}"
    key("left enter up end left:2")
if error:
    "if err != nil {}"
    key("left enter")
if error return:
    "if err != nil {}"
    key("left enter")
    "return err"
if error equals:
    "if err := ; err != nil {}"
    key("left enter up end left:14")
shell iffae:
    "else if  {}"
    key("left enter up end left:2")
shells:
    "else {}"
    key("left enter up end left:2")
switcher:
    "switch  {}"
    key("left enter up end left:2")
selector:
    "select  {}"
    key("left enter up end left:2")
case when:
    "case :"
    key("left")
case default:
    "default:"
    key("enter")
while loop:
    "for  {}"
    key("left enter up end left:2")
for loop:
    "for i := 0; i<; i++ {}"
    key("left enter up end left:7")
for each:
    "for  := range  {}"
    key("left enter up end left:12")

(end | finish) timer: "elapsed := time.Since(start)\nfmt.Printf(\"execution took %s\", elapsed)"
(start | begin) timer: "start := time.Now()"

import:
    "import ()"
    key("left enter")

# Functions, methods
create function [<phrase>]$:
    "func "
    insert(user.camel(phrase or ""))
    "() {}"
    key(left enter up end left:3)
private {user.file_types} [<phrase>]$:
    "func ({user.first_letter_lowercase(file_types)} *{file_types}) {user.camel(phrase or '')}() {{}}"
    key(left enter up end left:3)
public {user.file_types} [<phrase>]$:
    "func ({user.first_letter_lowercase(file_types)} *{file_types}) {user.title(phrase or '')}() {{}}"
    key(left enter up end left:3)
type struct [<phrase>]$:
    "type {user.title(phrase or '')} struct {{}}"
    key(left enter up home right:5)
variable <phrase>:
    "var {user.camel(phrase or '')} "
camel <phrase>: insert(user.camel(phrase))

type <user.go_type>: user.insert_fancy(go_type)
make <user.go_map>: user.insert_fancy("make({go_map})")

document {user.doclinks}: user.browser_open(doclinks)
{user.go_stdlib}: user.insert_function(go_stdlib)
package {user.go_packages}: insert(go_packages)

deferral: "defer "
continual: "continue"
breaker: "break"
return: "return "
constant: "const "
assign: " := "
error assign: "err := "
