SELECT WEEK(trips_datetime) number_of_week,
	   STR_TO_DATE(CONCAT(YEAR(trips_datetime), ' ' ,WEEK(trips_datetime), ' 0'), '%X %V %w') as week_from,
	   DATE_ADD(STR_TO_DATE(CONCAT(YEAR(trips_datetime), ' ' ,WEEK(trips_datetime), ' 0'), '%X %V %w'), INTERVAL 6 DAY) week_to,
	   COUNT(1) / (SELECT COUNT(1) FROM  trips WHERE region = @param_region)
  FROM trips AS t
 WHERE region = @param_region
 GROUP BY WEEK(trips_datetime),
	   STR_TO_DATE(CONCAT(YEAR(trips_datetime), ' ' ,WEEK(trips_datetime), ' 0'), '%X %V %w'),
	   DATE_ADD(STR_TO_DATE(CONCAT(YEAR(trips_datetime), ' ' ,WEEK(trips_datetime), ' 0'), '%X %V %w'), INTERVAL 6 DAY)
 ORDER BY 1;