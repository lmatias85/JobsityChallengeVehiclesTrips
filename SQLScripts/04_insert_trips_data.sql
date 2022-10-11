INSERT INTO trips (region, origin_coord, destination_coord, trips_datetime, datasource, process_date, process_user)
SELECT MIN(region),
	   origin_coord,
	   destination_coord,
	   trip_datetime,
	   MIN(datasource),
	   CURRENT_DATE(),
	   USER()
  FROM trips_raw
 GROUP BY origin_coord,
 	   destination_coord,
 	   trip_datetime;