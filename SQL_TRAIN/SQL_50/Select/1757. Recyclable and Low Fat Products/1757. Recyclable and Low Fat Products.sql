-- Link : https://leetcode.com/problems/recyclable-and-low-fat-products/?envType=study-plan-v2&envId=top-sql-50
-- Author : Aghilas SMAIL

select product_id
from Products 
where low_fats = 'Y' and recyclable = 'Y'
group by product_id;