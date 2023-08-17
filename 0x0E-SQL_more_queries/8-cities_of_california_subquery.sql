-- lists all cities of California found in the database hbtn_0d_usa
-- states table contains one record where name = California (but the id can be different)
-- Results sorted in ascending order by cities.id
-- not allowed to use the JOIN keyword

SELECT id, name
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = 'California'
	)
ORDER BY id ASC;
