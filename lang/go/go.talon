title: /\.go/
-
iffae:
    "if  {}"
    key("left enter up end left:2")
shell iffae:
    "else if  {}"
    key("left enter up end left:2")
shells:
    "else {}"
    key("left enter up end left:2")
switch:
    "switch  {}"
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
    key("left enter up home right:4")

value true: "true"
value false: "false"
value (null|nil): "nil"

import:
    "import ()"
    key("left enter")


function [<phrase>]$:
    "func "
    insert(user.camel(phrase or ""))
    "() {}"
    key(left enter up end left:3)
type struct:
    "type  struct {}"
    key(left enter up home right:5)
return: "return "
type int: "int"
type bool: "bool"
type string: "string"
assign: " := "

document {user.doclinks}: user.browser_open(doclinks)
{user.go_stdlib}: user.insert_function(go_stdlib)
package {user.go_packages}: insert(go_packages)
