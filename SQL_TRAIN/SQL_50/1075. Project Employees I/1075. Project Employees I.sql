-- Link : https://leetcode.com/problems/project-employees-i/description/?envType=study-plan-v2&envId=top-sql-50
-- author : Aghilas SMAIL


select P.project_id,
        ROUND(AVG(e.experience_years),2) as average_years
from 
    Project p
join
    Employee e
where 
    P.employee_id = e.employee_id
group by
    P.project_id;