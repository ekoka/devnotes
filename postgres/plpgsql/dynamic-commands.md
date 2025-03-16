ref: 
https://www.postgresql.org/docs/current/plpgsql-statements.html#PLPGSQL-STATEMENTS-EXECUTING-DYN
- see string functions
https://www.postgresql.org/docs/current/functions-string.html
- see `quote_` functions
https://www.postgresql.org/docs/current/functions-string.html#FUNCTIONS-STRING-OTHER
- see `format()`
https://www.postgresql.org/docs/current/functions-string.html#FUNCTIONS-STRING-FORMAT

## syntax

    EXECUTE command-string [INTO [STRICT] target] [USING expression [, ...] ];

- `command-string` is an expression yielding a string containing the command to be executed.
- `target` is a record variable, a row variable, or comma-separated list of simple variables, record/row fields, into which the results of the command will be stored. The list must exactly match the structure of the query's results. 
- the `USING` clause supplies values to be inserted into the command as `$1`, `$2`, etc.

    DECLARE
        c int;
    BEGIN
        ...
        EXECUTE 'select count(*) from mytable where inserted_by = $1 and inserted <= $2'
        INTO c
        USING checked_user, checked_date;
        ...
    END;
    
- no substitution of plpgsql variable is done on the computed command string.
- any variable values must be inserted in the command string as it is constructed, or parameters can be used (see later).
- there's no plan caching for commands executed via `EXECUTE`.

- providing table or column name dynamically can be done by inserting them in the query string. 
    EXECUTE 'select count(*) from '
        || quote(table_name)  -- <-- dynamically provided table name
        || ' where inserted_by = $1 and inserted <= $2'
    INTO c
    USING checked_user, checked_date;

- or better yet use `forma()` and `%I`
    
    EXECUTE format(
        'select count(*) from %I '
        'where inserted_by = $1 and inserted <= $2', 
        table_name
    )
    INTO c
    USING checked_user, checked_date;

- Also note that parameter symbols only work for `SELECT`, `INSERT`, `UPDATE`, and `DELETE`. For other statement types insert values textually (even data).

- `SELECT INTO` is not currently supported within `EXECUTE`; instead, execute a plain `SELECT` command and specify `INTO` as part of the `EXECUTE` itself

- note that the plpgslq `EXECUTE` is not related to the `EXECUTE` SQL statement.

## quoting values

    -- with format() and %I
    EXECUTE format(
        'UPDATE tbl SET %I = $1 '
        'WHERE key = $2', 
        colname
    ) 
    USING newvalue, keyvalue;

    -- with quoting functions
    
    EXECUTE 'UPDATE tbl SET '
        || quote_ident(colname)
        || ' = '
        || quote_literal(newvalue)
        || ' WHERE key = '
        || quote_literal(keyvalue); 

