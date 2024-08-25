-- link : https://leetcode.com/problems/product-sales-analysis-i/description/?envType=study-plan-v2&envId=top-sql-50
-- Author : Aghilas SMAIL


Select p.product_name, s.year, s.price 
from Product p
Join Sales s ON s.product_id = p.product_id;
