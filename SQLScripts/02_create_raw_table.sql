USE jobsity_db;
DROP TABLE IF EXISTS trips_raw;
CREATE TABLE trips_raw(
    region varchar(150),
	origin_coord varchar(200),
	destination_coord varchar(200),
	trip_datetime date,
	datasource varchar(200)
);