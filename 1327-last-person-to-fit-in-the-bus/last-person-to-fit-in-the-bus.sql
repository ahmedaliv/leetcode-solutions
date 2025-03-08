WITH RunningSum AS (
    SELECT person_name, 
           turn, 
           weight, 
           SUM(weight) OVER (ORDER BY turn) AS running_weight
    FROM Queue
)
SELECT person_name
FROM RunningSum
WHERE running_weight <= 1000
ORDER BY turn DESC
LIMIT 1;
