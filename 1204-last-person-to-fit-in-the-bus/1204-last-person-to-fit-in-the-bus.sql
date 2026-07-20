# Write your MySQL query statement below
select person_name
from(select turn,person_id,person_name,
sum(weight) over(order by turn) as total_weight 
from Queue) t
where total_weight<=1000
order by turn desc
limit 1
