`NULL` can be used like python's `pass`, but is not necessary

    BEGIN
        z = x/y;
    EXCEPTION
        WHEN division_by_zero THEN
            NULL; -- ignore the error
    END;

or 
    
    BEGIN
        z = x/y;
    EXCEPTION
        WHEN division_by_zero THEN -- ignore the error
    END;
