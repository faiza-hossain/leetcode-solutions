# Write your MySQL query statement below
select eu.unique_id as unique_id,e.name as name
from Employees as e
left JOIN EmployeeUNI as eu on eu.id=e.id
