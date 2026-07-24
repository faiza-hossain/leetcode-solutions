# Write your MySQL query statement below
select visited_on,
(select sum(amount)
from Customer c2
where c2.visited_on between DATE_SUB(c1.visited_on,interval 6 day) and c1.visited_on
) as amount,
(select round(sum(amount)/7,2) 
from Customer c2
where c2.visited_on between DATE_SUB(c1.visited_on,interval 6 day) and c1.visited_on
)as average_amount
from Customer c1
where DATEDIFF(visited_on,(select min(visited_on) from Customer))>=6
group by visited_on
order by visited_on asc