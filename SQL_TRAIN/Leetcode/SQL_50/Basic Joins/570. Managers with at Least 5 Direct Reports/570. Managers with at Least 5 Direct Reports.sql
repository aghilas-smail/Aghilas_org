-- Link : https://leetcode.com/problems/managers-with-at-least-5-direct-reports/?envType=study-plan-v2&envId=top-sql-50
-- Author : Aghilas SMAIL


select E.name 
from Employee E
where E.id IN (
    select managerId
    from Employee
    where managerId is not null
    group by managerId
    having count(*) >=5
);
