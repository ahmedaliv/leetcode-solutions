SELECT p.project_id,
ROUND(AVG(e.experience_years),2) as average_years
from employee e
inner join project p
on e.employee_id = p.employee_id
group by p.project_id
