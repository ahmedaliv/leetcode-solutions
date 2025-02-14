SELECT p.product_id, 
       COALESCE(ROUND(SUM(u.units * p.price) / NULLIF(SUM(u.units)::NUMERIC, 0), 2), 0) AS average_price
FROM Prices p
LEFT JOIN UnitsSold u 
ON p.product_id = u.product_id 
AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;
