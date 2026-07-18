# Write your MySQL query statement below
select
   distinct(num) as ConsecutiveNums 
from (
    select num,
    lag(num,1) over(order by id asc) as prev1,
    lag(num,2) over(order by id asc) as prev2
    from logs
) as temp
where num=prev1
    and num=prev2