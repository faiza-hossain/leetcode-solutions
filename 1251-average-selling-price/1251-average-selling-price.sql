# Write your MySQL query statement below
select p.product_id,
round
(COALESCE(sum(price*units)/sum(units),0)
,2) as average_price
from Prices p
LEFT JOIN UnitsSold u on p.product_id=u.product_id 
and u.purchase_date BETWEEN p.start_date and p.end_date
group by p.product_id
