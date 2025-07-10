https://www.postgresql.org/docs/current/functions-datetime.html

    age(timestamp, timestamp) 	| age(timestamp '2001-04-10', timestamp '1957-06-13') 	| 43 years 9 mons 27 days
    age(timestamp) 	            | age(timestamp '1957-06-13') |	43 years 8 mons 3 days

    date_part(text, timestamp) 	| date_part('hour', timestamp '2001-02-16 20:38:40') | 20
    date_part(text, interval)   | date_part('month', interval '2 years 3 months') | 3
    date_trunc(text, timestamp) | date_trunc('hour', timestamp '2001-02-16 20:38:40') 	2001-02-16 20:00:00

    extract(field from timestamp) | extract(hour from timestamp '2001-02-16 20:38:40') 	20
    extract(field from interval)  | extract(month from interval '2 years 3 months') 	3

    isfinite(date)              | isfinite(date '2001-02-16') 	true
    isfinite(timestamp)         | isfinite(timestamp '2001-02-16 21:28:30') 	true
    isfinite(interval) 	boolean 	Test for finite interval 	isfinite(interval '4 hours') 	true

    justify_days(interval) 	interval 	Adjust interval so 30-day time periods are represented as months 	justify_days(interval '35 days') 	1 mon 5 days
    justify_hours(interval) 	interval 	Adjust interval so 24-hour time periods are represented as days 	justify_hours(interval '27 hours') 	1 day 03:00:00
    justify_interval(interval) 	interval 	Adjust interval using justify_days and justify_hours, with additional sign adjustments 	justify_interval(interval '1 mon -1 hour') 	29 days 23:00:00

### Timestamps

    clock_timestamp() 	    # timestamp with time zone 	Current
    current_date            # Current date
    current_time 	 	    # Current time of day
    current_timestamp 	    # Current date and time
    localtime 	            # Current time of day
    localtimestamp 	        # Current date and time
    now() 	                # Current date and time
    statement_timestamp()   # Current date and time (start of current statement)
    timeofday()             # Current date and time (like clock_timestamp, but as a text string)
    transaction_timestamp()
