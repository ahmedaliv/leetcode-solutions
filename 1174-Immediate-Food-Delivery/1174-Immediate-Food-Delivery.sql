SELECT 
    ROUND(AVG(CASE WHEN order_date = customer_pref_delivery_date THEN 1.0 ELSE 0 END) * 100, 2) 
    AS immediate_percentage
FROM (
    SELECT 
        customer_id,
        order_date,
        customer_pref_delivery_date,
        ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY order_date ASC) AS rn
    FROM Delivery
) t
WHERE rn = 1;
