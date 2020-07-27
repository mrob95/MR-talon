title: /\.sql/
-
# Commands
case when:
    "CASE WHEN  END"
    key(left:4)
create table: "CREATE TABLE "
delete: "DELETE "
distinct: "DISTINCT "
from: "FROM "
for system time: "FOR SYSTEM TIME "
group by: "GROUP BY "
having: "HAVING "
insert into:
    "INSERT INTO "
    key(enter:2)
    "VALUES "
    key(up:2 end)
is not null: " IS NOT NULL"
is null: " IS NULL"
#
left join: "LEFT JOIN "
right join: "RIGHT JOIN "
full join: "FULL JOIN "
inner join: "INNER JOIN "
outer join: "OUTER JOIN "
normal join: "JOIN "
#
limit: "LIMIT "
not equals: " <> "
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
semi: key(end ;)