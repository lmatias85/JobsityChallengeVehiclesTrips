SELECT WEEK(trips_datetime) number_of_week,
	   STR_TO_DATE(CONCAT(YEAR(trips_datetime), ' ' ,WEEK(trips_datetime), ' 0'), '%X %V %w') as week_from,
	   DATE_ADD(STR_TO_DATE(CONCAT(YEAR(trips_datetime), ' ' ,WEEK(trips_datetime), ' 0'), '%X %V %w'), INTERVAL 6 DAY) week_to,
	   COUNT(1) /
	   (SELECT COUNT(1)
	      FROM trips
	       WHERE (CAST(SUBSTR(origin_coord ,
				    LOCATE("(" ,origin_coord) + 1,
				    LOCATE(" " ,origin_coord, LOCATE("(" ,origin_coord)) - LOCATE("(" ,origin_coord)) AS DOUBLE) >= @param_x1
				    AND
				    CAST(SUBSTR(origin_coord,LOCATE(" " ,origin_coord, LOCATE("(" ,origin_coord)),
				   	LENGTH(SUBSTR(origin_coord,LOCATE(" " ,origin_coord, LOCATE("(" ,origin_coord))))-1)AS DOUBLE) <= @param_y2)
				OR (CAST(SUBSTR(destination_coord  ,
				    LOCATE("(" ,destination_coord) + 1,
				    LOCATE(" " ,destination_coord, LOCATE("(" ,destination_coord)) - LOCATE("(" ,destination_coord)) AS DOUBLE) >= @param_x1
				    AND
				    CAST(SUBSTR(destination_coord,LOCATE(" " ,destination_coord, LOCATE("(" ,destination_coord)),
				   	LENGTH(SUBSTR(destination_coord,LOCATE(" " ,destination_coord, LOCATE("(" ,destination_coord))))-1)AS DOUBLE) <= @param_y2)) AS avg_num_of_trips
  FROM trips t
 WHERE (CAST(SUBSTR(origin_coord ,
	    LOCATE("(" ,origin_coord) + 1,
	    LOCATE(" " ,origin_coord, LOCATE("(" ,origin_coord)) - LOCATE("(" ,origin_coord)) AS DOUBLE) >= @param_x1
	    AND
	    CAST(SUBSTR(origin_coord,LOCATE(" " ,origin_coord, LOCATE("(" ,origin_coord)),
	   	LENGTH(SUBSTR(origin_coord,LOCATE(" " ,origin_coord, LOCATE("(" ,origin_coord))))-1)AS DOUBLE) <= @param_y2)
	OR (CAST(SUBSTR(destination_coord  ,
	    LOCATE("(" ,destination_coord) + 1,
	    LOCATE(" " ,destination_coord, LOCATE("(" ,destination_coord)) - LOCATE("(" ,destination_coord)) AS DOUBLE) >= @param_x1
	    AND
	    CAST(SUBSTR(destination_coord,LOCATE(" " ,destination_coord, LOCATE("(" ,destination_coord)),
	   	LENGTH(SUBSTR(destination_coord,LOCATE(" " ,destination_coord, LOCATE("(" ,destination_coord))))-1)AS DOUBLE) <= @param_y2)
  GROUP BY WEEK(trips_datetime),
	    STR_TO_DATE(CONCAT(YEAR(trips_datetime), ' ' ,WEEK(trips_datetime), ' 0'), '%X %V %w'),
	    DATE_ADD(STR_TO_DATE(CONCAT(YEAR(trips_datetime), ' ' ,WEEK(trips_datetime), ' 0'), '%X %V %w'), INTERVAL 6 DAY)
  ORDER BY 1 ;