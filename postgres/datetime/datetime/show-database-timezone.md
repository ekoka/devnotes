- Showing the timezone setting of the database server

    SHOW TIMEZONE;

    # or  

    SELECT CURRENT_SETTING('TIMEZONE');  # or 'timezone'

- The `timezone` setting is usually in `/etc/postgresql/postgresql.conf`

    timezone = 'America/Toronto'

- setting time zone for a client session

    SET TIMEZONE TO 'UTC';

- getting timezone info based on the timezone

    SELECT * FROM pg_timezone_names WHERE name = current_setting('TIMEZONE');

- show timezone offset relative to UTC (including those with half and quarter tz)   

    SET SESSION timezone TO 'Asia/Kabul';           -- Setting tz to Kabul
    SELECT NOW();                                   -- 2023-05-25 20:26:11.682872+04:30
    SELECT EXTRACT(TIMEZONE FROM now());            -- 16200 (Kabul is 16200 seconds from UTC)
    SELECT EXTRACT(TIMEZONE FROM now())/3600.0;     -- in hours (Kabul is 4.5 hours from UTC)
