title: /\.sql/
-
# Functions
fun average:
    "AVG()"
    key(left)
fun count:
    "COUNT()"
    key(left)
fun length:
    "LENGTH()"
    key(left)
fun max:
    "MAX()"
    key(left)
fun min:
    "MIN()"
    key(left)
fun sum:
    "SUM()"
    key(left)
# Commands
case when:
    "CASE WHEN  END"
    key(left:4)
delete: "DELETE "
distinct: "DISTINCT "
from: "FROM "
for system time: "FOR SYSTEM TIME "
group by: "GROUP BY "
having: "HAVING "
insert into: "INSERT INTO "
is not null: " IS NOT NULL"
is null: " IS NULL"
left join: "LEFT JOIN "
right join: "RIGHT JOIN "
full join: "FULL JOIN "
inner join: "INNER JOIN "
outer join: "OUTER JOIN "
normal join: "JOIN "
limit: "LIMIT "
not equals: " <> "
not like: "NOT LIKE "
on columns: "ON "
order ascending: "ASC "
order by: "ORDER BY "
order descending: "DESC "
select every: "SELECT *"
select: "SELECT "
union: "UNION "
update: "UPDATE"
using: "USING "
value null: "NULL"
where: "WHERE "
with as:
    "WITH  AS ()"
    key(left enter:2 up:2 end left:5)
# Logical
lodge and: " AND "
lodge as: " AS "
lodge between: " BETWEEN "
lodge in: " IN "
lodge is: " IS "
lodge is not: " IS NOT "
lodge like: " LIKE "
lodge or: " OR "
lodge on: " ON "
lodge then: " THEN "
lodge not: " NOT "