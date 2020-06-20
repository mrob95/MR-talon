title: /.*\.c/
title: /.*\.h/
-
type {c_types}: insert(c_types)
integer main:
	"int main(int argc, char **argv) {}"
	key(left enter)
assign: " = "
arrow: "->"
file size:
	"""fseek(fp, 0, SEEK_END);
    int sz = ftell(fp);
    rewind(fp);
	"""
for loop:
	"for (int i=0; i<; i++) {}"
	key(left enter)
for each token:
	'for (char *tok=strtok(, ""); tok!=NULL; tok=strtok(NULL, "")) {}'
	key(left enter up home right:22)
iffae:
	"if () {}"
	key(left enter up home right:4)
shells:
	"else {}"
	key(left)
shell iffae:
	"else if () {}"
	key(left enter up end left:3)
hash include:
	"#include <>"
	key(left)
hash define: "#define "
structure:
	"struct  {};"
	key(left:2 enter up end left:2)
semi: key(end end ;)
type def struct:
	"typedef struct {} ;"
	key(left:3 enter down end left)
type def enum:
	"typedef enum {} ;"
	key(left:3 enter down end left)
return:
	"return ;"
	key(left)
value false: "false"
value true: "true"
value null: "NULL"
while loop:
	"while () {}"
    key(left enter up home right:7)
