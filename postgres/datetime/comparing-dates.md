## Refs:
- https://stackoverflow.com/questions/19469154/how-to-compare-dates-in-datetime-fields-in-postgresql

- Selecting timestamped (date and time) rows that match a specific date

    -- updated is a timestamp column (i.e. date & time)
    SELECT * FROM table
    WHERE
        updated >= '2020-07-29'
        AND updated < ('2020-07-29'::date + '1 day'::interval);

- remember that postgres cast values to the same type prior to comparing them, so be mindful when comparing date and datetime. So

    updated_at <= '2020-07-29'

will be evaluated as

    updated_at <= '2020-07-29 00:00:00'

which excludes all records updated after midnight.

### Using the `range` type

    select * from table
    where
        update_date <@
        tsrange('2020-07-29', '2020-07-29'::date + 1, '[)');

- `tsrange` — range of timestamp without time zone
- `tstzrange` — range of timestamp with time zone
- `<@` 	range is contained by.      e.g. int4range(2,4) <@ int4range(1,7)    T
- `<@` 	element is contained by.    e.g. 42 <@ int4range(1,7) 	             F
- `@>` 	contains range.             e.g. int4range(2,4) @> int4range(2,3) 	 T
- `@>` 	contains element. 	        e.g. '[2011-01-01,2011-03-01)'::tsrange @> '2011-01-10'::timestamp 	T

http://www.postgresql.org/docs/current/static/rangetypes.html
http://www.postgresql.org/docs/current/static/functions-range.html
