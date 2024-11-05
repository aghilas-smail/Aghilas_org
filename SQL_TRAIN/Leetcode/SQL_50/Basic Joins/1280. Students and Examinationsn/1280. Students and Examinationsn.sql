-- Link : https://leetcode.com/problems/students-and-examinations/?envType=study-plan-v2&envId=top-sql-50
-- Author : Aghilas SMAIL


select 
    s.student_id, 
    s.student_name, 
    sub.subject_name, 
    count(e.student_id) as attended_exams
from 
    Students s
inner join 
    Subjects sub
left join 
    Examinations e
ON 
    s.student_id = e.student_id AND sub.subject_name = e.subject_name
GROUP BY 
    s.student_id, s.student_name, sub.subject_name
ORDER BY 
    s.student_id, sub.subject_name;
