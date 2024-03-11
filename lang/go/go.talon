title: /\.go$/
-
iffae: "if "
if error:
    "if err != nil {}"
    key("left enter")
if error return:
    "if err != nil {}"
    key("left enter")
    "return err"
shell iffae: "else if "
shells: "else "
switcher: "switch "
selector: "select "
case when: "case "
case default: "default:"
while loop:
    "for  {}"
    key("left enter up end left:2")
for loop:
    "for i := 0; i<; i++ {}"
    key("left enter up end left:7")
for each:
    "for  := range  {}"
    key("left enter up end left:12")

assign: " := "
error assign: "err := "

word if: "if "
word else: "else "
word switch: "switch "
word select: "select "
word case: "case "
word default: "default"
word for: "for "
[word] return: "return "
word break: "break"
word continue: "continue"
word defer: "defer "
word go: "go "
word import: "import "
word package: "package "
word type: "type "
word var: "var "
word const: "const "
word struct: "struct "
word interface: "interface "
word (func | func): "func "

(end | finish) timer: "elapsed := time.Since(start)\nfmt.Printf(\"execution took %s\", elapsed)"
(start | begin) timer: "start := time.Now()"

# Functions, methods
create function [<phrase>]$:
    "func {user.camel(phrase or '')}() {{}}"
    key(left enter up end left:3)
create test [<phrase>]$:
    "func Test{user.title(phrase or '')}(t *testing.T) {{}}"
    key(left enter up end left:3)
private {user.file_types} [<phrase>]$:
    "func ({user.first_letter_lowercase(file_types)} *{file_types}) {user.camel(phrase or '')}() {{}}"
    key(left enter up end left:3)
public {user.file_types} [<phrase>]$:
    "func ({user.first_letter_lowercase(file_types)} *{file_types}) {user.title(phrase or '')}() {{}}"
    key(left enter up end left:3)
create structure [<phrase>]$:
    "type {user.title(phrase or '')} struct {{}}"
    key(left enter up end left:9)
create interface [<phrase>]$:
    "interface {user.title(phrase or '')} {{}}"
    key(left enter up end left:9)
variable <phrase>:
    "var {user.camel(phrase or '')} "
camel <phrase>: insert(user.camel(phrase))
tag jason [<phrase>]: "`json:\"{user.snake(phrase or '')}\"`"
produces type <user.go_type>:
    key("end left:2 space ( ) left")
    user.insert_fancy(go_type)
produces type <user.go_type> and error:
    key("end left:2 space ( ) left")
    user.insert_fancy(go_type)
    ", error"
format error <phrase>$: "fmt.Errorf(\"{phrase}\")"
wrap error <phrase>$: "fmt.Errorf(\"{phrase}: %q\", err)"

type <user.go_type>: user.insert_fancy(go_type)
make <user.go_map>: user.insert_fancy("make({go_map})")

document {user.doclinks}: user.browser_open(doclinks)
{user.go_stdlib}: user.insert_function(go_stdlib)
package {user.go_packages}: insert(go_packages)
