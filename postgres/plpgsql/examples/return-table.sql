-- explicit multiple output params 
-- explicit SETOF record

    -- RETURN (param1, param2) would create an error
    CREATE OR REPLACE FUNCTION fnc (out param1 int, out param2 int) 
    RETURNS SETOF record
    AS $$
    BEGIN
        param1 = 3
        param2 = 6
        RETURN NEXT;
        param1 = 2
        param2 = 5
        RETURN NEXT;
    END;
    $$ LANGUAGE plpgsql;
    
    -- usage
    select param1, param2 from fnc();

    
-- no output params declared
-- explicit SETOF record

    CREATE OR REPLACE FUNCTION fnc() 
    RETURNS SETOF record AS $$
    BEGIN
        return next row(22, 33);
        return next row(11, 88);
    END;
    $$ LANGUAGE plpgsql;

    -- usage: (requires column definition list)
    
    select * from fnc() as (p1 int, p2 int);

-- explicit RETURNS TABLE(...)

    CREATE OR REPLACE FUNCTION fnc() 
    RETURNS TABLE(param1 int, param2 int) AS $$
    BEGIN
        param1 = 22;
        param2 = 33;
        return next; 
        param1 = 55;
        param2 = 88;
        return next;
    END;
    $$ LANGUAGE plpgsql;

    -- usage
    select param1, param2 from fnc();
