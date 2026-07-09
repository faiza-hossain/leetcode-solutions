# Write your MySQL query statement below
select contest_id,ROUND(
    COUNT(u.user_id) * 100 /
    (SELECT COUNT(*) FROM Users),
    2
) as percentage 
from Users u
JOIN Register r on r.user_id =u.user_id 
GROUP BY contest_id
ORDER BY percentage desc,contest_id asc
