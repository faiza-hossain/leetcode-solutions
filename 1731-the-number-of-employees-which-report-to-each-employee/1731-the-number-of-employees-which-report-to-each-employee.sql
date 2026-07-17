# Write your MySQL query statement below
select e.employee_id,e.name,count(e1.reports_to) reports_count,ceiling(round(avg(e1.age)))average_age
from Employees e
JOIN Employees e1 on e.employee_id=e1.reports_to
group by e.employee_id
order by employee_id asc