WITH MostActiveUser AS (
    SELECT u.name AS results
    FROM USERS u
    JOIN MOVIERATING mr ON mr.user_id = u.user_id
    GROUP BY u.user_id, u.name
    ORDER BY COUNT(mr.user_id) DESC, u.name ASC
    LIMIT 1
),
TopRatedMovie AS (
    SELECT m.title AS results
    FROM MOVIES m
    JOIN MOVIERATING mr ON m.movie_id = mr.movie_id
    WHERE mr.created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY m.movie_id, m.title
    ORDER BY AVG(mr.rating) DESC, m.title ASC
    LIMIT 1
)

SELECT results FROM MostActiveUser
UNION ALL
SELECT results FROM TopRatedMovie;
