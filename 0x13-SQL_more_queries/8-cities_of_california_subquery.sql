-- Use sub queries
SELECT id, name FROM cities WHERE state_id IN (SELECT id FROM states WHERE states.name = 'California') ORDER BY cities.id;
