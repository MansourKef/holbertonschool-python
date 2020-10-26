-- Another select query
SELECT band_name, IFNULL((split - formed), 0) lifespan FROM metal_bands ORDER BY lifespan DESC;
