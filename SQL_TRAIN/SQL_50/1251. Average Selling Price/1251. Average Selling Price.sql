-- Link : https://leetcode.com/problems/average-selling-price/?envType=study-plan-v2&envId=top-sql-50
-- Author : Aghilas SMAIL

select p.product_id, 
        ROUND(SUM(us.units * p.price) / SUM(us.units),2) as average_price
from 
    UnitsSold us
JOIN
    Prices p
on 
    us.product_id = p.product_id
    and us.purchase_date between p.start_date and p.end_date
group by
    p.product_id