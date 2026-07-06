# Write your MySQL query statement below
select s.student_id,s.student_name,sub.subject_name,
count(e.student_id) as attended_exams
from Students as s
CROSS JOIN Subjects as sub  
LEFT JOIN Examinations as e 
on sub.subject_name=e.subject_name
and s.student_id=e.student_id
group by sub.subject_name,s.student_name,s.student_id
order by s.student_id,s.student_name,sub.subject_name