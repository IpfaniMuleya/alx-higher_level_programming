-- Select cities of California by referencing the state_id from the states table
SELECT id, 
name FROM cities WHERE state_id = (
	SELECT id FROM states WHERE name = 'California'
) 
ORDER BY id ASC;
