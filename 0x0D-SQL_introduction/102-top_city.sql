-- Display top 3 city temps during July and August ordered by temp descending

SELECT city, AVG(value) AS avg_temp FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city ORDER BY avg_temp DESC
LIMIT 3;
