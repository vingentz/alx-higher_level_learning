-- List all records of second_table(hbtn_0c_0)
-- list rows without name value, display score, name and in descending score

SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
