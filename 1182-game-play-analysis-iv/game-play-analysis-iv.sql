WITH first_logins AS (
    SELECT player_id, MIN(event_date) AS first_login
    FROM activity
    GROUP BY player_id
),
consec_logins AS (
    SELECT a.player_id
    FROM activity a
    JOIN first_logins f 
      ON a.player_id = f.player_id
     AND a.event_date = f.first_login + INTERVAL '1 day'
)
SELECT 
    ROUND(
        (SELECT COUNT(*) FROM consec_logins)::DECIMAL / (SELECT COUNT(*) FROM first_logins),
        2
    ) AS fraction;
