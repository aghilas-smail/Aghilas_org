-- Link : https://leetcode.com/problems/rising-temperature/description/?envType=study-plan-v2&envId=top-sql-50
-- Author : Aghilas SMAIL

SELECT 
    w1.id
FROM 
    Weather w1
WHERE 
    w1.temperature > 
    (SELECT temperature 
    FROM Weather 
    WHERE recordDate = DATE_SUB(w1.recordDate, INTERVAL 1 DAY));
