-- Write your PostgreSQL query statement below

WITH first_year_cte AS (
    select product_id,quantity,price,year,
    RANK() OVER (PARTITION BY product_id ORDER BY year) as fy
    from sales
)

select 
product_id, year as first_year, quantity, price
from first_year_cte
where fy = 1