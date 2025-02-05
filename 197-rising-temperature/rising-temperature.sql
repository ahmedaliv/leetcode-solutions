-- Write your PostgreSQL query statement below

SELECT ID
FROM WEATHER W1
WHERE EXISTS (
    SELECT 1 
    FROM WEATHER W2
    WHERE W1.recordDate - W2.recordDate = 1
    and W1.temperature > W2.temperature
)