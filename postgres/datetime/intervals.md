### INTERVALS

- the difference between two `TIMESTAMP` is always an `INTERVAL`

    TIMESTAMP '1999-12-30' - TIMESTAMP '1999-12-11' = INTERVAL '19 days'

- you may add or subtract an INTERVAL to a TIMESTAMP to produce another TIMESTAMP

    TIMESTAMP '1999-12-11' + INTERVAL '19 days' = TIMESTAMP '1999-12-30'

- you may add or subtract two INTERVALS

    INTERVAL '1 month' + INTERVAL '1 month 3 days' = INTERVAL '2 months 3 days'

- to only divide INTERVALS consisting of days, hours, minutes and seconds

    EXTRACT(EPOCH FROM INTERVAL '4 hours') / EXTRACT(EPOCH FROM INTERVAL '2 hours') = 2

- many larger `INTERVAL` values, like the calendar values they reflect, are not constant in length when expressed as small `INTERVAL` values

    TIMESTAMP '2001-07-02' + INTERVAL '1 month' = TIMESTAMP '2001-08-02'
    TIMESTAMP '2001-07-02' + INTERVAL '31 days' = TIMESTAMP '2001-08-02'

but

    TIMESTAMP '2001-02-02' + INTERVAL '1 month' = TIMESTAMP '2001-03-02'
    TIMESTAMP '2001-02-02' + INTERVAL '31 days' = TIMESTAMP '2001-03-05'

### Casting with double colon syntax

    '2012-05-03'::date + '1 day'::interval

### See also

##### INTERVAL input
https://www.postgresql.org/docs/current/datatype-datetime.html#DATATYPE-INTERVAL-INPUT

##### INTERVAL output
https://www.postgresql.org/docs/current/datatype-datetime.html#DATATYPE-INTERVAL-OUTPUT

### Operations with DATES
- the difference between two DATES is always an INTEGER representing the number of DAYS difference

    DATE '1999-12-30' - DATE '1999-12-11' = INTEGER 19

- you may add or subtract an INTEGER to a DATE to produce another DATE

    DATE '1999-12-11' + INTEGER 19 = DATE '1999-12-30'


- displaying DATE as text, or convert text into a DATE or INTERVAL

    # TODO
    to_date(), to_char() and interval()

- getting the month as an integer out of a date

    # TODO
    extract()

- convert date to Unix timestamp

    EXTRACT(EPOCH from TIMESTAMP '2014-01-28 00:00:00')
    EXTRACT(EPOCH from my_timestamp_field)


### Refs:

    https://wiki.postgresql.org/wiki/Working_with_Dates_and_Times_in_PostgreSQL
    https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-interval/
