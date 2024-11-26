-- Link : https://leetcode.com/problems/product-price-at-a-given-date/description/?envType=study-plan-v2&envId=top-sql-50
Dans cette exemple, y'a 2 condition:
    - Si le prix d'un produit a été changer aprés le 18 aout alors on mette le prix qui a dans la table.
    - Sinon on mette une valeur par defaut qui est le 10.
select p1.product_id, 
       coalesce(p2.new_price, 10) as price
from 
    (select distinct product_id from Products) p1
left join
    Products p2 on p1.product_id = p2.product_id
    and p2.change_date = (
        select max(change_date)
        from Products p3
        where p3.product_id = p1.product_id and p3.change_date <= '2019-08-16'
    )
order by
    p1.product_id

