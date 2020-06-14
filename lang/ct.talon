title: /.*\.c/
title: /.*\.h/
-
type {c_types}: insert(c_types)
assign: " = "
file size:
	"""fseek(fp, 0, SEEK_END);
    int sz = ftell(fp);
    rewind(fp);
	"""
for loop:
	"for (i=0; i<; i++) {}"
	key(left enter)
iffae:
	"if () {}"
	key(left enter up home right:4)
hash include:
	"#include <>"
	key(left)
hash define: "#define "
shells:
	"else {}"
	key(left enter)
structure:
	"struct  {};"
	key(left:2 enter up end left:2)
semi: key(end end ;)
type def struct:
	"typedef struct {} ;"
	key(left:3 enter down end left:2)
return:
	"return ;"
	key(left)
value false: "false"
value true: "true"
value null: "NULL"
while loop:
	"while () {}"
    key(left enter up home right:7)
