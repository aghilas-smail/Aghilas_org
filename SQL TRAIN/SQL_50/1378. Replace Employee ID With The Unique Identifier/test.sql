-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/description/?envType=study-plan-v2&envId=top-sql-50
-- Write your MySQL query statement below
SELECT e.name,
       eu.unique_id
FROM Employees e
LEFT JOIN EmployeeUNI eu
ON e.id = eu.id;
