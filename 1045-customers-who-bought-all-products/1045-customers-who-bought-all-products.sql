# Write your MySQL query statement below
select customer_id
from Customer c
JOIN Product p on p.product_key =c.product_key 
group by customer_id
having count(distinct p.product_key)=(select count(*) from Product)
