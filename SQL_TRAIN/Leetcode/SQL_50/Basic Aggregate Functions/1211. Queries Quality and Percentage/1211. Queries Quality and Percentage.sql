-- Link : https://leetcode.com/problems/queries-quality-and-percentage/?envType=study-plan-v2&envId=top-sql-50
-- Author : Aghilas SMAIL

select 
    query_name, 
    round(avg(rating/position), 2) as quality, 
    round(avg(case when rating < 3 then 1 else 0 end) * 100.0, 2) as poor_query_percentage

from 
    Queries
where 
    query_name is not null
group by 
    query_name