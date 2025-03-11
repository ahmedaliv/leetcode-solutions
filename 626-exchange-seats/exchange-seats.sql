-- Write your PostgreSQL query statement below

SELECT 
    CASE 
        WHEN ID % 2 = 1 AND ID < (SELECT MAX(ID) FROM SEAT) THEN ID + 1
        WHEN ID % 2 = 0 THEN ID - 1
        ELSE ID
    END AS id,
    student
FROM SEAT
ORDER BY ID