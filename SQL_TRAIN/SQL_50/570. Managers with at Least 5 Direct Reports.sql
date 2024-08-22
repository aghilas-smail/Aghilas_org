# Write your MySQL query statement below
select E.name 
from Employee E
where E.id IN (
    select managerId
    from Employee
    where managerId is not null
    group by managerId
    having count(*) >=5
);
