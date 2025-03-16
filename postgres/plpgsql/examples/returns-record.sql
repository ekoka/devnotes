-- explicit multiple output params 
-- no RETURNS record (i.e. implicit declaration) 

    -- RETURN (param1, param2) would create an error
    CREATE OR REPLACE FUNCTION fnc(out param1 int, out param2 int) AS $$
    BEGIN
        param1 = 33;
        param2 = 99;
    END;
    $$ LANGUAGE plpgsql;
    
    -- usage
    select param1, param2 from fnc();

    
-- no output params declared
-- explicit `RETURNS record` declarations 
-- explicit return values

    CREATE OR REPLACE FUNCTION fnc() 
    RETURNS record AS $$
    DECLARE
    param1 int;
    param2 int;
    BEGIN
        param1 = 22; 
        param2 = 33; 
        return (param1, param2);
    END;
    $$ LANGUAGE plpgsql;

    -- usage 
    select fnc(); 
    -- with column definition list
    select * fnc() AS (p1 int, p2 int);
