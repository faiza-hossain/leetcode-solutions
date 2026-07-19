SELECT p.product_id,
COALESCE(
    (
    select p1.new_price
    from Products as p1
    where p.product_id=p1.product_id
         and p1.change_date<='2019-08-16'
    order by p1.change_date DESC
    limit 1
), 10) as price
From (select distinct product_id
from Products) as p