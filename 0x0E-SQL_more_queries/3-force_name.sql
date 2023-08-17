-- creates the table force_name on your MySQL server
-- force_name description of id INT and name VARCHAR(256) cant be null

CREATE TABLE IF NOT EXISTS force_name(
	id INT,
	name VARCHAR(256) NOT NULL
);
