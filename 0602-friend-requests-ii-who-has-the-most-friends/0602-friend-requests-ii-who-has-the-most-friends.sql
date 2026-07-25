# Write your MySQL query statement below
select t.id as id,count(id) num
from (select accepter_id id
from RequestAccepted r
UNION ALL
select requester_id id
from RequestAccepted r) as t
group by t.id
order by count(id) desc
limit 1
