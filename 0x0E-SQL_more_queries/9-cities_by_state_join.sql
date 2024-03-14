-- Script to list all cities with their corresponding states
-- Select cities and their corresponding state names
SELECT cities.id, cities.name, states.name 
FROM cities 
LEFT JOIN states ON states.id = cities.state_id 
ORDER BY cities.id;
