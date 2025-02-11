-- Write your PostgreSQL query statement below
WITH TOTAL AS (
    SELECT 
        s.user_id,
        COUNT(c.user_id) AS TOTAL_MESSAGES 
    FROM 
        SIGNUPS S
    LEFT JOIN 
        CONFIRMATIONS C
    ON 
        S.USER_ID = C.USER_ID
    GROUP BY 
        s.user_id
),
CONFIRMED AS (
    SELECT 
        s.user_id,
        COUNT(c.user_id) AS CONFIRMED_MESSAGES 
    FROM 
        SIGNUPS S
    LEFT JOIN 
        CONFIRMATIONS C
    ON 
        S.USER_ID = C.USER_ID
    WHERE 
        C.ACTION = 'confirmed'
    GROUP BY 
        s.user_id
)

SELECT 
    t.user_id, 
    CASE 
        WHEN t.TOTAL_MESSAGES = 0 THEN 0
        ELSE ROUND(COALESCE(c.CONFIRMED_MESSAGES, 0) * 1.0 / t.TOTAL_MESSAGES, 2)
    END AS confirmation_rate
FROM 
    TOTAL t
LEFT JOIN 
    CONFIRMED c 
ON 
    t.user_id = c.user_id
ORDER BY 
    t.user_id;