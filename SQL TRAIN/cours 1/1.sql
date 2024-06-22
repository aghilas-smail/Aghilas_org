-- AUTHOR SMAIL AGHILAS
-- LINK : https://app.solers.io/candidat/tests/11584

SELECT DATE(created_at) as day, description, COUNT(*) AS count
FROM events
WHERE name = 'trained'
GROUP BY day, description
ORDER BY day

-- TEST PASSED !