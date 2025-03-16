## LOOP
- `LOOP` defines an unconditional loop that is repeated indefinetely until terminated by an `EXIT` or `RETURN` statement.

    [ <<label>> ]
    LOOP
        statements
    END LOOP [ label ];

## EXIT

    exit [ label ] [ WHEN boolean-expression ];

## WHILE

    [ <<label>> ]
    WHILE boolean-expression LOOP
        statements
    END LOOP [ label ];

- e.g.

    WHILE amount_owed > 0 AND gift_certificate_balance > 0 LOOP
        statements
    END LOOP;

    WHILE NOT done LOOP
        statements
    END LOOP;

## FOR

    [ <<label>> ]
    FOR name IN  [REVERSER] expression .. expression [BY expression] LOOP
        statements
    END LOOP [ label ];

- e.g.

    FOR i IN 1..10 LOOP
        -- i will be 1,2,3 ... 10
    END LOOP;
    
    FOR i IN REVERSE 10..1 LOOP
        -- i will be 10, 9, 8 ... 1
    END LOOP;
    
    FOR i IN REVERSE 10..1 LOOP BY 2
        -- i will be 10, 8, 6... 2
    END LOOP;

## `FOREACH` to loop through `ARRAY` structures
- syntax 

    [ <<label>> ]
    FOREACH target [ SLICE number ] IN ARRAY expression LOOP
        statements
    END LOOP [ label ];
    
- if `SLICE` starts at 0 (default), the loop iterates through individual elements of the array produced by evaluating the `expression`. 
- the `target` variable is assigned each element value in sequence

- e.g.

    CREATE FUNCTION sum(int[]) RETURNS int8 AS $$
    DECLARE
        s int8 := 0;
        x int;
    BEGIN
        FOREACH x IN ARRAY $1 LOOP
            s := s + x;
        END LOOP;
        RETURN s;
    END;
    $$ LANGUAGE plpgsql;


    CREATE OR REPLACE FUNCTION looptest()
    RETURNS SETOF text
    AS $$
    DECLARE 
        name text;
        -- foo text[] = '{a, b, c}';
    BEGIN
        -- foreach name in ARRAY foo loop
        foreach name in ARRAY '{a, b, c}'::text[] loop
        return next name; 
        end loop;
    end;
    $$ language plpgsql;
    
    -- or 
    
    CREATE OR REPLACE FUNCTION looptest()
    RETURNS SETOF text
    AS $$
    DECLARE 
        name text;
        -- foo text[] = '{a, b, c}';
    BEGIN
        -- foreach name in ARRAY foo loop
        foreach name in ARRAY '{a, b, c}'::text[] loop
        return next name; 
        end loop;
    end;
    $$ language plpgsql;
