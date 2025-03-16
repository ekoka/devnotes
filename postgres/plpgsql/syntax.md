## PL/pgSQL functions are defined with `CREATE FUNCTION` commands

    CREATE FUNCTION somefunc () RETURNS integer
    AS  'function body text'
    LANGUAGE plpgsql;

- or to make it easier to define the body
    
    CREATE FUNCTION somefunc () RETURNS integer
    AS  $$
    function body text
    $$ 
    LANGUAGE plpgsql;


## the body text

    [ <<label>> ]
    [ DECLARE
        declarations ]

    BEGIN
        statements
    END [ label ];

