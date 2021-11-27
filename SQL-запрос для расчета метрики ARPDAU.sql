
WITH revenue AS (SELECT CAST(event_time AS DATE) date, 
						SUM(event_value) rev 
				FROM events
				GROUP BY CAST(event_time AS DATE)),
	dau AS	(SELECT CAST(event_time AS DATE) date, 
					COUNT(DISTINCT(user_id)) cnt 
			FROM events WHERE event_name = 'launch' 
			GROUP BY CAST(event_time AS DATE))
			
SELECT	
	r.date,
	rev / cnt arpdau
			
FROM revenue r
LEFT JOIN dau d
ON r.date = d.date
		
order by 1