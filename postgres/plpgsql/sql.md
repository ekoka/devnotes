
## SQL command that do not produce a value
- if the SQL command does not return rows, you can just write it. 

    CREATE TABLE mytable (id int primary key, data text);
    INSERT INTO mytable values (1, 'one'), (2, 'two');

##  SQL commands that return values
#####  Capturing at most one row from the SQL result
ref: https://www.postgresql.org/docs/14/plpgsql-statements.html#PLPGSQL-STATEMENTS-SQL-ONEROW

- write the SQL command as usual, but capture the output with an `INTO [STRICT] target`

    SELECT select_expressions INTO [STRICT] target FROM ...;
    INSERT ... RETURNING expressions INTO [STRICT] target;
    UPDATE ... RETURNING expressions INTO [STRICT] target;
    DELETE ... RETURNING expressions INTO [STRICT] target;

- where `target` can be:
    - a record variable
    - a row variable
    - a comma-separated list of simple variables and record/row fields.

    e.g. 

    SELECT user_id, firstname INTO user_id, name FROM buyers;  

- PL/pgSQL variables will be substituted into the rest of the command (i.e. everything but the `INTO` clause)
- the plan is cached as usual.
- it works for `SELECT`, `INSERT/UPDATE/DELETE` with `RETURNING` and certain utility commands that return row sets, such as `EXPLAIN`. 
- except for the `INTO` clause, the SQL command is the same as outside PL/pgSQL.

- the `INTO` clause can appear almost anywhere in the SQL command, although it is customarily written either just before or just after the list of `select_expression` in a `SELECT` command.

- if `STRICT` is not specified then `target` is set to the first row returned, or to nulls if the command returns no rows. Rows after the first are discarded. Check the special `FOUND` variable to determine whether a row was returned.

    SELECT * INTO myrec FROM emp WHERE empname = myname;
    IF NOT FOUND THEN
        RAISE EXCEPTION 'employee % not found', myname;
    END IF;

- if `STRICT` is specified the command must return exactly one row or a run-time error will be reported (`NO_DATA_FOUND` or `TOO_MANY_ROWS`), which can be handled in an `EXCEPTION` block.

    SELECT * INTO STRICT myrec FROM emp WHERE empname = myname;
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            RAISE EXCEPTION 'employee % not found', myname;
        WHEN TOO_MANY_ROWS THEN
            RAISE EXCEPTION 'employee % not unique', myname;
    END IF;
    
- `INSERT/UPDATE/DELETE` with `RETURNING` that return more than one row, even without `STRICT`, PL/pgSQL reports an error.

## returning multiple rows 

- ref: 
    https://dba.stackexchange.com/questions/186257/how-can-i-return-multiple-rows-of-records-in-pl-pgsql
    https://stackoverflow.com/questions/22010405/how-to-return-multiple-row-from-multiple-table-in-plpgsql
#### defining a function returning a `TABLE` (preferred approach)

- with `RETURN NEXT` in `FOR LOOP` structure

    CREATE OR REPLACE FUNCTION foo_bar() 
    RETURNS TABLE (foo_a int, foo_b int, bar_a int, bar_b int) AS $$
    BEGIN            
    FOR foo_a, foo_b, bar_a, bar_b IN 
        SELECT f.a fa, f.b fb, b.a ba, b.b bb
            FROM foo f 
                JOIN bar b 
                    ON f.id = bar.foo_id
    LOOP
        RETURN NEXT;
    END LOOP;
    RETURN;
    END;
    $$ LANGUAGE plpgsql;

- using 

    postgres=# SELECT * FROM foo_bar();

- with `RETURN QUERY` 

    DROP FUNCTION IF EXISTS test_function();
    CREATE OR REPLACE FUNCTION test_function()
        RETURNS TABLE (id int, str text, is_even boolean)
        LANGUAGE plpgsql as $$
    BEGIN
        RETURN QUERY
            SELECT i, format('str%s', i), i/2*2 = i
            FROM generate_series(1, 3) i;
        -- you can use return query multiple times
        -- or assign values to columns
        -- and return the row:
        id = 100;
        str = 'extra';
        is_even = true;
        RETURN NEXT; -- without a parameter
    END $$;

- using 

    postgres=# SELECT * FROM test_function();

    
    
#### defining a function returning a `SETOF RECORD`

    CREATE OR REPLACE FUNCTION test_function()
        RETURNS SETOF RECORD AS $$
    DECLARE
        rec RECORD;
    BEGIN
        FOR rec IN
            SELECT i, format('str%s', i), i/2*2 = i
            FROM generate_series(1, 3) i
        LOOP
            RETURN NEXT rec;
        END LOOP;
    END $$
    LANGUAGE plpgsql;

- using    

    SELECT test_function();         -- NO

        ERROR:  set-valued function called in context that cannot accept a set  

    SELECT * FROM test_function();  -- NO

        ERROR:  a column definition list is required for functions returning "record"

    SELECT * FROM test_function() 
        AS (id int, str text, is_even boolean);
