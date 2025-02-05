-- Write your PostgreSQL query statement below

SELECT W1.ID
FROM WEATHER W1
INNER JOIN WEATHER W2
ON W1.recordDate - W2.recordDate = 1
AND W1.temperature > W2.temperature;