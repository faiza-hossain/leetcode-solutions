# Write your MySQL query statement below
select distinct(author_id) as id
from(select author_id
from Views
where author_id=viewer_id) as t
order by author_id asc