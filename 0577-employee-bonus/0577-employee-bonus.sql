# Write your MySQL query statement below
select e.name as name,b.bonus as bonus
from Employee as e
LEFT JOIN Bonus as b on e.empId=b.empId
where b.bonus<1000 or b.bonus IS NULL
order by e.empId