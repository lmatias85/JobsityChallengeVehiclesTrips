SELECT tmp.region,
	   tmp.datasource
  FROM (SELECT region,
			   datasource,
			   COUNT(1) over (partition BY region) AS comm,
			   ROW_NUMBER()  over (partition BY region ORDER BY trips_datetime DESC) AS pos
		  FROM trips) AS tmp
 WHERE tmp.pos = 1
 ORDER BY tmp.comm DESC
 limit 2;