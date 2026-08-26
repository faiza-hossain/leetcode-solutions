# Write your MySQL query statement below
UPDATE Salary 
set sex = case when sex='f' then 'm' else 'f' end 
