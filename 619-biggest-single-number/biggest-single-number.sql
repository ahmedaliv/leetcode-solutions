SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MYNUMBERS
    GROUP BY num
    HAVING COUNT(*) = 1
) AS single_numbers;
