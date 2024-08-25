-- Link : https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/?envType=study-plan-v2&envId=top-sql-50
-- Author : Aghilas SMAIL

select v.customer_id, Count(*) AS count_no_trans
from visits v 
left join Transactions t ON t.visit_id = v.visit_id
where transaction_id is null
group by v.customer_id
Order by count_no_trans