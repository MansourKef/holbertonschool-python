-- Use sub queries
SELECT id, name FROM cities WHERE state_id in (SELECT id from states WHERE states.name = 'California') Order By cities.id;
