SELECT 
    c.visited_on,
    (
        SELECT SUM(amount)
        from customer
        WHERE visited_on BETWEEN DATE_SUB(c.visited_on, INTERVAL 6 DAY) AND c.visited_on
    ) as amount,
    ROUND(
        (
            SELECT SUM(amount) / 7 
            FROM customer
            WHERE visited_on BETWEEN DATE_SUB(c.visited_on, INTERVAL 6 DAY) AND c.visited_on
        )
    ,2) as average_amount
FROM customer c
WHERE c.visited_on >= (
    SELECT DATE_ADD(MIN(visited_on),INTERVAL 6 DAY)
    FROM customer 
)
GROUP BY c.visited_on;