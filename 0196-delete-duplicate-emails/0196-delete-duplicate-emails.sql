# Write your MySQL query statement below
DELETE p
from Person p
JOIN Person p1 on p.email=p1.email
and p.id>p1.id