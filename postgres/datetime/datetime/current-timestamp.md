 
- different ways

    SELECT NOW();
    -- 2023-05-25 12:50:11.682872-04
    --                           ^-- tz is UTC-04
    
    SELECT CURRENT_TIMESTAMP;
    -- 2023-05-25 12:50:11.682872-04

- specify which time zone

    SELECT NOW()                AT TIME ZONE 'utc';
    -- 2023-05-25 16:50:42.669508
    SELECT NOW()                AT TIME ZONE 'america/montreal';
    -- 2023-05-25 12:51:32.830409
    
    -- alternate syntax
    SELECT CURRENT_TIMESTAMP    AT TIME ZONE 'utc';
    SELECT TIMEZONE('UTC', NOW());
    SELECT TIMEZONE('UTC', CURRENT_TIMESTAMP);

- 

