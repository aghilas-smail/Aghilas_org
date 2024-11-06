 -- Link : https://leetcode.com/problems/product-sales-analysis-iii/description/?envType=study-plan-v2&envId=top-sql-50

 select s.product_id, s.year AS first_year, s.quantity, s.price
 FROM Sales s -- on utilise une sous requet pour filtrer tous les ligne avec l'année est minumum pour chaque produit
 INNER JOIN (SELECT product_id, MIN(year) as first_year
             FROM Sales
             GROUP BY product_id) t 
 ON s.product_id = t.product_id and s.year = t.first_year;
 