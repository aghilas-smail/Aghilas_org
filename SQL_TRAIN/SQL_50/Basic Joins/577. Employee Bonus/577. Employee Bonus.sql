-- Link : https://leetcode.com/problems/employee-bonus/description/?envType=study-plan-v2&envId=top-sql-50
-- Author : Aghilas SMAIL


select e.name, b.bonus
from Employee e
Left join Bonus b On e.empId = b.empId
where bonus < 1000 or bonus is null;