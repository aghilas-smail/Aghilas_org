-- Link : https://leetcode.com/problems/classes-more-than-5-students/?envType=study-plan-v2&envId=top-sql-50

SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5 -- On utilise Having pour ce genre d'exemple qui ce répete souvent.