title: /.*\.r$/
title: /.*\.R$/
app: RStudio
-
graph {r_graph}:
    user.insert_function(r_graph)
graph {r_graph_misc}:
    insert(r_graph_misc)
library {r_libraries}:
    insert("library({r_libraries})")
# ------------------------------------------------
assign: " <- "
add comment: "# "
pipe: " %>% "
data pipe: " %$% "
chain:
    key(end)
    " %>%"
    key(enter)
data chain:
    key(end)
    " %$%"
    key(enter)
tell add:
	key(end space + enter)
iffae:
	"if ()"
	key(left)
shells: "else "
breaker: "break"
for each:
	"for ( in )"
	key(left:6)
for loop:
	"for (i in 1:)"
	key(left)
while loop:
	"while ()"
	key(left)
lodge and: " & "
lodge in: " %in% "
lodge or: " | "
function:
	"function()"
	key(left)
value null: "NULL"
value NA: "NA"
value true: "TRUE"
value false: "FALSE"