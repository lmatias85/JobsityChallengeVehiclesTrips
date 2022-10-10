USE jobsity_db;
CREATE TABLE trips(
	region varchar(150),
	origin_coord varchar(200),
	destination_coord varchar(200),
	datetime_ datetime,
	datasource varchar(200),
	process_date datetime,
	process_user varchar(100)
);