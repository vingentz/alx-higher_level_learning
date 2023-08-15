-- create first table in current database
-- with int and varchar(256), if exists, script shouldnt fail

CREATE TABLE IF NOT EXISTS first_table(
	id INT,
	name VARCHAR(256));
