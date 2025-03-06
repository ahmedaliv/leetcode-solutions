SELECT DISTINCT num AS ConsecutiveNums
FROM Logs l1
WHERE num = (SELECT num FROM Logs WHERE id = l1.id + 1)
AND num = (SELECT num FROM Logs WHERE id = l1.id + 2);
