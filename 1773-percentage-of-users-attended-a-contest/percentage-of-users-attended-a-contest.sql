-- Write your PostgreSQL query statement below
SELECT r.contest_id, 
ROUND(count(distinct r.user_id) * 100.0 /(select count(*) from users),2) as percentage
from register r
group by r.contest_id
order by percentage desc, contest_id asc