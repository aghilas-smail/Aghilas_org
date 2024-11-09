-- Link : https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/description/?envType=study-plan-v2&envId=top-sql-50

select 
a1.employee_id, 
a1.name,
count(*) AS reports_count,
round(avg(a2.age)) AS average_age
from Employees a1 join Employees a2 
where a1.employee_id = a2.reports_to
group by a1.employee_id, name
order by a1.employee_id