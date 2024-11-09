-- link : https://leetcode.com/problems/biggest-single-number/description/?envType=study-plan-v2&envId=top-sql-50
select 
    MAX(a.num) AS num
from 
    (Select num 
    from MyNumbers 
    GROUP BY num 
    HAVING COUNT(*) = 1) 
AS a;