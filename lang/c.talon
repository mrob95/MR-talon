title: /.*\.c/
title: /.*\.cpp/
title: /.*\.h/
-
# type {user.c_types}: insert(c_types)
type <user.c_type>: insert(c_type)
variable <user.c_type> <phrase>:
	insert(c_type)
	insert(user.snake(phrase))
standard {user.cpp_std}: "std::{cpp_std}"
integer main:
	"int main(int argc, char **argv) {}"
	key(left enter)
assign: " = "
arrow: "->"
left shift: " << "
right shift: " >> "
file size:
	"""fseek(fp, 0, SEEK_END);
    int sz = ftell(fp);
    rewind(fp);
	"""
for loop:
	"for (int i=0; i<; i++) {}"
	key(left enter up end left:8)
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
hash include: "#include "
hash define: "#define "
hash undefine: "#undef "
hash if: "#if "
hash if (def|defined): "#ifdef "
hash if not (def|defined): "#ifndef "
hash endif: "#endif "
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
template header file:
	"#ifndef \n#define \n\n#endif"
	key(ctrl-home end ctrl-down _ h left:2)