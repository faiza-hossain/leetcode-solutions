# Write your MySQL query statement below
select sell_date,count(DISTINCT product) as num_sold ,
GROUP_CONCAT(distinct product order by product asc separator ',') as products
FROM Activities 
GROUP BY sell_date 
order by sell_date asc;
