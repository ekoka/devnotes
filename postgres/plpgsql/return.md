https://www.postgresql.org/docs/14/plpgsql-control-structures.html
https://www.postgresql.org/docs/14/plpgsql-statements.html#PLPGSQL-STATEMENTS-SQL-ONEROW   

- unless returning `void` or specifying output parameters (with `OUT`), the function must explicitly `RETURN`. 
- if output params are specified, upon returning (whether implicitly or explicitly with `RETURN`), their final values are returned.

## returning from a function

- `RETURN`
- `RETURN expression`



The return value of a function cannot be left undefined. If control reaches the end of the top-level block of the function without hitting a RETURN statement, a run-time error will occur. This restriction does not apply to functions with output parameters and functions returning void, however. In those cases a RETURN statement is automatically executed if the top-level block finishes.

## returning no values
- declare the function as returning `void`
    
    CREATE function somefunc() RETURNS void AS
    $$
        ...
    $$ language pspgsql;

- `RETURN` in the body is optional, but can be used to exit early.

## returning at most a single instance of some type (including composite-types, i.e. a `ROW`)
    
- i.e. functions defined to return a single instance of a type (as opposed to a `SET OF` a type).

    https://www.postgresql.org/docs/14/plpgsql-control-structures.html
    https://www.postgresql.org/docs/14/plpgsql-statements.html#PLPGSQL-STATEMENTS-SQL-ONEROW   

##### function declared with explicit output parameters (`OUT`) 
    
    CREATE function somefunc(OUT param1 sometypeA, param2 sometype2) AS
    $$
        ...
    $$ language pspgsql;

- upon exiting, the function implicitly returns last values of `param1` and `param2` in a composite-value (i.e. a `ROW`).
- `RETURN` statement in the body is optional, but can be specified to end function early.
- the `RETURNS sometype` declaration in the definition also becomes redundant and can be omitted. 

##### function declared with no output params

    CREATE function somefunc() RETURNS sometype AS
    $$
        ...
        RETURN expression;
    $$ language pspgsql;
    
- function definition must declare that it `RETURNS sometype`.
- `RETURN expression` terminates the function and returns the value of `expression`.
- value of `expression` must match the declared return type.

## returning multiple rows

- function must be declared with `RETURNS SETOF sometype`.
    
    CREATE function somefunc() RETURNS SETOF sometype AS
    $$
        ...
    $$ language pspgsql;

- alternatively it can be declared with `RETURNS TABLE(...)`, which is exactly equivalent to declaring some output parameters and specify `RETURNS SETOF sometype`. 
    see https://www.postgresql.org/docs/14/plpgsql-declarations.html#PLPGSQL-DECLARATION-PARAMETERS
    
    CREATE function somefunc() 
    RETURNS TABLE(id integer, name text, role text) AS
    $$
        ...
    $$ language pspgsql;

    -- equivalent to 

    CREATE function somefunc(OUT id integer, OUT name text, OUT role text) 
    RETURNS SETOF ROW AS
    $$
        ...
    $$ language pspgsql;

- the individual items to return are specified by a sequence of `RETURN NEXT` or `RETURN QUERY` commands (can be intermixed), and then a final `RETURN` command with no argument to indicate that the function has finished executing. 

    RETURN NEXT expression;
    RETURN QUERY query;

- the results of `NEXT expression` and `QUERY query` are appended to the function's resultset, which is not returned until the function terminates (consult the documentation for performance issues).

- `RETURN NEXT` can be used with both scalar and composite data types. with a composite result type, an entire “table” of results will be returned. RETURN QUERY appends the results of executing a query to the function's result set. 

- refs: 
    https://www.postgresql.org/docs/current/plpgsql-control-structures.html#PLPGSQL-STATEMENTS-RETURNING
    https://dba.stackexchange.com/questions/186257/how-can-i-return-multiple-rows-of-records-in-pl-pgsql
    https://stackoverflow.com/questions/22010405/how-to-return-multiple-row-from-multiple-table-in-plpgsql

## returning from a procedure
- a procedure does not have a return value. It can thus end without a `RETURN`.
- to exit the code early simply `RETURN` without a value.


