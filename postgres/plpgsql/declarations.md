ref: https://www.postgresql.org/docs/current/plpgsql-declarations.html

## function params can be accessed using `$n` in the body (starting at `$1`)

    create function myfunc(text, int) returns bool
    as $$
    declare
        name text;
        user_id int;
    begin
        name text; = $1;
        user_id int; = $2;
    end;
    $$ language plgsql;
        
## params can also be aliased 

- in the function declaration (preferred method)

    create function myfunc(name text, id int) returns bool
    as $$
    DECLARE
        -- params can be used as is
        firstname text = name;
    BEGIN
        -- or they can be qualified with the function's name
        user_id int = myfunc.id
    END
    $$ language plgsql;

- or using an `ALIAS` (type is inferred)
    
    create function myfunc(text, int) returns bool
    as $$
    DECLARE
        name ALIAS for $1;
        user_id ALIAS for $2;
    BEGIN
        -- you cannot prefix these aliases with the function's name
        id int = myfunc.user_id;    -- no 
        id int = user_id;           -- yes
    END
    $$ language plgsql;

## output params can be similarly declared with `OUT` and an optional alias

- the `RETURNS` and `RETURN` declarations becomes redundant if including `OUT` variables

    create function sum_n_product(int, int, OUT sum int, OUT prod int)
    as $$
    BEGIN
        sum = $1 + $2;
        prod = $1 * $2;
    END
    $$ language plgsql;

- when calling the function, omit the `OUT` variables (also works in procedures, but all variables must be specified)

    select * from sum_n_product(2, 3);

    sum | prod
    ----------
      5 |    6
    
