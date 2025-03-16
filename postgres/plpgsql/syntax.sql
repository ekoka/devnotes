-- syntax
CREATE FUNCTION somefunc() RETURNS integer AS $$
-- label
<< outerblock >>
DECLARE
-- variable declarations block 
    quantity integer := 30;
BEGIN
-- statement declarations block 
    RAISE NOTICE 'Quantity here is %', quantity;  -- Prints 30
    quantity := 50;
    --
    -- Create a subblock
    --
    DECLARE
        quantity integer := 80;
    BEGIN
        RAISE NOTICE 'Quantity here is %', quantity;  -- Prints 80
        RAISE NOTICE 'Outer quantity here is %', outerblock.quantity;  -- Prints 50
    END;

    RAISE NOTICE 'Quantity here is %', quantity;  -- Prints 50

    RETURN quantity;
END; -- or END outerblock; 
$$ LANGUAGE plpgsql;


