# Write your MySQL query statement below
select d.name as Department,
e.name as Employee,e.salary as Salary
from Employee e
JOIN Department d on e.departmentId=d.id
where (
    select count(distinct e1.salary)
    from Employee e1
    where e1.departmentId=e.departmentId
    and e1.salary > e.salary
) <3
