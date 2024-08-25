-- Link : https://leetcode.com/problems/percentage-of-users-attended-a-contest/?envType=study-plan-v2&envId=top-sql-50
-- Author : Aghilas SMAIL

select r.contest_id, round(count(distinct r.user_id)/count(distinct u.user_id)*100,2) as percentage
-- we found the number of user of each contest_id in register table and we divid the result on the number total of user in User table
from Users u, Register r
group by contest_id
order by percentage DESC, contest_id asc 